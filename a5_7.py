def calculate_investment(initial_investment, annual_interest, years):
    investment=initial_investment
    for year in range(1, years+1):
        investment+=investment*(annual_interest/100)
        print(f"Year {year}: ${investment:.2f}")
initial_investment=float(input("Enter initial investment: $"))
annual_interest=float(input("Enter annual interest rate (%): "))
years=int(input("Enter number of yours: "))

calculate_investment(initial_investment, annual_interest, years)