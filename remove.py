import os
import shutil
import time

path = "C:/Users/basag/OneDrive/Desktop/useless"
days = time.time()
print(days)
true=True
ctime=os.stat(path).st_ctime
dif=ctime-days

if(os.path.exists(path)== true & ctime > 300) :
    os.walk(path)
    os.path.join
    os.remove(path)

    
