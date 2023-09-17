# Input: Allow the user to enter the first name and number of steps walked
first_name = input("Enter your first name: ")
number_of_steps = int(input("Enter the number of steps walked in a day: "))

# Processing: Calculate the number of calories burned
calories_burned = number_of_steps * 0.25

# Output: Display the first name and calories burned
print(f"{first_name}, you burned {calories_burned:.2f} calories today.")