
parking_time = list()

parking_time.append(int(input('Hours:')))
parking_time.append(int(input('Minutes:')))

if parking_time[1] <= 20 and parking_time[0] == 0:
    park_fee = 0
    
elif parking_time[1] > 20 or parking_time[0] > 0:
    park_time = parking_time[0] + 1
    park_fee = park_time * 30

if park_fee == 60:
    park_fee =30
    
print(f'car park fee = {park_fee} baht')

