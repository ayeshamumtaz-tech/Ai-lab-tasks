
# Lab 1 – AI Paradigms: Supporting Files

These files are part of the Lab 1 scholarship-screening exercise. They demonstrate basic AI concepts, rule-based decision-making, and the comparison between symbolic and data-driven approaches.

## Files

- `task2_comparee.py` – The modified rule-based scholarship checker for Task 2. It retains the minimum score requirement (70) and document completeness, with two additional conditions: minimum attendance (75%) and maximum family income (100,000). It includes exactly four test cases and displays the input, expected result, actual result, and reason for each case.

- `Task 1 & 3.docx` – Contains the written work for Task 1 and Task 3, including the AI timeline, historical concepts, and comparison between conversational ability and general intelligence.

## Requirements

- Python 3
- No external libraries required

## How to Run

Open a terminal in the project folder and execute:

```bash
python task2_comparee.py
```

The program displays the results of all four test cases in the terminal.

## Testing

The Python program includes four test cases:

1. An application that satisfies all four conditions.
2. An application with attendance below 75%.
3. An application with family income above 100,000.
4. A boundary test where the values are exactly at the required thresholds.

## Assumptions and Limitations

The score threshold of 70 and document completeness requirement are retained from the lab instructions. Attendance of at least 75% and family income not exceeding 100,000 are additional synthetic assumptions used for demonstration, not official scholarship policies.

The program follows fixed conditions and returns either **Eligible** or **Not Eligible**. It does not use a trained machine learning model or make actual scholarship award decisions. Real scholarship screening would require approved criteria, reliable applicant data, and human verification.
