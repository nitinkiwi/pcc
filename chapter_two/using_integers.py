import datetime
today = datetime.date.today()
year = today.year
print(4+4)
print(10-2)
print(2*4)
print(32/4)
print(8**2)
yearOfBirth = input("In which year were you born? ")
intYearOfBirth = int(yearOfBirth)
age = year - intYearOfBirth
print(f"If you were born in {yearOfBirth} then you must be approximately {age} years old!")