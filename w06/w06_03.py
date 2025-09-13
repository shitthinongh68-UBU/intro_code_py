input_count = int(input())
item = set()

for i in range (input_count):
    text_input = str(input()).strip()
    item.add(text_input)

item_list = sorted(item)

for i in item_list:
    print(i)
    