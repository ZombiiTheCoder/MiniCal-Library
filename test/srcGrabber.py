import os
import shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def clean():
    try:
        shutil.rmtree("src")
    except:
        print("")
clean()
os.chdir("../")
os.system("Xcopy src test\src /e /h /c /i")
os.chdir("test")
os.system("clear")
os.system("cls")