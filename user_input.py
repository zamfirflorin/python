
user_input =input("Enter temperature: ")
name = input()
surname = input()
today = 'vineri'

firstmessage = "Hello %s %s %s!" % (user_input, name, surname)
message = f"Hello {user_input} {surname} overriden {today}"
print(firstmessage)
print(message)
print(type(user_input))
