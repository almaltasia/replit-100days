# Day 4 Challenge
# 1. Ask your users to list a bunch of information about them: things they like, things they hate, names of family and friends... it's up to you how many and what kinds of things you pick. Keep it wacky!
# 2. Now construct your story - it can be about anything you want, but must use the variables you've created in step 1
# 3. Make sure to only work one paragraph at a time. Otherwise things could get a bit messy.

# Solution
likes=input("What do you likes?")
hate=input("What do you hate?")
famName=input("What are your family members names?")
friendName=input("What are your friends names?")
print()
print("My Friend is", friendName,"he is born from", famName, "and he likes", likes, "and he hates", hate)

# print color
print("\033[31m", "Hello World")