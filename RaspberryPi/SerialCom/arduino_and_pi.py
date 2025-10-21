#!/usr/bin/python
#coding: utf-8

import serial
import time
from threading import Thread

class Arduino(Thread) :
    #On Linux, ports look like this : "/dev/ttyACM0"
    #On Windows, it looks like this : "COM8" 
    def __init__(self,port="COM8",baudrate=9600) :
        Thread.__init__(self)
        self.api=serial.Serial(port,baudrate,timeout=1)
        self.on=True
        self.unicode_error=0
        self.msg="Rien reçu"
    def run(self) :
        while self.on :
            try :
                self.msg=self.api.read_until("#").decode()
                if self.msg!="#" :
                    print(self.msg)
            except UnicodeDecodeError :
                self.unicode_error+=1
    def send_msg(self,msg:str) :
        print(f"Sending data : {msg}")
        msg=msg+"#"
        self.api.write(bytes(msg,"utf-8"))
    def get_msg(self) :
        to_return=self.msg
        return to_return


if __name__=="__main__" :
    on = True
    while on :
        rah=Arduino()
        #rah.start()
        rah.send_msg("coucou")
        time.sleep(2)
        rah.send_msg("0")
        for i in range(0,10) :
            time.sleep(1)
            rah.send_msg(f"00:0{i+1}")
        rah.on=False
        #rah.join()
        on = False
