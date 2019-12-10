import numpy as np
import pandas as pd

def exp1():
    data_arr = np.array(['a', 'b', 'c', 'd', 'e'])
    s = pd.Series(data_arr)
    print(s)

    print("\n----------------------------------------------\n")
    data = {'names': ['Suranjan Benarjee', 'Subramanyam Vegi', 'Sourabh Nath Agrawal', 'Sarosh Ahmed'],
            'age': [29, 25, 25, 24]}
    df = pd.DataFrame(data, index=['Elder-1', 'Elder-2', 'Elder-3', 'Younger'])
    print(df)

    print("\n----------------------------------------------\n")
    # data = {'Item-1' : pd.DataFrame(np.random.randn(4,3)),
    #         'Item-2' : pd.DataFrame(np.random.randn(4,2))}
    # p = pd.Panel(data)
    # print(p)


def exp2():
    df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
    df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    print(df)
    print(df['one'].isnull())
exp2()