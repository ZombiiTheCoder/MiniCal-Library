package binary.circuits;

import binary.config.config;
import binary.converter.converter;
import binary.gates.gates;

public class circuits{

    public static String adder(String a, String b, boolean carryIn){
        boolean[] bina = converter.DecompileString(converter.FixBinary(a));
        boolean[] binb = converter.DecompileString(converter.FixBinary(b));
    
        boolean[] sum = new boolean[config.BitLimit];
        int e = config.BitLimit-1;
        boolean carry=carryIn;
        for (int i=0; i<config.BitLimit; i++) {
            var sum1 = gates.Xor(bina[e], binb[e]);
            var sum2 = gates.Xor(sum1, carry);
            carry = gates.Or(gates.And(bina[e], binb[e]), gates.And(sum1, carry));
            sum[i]=sum2;
            e--;
        }
    
        return converter.CompileString(converter.ReverseList(sum));
    }
    
    public static String subtractor(String a, String b){
        boolean[] bina = converter.DecompileString(converter.FixBinary(a));
        boolean[] binb = converter.DecompileString(converter.FixBinary(b));
    
        boolean[] sum = new boolean[config.BitLimit];
        int e = config.BitLimit-1;
        boolean carry=false;
        for (int i=0; i<config.BitLimit; i++) {
            var sum1 = gates.Xor(gates.Not(bina[e]), binb[e]);
            var sum2 = gates.Xor(sum1, carry);
            carry = gates.Or(gates.And(gates.Not(bina[e]), binb[e]), gates.And(sum1, carry));
            sum[i]=gates.Not(sum2);
            e--;
        }
    
        return converter.CompileString(converter.ReverseList(sum));
    }

}