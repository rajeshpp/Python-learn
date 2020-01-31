#!/usr/bin/env python
import time
d,e={},{}
input_file="file.txt"

for n,l in enumerate(open(input_file)):
    line=[i.strip() for i in l.strip().split(",")][0].split('_')[2:]
    dates,times=line[0],line[1].split('.')[0]
    day,month,year,hours,minutes,seconds=int(dates[0:2]),int(dates[2:4]),int(dates[4:]),int(times[0:2]),int(times[2:4]),int(times[4:])
    t = time.mktime( (year,month,day,hours,minutes,seconds,0,0,0))
    combined_time=dates+times
    d.setdefault(combined_time,[])
    d[combined_time].append(t)
    e[t]=combined_time

date_string=e[max(e)][0:8]+'_'+e[max(e)][8:]
print(date_string)