"""
CodeAlpha Python Programming Internship — Task 3: Task Automation
Extracts email addresses from an input text file and writes unique addresses
to a separate output text file.
"""

import re
from pathlib import Path

EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)


def extract_emails(input_path, output_path):
    source = Path(input_path)
    destination = Path(output_path)

    if not source.is_file():
        raise FileNotFoundError(
            f"Input file '{source}' was not found. Create it and try again."
        )

    text = source.read_text(encoding="utf-8")
    found_emails = EMAIL_PATTERN.findall(text)

    # Preserve the first-seen order while removing duplicates.
    unique_emails = list(dict.fromkeys(email.lower() for email in found_emails))
    destination.write_text(
        "\n".join(unique_emails) + ("\n" if unique_emails else ""),
        encoding="utf-8",
    )
    return unique_emails


def main():
    print("=" * 42)
    print("         EMAIL ADDRESS EXTRACTOR")
    print("=" * 42)
    input_name = input("Enter input text filename [sample_text.txt]: ").strip()
    output_name = input("Enter output filename [extracted_emails.txt]: ").strip()

    input_name = input_name or "sample_text.txt"
    output_name = output_name or "extracted_emails.txt"

    try:
        emails = extract_emails(input_name, output_name)
        print(f"\nFound {len(emails)} unique email address(es).")
        for email in emails:
            print(f"- {email}")
        print(f"\nResults saved to: {output_name}")
    except (OSError, UnicodeError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
