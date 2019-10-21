# import sys,os, struct
# print(os.getcwd())
# file_path = 'D://PSI-1931/mytest/binary_files/latlon.bin'
# # print(os.path.abspath('latlon.bin'))
# encoding = 'utf-8'
# with open(file_path, 'rb') as file:
#     for line in file:
#         print(line.decode(encoding))
#         # print(type(line))
import re
emai_list=['subramanyam586@gmail.com',
           'python.developer.subramanyam@gmail.com',
           'subramanyam.vegi@terralogic.com',
           'subramanyam.v@sedots.com',
           'subramanyam.v@hyd.actcorp.in',
           'subramanyam.v@roi.actcorp.in.bangalore']
for mail in emai_list:
    res = re.fullmatch(r'[a-zA-Z0-9_.]+\@[a-zA-Z0-9.]+\.[a-z]{2,3}', str(mail), re.I)
    if res != None:
        print(res)
# while True:
while False:
    email = input('Please enter email \t:\t')
    val = re.fullmatch(r'[a-zA-Z0-9_.]+[AT|@]{1}[a-zA-Z0-9.]+\.[a-z]{2,3}',email)
    print(val)