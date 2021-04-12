# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
def interest_after_year(start, years):
    final_amount = start * 1.1 ** years
    return final_amount

print(100 * 1.1 ** 7)
print(interest_after_year(start=100, years=7))
