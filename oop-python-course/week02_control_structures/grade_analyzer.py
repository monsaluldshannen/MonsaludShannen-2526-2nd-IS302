name_shnn = input("Enter student name: ")

grade1_shnn = float(input("Enter grade 1: "))
grade2_shnn = float(input("Enter grade 2: "))
grade3_shnn = float(input("Enter grade 3: "))

average_shnn = (grade1 + grade2 + grade3) / 3

print("\nStudent:", name)
print("Average:", average)

if 90 <= average <= 100:
    print("Remark: Excellent")
elif 85 <= average <= 89:
    print("Remark: Very Good")
elif 80 <= average <= 84:
    print("Remark: Good")
elif 75 <= average <= 79:
    print("Remark: Fair")
else:
    print("Remark: Failed")