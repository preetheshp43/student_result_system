print("Student Result System")

def grade_calculator():
    s1 = int(input("Enter marks for Subject 1: "))
    s2 = int(input("Enter marks for Subject 2: "))
    s3 = int(input("Enter marks for Subject 3: "))
    s4 = int(input("Enter marks for Subject 4: "))
    s5 = int(input("Enter marks for Subject 5: "))

    total = s1 + s2 + s3 + s4 + s5
    avg = total / 5

    print("Total Marks =", total)
    print("Average =", avg)

    if avg >= 90:
        print("Grade: A")
    elif avg >= 75:
        print("Grade: B")
    elif avg >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")


def sgpa_calculator():
    credits = [3,3,3,3,3]   # example credits
    grade_points = []

    for i in range(5):
        gp = float(input(f"Enter grade point for subject {i+1}: "))
        grade_points.append(gp)

    total = 0
    total_credits = sum(credits)

    for i in range(5):
        total += grade_points[i] * credits[i]

    sgpa = total / total_credits
    print("SGPA =", round(sgpa,2))


def cgpa_calculator():
    sem = int(input("Enter number of semesters: "))
    total = 0

    for i in range(sem):
        sgpa = float(input(f"Enter SGPA of semester {i+1}: "))
        total += sgpa

    cgpa = total / sem
    print("CGPA =", round(cgpa,2))


print("1. Grade Calculator")
print("2. SGPA Calculator")
print("3. CGPA Calculator")

choice = input("Enter choice: ")

if choice == '1':
    grade_calculator()
elif choice == '2':
    sgpa_calculator()
elif choice == '3':
    cgpa_calculator()
else:
    print("Invalid choice")