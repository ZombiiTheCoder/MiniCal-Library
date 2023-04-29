namespace minicallib_circuits{

    using minicallib_config;
    using minicallib_converter;

    public class circuits{

        public static String adder(String a, String b, boolean carryIn){
            boolean[] bina = minicallib_converter.converter.DecompileString(minicallib_converter.converter.FixBinary(a));
            boolean[] binb = minicallib_converter.converter.DecompileString(minicallib_converter.converter.FixBinary(b));
        
            boolean[] sum = new boolean[config.BitLimit];
            int e = minicallib_config.config.BitLimit-1;
            boolean carry=carryIn;
            for (int i=0; i<minicallib_config.config.BitLimit; i++) {
                var sum1 = gates.Xor(bina[e], binb[e]);
                var sum2 = gates.Xor(sum1, carry);
                carry = gates.Or(gates.And(bina[e], binb[e]), gates.And(sum1, carry));
                sum[i]=sum2;
                e--;
            }
        
            return minicallib_converter.converter.CompileString(minicallib_converter.converter.ReverseList(sum));
        }
        
        public static String subtractor(String a, String b){
            boolean[] bina = minicallib_converter.converter.DecompileString(minicallib_converter.converter.FixBinary(a));
            boolean[] binb = minicallib_converter.converter.DecompileString(minicallib_converter.converter.FixBinary(b));
        
            boolean[] sum = new boolean[minicallib_config.config.BitLimit];
            int e = minicallib_config.config.BitLimit-1;
            boolean carry=false;
            for (int i=0; i<minicallib_config.config.BitLimit; i++) {
                var sum1 = gates.Xor(gates.Not(bina[e]), binb[e]);
                var sum2 = gates.Xor(sum1, carry);
                carry = gates.Or(gates.And(gates.Not(bina[e]), binb[e]), gates.And(sum1, carry));
                sum[i]=gates.Not(sum2);
                e--;
            }
        
            return minicallib_converter.converter.CompileString(minicallib_converter.converter.ReverseList(sum));
        }

    }
}