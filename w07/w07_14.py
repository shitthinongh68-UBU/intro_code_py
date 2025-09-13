mortercycle_price = int(input('Motorcycle Price:'))
interest_rate = int(input('Interest Rate:'))
down_payment = int(input('Down Payment:'))
duration = int(input('Duration:'))

monthly_interest = mortercycle_price * interest_rate / 100
monthly_installment = (mortercycle_price - down_payment) / duration + monthly_interest

print(f'{monthly_installment:,.2f}')