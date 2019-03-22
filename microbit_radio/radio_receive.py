import time
import microbit

def receive_msg():
    try:

        r = microbit.radio.receive_bytes()

        if r != "None":
            #print(r)
            msg = r[len(r) - 20 : len(r) - 1]
            return msg
        
    except Exception as e: # reset radio on error
        print("reset %s" % str(e))
        microbit.radio.off()
        microbit.radio.on()
