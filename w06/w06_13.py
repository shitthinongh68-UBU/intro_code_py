product_detail = {
    's001': 15,
    's002': 120,
    's003': 50,
    's004': 25,
    's005': 3.5,
    's006': 10.25,
    's007': 264,
    's008': 79,
    's009': 99,
    's010': 75.5
}

sum_price = 0

input_str = input('shopping cart: ')
shopping_cart = input_str.split(', ')
for product in shopping_cart:
    sum_price += product_detail[product]

print(f'total {sum_price:.2f} baht')

#Fixed By ChatGPT

""" product_detail = {
    's001': 15,
    's002': 120,
    's003': 50,
    's004': 25,
    's005': 3.5,
    's006': 10.25,
    's007': 264,
    's008': 79,
    's009': 99,
    's010': 75.5
}

sum_price = 0

input_str = input().strip()  # ไม่มีข้อความใน input()

print('shopping cart:')

if input_str:  # ตรวจสอบว่ามีสินค้าใน input
    shopping_cart = input_str.split(', ')
    for product in shopping_cart:
        sum_price += product_detail[product]
    print(f'total {sum_price:.2f} baht')
 """

