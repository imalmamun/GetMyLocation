import re # Regular Expression library
import numpy as np
text='gggsd 01845545555 ddddd  hhhhhhh +8801862979800,+8801962979800, njjhhjjjj,+8801762979800,'
phone_number_pattern ='(\+8801)(3|5|7|8|9)\d{8}'

def find_all_bd_numbers(word):
  compiled=re.compile(phone_number_pattern)
  flag=compiled.match(word)
  if flag:
    print('phone number',flag.group())


split_text_file=re.split(r'\s',text)


for word in split_text_file:
  find_all_bd_numbers(word)

  here is something.......
