import os
import datetime
root_dir = 'test-root'
sub_dir = '/test-root-sub-dir'

def get_cwd():
    cwd = os.getcwd()
    print(cwd)


def create_dir():
    os.mkdir(root_dir)


def create_sub_dir():
    os.mkdir(root_dir + sub_dir)


def create_multiple_dirs():
    os.makedirs('sub1/sub2/sub3/sub4')


def remove_directory():
    os.rmdir(root_dir+sub_dir)


def remove_multiple_dirs():
    os.removedirs("sub1/sub2/sub3/sub4")


def rename_dir():
    os.rename(root_dir,'root-test')


def to_know_contents_of_dir():
    print(os.listdir())
    # print(os.listdir('.'))


def walk_dir():
    for dir_path, dir_names, file_nams in os.walk("."):
        print('Directory Path\t:\t',dir_path)
        print('Directory Name\t:\t',dir_names)
        print('File Name\t:\t',file_nams)


def stats_of_file():
    stats = os.stat('indian_cricket_captains.txt')
    # print(stats)
    print('Last Accessed Time :\t',datetime.datetime.fromtimestamp(stats.st_atime))
    print('Last Modified Time :\t',datetime.datetime.fromtimestamp(stats.st_mtime))
    print('Last Changed Time :\t',datetime.datetime.fromtimestamp(stats.st_ctime))


# create_dir()
# create_sub_dir()
# remove_directory()
# create_multiple_dirs()
# remove_multiple_dirs()
# rename_dir()
# get_cwd()
# to_know_contents_of_dir()
# walk_dir()
stats_of_file()