import glob
import os
import pathlib

ropar = r"C://Users/sbrstrkkdwmdr/AppData/Local/osu!/Skins/test/-     sbrstrkkdw v15 [- h]"

print("Please select the exact folder location of your osu! skin")
print("(eg. C:/Users/sbrstrkkdwmdr/AppData/Local/osu!/Skins/skin_name)")
ropar = input('')

os.chdir(ropar)

check_files_keep = glob.glob("*@2x.png")

for text in check_files_keep:
    sdVersion = ropar + "/" + text.replace('@2x.png', '.png')
    exists = os.path.exists(sdVersion)
    if exists:
        print('deleting: ' + sdVersion)
        pathlib.Path.unlink(sdVersion)