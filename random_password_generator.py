import random

# Lists of characters to choose from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# User input for password criteria
ur_letter = int(input("\nHow many letters do you want to include: "))
ur_number = int(input("How many numbers do you want to include: "))
ur_symbol = int(input("How many symbols do you want to include: "))

# Generate random password based on user input
password_list = []

# Add random letters to the password
for _ in range(ur_letter):
    password_list.append(random.choice(letters))

# Add random numbers to the password
for _ in range(ur_number):
    password_list.append(random.choice(numbers))

# Add random symbols to the password
for _ in range(ur_symbol):
    password_list.append(random.choice(symbols))

# Shuffle the password characters
random.shuffle(password_list)

# random_password = ""
# for password in password_list:
#     random_password += password

# Convert the list to a string to create the final password
random_password = ''.join(password_list)

# Display the random password
print(f"\nYour random password is: {random_password}\n")
