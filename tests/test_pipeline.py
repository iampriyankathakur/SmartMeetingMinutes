from src.pipeline import run_pipeline
from pathlib import Path

def test_run_creates_output(tmp_path):
    inp = tmp_path / "transcript.txt"
    out = tmp_path / "output.md"
    inp.write_text("Alice: Please do X. Action: Bob to do X.")
    run_pipeline(str(inp), str(out))
    assert out.exists()
    txt = out.read_text()
    assert "Meeting Summary" in txt
