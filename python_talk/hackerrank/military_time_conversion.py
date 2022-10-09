# input_str = "11:21:30PM"
input_str = "12:12:20AM"

hour= input_str.split(":")[0] # '12'
minute = input_str.split(":")[1] # '12'
second = input_str.split(":")[2][0:2] # '20'
am_pm = input_str.split(":")[2][2:] # 'AM'

if am_pm == "PM": 
    hour = int(hour) + 12
elif am_pm == "AM" and hour == "12": 
    hour = "00" # '00'


output = f"{hour}:{minute}:{second}" # output = '00:12:20' 

print(output)