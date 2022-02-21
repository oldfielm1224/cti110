user_int = int(input('Enter integer (32 - 126):\n'))

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
user_float = float(input('Enter float:\n'))
# FIXME (2): Output the four values in reverse
user_char = input('Enter character:\n')
# FIXME (3): Convert the integer to a characer, and output that character
user_str = input('Enter string:\n')
print(user_int, user_float, user_char, user_str)
print(user_str, user_char, user_float, user_int)
print(user_int,'converted to a character is',chr(int(user_int)))
