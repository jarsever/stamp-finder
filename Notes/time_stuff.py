from datetime import datetime

x = datetime(1970,1,1)
print x
# 1970-01-01 00:00:00

y = datetime(1988,1,29)
print y
# 1988-01-29 00:00:00

print (y - x).total_seconds()
# 570412800.0

z = (y - x).total_seconds()
print datetime.fromtimestamp(int(z))
1988-01-28 17:00:00
