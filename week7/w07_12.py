call_start_time = input().split(':')
call_end_time = input().split(':')

call_time_hours = (int(call_end_time[0]) - int(call_start_time[0]))*60
call_time_minute = (int(call_end_time[1]) - int(call_start_time[1]))

total_call_cost = (call_time_hours + call_time_minute) * 1.5 

print(f'{total_call_cost:.2f}')