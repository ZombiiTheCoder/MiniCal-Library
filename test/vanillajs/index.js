import { adder, subtractor } from "../../src/languages/vanillajs/binary/circuits.js"
import { FixBinary } from "../../src/languages/vanillajs/binary/converter.js"

let actual=""
let expected=""

console.log("MiniCalLib(Vanilla Js) Test")
console.log("\n")
console.log("Test Binary Elongator(Fixer)")
actual=FixBinary("1010")
expected="0000000000001010"
console.log("Expected: "+expected+" == Actual: "+actual+" -> "+String(expected==actual))
console.log("\n")
console.log("Test Binary Adder")
actual=adder("100101", "100011110", false)
expected=FixBinary("101000011")
console.log("Expected: "+expected+" == Actual: "+actual+" -> "+String(expected==actual))
console.log("\n")
console.log("Test Binary Subtractor")
actual=subtractor("110100", "100101")
expected=FixBinary("1111")
console.log("Expected: "+expected+" == Actual: "+actual+" -> "+String(expected==actual))
console.log("\n")



document.body.append("MiniCalLib(Vanilla) Test")
document.body.append(document.createElement("br"))
document.body.append(document.createElement("br"))
document.body.append("Test Binary Elongator(Fixer)")
actual=FixBinary("1010")
expected="0000000000001010"
document.body.append(document.createElement("br"))
document.body.append("Expected: "+expected+" == Actual: "+actual+" -> "+String(expected==actual))
document.body.append(document.createElement("br"))
document.body.append(document.createElement("br"))
document.body.append("Test Binary Adder")
document.body.append(document.createElement("br"))
actual=adder("100101", "100011110", false)
expected=FixBinary("101000011")
document.body.append("Expected: "+expected+" == Actual: "+actual+" -> "+String(expected==actual))
document.body.append(document.createElement("br"))
document.body.append(document.createElement("br"))
document.body.append("Test Binary Subtractor")
document.body.append(document.createElement("br"))
actual=subtractor("110100", "100101")
expected=FixBinary("1111")
document.body.append("Expected: "+expected+" == Actual: "+actual+" -> "+String(expected==actual))
document.body.append(document.createElement("br"))