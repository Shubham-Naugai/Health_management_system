# Health management system
# clients :- Ryuk, harry, shubham

print("ID", "NAME\n"
      "1.", "RYUK\n"
      "2.", "HARRY\n"
      "3.", "SHUBHAM\n")
def getdate():
    import datetime
    return datetime.datetime.now()

def ryuk():
    y = input("Enter 1 for log data and 2 for retrieve data : ")
    if y == "1":
        x = input("Enter 1 for diet plan and 2 for exercise plan : ")
        if x == "1":
            f = open("Ryuk_diet.txt", "a")
            z = input("Type here\n")
            f.write("RYUK DIET PLAN\n"
            "[{}] : {}".format(getdate(), z))
            f.close()
        elif x == "2":
            f = open("Ryuk_exercise.txt", "a")
            z = input("Type here\n")
            f.write("RYUK EXERCISE PLAN\n"
            "[{}] : {}".format(getdate(), z))
            f.close()
    if y == "2":
        x = input("Enter 1 diet plan and 2 for exercise plan : ")
        if x == "1":
            f = open("Ryuk_diet.txt", "r")
            print(f.read())
            f.close()
        elif x == "2":
            f = open("Ryuk_exercise.txt", "r")
            print(f.read())
            f.close()

def harry():
    y = input("Enter 1 for log data and 2 for retrieve data : ")
    if y == "1":
        x = input("Enter 1 for diet plan and 2 for exercise plan : ")
        if x == "1":
            f = open("Harry_diet.txt", "a")
            z = input("Type here\n")
            f.write("HARRY DIET PLAN\n"
            "[{}] : {}".format(getdate(), z))
            f.close()
        elif x == "2":
            f = open("Harry_exercise.txt", "a")
            z = input("Type here\n")
            f.write("HARRY EXERCISE PLAN\n"
            "[{}] : {}".format(getdate(), z))
            f.close()
    if y == "2":
        x = input("Enter 1 diet plan and 2 for exercise plan : ")
        if x == "1":
            f = open("Harry_diet.txt", "r")
            print(f.read())
            f.close()
        elif x == "2":
            f = open("Harry_exercise.txt", "r")
            print(f.read())
            f.close()

def shubham():
    y = input("Enter 1 for log data and 2 for retrieve data : ")
    if y == "1":
        x = input("Enter 1 for diet plan and 2 for exercise plan : ")
        if x == "1":
            f = open("Shubham_diet.txt", "a")
            z = input("Type here\n")
            f.write("SHUBHAM DIET PLAN\n"
            "[{}] : {}".format(getdate(), z))
            f.close()
        elif x == "2":
            f = open("Shubham_exercise.txt", "a")
            z = input("Type here\n")
            f.write("SHUBHAM EXERCISE PLAN\n"
            "[{}] : {}".format(getdate(), z))
            f.close()
    if y == "2":
        x = input("Enter 1 diet plan and 2 for exercise plan : ")
        if x == "1":
            f = open("Shubham_diet.txt", "r")
            print(f.read())
            f.close()
        elif x == "2":
            f = open("Shubham_exercise.txt", "r")
            print(f.read())
            f.close()

r = input("Enter the ID or NAME whose data you want to log or retrieve : ")
if r == "1" or r == "ryuk":
    ryuk()
elif r == "2" or r == "harry":
    harry()
elif r== "3" or r == "shubham":
    shubham()
