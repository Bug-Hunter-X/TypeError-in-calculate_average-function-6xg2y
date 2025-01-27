def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 # Handle case where no numeric values are present
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_string = [10, 20, '30', 40, 50]
average_mixed = calculate_average(my_list_with_string)
print(f"The average of mixed list is: {average_mixed}") #This will correctly return average of numbers only