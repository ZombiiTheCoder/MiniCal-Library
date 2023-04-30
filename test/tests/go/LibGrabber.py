import os
import shutil
def clean():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        shutil.rmtree(r"binary")
        os.remove("test.go")
        os.remove("go.mod")
    except:
        print("")
def Grab():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    clean()
    os.chdir("../../../")
    os.system(r"Xcopy src\languages\go\binary\ test\tests\go\binary /e /h /c /i")
    os.system(r"copy src\languages\go\test.go test\tests\go\test.go")
    os.system(r"copy src\languages\go\go.mod test\tests\go\go.mod")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system("go run .")
    os.system("clear")
    os.system("cls")
# Grab()
# clean()