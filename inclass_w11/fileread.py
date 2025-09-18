f = open('./inclass_w11/src/notebook_price.csv', 'r')

for line in f:
    try:
        row = line.strip().split(',')
        price = int(row[-1])
    except:
        continue
    if price <= 20000:
        print(line.strip())