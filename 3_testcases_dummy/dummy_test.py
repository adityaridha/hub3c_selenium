import time
from datetime import datetime

print(time.localtime(time.time()))

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


print(datetime.now())
