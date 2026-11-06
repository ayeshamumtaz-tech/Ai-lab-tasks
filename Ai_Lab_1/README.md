# Lab 1 – AI Paradigms: Supporting Files

These files support the Lab 1 scholarship-screening exercise. They use only standard Python and require no external packages.

## Files

- `lab1_rules.py` – the extended rule-based checker for Task 2. It retains `score >= 70` and document completeness, then adds minimum attendance (75%) and minimum practical score (60%). It tests exactly four core cases and prints each input, expected result, actual result, and reason.
- `lab1_compare.py` – the rule-based versus probability-threshold comparison from the lab manual's Section 1.5. The probability values are invented demonstration inputs; the script does not train a model or measure prediction accuracy.
- `Lab1_Report_Tasks2_3_Addendum.docx` – report-ready Task 2 and Task 3 sections, plus the disagreement table required by the submission checklist.

## Requirements

- Python 3
- No third-party libraries

## Run

Open a terminal in this folder and run:

```bash
python lab1_rules.py
python lab1_compare.py
```

The output is printed in the terminal. The test inputs are synthetic lab examples, not real applicant records. `Review` means that an application is flagged for a human reviewer; it is not a scholarship award decision.

## Assumptions and limitations

The lab's score threshold of 70 is retained. For this demonstration, attendance of at least 75% and a practical score of at least 60/100 are additional synthetic lab assumptions, not official scholarship policy. The rule-based program follows fixed conditions and reports the first failed condition. The probability-threshold script uses supplied invented values; it has no trained model and cannot establish accuracy. Real scholarship decisions require approved policy, validated data, privacy safeguards, and human review.
- `task2_output.txt` – captured output from the four Task 2 core cases.
- `compare_output.txt` – captured output from the Section 1.5 comparison cases.
