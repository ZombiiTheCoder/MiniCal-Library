const { DecompileString, CompileString, FixBinary, ReverseList } = require("./converter.js")
const { BitLimit } = require("./config.js")
const { Not, And, Nand, Nor, Or, Xor, Xnor} = require("./gates.js")

function adder(a, b, carryIn){
    let bina = DecompileString(FixBinary(a))
    let binb = DecompileString(FixBinary(b))

    let sum = new Array(BitLimit)
    let e = BitLimit-1
    let carry=carryIn
	for (let i=0; i<BitLimit; i++) {
        var sum1 = Xor(bina[e], binb[e])
        var sum2 = Xor(sum1, carry)
        carry = Or(And(bina[e], binb[e]), And(sum1, carry))
        sum[i]=sum2
        e=e-1
    }

    return CompileString(ReverseList(sum))
}

function subtractor(a, b){
    let bina = DecompileString(FixBinary(a))
    let binb = DecompileString(FixBinary(b))

    let sum = new Array(BitLimit)
    let e=BitLimit-1
    let carry=0
	for (let i=0; i<BitLimit; i++) {
        var sum1 = Xor(Not(bina[e]), binb[e])
        var sum2 = Xor(sum1, carry)
        carry = Or(And(Not(bina[e]), binb[e]), And(sum1, carry))
        sum[i]=Not(sum2)
        e=e-1
    }

    return CompileString(ReverseList(sum))
}

module.exports = { adder, subtractor }