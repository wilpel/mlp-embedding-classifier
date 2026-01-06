# Embedding ML

Semantic text classification using OpenAI embeddings and neural networks.

## Overview

This project demonstrates how to use text embeddings for classification tasks that require **semantic understanding** rather than pattern matching. Instead of regex or keyword matching, we convert text to high-dimensional vectors that capture meaning, then train classifiers on these vectors.

### Key Insight

OpenAI's embeddings encode semantic meaning. Text like "contact john.smith@email.com" and "reach me at 555-1234" are close in embedding space because they both describe **contacting a specific person**. A neural network learns which embedding dimensions indicate the patterns we care about.

## Features

### 1. PII Detection

Detects personal identifiable information in text:
- Names + email addresses
- Names + phone numbers
- Physical addresses
- Social Security Numbers
- Dates of birth
- Financial information (account numbers, credit cards)
- Medical record numbers
- Driver's licenses and IDs

**Accuracy: ~98%** on held-out test data.

### 2. Resume Similarity

Finds which embedding dimensions matter for professional similarity:
- Identifies 60-80 dimensions (out of 1536) that capture 90% of what makes resumes similar
- Enables focused comparison using only relevant dimensions
- Improves same-field similarity scores while filtering noise

## Project Structure

```
embedding-ml/
├── src/
│   ├── embeddings.py        # OpenAI embedding wrapper
│   ├── pii_detector.py      # PII detection model
│   └── resume_similarity.py # Resume similarity model
├── data/
│   ├── pii_data.py          # PII training data (200+ examples)
│   └── resume_data.py       # Resume training data (8 categories)
├── models/
│   ├── pii_model.pkl        # Trained PII model
│   └── resume_model.pkl     # Trained resume model
├── train_pii.py             # Train PII detector
├── train_resume.py          # Train resume similarity
├── demo.py                  # Demo both models
└── requirements.txt
```

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up OpenAI API key
echo "OPENAI_API_KEY=your-key-here" > .env
```

## Usage

### Train Models

```bash
# Train PII detector
python train_pii.py

# Train resume similarity
python train_resume.py
```

### Run Demo

```bash
python demo.py
```

### Use in Code

```python
from src.pii_detector import PIIDetector
from src.resume_similarity import ResumeSimilarity

# PII Detection
detector = PIIDetector().load()
results = detector.detect([
    "Contact John at john@email.com",
    "The meeting is at 3 PM tomorrow"
])
for r in results:
    print(f"{r['contains_pii']}: {r['confidence']:.1f}%")

# Resume Similarity
similarity = ResumeSimilarity().load()
result = similarity.compare(resume1, resume2)
print(f"Similarity: {result['focused_similarity']:.3f}")
print(f"Match level: {result['match_level']}")
```

## How It Works

### Architecture

```
Text → OpenAI Embedding (1536 dims) → Neural Network → Classification
                                           ↓
                                   (256 → 128 → 64)
                                   Learns dimension combinations
```

### PII Detector

1. **Embeddings**: Convert text to 1536-dimensional vectors
2. **Scaling**: StandardScaler normalizes features
3. **MLP**: 3-layer neural network (256→128→64) learns patterns
4. **Output**: Probability of containing PII

The MLP learns non-linear combinations of dimensions. Unlike simpler models that look at dimensions independently, it can detect patterns like "dimension 42 high AND dimension 891 low = PII".

### Resume Similarity

1. **Pair Creation**: Generate similar (same field) and dissimilar (different field) pairs
2. **Feature Engineering**: Absolute difference between embeddings
3. **GradientBoosting**: Identifies which dimensions distinguish similar from dissimilar
4. **Focused Comparison**: Use only important dimensions for similarity calculation

This reduces noise from irrelevant dimensions and improves discrimination.

## Training Data

### PII Data
- **117 PII examples**: emails, phones, addresses, SSNs, DOBs, financial, medical
- **90 clean examples**: business communications, technical docs, announcements
- Balanced classes for robust training

### Resume Data
- **8 categories**: Engineering, Marketing, Finance, Healthcare, Legal, Sales, Design, Operations
- **25 resumes per category**: Varied roles and seniority levels
- Total: 200 resumes for pair-based training

## Results

### PII Detection
```
Test Accuracy: 98.11%
CV Mean: 98.09% (+/- 2.43%)

              precision    recall  f1-score
No PII           0.96      1.00      0.98
Contains PII     1.00      0.96      0.98
```

### Resume Similarity
```
Accuracy: 89%+ on pair classification

Same field comparisons improved:
  Engineer vs Engineer: 0.53 → 0.72 (focused)
  Marketing vs Marketing: 0.59 → 0.78 (focused)

Cross-field properly separated:
  Engineer vs Marketing: 0.41 → 0.36 (focused)
```

## Extending

### Add New PII Categories

Edit `data/pii_data.py`:
```python
PII_TEXTS = [
    # Add new examples
    "New PII pattern example here...",
]
```

Then retrain: `python train_pii.py`

### Add New Resume Categories

Edit `data/resume_data.py`:
```python
NEW_CATEGORY_RESUMES = [
    "Resume text 1...",
    "Resume text 2...",
]

RESUME_CATEGORIES = {
    ...
    "new_category": NEW_CATEGORY_RESUMES,
}
```

Then retrain: `python train_resume.py`

## Requirements

- Python 3.10+
- OpenAI API key
- Dependencies: openai, scikit-learn, numpy, python-dotenv

## License

MIT
