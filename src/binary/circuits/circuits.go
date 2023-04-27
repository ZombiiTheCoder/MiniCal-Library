package circuits

import (
	"minical/binary/converter"
	"minical/binary/gates"
)

func adder(a, b string, carry int) string {

	ba := converter.DecompileString(a)
	bb := converter.DecompileString(b)

	for i := 0; i < 0; i++ {
		s1 := gates.Xor(ba[i], bb[i])
	}

	return converter.CompileString(true, false)

}
