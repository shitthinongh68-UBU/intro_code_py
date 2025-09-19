f = open('inclass_w11/src/notebook_price.csv', 'r')

def showvalue_inlist(list):
    for l in list:
        print(l)

def Normalread(file):
    for line in file:
        print(line.strip().split())

def conditionreadCSV(file):   
    for line in file:
        single_line = line.strip().split(',')
        try:
            price = float(single_line[-1])
            data = single_line
        except:
            header = single_line
            continue

        if price >= 20000: print(data)
        else: continue


def SortedCSV(file):
    comp_list = list()
    for line in file:
        single_line = line.strip().split(',')
        try:
            price = float(single_line[-1])
            data = single_line
        except:
            header = single_line
            continue
        
        comp_list.append(data)

    comp_list_sorted = sorted(comp_list, key=lambda x: float(x[-1]))
    showvalue_inlist(comp_list_sorted)