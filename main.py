import importlib
import sys
from datetime import datetime

if __name__ == '__main__':
    print(sys.argv, len(sys.argv))



    if 1 == len(sys.argv):
        now = datetime.now()
        runDay = now.day
        runPart = 1
        runFile = 'example.txt'
    else:
        runDay = int(sys.argv[1])
        runPart = int(sys.argv[2])
        runFile = sys.argv[3]

    name = f'day{runDay:02d}'
    print(f'Running {name} part {runPart} from {runFile}')
    day = importlib.import_module(name + '.main')
    day.run(runPart, name+"/"+runFile)



