""" month_arry = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'December']

month_index = int(input())
print(month_arry[month_index - 1])
 """

month_arry = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

month_index = int(input())

# ถ้า month_index มากกว่าหรือเท่ากับ 1 และ น้อยกว่าหรือเท่า 12 ให้เป็นจริง

if 1 <= month_index <= 12:
    print(month_arry[month_index - 1])
else:
    # If the index is out of range, print nothing (or handle as required by the test)
    print('')