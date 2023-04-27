function Not(a) {
	return !a
}

function And(a, b) {
	return a == b
}

function Nand(a, b) {
	return Not(And(a, b))
}

function Nor(a, b) {
	return And(Not(a), Not(b))
}

function Or(a, b) {
	return Not(And(Not(a), Not(b)))
}

function Xor(a, b) {
	return Or(And(Not(a), b), And(a, Not(b)))
}

function Xnor(a, b) {
	return Not(Or(And(Not(a), b), And(a, Not(b))))
}

const gates = {
    Not: Not,
    And: And,
    Nand: Nand,
    Nor: Nor,
    Or: Or,
    Xor: Xor,
    Xnor: Xnor
}

export { gates }