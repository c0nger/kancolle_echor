"""
this file can replace scheduler.bat ;-)

launcher made by conger.g (conger.g@gmail.com)

ver 0.2 : avoid minus time status
"""
import os,sys,time
from random import choice
sleep_time_file = r'sleep_time'


def version_info():
    print ("\nKancolle Expedition AutoBot;-) by Conger, Loader based on [niyuna / kancolle_echor project] in Github,")
    print ("Warning : This script is used at your own risk!!!")
    print ("https://github.com/niyuna/kancolle_echor\n")

def loop():
    while True:
        os.system("module.py")
        f = open(sleep_time_file,'r')
        try:
            result = f.readline()
            f.close()
        except:
            f.close()
            sys.exit(0)
        sleeptimer = float(result)
        print ("\n\nRe-Expedition will be start in %s second... please wait ;-)...\n\n"%sleeptimer)
        # to avoid anti-bot check
        r = range(15,30)
        r3 = choice(r)
        r2 = float(r3)
        print ("to avoid anti-autobot, random time %s sec gap delay added to sleeptimer.... Please Be Patient!\n\n"%r2)
        #avoid minus time, go to default safe sleep mode
        if sleeptimer<0:
            print ("Warning! sleeptimer is something wrong ;-( switch to safe sleeptimer Mode..... it will be fine... dont'worry")
            time.sleep(600)
        #normal status
        if sleeptimer>0:
            time.sleep(sleeptimer)
        time.sleep(r2)


def main():
    version_info();
    loop();


if __name__ == '__main__':
    main()
