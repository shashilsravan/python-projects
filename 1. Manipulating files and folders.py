import os
import shutil

# Reading from a file

# fo = open("my_file", "r")
# temp = fo.readline()
# while temp:
#     print(temp)
#     temp = fo.readline()
# fo.close()
# print("Done!")


# Writing to a file

# lis = [
#     "Hey!\n",
#     "Hello this is an example file\n",
#     "Made to ensure that my py program is working correct\n",
#     "Hope you have liked it\n",
#     "This is 5th line\n",
#     "so i am ending in 7th line\n",
#     "yeap in this line! Bye bye"
# ]
# fo = open("my_file", "w")
# fo.writelines(lis)
# fo.close()
# print("Done!")


# Appending to the file

# fo = open("my_file", "a")
# fo.write("\nGud morning from 8th line")
# fo.close()
# print("Done!")


#  Creating folder and moving files into it

# os.mkdir("New_Polder")
# shutil.move("my_file", "New_Polder\\my_file")
# print("Done!")
# You can use shutil.copy() to copy files


# Renaming files

# os.rename("New_Polder\\my_file", "New_Polder\\file.txt")
# print("Done!")


# Removing a file

# os.remove(file_name)
# print("Done!")