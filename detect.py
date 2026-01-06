#!/usr/bin/env python3
"""
PII Detection CLI

Usage:
    python detect.py "Your text to analyze here"
    python detect.py -i                           # Interactive mode
    python detect.py -f file.txt                  # From file
"""
import sys
import argparse

sys.path.insert(0, ".")
from src.pii_detector import PIIDetector


def detect_text(detector: PIIDetector, text: str):
    """Detect and print results for a single text."""
    result = detector.detect_single(text)

    if result["contains_pii"]:
        print(f"\n[!] PII DETECTED ({result['confidence']:.1f}% confidence)")
    else:
        print(f"\n[✓] Clean ({result['confidence']:.1f}% confidence)")

    print(f"\nText: \"{text}\"")
    print(f"PII Probability: {result['prob_pii']*100:.1f}%")


def interactive_mode(detector: PIIDetector):
    """Run in interactive mode."""
    print("=" * 50)
    print("PII DETECTOR - Interactive Mode")
    print("=" * 50)
    print("Enter text to analyze (or 'quit' to exit)\n")

    while True:
        try:
            text = input("> ").strip()
            if text.lower() in ("quit", "exit", "q"):
                break
            if not text:
                continue
            detect_text(detector, text)
            print()
        except (KeyboardInterrupt, EOFError):
            break

    print("\nGoodbye!")


def main():
    parser = argparse.ArgumentParser(description="Detect PII in text")
    parser.add_argument("text", nargs="?", help="Text to analyze")
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("-f", "--file", help="Read text from file")
    args = parser.parse_args()

    # Load model
    detector = PIIDetector().load()

    if args.interactive:
        interactive_mode(detector)
    elif args.file:
        with open(args.file) as f:
            text = f.read().strip()
        detect_text(detector, text)
    elif args.text:
        detect_text(detector, args.text)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
