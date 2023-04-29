package gates

func Not(a bool) bool {
	o := true
	if a == true {
		o = false
	}
	return o
}

func And(a, b bool) bool {
	o := false
	if a == true && b == true {
		o = true
	}
	return o
}

func Nand(a, b bool) bool {
	return Not(And(a, b))
}

func Nor(a, b bool) bool {
	return And(Not(a), Not(b))
}

func Or(a, b bool) bool {
	return Not(And(Not(a), Not(b)))
}

func Xor(a, b bool) bool {
	return Or(And(Not(a), b), And(a, Not(b)))
}

func Xnor(a, b bool) bool {
	return Not(Or(And(Not(a), b), And(a, Not(b))))
}
