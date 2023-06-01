import os, sys, time, base64, shutil, datetime

sys.path.append(os.path.abspath(".console"))
import console

def main():
  time.sleep(1)
  console.log("[{}] Running vhacks on linux ...".format(datetime.datetime.now().strftime("%H:%M:%S"))
  os.system("python2 vhacks.pyc")
main()
