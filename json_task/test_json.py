import re, json
import employee as emp

def parse_json_file_data():
    emp_list=[]
    with open('text_json.json','r') as file:
        file_data = json.load(file)
        for key,value in file_data.items():
            if 'data_list' in file_data.keys():
                data_list = file_data.get(key)
                for nested_item in range(0,len(data_list)):
                    e = emp.Employee()
                    e.set_esal(data_list[nested_item].get('e_sal'))
                    e.set_no(data_list[nested_item].get('e_no'))
                    e.set_city(data_list[nested_item].get('e_city'))
                    e.set_mobile(data_list[nested_item].get('e_mobile'))
                    e.set_name(data_list[nested_item].get('e_name'))
                    emp_list.append(e)
        for data in emp_list:
            print(data.get_no(),'\t',data.get_name(),'\t',data.get_esal(),'\t',data.get_city(),'\t',data.get_mobile())
            print('')
# parse_json_file_data()

def parse_mixed_data_file():
    data_list = []
    with open('text_json_sample.txt', 'r') as f:
        # print(f.readlines())
        item = re.findall(r'{(.*?)}',str(f.readlines()), re.IGNORECASE)
        # item = re.findall(r'{\.*',str(f.readlines()), re.IGNORECASE)
        print(item)
        # print(len(item))
        for i in item:
            i.replace('\\\n','').replace('\\\n\\','').replace(',\'\\n\\',',').replace('\\','').replace('\\t','').replace(',,',',')
            print(i)
            # my_dict = json.loads(i)
            # print(my_dict)
            # data_list.append(my_dict)
            # print(data_list)
parse_mixed_data_file()