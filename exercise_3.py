def letter_count(s):
    letter_dict = {}
    lower_case = s.lower()
    for lets in lower_case:
        if lets == " ":
            continue
        letter_dict[lets] = lower_case.count(lets)
    return letter_dict

user_in = input("Enter a string: ")
print(letter_count(user_in))