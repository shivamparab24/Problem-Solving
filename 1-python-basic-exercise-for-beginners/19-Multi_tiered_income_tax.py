# Practice Problem: Calculate income tax for a given income based on these rules:

# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% tax


def calc_income_tax(income):

    print(f"The income is {income}")
    income_tax = 0

    if income <= 10000:
        income_tax = 0
    elif income <= 20000:
        income_tax = (income - 10000) * (10/100)
    else:
        income_tax = 0
        income_tax += 10000 * (10/100)
        income_tax += (income - 20000) * (20/100)

    return income_tax


def calc_income_tax_2(income):

    brackets = [
        (10000, 0.0),
        (10000, 0.10),
        (float('inf'), 0.20)
    ]

    tax = 0
    remaining = income

    for limit, rate in brackets:

        taxable = min(remaining, limit)
        tax += taxable * rate
        remaining -= taxable

        if remaining <= 0:
            break

    return tax


if __name__ == '__main__':
    n = int(input("Enter the income to calculate income tax: "))
    print(calc_income_tax(n))
    print(calc_income_tax_2(n))