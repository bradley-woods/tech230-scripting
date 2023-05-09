import os

# Print something to the terminal
os.system('echo "Hello World!"')

# Manipulate directories
# 1. create directory variable
directory = "test_dir2"

# 2. path to the parent directory
parent_dir = "C:/Users/bradl/PycharmProjects/tech_230"

# 3. path to the created directory
path = os.path.join(parent_dir, directory)

# 4. create directory
# os.mkdir(path)
# print("Directory '% s' created" % directory)

# 5. make a new file
filename = "testfile.txt"
filepath = os.path.join(path, filename)

# 6. open the file, input the contents and write to it
with open(filepath, "w") as file1:
    toFile = "Contents of file are written here"
    file1.write(toFile)
print("File " + filename + " created in " + directory + " folder")
