import subprocess

import glob
import os

ropar = [r"C://Users/sbrstrkkdwmdr/AppData/Local/osu!/Skins/test/-     sbrstrkkdw v15 [- h]"]

print("Please select the exact folder location of your osu! skin folder")
print("(eg. C:/Users/sbrstrkkdwmdr/AppData/Local/osu!/Skins)")
temp = input()

tempcurrent = os.getcwd()
os.chdir(temp)
ropar = glob.glob("*");
os.chdir(tempcurrent)

for pth in ropar: 
    child = subprocess.Popen(['python', 'removeSd.py'], stdin=subprocess.PIPE)
    tstr = temp + '/' + pth
    encoded = tstr.encode('utf-8')
    child.communicate(encoded)
