
#prompts user to enter the monthly investment
while (monthly_investment := float(input('Enter the monthly invest amount: '))) <= 0:
    print('ERROR: investment must be a positive number')

#prompts user to enter the yearly interest    
while (yearly_investment := float(input('Enter the yearly interest rate: '))) <= 0:
    print('ERROR: yearly interest rate must be a positive number')

#prompts user to enter the years they want to invest
while (investment_years := int(input('Enter how many years to invest: '))) <= 0:
     print('ERROR: investment period must be a positive number')

#calculates the monthly rate
months_rate = (yearly_investment / 100) / 12

#calculates the year
years = investment_years * 12

#total before compound investment revenue 
total = 0.0

#calculates compound investment revenue
for months in range(1, years + 1):

    total += monthly_investment
    total *= (1 + months_rate)

    #outputs the total investment revenue
    print(f'Month {months} revenue: {total}')

#outputs the user's years of investment 
print(f'After {investment_years}, you will receive a total investment of {total: ,.2f} at a yearly rate of {yearly_investment}')
