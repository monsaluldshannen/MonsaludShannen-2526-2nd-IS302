def calculate_average(g1, g2, g3):
    return (g1 + g2 + g3) / 3

def get_remark(avg):
    if 90 <= avg <= 100:
        return "Excellent"
    elif 85 <= avg <= 89:
        return "Very Good"
    elif 80 <= avg <= 84:
        return "Good"
    elif 75 <= avg <= 79:
        return "Fair"
    else:
        return "Failed"

# Main program
name_shnn = input("Enter student name: ")

grade1_shnn = float(input("Enter grade 1: "))
grade2_shnn = float(input("Enter grade 2: "))
grade3_shnn = float(input("Enter grade 3: "))

average_shnn = calculate_average(grade1_shnn, grade2_shnn, grade3_shnn)
remark_shnn = get_remark(average_shnn)

print("\nStudent:", name_shnn)
print("Average:", average_shnn)
print("Remark:", remark_shnn)