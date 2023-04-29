try:
    from config import *
except:
    from tests.python.binary.config import *

def BoolToStr(a):

	o = "0"
	if a == True:
		o = "1"
	

	return o



def StrToBool(a) :

	o = False
	if a == "1":
		o = True
	

	return o



def CompileString(*boolr):

	ns = []

	for i in range(BitLimit) :

		for q in boolr:
			ns = ns + [BoolToStr(q[i])]

	

	return "".join(ns)



def DecompileString(a):

	ns = []

	for i in range(len(list(a))) :

		ns = ns + [StrToBool(list(a)[i])]

	return ns

def ReverseList(l):
	e=len(l)-1
	l2=[]
	for _ in range(len(l)):
		l2=l2+[l[e]]
		e=e-1
	return l2

def FixBinary(bin):
	a=ReverseList(DecompileString(bin))
	if BitLimit-len(a) < 0:
		print("FATAL ERROR: Number Is Larger Than BitLimit "+str(BitLimit))
		exit()
	if BitLimit-len(a) != 0 or not BitLimit-len(a) < 0:
		for _ in range(BitLimit-len(a)):
			a=a+[False]

	return CompileString(ReverseList(a))