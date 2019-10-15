
class Demo1:
    __current_company = 'ACT Fibernet'
    alexa = 'Amazon'                    # Static Variable
    def __init__(self):
        self.google_mini = 'Google'     # Instant Variable
        Demo1.act_tv = 'ACT Fibernet'   # Class Variable
        self.__current_company = 'Terralogic'
        print(id(self.__current_company))

    @classmethod
    def class_method(cls):
        print(cls.alexa)
        # print(cls.google_mini)
        print(cls.act_tv)

    @staticmethod
    def static_method():
        print(Demo1.alexa)
        # print(Demo1.google_mini)
        print(Demo1.act_tv)

# d= Demo1()
# d.static_method()
# d.class_method()
# Demo1.class_method()
# Demo1.static_method()
# print(Demo1.__current_company)
# print(d.google_mini)
# d.__current_company='Terralogic'
# print(id(d.__current_company))
# print(d.__current_company)

def assertion_exaple():
    for i in range(1,10):
        try:
            print(i)
            assert i>10,'i value greater than 10'
        except Exception as e:
            print(e)
            continue
assertion_exaple()