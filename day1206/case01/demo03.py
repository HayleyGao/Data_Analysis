import time
import pandas as pd
from datetime import datetime


#https://woj.app/5586.html
#日期字符串转换为时间戳

mylist = ["23/03/2015 00:00"]
test = time.mktime(datetime.strptime(mylist[0], "%d/%m/%Y %H:%S").timetuple())
print(test)


