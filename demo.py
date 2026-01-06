#!/usr/bin/env python3
"""
Demo script for PII detection and Resume similarity.

Usage:
    python demo.py
"""
import sys
sys.path.insert(0, ".")

from src.pii_detector import PIIDetector
from src.resume_similarity import ResumeSimilarity


def demo_pii():
    """Demonstrate PII detection."""
    print("=" * 60)
    print("PII DETECTION DEMO")
    print("=" * 60)

    detector = PIIDetector().load()
    print(f"Model loaded: {detector.model.hidden_layer_sizes}\n")

    test_texts = [
        # Clean
        "The quarterly report shows 15% revenue growth. The board approved additional investment in R&D.",
        "Please review the pull request before merging. Focus on the error handling improvements.",
        "The team meeting has been rescheduled to Thursday at 3 PM. Please update your calendars.",

        # PII
        "Contact John Smith at john.smith@email.com or call 555-123-4567 for more information.",
        "Ship to: 123 Main Street, Apt 4B, New York, NY 10001. Please require signature on delivery.",
        "Patient: Sarah Johnson, DOB: 05/15/1987, SSN: 123-45-6789, Insurance ID: BCBS-998877.",
    ]

    results = detector.detect(test_texts)

    for r in results:
        icon = "[!]" if r["contains_pii"] else "[ ]"
        status = "PII DETECTED" if r["contains_pii"] else "Clean"
        print(f"{icon} {status} ({r['confidence']:.1f}%)")
        print(f"    \"{r['text'][:70]}{'...' if len(r['text']) > 70 else ''}\"")
        print()


def demo_resume():
    """Demonstrate resume similarity."""
    print("=" * 60)
    print("RESUME SIMILARITY DEMO")
    print("=" * 60)

    similarity = ResumeSimilarity().load()
    print(f"Model loaded: {len(similarity.important_dims)} focused dimensions\n")

    # Sample resumes
    software_engineer = """
    Software engineer with 5 years experience in Python, Java, and cloud technologies.
    Built scalable microservices at tech startups. Strong background in algorithms,
    data structures, and system design. BS Computer Science from MIT.
    """

    another_engineer = """
    Full stack developer proficient in React, Node.js, and PostgreSQL.
    Developed e-commerce platforms handling millions of transactions.
    Experience with AWS, Docker, and CI/CD pipelines.
    """

    marketing_manager = """
    Digital marketing manager with 7 years experience driving growth for B2B SaaS.
    Expert in SEO, PPC, and content marketing. Increased organic traffic 300%.
    MBA from Wharton. Google Ads and Analytics certified.
    """

    pairs = [
        (software_engineer, another_engineer, "Software Eng vs Software Eng"),
        (software_engineer, marketing_manager, "Software Eng vs Marketing"),
    ]

    for r1, r2, desc in pairs:
        result = similarity.compare(r1, r2)
        print(f"{desc}:")
        print(f"  Full similarity:    {result['full_similarity']:.3f}")
        print(f"  Focused similarity: {result['focused_similarity']:.3f}")
        print(f"  Match level: {result['match_level']}")
        print()


if __name__ == "__main__":
    print("\n")
    demo_pii()
    print("\n")
    demo_resume()
