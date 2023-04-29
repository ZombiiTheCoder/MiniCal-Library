namespace minicallib_converter{

    using System;
    using config;

    public class converter {
        
        public static String BoolToStr(boolean a) {

            String o = "0";
            if (a == true) { o = "1"; }
        
            return o;
        
        }

        public static boolean StrToBool(String a) {

            boolean o = false;
            if (a.contains("1")) { o = true; }
        
            return o;
        
        }
        
        public static String CompileString(params bool[] bools) {
        
            String[] ns = new String[config.BitLimit];
        
            for (int i = 0; i < bools.length; i++) {
        
                ns[i] = BoolToStr(bools[i]);
        
            }
        
            string s = ns.ToString();

            return s;
        
        }
        
        public static boolean[] DecompileString(String a){

            boolean[] ns = new boolean[a.length()];
            for (int i=0; i<a.split("").length; i++) {
                ns[i] = StrToBool(a.split("")[i]);
            }
            return ns;
        }
        
        public static bool[] ReverseList(bool[] l){
            int e=l.length-1;
            boolean[] l2= new boolean[l.length];
            for (int i=0; i<l.length; i++) {
        
                l2[e]=l[i];
                e--;
            }
            return l2;
        }
        
        public static String FixBinary(String bin){
            boolean[] a = ReverseList(DecompileString(bin));
            boolean[] a2 = new boolean[config.BitLimit];
            if (config.BitLimit-a.length < 0){
                Console.WriteLine("FATAL ERROR: Number Is Larger Than BitLimit "+string.Format("%s", config.BitLimit));
            }
            int e= a.length;
            for (int i=0; i<e; i++){
                a2[i] = a[i];
            }
            if (config.BitLimit-e != 0 || config.BitLimit-e > -1){
                for (int i=0; i<(config.BitLimit-(e)); i++) {
                    a2[i+(e)] = false;
                }
            }
            return CompileString(ReverseList(a2));
        }


    }
}