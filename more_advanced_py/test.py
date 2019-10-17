""" @Property Implementation"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def got_marks(self):
        print('PROPERTY')
        return self.name +' Obtained '+self.marks+' Marks '

    @got_marks.setter
    def got_marks(self, sentence):
        name, rand, marks = sentence.split(' ')
        print('SETUP')
        self.name = name
        self.marks = marks

    @got_marks.deleter
    def got_marks(self):
        self.name = None
        self.marks = None

def call_student():
    st = Student('Subramanyam.V','866')
    # print(st.name)
    # print(st.marks)
    # print(st.got_marks)
    # st.name = 'Vegi Subramanyam'
    # print(st.got_marks)
    st.got_marks = 'Subbu got 507'
    print(st.name)
    print(st.marks)
    print(st.got_marks)
    del st.got_marks
    print(st.name)
    print(st.marks)

# call_student()


""" Closures Implementation """
def closure_fun(up):
    val = 0
    def nested_fun(arg):
        print(up,'\t',arg)
        nonlocal val
        for i in range(up+1):
            val += i
        val *= arg
        print('Total is : {}'.format(val))
    return nested_fun
sum_value = closure_fun(10)
sum_value(5)
sum_value(25)
# del closure_fun
# sum_value()