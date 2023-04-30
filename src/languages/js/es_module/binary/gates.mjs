export function Not(a) {
	let o = true
    if (a == true){
        o=false
    }
    return o
}

export function And(a, b) {
	let o = false
    if (a == true && b == true){
        o = true
    }
    return o
}

export function Nand(a, b) {
	return Not(And(a, b))
}

export function Nor(a, b) {
	return And(Not(a), Not(b))
}

export function Or(a, b) {
	return Not(And(Not(a), Not(b)))
}

export function Xor(a, b) {
	return Or(And(Not(a), b), And(a, Not(b)))
}

export function Xnor(a, b) {
	return Not(Or(And(Not(a), b), And(a, Not(b))))
}
