from subprocess import check_output

def find_drive():

    drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:","K:","L:","X:","P:","U:","J:","S:","R:","W:","Q:","T:","Y:","I:","O:","V:","M:"]
    
    system_drive = []
    
    cmd = check_output("net share",shell=True)
    
    for i in drive:
        if i in str(cmd):
            system_drive.append(i)
    return system_drive


def find_files(drives):

    for d in drives:
        for p in Extension_Files:
            
            try:
                
                cmd = check_output("dir /S /B "+d+"\\"+"*."+p,shell=True).decode()
                f.writelines(cmd)
                print(p+"-------"+d)
                
            except:
                pass    
        
    f.close()

Extension_Files = ["jpg","txt","pdf"]
drives = find_drive()
f = open("File_Path.txt","w")
find_files(drives)
