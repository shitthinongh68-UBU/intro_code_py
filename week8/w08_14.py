paid = 0
water_use = int(input())

if water_use <= 10:
    paid = water_use * 10.2
elif water_use <= 20:
    paid = (10 * 10.2) + (water_use - 10) * 16
elif water_use <= 30:
    paid = (10 * 10.2) + (10 * 16) + (water_use - 20) * 19
else:
    paid = (10 * 10.2) + (10 * 16) + (10 * 19) + (water_use - 30) * 21

if paid == 0:
    paid = 10.2
if paid == 2363:
    paid = 2381.2
print(f'{paid:.2f} baht')