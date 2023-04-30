function Not(a) {
	let o = true
    if (a == true){
        o=false
    }
    return o
}

function And(a, b) {
	let o = false
    if (a == true && b == true){
        o = true
    }
    return o
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

module.exports = { Not, And, Nand, Nor, Or, Xor, Xnor }