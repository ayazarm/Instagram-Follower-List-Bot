from difflib import Differ

from numpy import diff

myfile1 = input("Enter First File's name for compare : ")
myfile2 = input("Enter Second File's name for compare : ")

ch1 = myfile1.split(".")
ch2 = myfile2.split(".")

if ch1[1] == "txt" and ch2[1] == "txt":
    with open(myfile1) as file_1, open(myfile2) as file_2:
        differ = Differ()

        for line in differ.compare(file_1.readlines(), file_2.readlines()):
            print(line)
    
else:
    print("File format Eror !")

  