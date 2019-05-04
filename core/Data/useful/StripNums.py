import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

data_in_array = []

with open("dist.male.first.txt", "r") as fileData:
    data_in_array = fileData.readlines()


clean_data = [item.rstrip("123 .4567\n890") for item in data_in_array]

# print (clean_data)

with open("male.first.txt", "w") as output_file:
    for item in clean_data:
        output_file.write("{}\n".format(item))
        # output_file.write("\n".join(str(item) for item in clean_data)) <-avoids a trailing new line at the end, in theory, but causes program to hang