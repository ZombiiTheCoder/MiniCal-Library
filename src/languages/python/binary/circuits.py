try:
    from converter import *
    from config import *
    from gates import *
except:
    from src.languages.python.binary.converter import *
    from src.languages.python.binary.config import *
    from src.languages.python.binary.gates import *

def adder(a, b, carryIn):
    bina = DecompileString(FixBinary(a))
    binb = DecompileString(FixBinary(b))

    sum=[]
    e=BitLimit-1
    carry=carryIn
    for _ in range(BitLimit):
        sum1 = Xor(bina[e], binb[e])
        sum2 = Xor(sum1, carry)
        carry = Or(And(bina[e], binb[e]), And(sum1, carry))
        sum = sum+[sum2]
        e=e-1

    return CompileString(ReverseList(sum))

def subtractor(a, b):
    bina = DecompileString(FixBinary(a))
    binb = DecompileString(FixBinary(b))

    sum=[]
    e=BitLimit-1
    carry=0
    for _ in range(BitLimit):
        sum1 = Xor(Not(bina[e]), binb[e])
        sum2 = Xor(sum1, carry)
        carry = Or(And(Not(bina[e]), binb[e]), And(sum1, carry))
        sum = sum+[Not(sum2)]
        e=e-1

    return CompileString(ReverseList(sum))

# print(subtractor("1000", "1100"))