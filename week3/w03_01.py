sec_input = int(input())
remain_min = sec_input // 60
remain_sec = sec_input - (remain_min * 60)
print(f'{sec_input} วินาที เท่ากับ {remain_min} นาที {remain_sec} วินาที')