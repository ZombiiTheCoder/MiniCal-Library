# import srcGrabber
def test():
    import os
    from tests.python.binary.converter import FixBinary
    from tests.python.binary.circuits import adder, subtractor
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("MiniCalLib(Python) Test")
    print("")
    print("Test Binary Elongator(Fixer)")
    actual=FixBinary("1010")
    expected="0000000000001010"
    print("Expected: "+expected+" == Actual: "+actual+" -> "+str(expected==actual))
    print("")
    print("Test Binary Adder")
    actual=adder("100101", "100011110", False)
    expected=FixBinary("101000011")
    print("Expected: "+expected+" == Actual: "+actual+" -> "+str(expected==actual))
    print("")
    print("Test Binary Subtractor")
    actual=subtractor("110100", "100101")
    expected=FixBinary("1111")
    print("Expected: "+expected+" == Actual: "+actual+" -> "+str(expected==actual))
    print("")

# srcGrabber.clean()