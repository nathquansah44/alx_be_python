monthly_income = float(input("Enter your monthly income: "))
monthly_espenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_espenses
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings is: $ {monthly_savings:.2f}")
print(f"Your projected annual savings after one year, with interest, is: $ {projected_annual_savings:.2f}")