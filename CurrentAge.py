'''
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99").
Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
'''
# Read the last two digits of the birth year and current year
birth_year = int(input())
current_year = int(input())
# Calculate the full birth year and current year
# Assuming the years are in the range 1900-1999 and 2000-2099
if current_year >= birth_year:
    age = current_year - birth_year
else:
    age = (current_year + 100) - birth_year
print(age)
