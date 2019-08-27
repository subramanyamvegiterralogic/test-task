import os, re
ip_list=[]

class MyTest:

    ip_dict={}
    ip_reachable={}
    reach = ''

    #Asking to Enter File Absolute Path
    while True:
        try:
            absolute_file_path = input('Enter Absolute File Path : ')
            print("File Absolute Path : "+os.path.abspath(absolute_file_path))
            # print((os.path.abspath('output.txt') == os.path.isfile(absolute_file_path)))
            if str(os.path.abspath('log.txt')) != absolute_file_path:
                continue
            else:
                break
        except Exception as e:
            print(e.message)
            continue

    # Validate IP is Correct ot not IF Correct it'll add to list to proceed further operations
    def returnValidIPs(self,ip_file_list):
        for ip_item in ip_file_list:
            flag = 0
            colon_split_data = ip_item.split(":")
            field = colon_split_data[1].split(".")
            for i in range(0, len(field)):
                if (int(field[i]) < 256):
                    flag += 1
                else:
                    flag = 0

            if (flag == 4):
                ip_list.append(ip_item)

    # It'll split IP and Host and returns only IP address
    def returnOnlyIP(self,ip):
        return ip.split(":")[1]

    # Reading IPs from ips_list file
    def fetch_ip(self):
        with open('log.txt','r') as f:
            data = f.readlines()
            log_parser = re.findall(r'host\d+:\d{1,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}',str(data),re.IGNORECASE);
            # log_parser = re.findall(r"host\d+:[0-255]\.[0-255]\.[0-255]{1}\.[0-255]{1}",str(data),re.IGNORECASE);
            print(log_parser)
            self.returnValidIPs(list(log_parser))

    # Writting Data to the output.txt File
    def writeToFile(self):
        with open('output.txt','w') as f:
            for key,val in self.ip_dict.items():
                data = (str(key)+' is repeated '+str(self.ip_dict.get(key))
                        +(' times and it\'s ' if self.ip_dict.get(key)>1 else ' time and it\'s ')+self.ip_reachable.get(key)+"\n")
                f.write(data)

    # IP Ping Operation Implementation
    def pingOperation(self,ip_list):
        for ip in ip_list:
            rep=os.system("ping -i 5 "+self.returnOnlyIP(ip))
            # rep = 1
            if rep == 0:
                reach = "Reachable"
                print("server is up")
            else:
                reach = "Not Reachable"
                print("server is down")
            if ip in self.ip_dict.keys():
                self.ip_dict[ip] = self.ip_dict.get(ip)+1
            else:
                self.ip_dict[ip] = 1
            self.ip_reachable[ip] = reach
        self.writeToFile()

    # Reading Data From output.txt file and Displaying on Console
    def printTextFileOutput(self):
        with open('output.txt','r') as f:
            data = f.readlines()
            list_data = [i.split('\n')[0] for i in data]
            for item in list_data:
                print(item)

#Creating reference variable for the class and Calling the functions of the class
reference = MyTest()
reference.fetch_ip()
reference.pingOperation(ip_list)
reference.printTextFileOutput()

