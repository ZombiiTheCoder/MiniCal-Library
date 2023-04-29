import os
import shutil
import time
def clean():
    try:
        os.remove("test.jar")
        1+1
    except:
        1+1
def Grab():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    clean()
    os.chdir("../../../")
    os.system(".\comptest.bat")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system("clear")
    os.system("cls")

# Grab()