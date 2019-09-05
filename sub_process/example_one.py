import subprocess
# host = input('Enter a host to PING : ')
p1=subprocess.Popen(['ping', '106.51.41.104'], stdout=subprocess.PIPE).stdout.read()
# output = p1.communicate()[0]
# print(output)
print(p1)