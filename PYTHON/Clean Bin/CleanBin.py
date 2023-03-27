import os
   
#* Clears  the bin
os.system('cmd /c "echo Y|PowerShell.exe -NoProfile -Command Clear-RecycleBin"')

#* Remove temporary files
for root, dirs, files in os.walk("C:\\Windows\\Temp"):
    for file in files:
        os.remove(os.path.join(root, file))
        