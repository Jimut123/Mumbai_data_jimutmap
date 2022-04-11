import os

for i in range(10):
    command = "git add Mumbai_00"+str(i)
    os.system(command)
    command = "Mumbai_00"+str(i)
    os.system("git commit -m {}".format(command))
    os.system("git push")


for i in range(10,30):
    command = "git add Mumbai_0"+str(i)
    os.system(command)
    command = "Mumbai_0"+str(i)
    os.system("git commit -m {}".format(command))
    os.system("git push")

