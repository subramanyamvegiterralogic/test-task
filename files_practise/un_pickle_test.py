from files_practise import employee
import pickle
f = open('emp.dat','rb')
print('Employee details')
obj = pickle.load(f)
obj.display()
# while True:
#     try:
#         pass
#     except EOFError as e:
#         print(e)
#     except Exception as e:
#         print(e)
f.close()
