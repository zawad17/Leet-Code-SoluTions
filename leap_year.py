def leap_year(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        leap = True
    return leap

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    print(leap_year(year))
