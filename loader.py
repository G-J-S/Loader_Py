import time
import sys

def load(char):
    time.sleep(0.3)
    sys.stdout.write("\r%s" % char )
    sys.stdout.flush()

loader = ["\\", "|", "/", "-"]

while(True):
    for i in range(len(loader)):
        load(loader[i])
