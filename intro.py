# This is the beginning of my coding journey ---
# Ask the user for their name

varName = input("Hello, what is your name? ").strip().title()

"""
$ Remove whitespace from str (accidental spaces)
varName = varName.strip()

$ Capitalize the user's name, in case they forget (only the first letter)
varName = varName.capitalize()

$ Capitalize every word, as if it were a title...
varName = varName.title()

$ Now, Do both "strip" and "capitalize"...
varName = varName.strip().title()

"""

# Hello, user (formated)...
print(f"hello, {varName}, how are you?")