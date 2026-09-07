# Implement a program that, given number of years as input, prints the number of months and days as output.
# Criteria:

#    each year has 365 days and 12 months
#    pretend that leap years do not exist

# Input example:

# Years: 5
# Output example:

# Months: 60, Days: 1825
# Output example:

# Months: 60, Days: 1825

# aantal jaren als input
nyears = int(input("How many years? "))


# maanden en dagen berekenen
def calc_months(nyears):
    return nyears * 12


def calc_days(nyears):
    return nyears * 365


months = calc_months(nyears)
days = calc_days(nyears)

# output geven
# print(nyears, "years contains", months, "months and", days, "days")
print("Months:", months, "Days:", days)

# print(nyears + "years contains" + months + "months")
# werkt niet?

# waarom nyears opnieuw benoemen steeds?
