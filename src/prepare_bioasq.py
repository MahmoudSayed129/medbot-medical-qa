import json
import os

# Define input/output paths
INPUT_PATH = "data/raw/BioASQ-training12b.json"
OUTPUT_PATH = "data/processed/bioasq_qa.json"

def load_bioasq_data(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["questions"]

def process_question_entry(entry):
    question = entry.get("body", "").strip()
    snippets = [s["text"].strip() for s in entry.get("snippets", []) if s.get("text")]
    answer = entry.get("exact_answer", "")

    # Normalize answer: handle list and nested list
    if isinstance(answer, list):
        if all(isinstance(a, list) for a in answer):  # Nested list
            answer = answer[0][0] if answer and answer[0] else ""
        elif all(isinstance(a, str) for a in answer):  # Flat list
            answer = answer[0] if answer else ""
    elif isinstance(answer, str):
        answer = answer.strip()

    context = " ".join(snippets)

    # Return None if any required part is missing
    if not question or not context or not answer:
        return None

    return {
        "question": question,
        "context": context,
        "answer": answer,
        "source": "BioASQ"
    }

def main():
    os.makedirs("data/processed", exist_ok=True)

    raw_entries = load_bioasq_data(INPUT_PATH)
    processed_entries = []

    for entry in raw_entries:
        qa = process_question_entry(entry)
        if qa:
            processed_entries.append(qa)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(processed_entries, f, indent=2, ensure_ascii=False)

    print(f"✅ Processed {len(processed_entries)} QA pairs.")
    print(f"📁 Saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
