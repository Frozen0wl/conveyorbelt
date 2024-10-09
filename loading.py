import selfmade_interface as cps
import time
loading_gate1 = 5
loading_gate2 = 6
lg1 = loading_gate1
lg2 = loading_gate2


def start():
    cps.run(lg1)
    cps.run(lg2)
    
def stop():
    cps.stop(lg1)
    cps.stop(lg2)
    
    
def load():
    cps.unblock(lg1)
    print("unblocked")
    start()
    print("started")
    time.sleep(1)
    print("waiting")
    while(not cps.detect(lg1)):
        continue
    cps.block(lg1)
    time.sleep(3)
    stop()
    print("done")
    
load()
    
    