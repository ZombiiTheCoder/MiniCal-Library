package converter

import (
	config "minical/binary/config"
	"strings"
)

func BoolToStr(a bool) string {

	o := ""
	if a == true {
		o = "1"
	}
	if a == false {
		o = "0"
	}

	return o

}

func StrToBool(a string) bool {

	o := false
	if a == "1" {
		o = true
	}

	return o

}

func CompileString(args ...bool) string {

	ns := make([]string, config.BitLimit())

	for i := 0; i < config.BitLimit(); i++ {

		ns = append(ns, BoolToStr(args[i]))

	}

	return strings.Join(ns, "")

}

func DecompileString(a string) []bool {

	ns := make([]bool, config.BitLimit())

	for i := 0; i < config.BitLimit(); i++ {

		ns = append(ns, StrToBool(strings.Split(a, "")[i]))

	}

	return ns

}
