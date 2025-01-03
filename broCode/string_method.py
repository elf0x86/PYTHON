name = input('Enter you full name: ')
name_len = len(name)
name_first_a = name.find('a') # return the first ocurence of the character
name_last_a  = name.rfind('a') # return the last  ocurence of the character
name_captial = name.capitalize()
name_upper   = name.upper()
name_lower   = name.lower()
name_digit   = name.isdigit() # return True of False for [0-9]
name_alpha   = name.isalpha() # return True of False for [A-z]

phone_number  = input('Enter your phone number: ')
phone_dashes  = phone_number.count('-')
phone_replace = phone_number.raplace('-', ' ')

print(help(str))
