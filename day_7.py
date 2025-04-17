# Day 7 Challenge
# Fake Fan Question Generato
# Create a program that asks what someone is interested in and includes nested if 
# statements to ask annoying follow-up questions to see if someone is the real deal!

# Make sure you include multiple if/elif statements and nested if statements too! 

fans = input("what are you a fan of: Volly or Football?" )
if fans == 'Volly':
    print('Great!')
    team = input('Who is your Favorite team? ')
    if team == 'Red Spark':
        print('oh, They are a great team!')
    else:
        print('oh, I have never heard of them.')
elif fans == 'Football':
    print('oh, nice!')
    team = input('Who is your Favorite team? ')
    if team == 'Arsenal':
        print('oh, they are a great team!')
    else:
        print('oh, I have never heard of them.')
else:
    print('oh, okey you are not a fan of any sport!')