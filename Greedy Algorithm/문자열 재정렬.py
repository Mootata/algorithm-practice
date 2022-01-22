string = input()
sorted_str = []
count = 0

for i in range(len(string)):
    if 48 <= ord(string[i]) <= 57: # 알파벳인지 확인하려면 isalpha()를 사용하면 됨..
        count += int(string[i])
    else:
        sorted_str.append(string[i])

sorted_str.sort()
if count != 0:
    sorted_str.append(str(count))
    
# print(''.join(sorted_str))

# for i in string:
#     if i.isalpha():
#         sorted_str.append(i)
#     else:
#         count += int(i)

# sorted_str.sort()

# if count != 0:
#     sorted_str.append(str(count))
    
# print(''.join(sorted_str))