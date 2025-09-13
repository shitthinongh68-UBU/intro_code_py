""" import datetime

member = {
    '001': {'name': 'Jack', 'lastname': 'Watson', 'tel': '0812345678', 'enrolled_date': datetime.date(2021, 8, 26)},
    '002': {'name': 'Rita', 'lastname': 'Srisan', 'tel': '0898765432', 'enrolled_date': datetime.date(2022, 5, 1)},
    '003': {'name': 'Mani', 'lastname': 'Chompu', 'tel': '0887776666', 'enrolled_date': datetime.date(2022, 7, 24)},
    '004': {'name': 'Wanee', 'lastname': 'Suwan', 'tel': '0823334567', 'enrolled_date': datetime.date(2022, 7, 30)},
    '005': {'name': 'Chat', 'lastname': 'Chacha', 'tel': '0681478523', 'enrolled_date': datetime.date(2022, 8, 1)},
    '006': {'name': 'Prawee', 'lastname': 'Waree', 'tel': '0855555555', 'enrolled_date': datetime.date(2022, 8, 5)},
    '007': {'name': 'Anan', 'lastname': 'Tanun', 'tel': '0858889999', 'enrolled_date': datetime.date(2022, 8, 26)},
}

member_id = input().strip()

print(f'ID: {member_id}')
print(f'Name: {member[member_id]['name']} {member[member_id]['lastname']}')
print(f'Tel: {member[member_id]['tel']}')
print(f'Enrolled Date: {member[member_id]['enrolled_date']}') """

#Fixed By ChatGPT

import datetime

member = {
    '001': {'name': 'Jack', 'lastname': 'Watson', 'tel': '0812345678', 'enrolled_date': datetime.date(2021, 8, 26)},
    '002': {'name': 'Rita', 'lastname': 'Srisan', 'tel': '0898765432', 'enrolled_date': datetime.date(2022, 5, 1)},
    '003': {'name': 'Mani', 'lastname': 'Chompu', 'tel': '0887776666', 'enrolled_date': datetime.date(2022, 7, 24)},
    '004': {'name': 'Wanee', 'lastname': 'Suwan', 'tel': '0823334567', 'enrolled_date': datetime.date(2022, 7, 30)},
    '005': {'name': 'Chat', 'lastname': 'Chacha', 'tel': '0681478523', 'enrolled_date': datetime.date(2022, 8, 1)},
    '006': {'name': 'Prawee', 'lastname': 'Waree', 'tel': '0855555555', 'enrolled_date': datetime.date(2022, 8, 5)},
    '007': {'name': 'Anan', 'lastname': 'Tanun', 'tel': '0858889999', 'enrolled_date': datetime.date(2022, 8, 26)},
}

member_id = input().strip()

result = (
    f"ID: {member_id}\n"
    f"Name: {member[member_id]['name']} {member[member_id]['lastname']}\n"
    f"Tel: {member[member_id]['tel']}\n"
    f"Enrolled Date: {member[member_id]['enrolled_date']}"
)

print(result)
