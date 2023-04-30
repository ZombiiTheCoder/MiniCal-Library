const { FixBinary } = require("./binary/converter.js")
const { adder, subtractor } = require("./binary/circuits.js")
let actual=""
let expected=""

console.log("MiniCalLib(Js (Node Modules)) Test")
console.log("")
console.log("Test Binary Elongator(Fixer)")
actual=FixBinary("1010")
expected="0000000000001010"
console.log("Expected: "+expected+" == Actual: "+actual+" -> "+String(expected==actual))
console.log("")
console.log("Test Binary Adder")
actual=adder("100101", "100011110", false)
expected=FixBinary("101000011")
console.log("Expected: "+expected+" == Actual: "+actual+" -> "+String(expected==actual))
console.log("")
console.log("Test Binary Subtractor")
actual=subtractor("110100", "100101")
expected=FixBinary("1111")
console.log("Expected: "+expected+" == Actual: "+actual+" -> "+String(expected==actual))
console.log("")