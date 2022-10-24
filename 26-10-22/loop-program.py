
# continue statement
while True:
    print("Who are you? ")
    name = input()
    if name != 'Hasan':
        continue
    print("Hello " + name + ". What is the passcode?")
    password = input()
    if password == "22":
        break
print("Hasan, Log in Successful ")

