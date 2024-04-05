import os
from notifypy import Notify


def notification():
    notify = Notify()
    notify.title = "OS Module Tutorial"
    notify.message = "Running the OS Module tutorial"
    notify.send()


def list_files():
    print(f"\nCurrent working directory : {os.getcwd()}\n")
    print("Available files :")
    for file in os.listdir():
        print(file)
    print()


def list_files_other_dir():
    path_ = input("Enter the path : ")
    os.chdir(path_)
    list_files()


if __name__ == "__main__":
    notification()
    list_files()
    list_files_other_dir()
