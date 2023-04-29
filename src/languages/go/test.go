package main

import (
	"fmt"
	"minicallib/binary/circuits"
	"minicallib/binary/converter"
	"strconv"
	"strings"
)

func main() {
	actual := ""
	expected := ""

	fmt.Println("MiniCalLib(Cs) Test")
	fmt.Println("")
	// fmt.Println("Test Binary Elongator(Fixer)")
	// actual = converter.FixBinary("1010")
	// expected = "0000000000001010"
	// fmt.Println("Expected: " + expected + " == Actual: " + actual + " -> " + strconv.FormatBool(strings.Contains(expected, actual)))
	// fmt.Println("")
	fmt.Println("Test Binary Adder")
	actual = circuits.Adder("100101", "100011110", false)
	expected = converter.FixBinary("101000011")
	fmt.Println("Expected: " + expected + " == Actual: " + actual + " -> " + strconv.FormatBool(strings.Contains(expected, actual)))
	fmt.Println("")
	// fmt.Println("Test Binary Subtractor")
	// actual = circuits.Subtractor("110100", "100101")
	// expected = converter.FixBinary("1111")
	// fmt.Println("Expected: " + expected + " == Actual: " + actual + " -> " + strconv.FormatBool(strings.Contains(expected, actual)))
	// fmt.Println("")
}
