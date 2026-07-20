def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average}")
    print(f"Grade: {grade}")

    below_40 = []
    for index, mark in enumerate(marks, start=1):
        if mark < 40:
            below_40.append(f"Subject {index}")

    if below_40:
        print("Subjects below 40:", ", ".join(below_40))
    else:
        print("Subjects below 40: None")


if __name__ == "__main__":
    analyze_result("Aarav", 101, [88.5, 35.0, 76.0, 92.5, 48.0])