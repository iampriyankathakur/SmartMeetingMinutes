import argparse
from .summarizer import summarize_text
from .extractor import extract_action_items

def run_pipeline(input_path: str, output_path: str):
    with open(input_path, "r", encoding="utf-8") as f:
        transcript = f.read()

    summary = summarize_text(transcript)
    actions = extract_action_items(transcript)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Meeting Summary\n\n")
        f.write(summary + "\n\n")
        if actions:
            f.write("## Action Items\n")
            for i, a in enumerate(actions, 1):
                f.write(f"{i}. {a}\n")
    print(f"Saved summary to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Smart meeting minutes pipeline")
    parser.add_argument("--input", required=True, help="Path to transcript file")
    parser.add_argument("--output", required=True, help="Path to output summary markdown")
    args = parser.parse_args()
    run_pipeline(args.input, args.output)

if __name__ == "__main__":
    main()
