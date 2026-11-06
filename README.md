# CodeAlpha Python Programming Tasks

This repository contains three console-based projects prepared for the CodeAlpha Python Programming internship task list.

## Included tasks

1. **Task 1 — Hangman Game** (`task1_hangman.py`)
   - Uses five predefined words.
   - Allows up to six incorrect guesses.
   - Validates input and avoids counting repeated guesses as incorrect.

2. **Task 2 — Stock Portfolio Tracker** (`task2_stock_portfolio_tracker.py`)
   - Uses a hardcoded dictionary of sample stock prices.
   - Accepts stock symbols and quantities.
   - Calculates each holding and the total portfolio value.
   - Optionally exports the summary to a CSV file.
   - **Note:** Prices are examples for coding practice, not live market data or investment advice.

3. **Task 3 — Email Address Extractor** (`task3_email_extractor.py`)
   - Reads a text file.
   - Extracts email-like addresses using a regular expression.
   - Removes duplicate addresses and writes the results to an output text file.

## Requirements

- Python 3.8 or newer
- No third-party packages required

## How to run

Open a terminal in this folder and run the required task:

```bash
python task1_hangman.py
python task2_stock_portfolio_tracker.py
python task3_email_extractor.py
```

For Task 3, `sample_text.txt` is included as a sample input. When prompted, press Enter to use `sample_text.txt` and `extracted_emails.txt`.

## GitHub submission

1. Create a public GitHub repository named `codealpha_tasks`.
2. Upload all files from this folder.
3. Copy the repository URL and enter it in the CodeAlpha submission form for each task field, if the form accepts the same repository URL for multiple tasks.
4. LinkedIn video links are optional according to the October Batch submission form.

## Suggested project explanation

- **Hangman:** The program randomly selects a word and lets the player guess letters until the word is complete or six incorrect guesses are used.
- **Stock Portfolio Tracker:** The program multiplies each entered stock quantity by its sample price and adds the values to calculate the portfolio total.
- **Email Extractor:** The program reads a text file, finds email addresses with a regular expression, removes duplicates, and saves the result to another file.
