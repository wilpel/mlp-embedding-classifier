#!/usr/bin/env python3
"""
Train PII Detection Model

Usage:
    python train_pii.py
"""
import sys
sys.path.insert(0, ".")

from data.pii_data import get_training_data, get_stats
from src.pii_detector import PIIDetector, print_report


def main():
    print("=" * 60)
    print("PII DETECTOR TRAINING")
    print("=" * 60)

    # Dataset stats
    stats = get_stats()
    print(f"\nDataset Statistics:")
    print(f"  Total samples: {stats['total_samples']}")
    print(f"  PII samples: {stats['pii_samples']}")
    print(f"  No PII samples: {stats['no_pii_samples']}")
    print(f"  Balance ratio: {stats['balance_ratio']:.2f}")

    # Load data
    texts, labels = get_training_data()

    # Train
    detector = PIIDetector()
    metrics, y_test, y_pred = detector.train(texts, labels)

    # Results
    print("\n" + "=" * 60)
    print("TRAINING RESULTS")
    print("=" * 60)
    print(f"\nTraining Accuracy: {metrics['train_accuracy']:.2%}")
    print(f"Test Accuracy: {metrics['test_accuracy']:.2%}")
    print(f"CV Mean: {metrics['cv_mean']:.2%} (+/- {metrics['cv_std'] * 2:.2%})")
    print(f"Iterations: {metrics['iterations']}")
    print(f"Final Loss: {metrics['loss']:.6f}")

    print_report(y_test, y_pred)

    # Save
    detector.save()

    print("\n" + "=" * 60)
    print("TRAINING COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
