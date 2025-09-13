number_of_data = int(input())
stu_info = dict()

for i in range(number_of_data):
    #68114640778 20 => stu_code = 68114640778, stu_score = 20
    stu_code, stu_score = input().split()
    
    #เก็บเป็นคีย์ 3 ตัวหลัง 68114640778 => 778 และเก็บ value => 20
    #{'778', '20'}
    stu_info[stu_code[-3:]] = stu_score

#รับข้อมูลจากผู้ใช้โดยรหัส สามตัวหลังจากที่ใส่ไป เช่น 778 
find_stu = input()

#พิมพ์ค่าคะแนนที่เก็บเป็น value โดยใช้ key หา
print(stu_info[find_stu])

