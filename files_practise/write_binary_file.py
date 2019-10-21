import urllib.request, re

# f = urllib.request.urlopen('https://www.redbus.in/info/contactus')
# f = urllib.request.urlopen('https://www.terralogic.com/contact-us')
f = urllib.request.urlopen('https://www.apsrtconline.in/oprs-web/home/contactus.do')
data = f.read()
# data = str(f.read())
print(data)
print(type(data))
# mobile_list = re.findall(r'[0-9-]{7}[0-9-]+', data)
mobile_list = re.findall(r'\+\d{2}\s?0?\d{10}', str(data), re.I)
email_list = re.findall(r'[a-zA-Z0-9_.]+\@[a-zA-Z0-9.]+\.[a-z]{2,3}', str(data), re.I)
# mobile_list = re.findall(r'[6-9]{1}[0-9]{9}]', str(data), re.I)
print(email_list)
for mobile_no in mobile_list:
    print(mobile_no)
