import re
def ipcheck():
    input_ip = input('Enter the ip:')
    # 1.Validate the ip adderess
    flag = 0

    pattern = "^host\d+:\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
    match = re.match(pattern, input_ip)
    if (match):
        colon_split_data = input_ip.split(":")
        field = colon_split_data[1].split(".")
        for i in range(0, len(field)):
            if (int(field[i]) < 256):
                flag += 1
            else:
                flag = 0
    if (flag == 4):
        print("valid ip")
    else:
        print('No match for ip or not a valid ip')

ipcheck()