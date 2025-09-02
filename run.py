from figma_capture import capture_sync
from ac_loader import load_acceptance_criteria
from llm_mapper import map_to_spec
from spec_writer import write_excel

def main():
    screenshot = capture_sync()
    ac_text = load_acceptance_criteria()
    rows = map_to_spec(screenshot, ac_text)
    path = write_excel(rows)
    print(f"✅ Tech Spec generated: {path}")

if __name__ == "__main__":
    main()
