namespace minicallib{

    using System;
    using minicallib_circuits;
    using minicallib_converter;
    internal static class Program{

        [STAThread]
        static void Main(string[] args){
            string actual="";
            string expected="";
            
            Console.WriteLine("MiniCalLib(Java) Test");
            Console.WriteLine("");
            Console.WriteLine("Test Binary Elongator(Fixer)");
            actual=minicallib_converter.converter.FixBinary("1010");
            expected="0000000000001010";
            Console.WriteLine("Expected: "+expected+" == Actual: "+actual+" -> "+string.Format("%s", expected.contains(actual)));
            Console.WriteLine("");
            Console.WriteLine("Test Binary Adder");
            actual=minicallib_circuits.circuits.adder("100101", "100011110", false);
            expected=minicallib_converter.converter.FixBinary("101000011");
            Console.WriteLine("Expected: "+expected+" == Actual: "+actual+" -> "+string.Format("%s", expected.contains(actual)));
            Console.WriteLine("");
            Console.WriteLine("Test Binary Subtractor");
            actual=minicallib_circuits.circuits.subtractor("110100", "100101");
            expected=minicallib_converter.converter.FixBinary("1111");
            Console.WriteLine("Expected: "+expected+" == Actual: "+actual+" -> "+string.Format("%s", expected.contains(actual)));
            Console.WriteLine("");
        }

    }
}