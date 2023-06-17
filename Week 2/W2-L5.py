# String Methods in Python
a = "Hello World"

# 1. len() - returns the length of the string
print(len(a))

# 2. lower() - returns the string in lower case
print(a.lower())

# 3. upper() - returns the string in upper case
print(a.upper())

# 4. replace() - replaces a string with another string  
print(a.replace("H", "J"))

# 5. split() - splits the string into substrings if it finds instances of the separator
print(a.split(" "))

# 6. strip() - removes any whitespace from the beginning or the end
print(a.strip())

# 7. count() - returns the number of times a specified value occurs in a string
print(a.count("l"))

# 8. find() - searches the string for a specified value and returns the position of where it was found
print(a.find("W"))

# 9. capitalize() - converts the first character to upper case
print(a.capitalize())

# 10. isalpha() - returns True if all the characters are alphabet letters (a-z)
print(a.isalpha())

# 11. isdigit() - returns True if all the characters are digits (0-9)
print(a.isdigit())

# 12. islower() - returns True if all the characters are in lower case
print(a.islower())

# 13. isupper() - returns True if all the characters are in upper case
print(a.isupper())

# 14. isspace() - returns True if all the characters in a string are whitespaces
print(a.isspace())

# 15. istitle() - returns True if the string follows the rules of a title
print(a.istitle())

# 16. isalnum() - returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)
print(a.isalnum())

# 17. endswith() - returns True if the string ends with the specified value
print(a.endswith("d"))

# 18. startswith() - returns True if the string starts with the specified value
print(a.startswith("H"))

# 19. join() - takes all items in an iterable and joins them into one string
print(" ".join(a))

# 20. swapcase() - swaps cases, lower case becomes upper case and vice versa
print(a.swapcase())

# 21. title() - converts the first character of each word to upper case
print(a.title())

# 22. rfind() - searches the string for a specified value and returns the last position of where it was found
print(a.rfind("l"))

# 23. rindex() - searches the string for a specified value and returns the last position of where it was found
print(a.rindex("l"))

# 24. rjust() - returns a right justified version of the string
print(a.rjust(20))

# 25. rstrip() - returns a right trim version of the string
print(a.rstrip())

# 26. lstrip() - returns a left trim version of the string
print(a.lstrip())

# 27. partition() - returns a tuple where the string is parted into three parts
print(a.partition(" "))

# 28. rpartition() - returns a tuple where the string is parted into three parts
print(a.rpartition(" "))

# 29. replace() - returns a string where a specified value is replaced with a specified value
print(a.replace("H", "J"))

# 30. rsplit() - splits the string at the specified separator, and returns a list
print(a.rsplit(" "))

# 31. splitlines() - splits the string at line breaks and returns a list
print(a.splitlines())

# 32. zfill() - fills the string with a specified number of 0 values at the beginning
print(a.zfill(20))

# 33. center() - returns a centered string
print(a.center(20))

# 34. expandtabs() - sets the tab size of the string
print(a.expandtabs(20))

# 35. format() - formats specified values in a string
print(a.format())

# 36. format_map() - formats specified values in a string
print(a.format_map(""))

# 37. index() - searches the string for a specified value and returns the position of where it was found
print(a.index("W"))

# 38. isdecimal() - returns True if all the characters are decimals (0-9)
print(a.isdecimal())

# 39. isidentifier() - returns True if the string is an identifier
print(a.isidentifier())

# 40. isnumeric() - returns True if all the characters are numeric (0-9)
print(a.isnumeric())

# 41. maketrans() - returns a translation table to be used in translations
print(a.maketrans(""))

# 42. translate() - returns a translated string
print(a.translate(""))

# 43. ljust() - returns a left justified version of the string
print(a.ljust(20))

