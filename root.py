# # from pathlib import Path
# import os,sys, subprocess
# DETACHED_PROCESS = 0x00000008
# file_str ="test_file.py"
# f =os.path.abspath(file_str)
# # pid = subprocess.Popen([sys.executable,f],creationflags=DETACHED_PROCESS).pid
# pid = subprocess.Popen([sys.executable,f],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
class NotEligible(Exception):
    def __init__(self, msg):
        self.message = msg


class QuantityExceededException(Exception):
    def __init__(self, msg):
        self.message = msg


age = int(input('Enter User Age \t:\t'))
if age>18:
    quantity = int(input('Enter No.of Items \t:\t'))
    if quantity < 6:
        pass
    else:
        raise QuantityExceededException("Maximum quantity reached")
else:
    raise NotEligible("You're not eligible for taking wine")
