import re, json
import employee as emp

emp_list=[]
with open('text_json.json','r') as file:
    file_data = json.load(file)
    print(file_data)
    for key,value in file_data.items():
        if 'data_list' in file_data.keys():
            data_list = file_data.get(key)
            for nested_item in range(0,len(data_list)):
                e = emp.Employee()
                esal = e.set_esal(data_list[nested_item].get('e_sal'))
                eno = e.set_no(data_list[nested_item].get('e_no'))
                ecity = e.set_city(data_list[nested_item].get('e_city'))
                emobile = e.set_mobile(data_list[nested_item].get('e_mobile'))
                ename = e.set_name(data_list[nested_item].get('e_name'))
                emp_list.append(e)
    for data in emp_list:
        print(data.get_no())
        print(data.get_name())
        print(data.get_esal())
        print(data.get_city())
        print(data.get_mobile())
        print('')
