import subprocess as sub


system_drives = []

drives = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]

cmd = sub.check_output("net share",shell=True).decode()

for i in drives:
    if i in str(cmd):
        system_drives.append(i)

print(system_drives)
