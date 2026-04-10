grades_shnn = []

for i in range(5):
    grade = float(input(f"Enter grade {i+1}: "))
    grades_shnn.append(grade)

average_shnn = sum(grades_shnn) / len(grades_shnn)
highest_shnn = max(grades_shnn)
lowest_shnn = min(grades_shnn)

print("\nAverage Grade:", average_shnn)
print("Highest Grade:", highest_shnn)
print("Lowest Grade:", lowest_shnn)