# Day 6 Challenge
# Make your own login program
# 1. Create a program where someone logins with their username and password correctly and then gets a lovely individual greeting.
# 2. Write a specific personalized greeting for 3 different people.
# 3. Don't forget an else statement for everyone else who shouldn't be logging in.

username = input("Username: ")
password = input("Password: ")
if username  == "user1" and password == "123":
    print("Hello, User1!")
elif username == "user2" and password == "456":
    print("Hello, User2!")
elif username == "user3" and password == "098":
    print("Hello, User3!")
else:
    print("Invalid username or password!")