# from pathlib import Path
import os,sys, subprocess
DETACHED_PROCESS = 0x00000008
file_str ="test_file.py"
f =os.path.abspath(file_str)
# pid = subprocess.Popen([sys.executable,f],creationflags=DETACHED_PROCESS).pid
pid = subprocess.Popen([sys.executable,f],stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)