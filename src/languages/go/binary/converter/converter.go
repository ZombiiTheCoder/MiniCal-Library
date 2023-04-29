package converter

import (
	"fmt"
	"minicallib/binary/config"
	"strconv"
	"strings"
)

func BoolToStr(a bool) string {

	o := "0"
	if a == true {
		o = "1"
	}

	return o

}

func StrToBool(a string) bool {

	o := false
	if strings.Contains(a, "1") {
		o = true
	}

	return o

}

func CompileString(args []bool) string {

	ns := make([]string, config.BitLimit())

	for i := 0; i < config.BitLimit(); i++ {

		ns = append(ns, BoolToStr(args[i]))

	}

	return strings.Join(ns, "")

}

func DecompileString(a string) []bool {

	ns := make([]bool, len([]rune(a)))
	for i := 0; i < len([]rune(a)); i++ {
		ns = append(ns, StrToBool(string([]rune(a)[i])))
	}
	return ns

}

func ReverseList(l []bool) []bool {
	e := len(l) - 1
	l2 := make([]bool, len(l))
	for i := 0; i < len(l); i++ {
		l2[e] = l[i]
		e--
	}
	return l2
}

func FixBinary(bin string) string {
	a := ReverseList(DecompileString(bin))
	a2 := make([]bool, config.BitLimit())
	fmt.Println(len(DecompileString(bin)))
	if config.BitLimit()-len(a) < 0 {
		fmt.Println("FATAL ERROR: Number Is Larger Than BitLimit " + strconv.Itoa(config.BitLimit()))
	}
	e := len(a)
	for i := 0; i < e; i++ {
		a2[i] = a[i]
	}
	if config.BitLimit()-e != 0 || config.BitLimit()-e > -1 {
		for i := 0; i < (config.BitLimit() - (e)); i++ {
			a2[i+(e)] = false
		}
	}
	return CompileString(ReverseList(a2))
}
