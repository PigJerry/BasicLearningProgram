name = input("What's your name? ")
print("Hello", name, "welcome to Python's world!")
print("I can help you to do something about temperature.")

running = True
while running:
    Celsius = input("If you want to change Celsius to Fahrenheit, please tell me the number. If not, print 'No': ")
    
    if Celsius == "no":
        Fahrenheit = input("If you want to change Fahrenheit to Celsius, please tell me the number: ")
        try:
            f = float(Fahrenheit)
            c = (f - 32) * 5 / 9
            print(f"{f}°F = {c}°C")
        except ValueError:
            print("Please enter a valid number!")
    else:
        try:
            c = float(Celsius)
            f = c * 9 / 5 + 32
            print(f"{c}°C = {f}°F")
        except ValueError:
            print("Please enter a valid number!")
    
    goodbye = input("Type 'goodbye' to quit, or press Enter to continue: ")
    if goodbye == "goodbye":
        running = False
        print("OK, see you next time!")

print("Program ended.")