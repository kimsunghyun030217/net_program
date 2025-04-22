days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June' : 30, 'July': 31, 'August':31, 'Sepyember':30, 
        'October':31,'November':30, 'December':31}
dict_keys = days.keys()
keys_list = list(dict_keys)
result1 = sorted(keys_list)
result2 = sorted(days.items(),key=lambda t :t[1])
print(result1)
print(result2)

result3 = input("월의 3자리만 입력 : ")

if (result3 in keys_list[0:3]):
    print(key_list)