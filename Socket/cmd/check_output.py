import subprocess

while True:
    cmd = input("shell=> ")
    c = subprocess.check_output(cmd,shell=True).decode()
    print(c)
