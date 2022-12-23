import re
inp_str = "Hey readers, we all are here be 49 the time 76!"
 
 
print("Original string : " + inp_str) 
 
num = re.findall(r'\d+', inp_str) 
 
print(num)