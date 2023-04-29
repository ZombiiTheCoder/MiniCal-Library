namespace MinicallibCircuits{

    using MinicallibConfig;
    using MinicallibConverter;
    using MinicallibGates;
    using System.Diagnostics;

    public class circuits{

        public static string adder(string a, string b, bool carryIn){
            bool[] bina = converter.Decompilestring(converter.FixBinary(a));
            bool[] binb = converter.Decompilestring(converter.FixBinary(b));
        
            bool[] sum = new bool[MinicallibConfig.config.BitLimit];
            int e = MinicallibConfig.config.BitLimit-1;
            bool carry=carryIn;
            for (int i=0; i<MinicallibConfig.config.BitLimit; i++) {
                bool sum1 = gates.Xor(bina[e], binb[e]);
                bool sum2 = gates.Xor(sum1, carry);
                carry = gates.Or(gates.And(bina[e], binb[e]), gates.And(sum1, carry));
                sum[i]=sum2;
                e--;
            }
        
            return converter.Compilestring(converter.ReverseList(sum));
        }
        
        public static string subtractor(string a, string b){
            bool[] bina = converter.Decompilestring(converter.FixBinary(a));
            bool[] binb = converter.Decompilestring(converter.FixBinary(b));
        
            bool[] sum = new bool[MinicallibConfig.config.BitLimit];
            int e = MinicallibConfig.config.BitLimit-1;
            bool carry=false;
            for (int i=0; i<MinicallibConfig.config.BitLimit; i++) {
                var sum1 = gates.Xor(gates.Not(bina[e]), binb[e]);
                var sum2 = gates.Xor(sum1, carry);
                carry = gates.Or(gates.And(gates.Not(bina[e]), binb[e]), gates.And(sum1, carry));
                sum[i]=gates.Not(sum2);
                e--;
            }
        
            return converter.Compilestring(converter.ReverseList(sum));
        }

    }
}