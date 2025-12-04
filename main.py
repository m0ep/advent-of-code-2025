import importlib
import sys
from datetime import datetime

if __name__ == '__main__':
    print(sys.argv, len(sys.argv))
    if 1 == len(sys.argv):
        now = datetime.now()
        runDay = now.day
    else:
        runDay = int(sys.argv[1])

    name = f'day{runDay:02d}'
    print("run " + name)
    day = importlib.import_module(name + '.main')
    day.run(name)



