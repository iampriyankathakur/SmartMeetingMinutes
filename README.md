# 📝 Smart Meeting Minutes Generator

Turn raw meeting transcripts into **structured minutes** with AI.
Automatically extracts:
- ✅ Key discussion points
- ✅ Decisions made
- ✅ Action items with owners

## Quick start
```bash
pip install -r requirements.txt
python -m src.pipeline --input data/sample_transcript.txt --output data/output_summary.md

## 🗂 Project Layout
smart-meeting-minutes/
│── README.md
│── requirements.txt
│── src/
│    ├── summarizer.py
│    ├── extractor.py
│    └── pipeline.py
│── data/
│    ├── sample_transcript.txt
│    └── output_summary.md
│── notebooks/
│    └── prototype.ipynb
│── tests/
│    └── test_pipeline.py
