import sys, os, subprocess, math, random, datetime, json

# sys module
# print(sys.version) # version of Python you're using

# os module
# print(os.getcwd())
# os.chdir("C:/Users/bradl/PycharmProjects/tech_230/")
# print(os.getcwd())
# os.mkdir("C:/Users/bradl/PycharmProjects/tech_230/python_test")

# subprocess module
# subprocess.run(["python", "hello_world.py"]) # runs other programs

# math module
# pi = math.pi
# pi_string = str(pi)
# print("The value of pi is " + pi_string)

# random module
# randnum = random.randrange(1, 100) # random number between 1 and 100
# print(randnum)

# datetime module
# date = datetime.datetime.now()
# print(date)

# json module
x = {
    "name": "Bradley",
    "age": 27,
    "city": "London"
}

y = json.dumps(x) # convert python dict to json string
print(type(y))
