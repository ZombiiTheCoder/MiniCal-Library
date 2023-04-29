using System;
using MinicallibCircuits;
using MinicallibConverter;

namespace minicallib{
    internal static class Program{

        static void Main(string[] args){
            string actual="";
            string expected="";
            
            Console.WriteLine("MiniCalLib(Cs) Test");
            Console.WriteLine("");
            Console.WriteLine("Test Binary Elongator(Fixer)");
            actual=converter.FixBinary("1010");
            expected="0000000000001010";
            Console.WriteLine("Expected: "+expected+" == Actual: "+actual+" -> "+expected.Contains(actual).ToString());
            Console.WriteLine("");
            Console.WriteLine("Test Binary Adder");
            actual=circuits.adder("100101", "100011110", false);
            expected=converter.FixBinary("101000011");
            Console.WriteLine("Expected: "+expected+" == Actual: "+actual+" -> "+expected.Contains(actual).ToString());
            Console.WriteLine("");
            Console.WriteLine("Test Binary Subtractor");
            actual=circuits.subtractor("110100", "100101");
            expected=converter.FixBinary("1111");
            Console.WriteLine("Expected: "+expected+" == Actual: "+actual+" -> "+expected.Contains(actual).ToString());
            Console.WriteLine("");
        }

    }
}