char = input("Enter a character: ")

if len(char) == 1:
    print(f"The ASCII code for '{char}' is {ord(char)}.")
else:
    print("Please enter only a single character.")