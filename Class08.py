#Scenario 01
employees = [("John", 50000, 4.5),("Alice", 60000, 4.7),("Bob", 45000, 4.2),("Emma", 55000, 4.6),("James", 48000, 4.4)]
satisfaction_weight = 0.4
sales_weight = 0.6


def calculate_weighted_score(employee):
    name, sales, satisfaction = employee
    return (sales * sales_weight) + (satisfaction * satisfaction_weight)

top_employee = max(employees, key=calculate_weighted_score)

print(f"Top-performing employee: {top_employee[0]}, Weighted Score: {calculate_weighted_score(top_employee):.2f}")


#Scenario 02
list = []

for i in range(1,11):
    if i % 2 == 0:
        sqrt = i ** 0.5
        list.append(sqrt)

print(list)
