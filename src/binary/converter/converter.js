import { config } from "../config/config.js"

function BoolToStr(a) {

	o = ""
	if (a == true) {
		o = "1"
	}
	if (a == false) {
		o = "0"
	}

	return o

}

function StrToBool(a) {

	o = false
	if (a == "1") {
		o = true
	}

	return o

}

function CompileString(...args) {

	ns = new String[config.BitLimit()]

	for (i = 0; i < config.BitLimit(); i++) {

		ns = append(ns, BoolToStr(args[i]))

	}

	returns.Join(ns, "")

}

function DecompileString(a) {

	ns = new Boolean[config.BitLimit()]

	for (i = 0; i < config.BitLimit(); i++) {

		ns = append(ns, StrToBool(a.split("")[i]))

	}

	return ns

}

const converter = {
    BoolToStr: BoolToStr,
    StrToBool: StrToBool,
    CompileString: CompileString,
    DecompileString: DecompileString
}

export { converter }