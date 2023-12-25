# User Registration System in Python

# Function to register a new user
def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email address: ")

    # Here, username, password, and email are variables storing user input

    # Saving the user data (For demonstration, we are just printing it)
    print("\nRegistration Successful!")
    print(f"Username: {username}")
    print(f"Email: {email}")

    # In a real application, this data would be stored in a database

# Calling the function to register a user
register_user()
