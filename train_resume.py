#!/usr/bin/env python3
"""
Train Resume Similarity Model

Usage:
    python train_resume.py
"""
import sys
sys.path.insert(0, ".")

from sklearn.metrics import classification_report
from data.resume_data import get_all_resumes, get_stats
from src.resume_similarity import ResumeSimilarity


def main():
    print("=" * 60)
    print("RESUME SIMILARITY TRAINING")
    print("=" * 60)

    # Dataset stats
    stats = get_stats()
    print(f"\nDataset Statistics:")
    print(f"  Total resumes: {stats['total_resumes']}")
    print(f"  Categories: {stats['categories']}")
    for cat, count in stats["resumes_per_category"].items():
        print(f"    {cat}: {count}")

    # Load data
    categories = get_all_resumes()

    # Train
    similarity = ResumeSimilarity()
    metrics, y_test, y_pred = similarity.train(categories)

    # Results
    print("\n" + "=" * 60)
    print("TRAINING RESULTS")
    print("=" * 60)
    print(f"\nAccuracy: {metrics['accuracy']:.2%}")
    print(f"Total dimensions: {metrics['total_dimensions']}")
    print(f"Important dimensions: {metrics['important_dimensions']}")
    print(f"Dimension reduction: {metrics['dimension_reduction']}")

    print("\nTop 10 Important Dimensions:")
    for dim, importance in metrics["top_dimensions"]:
        print(f"  Dimension {dim:4d}: {importance:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["Different Field", "Same Field"]))

    # Save
    similarity.save()

    # Demo
    print("=" * 60)
    print("SIMILARITY DEMO")
    print("=" * 60)

    test_pairs = [
        (categories["engineering"][0], categories["engineering"][1], "Engineer vs Engineer"),
        (categories["marketing"][0], categories["marketing"][1], "Marketing vs Marketing"),
        (categories["engineering"][0], categories["marketing"][0], "Engineer vs Marketing"),
        (categories["finance"][0], categories["healthcare"][0], "Finance vs Healthcare"),
    ]

    print(f"\nUsing {metrics['important_dimensions']} focused dimensions:\n")

    for r1, r2, desc in test_pairs:
        result = similarity.compare(r1, r2)
        print(f"{desc}:")
        print(f"  Full similarity:    {result['full_similarity']:.3f}")
        print(f"  Focused similarity: {result['focused_similarity']:.3f}")
        print(f"  Match level: {result['match_level']}")
        print()

    print("=" * 60)
    print("TRAINING COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
