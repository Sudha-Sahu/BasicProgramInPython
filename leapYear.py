# Checking given year is leap year or not

year = int(input("Enter any year to check if it is leap year or not : "))
if (year > 999) and (year < 10000):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(year, " is a Leap year")
    else:
        print(year, " is not a Leap Year")
else:
    print("invalid inputs")
