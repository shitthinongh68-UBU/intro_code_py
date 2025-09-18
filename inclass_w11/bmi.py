while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
    except Exception as e:
        print('กรอกข้อมูลไม่ถูกต้อง กรุณาป้อนตัวเลขใหม่')
        continue

    try:
        bmi = weight / (height / 100) ** 2
        print(f'Your BMI is {bmi:.2f}')
        break

    except Exception as e:
        print('ความสูงต้องไม่เป็นศูนย์')

    