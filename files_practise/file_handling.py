captain_list= ['Ajinkya Rahane\n', 'Virat Kohli\n', 'Mahendra Singh Dhoni\n', 'Anil Kumble\n', 'Virender Sehwag\n', 'Rahul Dravid\n',
               'Sourav Ganguly\n', 'Sachin Tendulkar\n', 'Mohammad Azharuddin\n', 'Krishnamachari Srikkanth\n', 'Ravi Shastri\n',
               'Dilip Vengsarkar\n', 'Kapil Dev\n', 'Gundappa Viswanath\n', 'Bishan Singh Bedi\n', 'Sunil Gavaskar\n']


file_name = 'indian_cricket_captains.txt'
def write_line_to_file():
    try:
        f = open(file_name,'a')
        name = input('Enter Name of the Captains \t:\t')
        f.write(name+'\n')
    except Exception as e:
        print(e)
    finally:
        f.close()


def write_multiple_lines_to_file():
    try:
        f = open(file_name, 'a')
        f.writelines(captain_list)
    except Exception as e:
        print(e)
    finally:
        f.close()


def read_all_line_from_file(number_of_chars = 0, seek_pos=0):
    try:
        with open(file_name, 'r') as read_file:
            if number_of_chars >=1:
                # data = read_file.read(number_of_chars)
                # print(data)
                # print(read_file.tell())
                # read_file.seek(seek_pos)
                data = read_file.read(number_of_chars)
                print(data)
                print(read_file.tell())
                read_file.seek(80)
                print(read_file.tell())
                print(read_file.read(80))
                print(read_file.tell())
            else:
                data = read_file.read()
                print(data)
                print(read_file.tell())
    except Exception as e:
        print(e)


def read_line_from_file():
    try:
        with open(file_name, 'r') as read_file:
            data1 = read_file.readline()
            print(data1, end='')
            data2 = read_file.readline()
            print(data2, end='')
            # for data in read_file:
            #     print(data)
    except Exception as e:
        print(e)


def read_lines_from_file():
    try:
        with open(file_name, 'r') as read_file:
            data = read_file.readlines()
            print(data)
    except Exception as e:
        print(e)


# write_line_to_file()
# write_multiple_lines_to_file()
# read_line_from_file()
# read_lines_from_file()
# read_all_line_from_file(40,90)


import os, sys
def file_exists():
    try:
        if os.path.isfile(file_name):
            print(True)
            f = open(file_name, 'r')
        else:
            print(False)

        if os.path.exists(file_name):
            print(True)
        else:
            print(False)

        lcount = wcount = ccount = 0
        for line in f:
            lcount = lcount+1
            ccount = ccount + len(line)
            words = line.split()
            wcount = wcount + len(words)
        print('Line Counts\t:\t',lcount)
        print('Word Counts\t:\t',wcount)
        print('Char Counts\t:\t',ccount)

    except Exception as e:
        print(e)
file_exists()