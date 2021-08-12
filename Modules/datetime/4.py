from datetime import datetime
 
now = datetime.now()
 
t = now.strftime("%H:%M:%S")
print("time:", t)
