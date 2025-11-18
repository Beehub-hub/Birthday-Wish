recipient_name = input("Enter recipient's name: ")
year_of_birth = int(input("Enter year of birth: "))
personal_message = input("Enter a short personalized message: ")
sender_name = input("Enter sender's name: ")

current_year = 2025
age = current_year - year_of_birth

print("\n----------------------------------------")
print(f"{recipient_name}, let's celebrate your {age} years of awesomeness!")
print(f"Wishing you a day filled with joy and laughter as you turn {age}!\n")
print(personal_message)
print("\nWith love and best wishes,")
print(sender_name)
print("----------------------------------------")











