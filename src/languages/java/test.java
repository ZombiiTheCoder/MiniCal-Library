import binary.circuits.circuits;
import binary.converter.converter;

public class test {

    public static void main(String[] args) {
        
        String actual="";
        String expected="";
        
        System.out.println("MiniCalLib(Java) Test");
        System.out.println("");
        System.out.println("Test Binary Elongator(Fixer)");
        actual=converter.FixBinary("1010");
        expected="0000000000001010";
        System.out.println("Expected: "+expected+" == Actual: "+actual+" -> "+String.format("%s", expected.contains(actual)));
        System.out.println("");
        System.out.println("Test Binary Adder");
        actual=circuits.adder("100101", "100011110", false);
        expected=converter.FixBinary("101000011");
        System.out.println("Expected: "+expected+" == Actual: "+actual+" -> "+String.format("%s", expected.contains(actual)));
        System.out.println("");
        System.out.println("Test Binary Subtractor");
        actual=circuits.subtractor("110100", "100101");
        expected=converter.FixBinary("1111");
        System.out.println("Expected: "+expected+" == Actual: "+actual+" -> "+String.format("%s", expected.contains(actual)));
        System.out.println("");
    }
        
}    