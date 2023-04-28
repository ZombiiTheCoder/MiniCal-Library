const { BitLimit } = require("./config.js")

function BoolToStr(a){

	let o = "0"
	if (a == true){
		o = "1"
	}	

	return o
}


function StrToBool(a){

	let o = false
	if (a == "1"){
		o = true
	}

	return o
}

function CompileString(boolr){

	let ns = new Array(BitLimit)

	for (let i=0; i<BitLimit; i++) {
		ns[i] = BoolToStr(boolr[i])
	}

	return ns.join("")
}


function DecompileString(a){

	let ns = new Array(a.split("").length)
	for (let i=0; i<a.split("").length; i++) {
		ns[i] = StrToBool(a.split("")[i])
	}
	return ns
}

function ReverseList(l){
	let e=l.length-1
	let l2=new Array(l.length)
	for (let i=0; i<l.length; i++) {

		l2[e]=l[i]
		e=e-1
	}
	return l2
}

function FixBinary(bin){
	let a=ReverseList(DecompileString(bin))
	if (BitLimit-a.length < 0){
		console.error("FATAL ERROR: Number Is Larger Than BitLimit "+String(BitLimit))
	}
	const e= a.length
	a.length = BitLimit
	if (BitLimit-e != 0 || BitLimit-e <! 0){
		for (let i=0; i<(BitLimit-(e)); i++) {
			a[i+e]=false
	}
}
	return CompileString(ReverseList(a))
}

module.exports = { StrToBool, BoolToStr, CompileString, DecompileString, ReverseList, FixBinary }