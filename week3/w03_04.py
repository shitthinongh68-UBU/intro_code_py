''' วิธีที่ 1 '''
# รับค่าในรูปแบบ list โดยใช้ eval แล้วเก็บไว้ใน score
score = eval('[' + str(input())+']')

# ทำการบวกข้อมูลใน list ซึ่งเก็บอยู่ใน score
sum_score = sum(score)

# หาค่าเฉลี่ยโดยนำค่าใน sum_score / จำนวนสมาชิกใน score (ใช้ len เพื่อหาสมาชิก)
avg_score = sum_score / len(score)

print(f'คะแนนรวม คือ {sum_score}\nคะแนนเฉลี่ยของนักเรียน คือ {avg_score}')

''' วิธีที่ 2 '''
# สร้างตัวแปรแต่ละวิชาขึ้นมาเฉพาะ แล้วให้ eval แทนค่าลงในตัวแปรแต่ละตัว
sub_1, sub_2, sub_3, sub_4, sub_5 = eval(input())

# บวกข้อมูลที่เก็บแยกกันอยู่ แล้วเก็บไว้ใน score_sum
score_sum = sub_1 + sub_2 + sub_3 + sub_4 + sub_5

# หาค่าเฉลี่ยโดยนำค่าใน score_sum / จำนวนตัวแปรที่นำมาบวกกันใน score_sum
score_avg = score_sum / 5

print(f'คะแนนรวม คือ {score_sum}\nคะแนนเฉลี่ยของนักเรียน คือ {score_avg}')