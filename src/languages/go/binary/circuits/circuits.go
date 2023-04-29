package circuits

import (
	"minicallib/binary/config"
	"minicallib/binary/converter"
	"minicallib/binary/gates"
)

func Adder(a, b string, carryIn bool) string {
	bina := converter.DecompileString(converter.FixBinary(a))
	binb := converter.DecompileString(converter.FixBinary(b))

	sum := make([]bool, config.BitLimit())
	e := config.BitLimit() - 1
	carry := carryIn
	for i := 0; i < config.BitLimit(); i++ {
		sum1 := gates.Xor(bina[e], binb[e])
		sum2 := gates.Xor(sum1, carry)
		carry = gates.Or(gates.And(bina[e], binb[e]), gates.And(sum1, carry))
		sum[i] = sum2
		e--
	}

	return converter.CompileString(converter.ReverseList(sum))
}

func Subtractor(a, b string) string {
	bina := converter.DecompileString(converter.FixBinary(a))
	binb := converter.DecompileString(converter.FixBinary(b))

	sum := make([]bool, config.BitLimit())
	e := config.BitLimit() - 1
	carry := false
	for i := 0; i < config.BitLimit(); i++ {
		sum1 := gates.Xor(gates.Not(bina[e]), binb[e])
		sum2 := gates.Xor(sum1, carry)
		carry = gates.Or(gates.And(gates.Not(bina[e]), binb[e]), gates.And(sum1, carry))
		sum[i] = gates.Not(sum2)
		e--
	}

	return converter.CompileString(converter.ReverseList(sum))
}
