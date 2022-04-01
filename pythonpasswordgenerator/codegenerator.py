import random
import array
max_len=12
number=['0','1','2','3','4','5','6','7','8','9',]
lower_characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbol=['~','@','#','$','%','^','&','*','(',')','<','>','?','/',',','.',':',';','"','|','*','-','+']
combined_list=number+lower_characters+upper_characters+symbol
random_number=random.choice(number)
random_upper= random.choice(upper_characters)
random_lower=random.choice(lower_characters)
random_symbol=random.choice(symbol)
temporary_password=random_number+random_lower+random_upper+random_number+random_symbol

for i in range (max_len - 4):
    temporary_password=temporary_password+random.choice(combined_list)

    temp_pass_list=array.array('u', temporary_password)
    password=""
 
for i in temp_pass_list:
    password=password+i
    print(password)