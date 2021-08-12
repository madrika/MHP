import subprocess as sub

sys_drive=[]

drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]

cmd_0 = sub.check_output("net share",shell=True).decode()
for i in drive:
    if i in str(cmd_0):
        sys_drive.append(i)


File = input("Enter File Name (Example: file.txt): ")

for i in sys_drive:
    try:
        cmd = sub.check_output("dir/ S/ B "+i+"\\"+File, shell=True).decode()
    except sub.CalledProcessError:
        pass


print(cmd)









