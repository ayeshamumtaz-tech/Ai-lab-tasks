
def scholarship_check(marks, documents, attendance_rate, family_income):
    if (marks >= 70 and
        documents == True and
        attendance >= 75 and
        family_income <= 100000):
        return "Eligible"
    else:
        return "Ineligible"
    
# Test Case 1: All conditions satisfied
marks = 85
documents = True
attendance = 82
family_income = 85000
expected = "Eligible"

actual = scholarship_check(marks, documents, attendance, family_income)

print("Test Case 1: Successful Application")
print("Input:", marks, documents, attendance, family_income)
print("Expected Result:", expected)
print("Actual Result:", actual)
print("Reason: All four conditions are satisfied.")
print()

# Test Case 2: Attendance below the required limit
marks = 85
documents = True
attendance = 68
family_income = 85000
expected = "Ineligible"

actual = scholarship_check(marks, documents, attendance, family_income)

print("Test Case 2: Low Attendance")
print("Input:", marks, documents, attendance, family_income)
print("Expected Result:", expected)
print("Actual Result:", actual)
print("Reason: Attendance is below the required 75%.")
print()

# Test Case 3: Family income exceeds the limit
marks = 85
documents = True
attendance = 82
family_income = 125000
expected = "Ineligible"

actual = scholarship_check(marks, documents, attendance, family_income)

print("Test Case 3: High Family Income")
print("Input:", marks, documents, attendance, family_income)
print("Expected Result:", expected)
print("Actual Result:", actual)
print("Reason: Family income exceeds the assumed limit of 100000.")
print()

# Test Case 4: Score at the minimum boundary
marks = 70
documents = True
attendance = 75
family_income = 100000
expected = "Eligible"

actual = scholarship_check(marks, documents, attendance, family_income)

print("Test Case 4: Boundary Test")
print("Input:", marks, documents, attendance, family_income)
print("Expected Result:", expected)
print("Actual Result:", actual)
print("Reason: All values meet their minimum or maximum thresholds exactly.")