import subprocess as sub

while True:
     ip = input("Enter IP: ")

     if ip=="Exit":
          break
     
     cmd = sub.check_output("ping -n 10 "+ip, shell=True).decode()

     print(cmd)
     print()
     print("____________________________")
     print()

     
