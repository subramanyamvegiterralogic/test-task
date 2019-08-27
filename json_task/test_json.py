import re

with open('text_json.txt','r') as file:
    file_data = file.readlines()
    re_result = re.findall(r'{.*}',str(file_data).replace('\n','').replace('\\n','').replace("\'",'').replace('\t','').replace('\\t','').replace(',,',',').strip())
    print(type(re_result))
    print(len(re_result))
    re_result1 = re.findall(r'\{(.*?)\}',str(re_result))
    print(type(re_result1))
    print(len(re_result1))
    for item in re_result1:
        print(item)
    # print(re_result)
    # print(file_data)