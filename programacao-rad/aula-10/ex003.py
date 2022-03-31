"""
import datetime
now = datetime.datetime.now()
print ("Data e hora atual: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
"""
from datetime import datetime

print(datetime.today())
print(datetime.today().strftime('%Y-%m-%d'))
