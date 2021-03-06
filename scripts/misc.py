# misc utility function and thing that need to be done
import sys
from datetime import datetime
import pytz

def add_dates(input, o, start="", next=""):
    output = []
    nextDay = False
    prev = 0
    with open(input, 'r') as fin:
        for line in fin:
            tokens = line.split(':')
            hour = int(tokens[0])
            if (hour < prev):
                nextDay = True

            if (nextDay):
                output.append("%s %s" % (next, line))
            else:
                output.append("%s %s" % (start, line))
            prev = hour

    with open(o, 'w') as fout:
        for x in output:
            fout.write(x)

#add_dates(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

eastern = pytz.timezone("US/Eastern")
tt = '11-14-2012 19:27:31'
dt = datetime.strptime(tt, '%m-%d-%Y %H:%M:%S')
dt2 = eastern.localize(dt)
print int(dt2.strftime('%s')) * 1000
print '1352937156199'
