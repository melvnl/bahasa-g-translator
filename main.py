def encode(input_string):
    vowels = "aeiou"
    result = ""

    for char in input_string:
        result += char
        if char.lower() in vowels:
            if char.lower() == 'a':
                result += "ga"
            elif char.lower() == 'e':
                result += "ge"
            elif char.lower() == 'i':
                result += "gi"
            elif char.lower() == 'o':
                result += "go"
            elif char.lower() == 'u':
                result += "gu"

    return result

def decode(modified_string):
    vowels = "aeiou"
    original_string = ""
    i = 0

    while i < len(modified_string):
        original_string += modified_string[i]
        if i + 2 < len(modified_string) and modified_string[i+1:i+3] in ['ga', 'ge', 'gi', 'go', 'gu']:
            i += 2
        i += 1

    return original_string

user_choice = input("Enter 'encode' to convert to bahasa G or 'decode' to convert to bahasa Indonesia: ")

if user_choice.lower() == 'encode':
    user_input = input("Enter a string in Bahasa Indonesia: ")
    result_string = encode(user_input)
    print("Decoded:", result_string)

elif user_choice.lower() == 'decode':
    modified_string = input("Enter a string in Bahasa G : ")
    original_string = decode(modified_string)
    print("Encoded:", original_string)

else:
    print("Invalid choice. Please enter 'encode' or 'decode'.")
