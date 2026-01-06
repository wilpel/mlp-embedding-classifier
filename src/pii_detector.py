"""
PII (Personal Identifiable Information) Detector

Uses embedding-based classification to detect personal data in text.
Detects: names, emails, phones, SSNs, addresses, DOBs, financial info, medical records, IDs.
"""
import pickle
import numpy as np
from pathlib import Path
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Handle imports for both package and direct execution
try:
    from src.embeddings import get_embeddings
except ImportError:
    from embeddings import get_embeddings


MODEL_PATH = Path(__file__).parent.parent / "models" / "pii_model.pkl"


class PIIDetector:
    """Detects personal identifiable information in text using embeddings."""

    def __init__(self, model_path: Path = MODEL_PATH):
        self.model = None
        self.scaler = None
        self.model_path = model_path

    def train(self, texts: list[str], labels: list[int], test_size: float = 0.2) -> dict:
        """
        Train the PII detection model.

        Args:
            texts: List of text samples
            labels: Binary labels (1=PII, 0=No PII)
            test_size: Fraction of data for testing

        Returns:
            Dictionary with training metrics
        """
        print(f"Generating embeddings for {len(texts)} texts...")
        embeddings = get_embeddings(texts)
        X = np.array(embeddings)
        y = np.array(labels)

        # Scale features
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=test_size, random_state=42, stratify=y
        )

        print(f"Training set: {len(X_train)} samples")
        print(f"Test set: {len(X_test)} samples")

        # Train MLP
        print("\nTraining neural network...")
        self.model = MLPClassifier(
            hidden_layer_sizes=(256, 128, 64),
            activation="relu",
            solver="adam",
            alpha=0.001,
            batch_size=32,
            learning_rate="adaptive",
            learning_rate_init=0.001,
            max_iter=500,
            early_stopping=True,
            validation_fraction=0.15,
            n_iter_no_change=20,
            random_state=42,
            verbose=False,
        )
        self.model.fit(X_train, y_train)

        # Evaluate
        y_train_pred = self.model.predict(X_train)
        y_test_pred = self.model.predict(X_test)

        train_acc = accuracy_score(y_train, y_train_pred)
        test_acc = accuracy_score(y_test, y_test_pred)

        # Cross-validation
        cv_scores = cross_val_score(self.model, X_scaled, y, cv=5)

        metrics = {
            "train_accuracy": train_acc,
            "test_accuracy": test_acc,
            "cv_mean": cv_scores.mean(),
            "cv_std": cv_scores.std(),
            "iterations": self.model.n_iter_,
            "loss": self.model.loss_,
        }

        return metrics, y_test, y_test_pred

    def save(self, path: Path = None):
        """Save model and scaler to disk."""
        path = path or self.model_path
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump({"model": self.model, "scaler": self.scaler}, f)
        print(f"Model saved to {path}")

    def load(self, path: Path = None):
        """Load model and scaler from disk."""
        path = path or self.model_path
        with open(path, "rb") as f:
            data = pickle.load(f)
        self.model = data["model"]
        self.scaler = data["scaler"]
        return self

    def detect(self, texts: list[str]) -> list[dict]:
        """
        Detect PII in texts.

        Returns:
            List of dicts with 'text', 'contains_pii', 'confidence', 'prob_pii'
        """
        if self.model is None:
            raise ValueError("Model not loaded. Call load() or train() first.")

        embeddings = get_embeddings(texts)
        X = np.array(embeddings)
        X_scaled = self.scaler.transform(X)

        predictions = self.model.predict(X_scaled)
        probabilities = self.model.predict_proba(X_scaled)

        results = []
        for text, pred, probs in zip(texts, predictions, probabilities):
            results.append({
                "text": text,
                "contains_pii": bool(pred),
                "confidence": float(max(probs) * 100),
                "prob_pii": float(probs[1]),
            })
        return results

    def detect_single(self, text: str) -> dict:
        """Detect PII in a single text."""
        return self.detect([text])[0]


def print_report(y_true, y_pred):
    """Print classification report and confusion matrix."""
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=["No PII", "Contains PII"]))

    cm = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:")
    print(f"                 Predicted")
    print(f"                 No PII  |  PII")
    print(f"Actual No PII      {cm[0][0]:3d}   |   {cm[0][1]:3d}")
    print(f"Actual PII         {cm[1][0]:3d}   |   {cm[1][1]:3d}")
