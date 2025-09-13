exchange_rate = {'usd' : 32.30,
                 'eur' : 37.58, 
                 'gbp' : 43.37, 
                 'jpy'  : 0.21 }

currency = input().strip()
amount = float(input())

print(f'{exchange_rate[currency] * amount:.2f} baht')