import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

data_in_array = []

with open("allcaps.all.last.txt", "r") as fileData:
    data_in_array = fileData.readlines()


proper_data = [item.title() for item in data_in_array]

# print (proper_data)

with open("all.last.txt", "w") as output_file:
    for item in proper_data:
        output_file.write("{}".format(item))
        # output_file.write("\n".join(str(item) for item in proper_data)) <-avoids a trailing new line at the end, in theory, but causes program to hang