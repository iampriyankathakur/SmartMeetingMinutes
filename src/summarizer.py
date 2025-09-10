from typing import Optional

def summarize_text(text: str, max_length: int = 150, min_length: int = 40, model_name: Optional[str] = "facebook/bart-large-cnn") -> str:
    """
    Try to use Hugging Face summarization; fallback to a simple heuristic if unavailable.
    """
    try:
        from transformers import pipeline
        summarizer = pipeline("summarization", model=model_name)
        # Some models have limits on input length; simple approach: send whole text
        output = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return output[0]['summary_text']
    except Exception:
        # fallback: return first 3 sentences
        import re
        sentences = re.split(r'(?<=[.!?]) +', text.strip())
        return " ".join(sentences[:3])
