"""
Resume Similarity Calculator

Uses embedding-based analysis to find important dimensions for resume matching.
Compares resumes using focused dimensions that matter for professional similarity.
"""
import pickle
import numpy as np
from pathlib import Path
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Handle imports for both package and direct execution
try:
    from src.embeddings import get_embeddings, cosine_similarity
except ImportError:
    from embeddings import get_embeddings, cosine_similarity


MODEL_PATH = Path(__file__).parent.parent / "models" / "resume_model.pkl"


class ResumeSimilarity:
    """Calculate resume similarity using learned important dimensions."""

    def __init__(self, model_path: Path = MODEL_PATH):
        self.model = None
        self.important_dims = None
        self.model_path = model_path
        self._embed_cache = {}

    def train(self, resume_categories: dict[str, list[str]], test_size: float = 0.2) -> dict:
        """
        Train model to identify which embedding dimensions matter for resume similarity.

        Args:
            resume_categories: Dict mapping category names to lists of resume texts
            test_size: Fraction of data for testing

        Returns:
            Dictionary with training metrics and important dimensions
        """
        # Create pairs
        print("Creating resume pairs...")
        similar_pairs, similar_labels = self._create_similar_pairs(resume_categories)
        dissimilar_pairs, dissimilar_labels = self._create_dissimilar_pairs(resume_categories)

        # Balance dataset
        np.random.seed(42)
        n_similar = len(similar_pairs)
        if len(dissimilar_pairs) > n_similar:
            indices = np.random.choice(len(dissimilar_pairs), n_similar, replace=False)
            dissimilar_pairs = [dissimilar_pairs[i] for i in indices]
            dissimilar_labels = [dissimilar_labels[i] for i in indices]

        all_pairs = similar_pairs + dissimilar_pairs
        all_labels = similar_labels + dissimilar_labels

        print(f"Total pairs: {len(all_pairs)} ({len(similar_pairs)} similar, {len(dissimilar_pairs)} dissimilar)")

        # Get embeddings
        print("\nGenerating embeddings...")
        unique_texts = list(set([p[0] for p in all_pairs] + [p[1] for p in all_pairs]))
        embeddings = get_embeddings(unique_texts)
        self._embed_cache = {text: emb for text, emb in zip(unique_texts, embeddings)}

        # Create feature vectors (absolute difference)
        print("Creating feature vectors...")
        X = []
        for r1, r2 in all_pairs:
            e1 = np.array(self._embed_cache[r1])
            e2 = np.array(self._embed_cache[r2])
            diff = np.abs(e1 - e2)
            X.append(diff)

        X = np.array(X)
        y = np.array(all_labels)

        # Train/test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42, stratify=y
        )

        # Train GradientBoosting for feature importances
        print("\nTraining classifier to find important dimensions...")
        self.model = GradientBoostingClassifier(
            n_estimators=100,
            max_depth=4,
            learning_rate=0.1,
            random_state=42,
        )
        self.model.fit(X_train, y_train)

        # Evaluate
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # Get important dimensions (cumulative 90% importance)
        importances = self.model.feature_importances_
        dim_importance = list(enumerate(importances))
        dim_importance.sort(key=lambda x: x[1], reverse=True)

        total = sum(importances)
        cumsum = 0
        self.important_dims = []
        for dim, imp in dim_importance:
            if cumsum < 0.90 * total:
                self.important_dims.append(dim)
                cumsum += imp
            else:
                break

        metrics = {
            "accuracy": accuracy,
            "total_dimensions": len(importances),
            "important_dimensions": len(self.important_dims),
            "dimension_reduction": f"{(1 - len(self.important_dims) / len(importances)) * 100:.1f}%",
            "top_dimensions": [(dim, float(importances[dim])) for dim in self.important_dims[:10]],
        }

        return metrics, y_test, y_pred

    def _create_similar_pairs(self, categories: dict) -> tuple[list, list]:
        """Create pairs from same category (similar)."""
        pairs, labels = [], []
        for resumes in categories.values():
            for i in range(len(resumes)):
                for j in range(i + 1, len(resumes)):
                    pairs.append((resumes[i], resumes[j]))
                    labels.append(1)
        return pairs, labels

    def _create_dissimilar_pairs(self, categories: dict) -> tuple[list, list]:
        """Create pairs from different categories (dissimilar)."""
        pairs, labels = [], []
        cat_list = list(categories.values())
        for i in range(len(cat_list)):
            for j in range(i + 1, len(cat_list)):
                for r1 in cat_list[i]:
                    for r2 in cat_list[j]:
                        pairs.append((r1, r2))
                        labels.append(0)
        return pairs, labels

    def save(self, path: Path = None):
        """Save model and important dimensions to disk."""
        path = path or self.model_path
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump({
                "model": self.model,
                "important_dims": self.important_dims,
            }, f)
        print(f"Model saved to {path}")

    def load(self, path: Path = None):
        """Load model and important dimensions from disk."""
        path = path or self.model_path
        with open(path, "rb") as f:
            data = pickle.load(f)
        self.model = data["model"]
        self.important_dims = data["important_dims"]
        return self

    def compare(self, resume1: str, resume2: str) -> dict:
        """
        Compare two resumes.

        Returns:
            Dict with full similarity, focused similarity, and recommendation
        """
        embeddings = get_embeddings([resume1, resume2])
        e1 = np.array(embeddings[0])
        e2 = np.array(embeddings[1])

        # Full similarity
        full_sim = cosine_similarity(e1.tolist(), e2.tolist())

        # Focused similarity (important dimensions only)
        if self.important_dims:
            e1_focused = e1[self.important_dims]
            e2_focused = e2[self.important_dims]
            focused_sim = cosine_similarity(e1_focused.tolist(), e2_focused.tolist())
        else:
            focused_sim = full_sim

        # Recommendation
        if focused_sim > 0.7:
            match_level = "High"
        elif focused_sim > 0.5:
            match_level = "Medium"
        else:
            match_level = "Low"

        return {
            "full_similarity": float(full_sim),
            "focused_similarity": float(focused_sim),
            "match_level": match_level,
            "dimensions_used": len(self.important_dims) if self.important_dims else "all",
        }

    def find_similar(self, target_resume: str, candidates: list[str], top_k: int = 5) -> list[dict]:
        """
        Find most similar resumes from candidates.

        Returns:
            List of dicts with candidate info sorted by similarity
        """
        results = []
        for candidate in candidates:
            comparison = self.compare(target_resume, candidate)
            results.append({
                "resume": candidate[:100] + "..." if len(candidate) > 100 else candidate,
                "similarity": comparison["focused_similarity"],
                "match_level": comparison["match_level"],
            })

        results.sort(key=lambda x: x["similarity"], reverse=True)
        return results[:top_k]
