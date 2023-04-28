def Not(a) :
	o = True
	if a == True:
		o=False
	return o

def And(a, b) :
	o = False
	if a == True and b == True:
		o=True
	return o

def Nand(a, b) :
	return Not(And(a, b))


def Nor(a, b) :
	return And(Not(a), Not(b))


def Or(a, b) :
	return Not(And(Not(a), Not(b)))


def Xor(a, b) :
	return Or(And(a, Not(b)), And(Not(a), b))


def Xnor(a, b) :
	return Not(Xor(a, b))

