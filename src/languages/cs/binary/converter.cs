namespace MinicallibConverter{

    using System;
    using MinicallibConfig;
    public class converter {
        
        public static string BoolToStr(bool a) {

            string o = "0";
            if (a == true) { o = "1"; }
        
            return o;
        
        }

        public static bool StrToBool(string a) {

            bool o = false;

            if (a.Contains("1")) { o = true; }
        
            return o;
        
        }
        
        public static string Compilestring(params bool[] bools) {
        
            string[] ns = new string[config.BitLimit];
        
            for (int i = 0; i < bools.Length; i++) {
        
                ns[i] = BoolToStr(bools[i]);
        
            }
        
            string s = String.Join("", ns);

            return s;
        
        }
        
        public static bool[] Decompilestring(string a){

            bool[] ns = new bool[a.Length];

            string[] ch = new string[a.Length]; 

            for (int i = 0; i < a.Length; i++) { 
                ch[i] = a[i].ToString(); 
            } 

            for (int i=0; i<ch.Length; i++) {
                ns[i] = StrToBool(ch[i]);
            }
            return ns;
        }
        
        public static bool[] ReverseList(bool[] l){
            int e=l.Length-1;
            bool[] l2= new bool[l.Length];
            for (int i=0; i<l.Length; i++) {
                l2[e]=l[i];
                e--;
            }
            return l2;
        }
        
        public static string FixBinary(string bin){
            bool[] a = ReverseList(Decompilestring(bin));
            bool[] a2 = new bool[config.BitLimit];
            if (config.BitLimit-a.Length < 0){
                Console.WriteLine("FATAL ERROR: Number Is Larger Than BitLimit "+string.Format("%s", config.BitLimit));
            }
            int e= a.Length;
            for (int i=0; i<e; i++){
                a2[i] = a[i];
            }
            if (config.BitLimit-e != 0 || config.BitLimit-e > -1){
                for (int i=0; i<(config.BitLimit-(e)); i++) {
                    a2[i+(e)] = false;
                }
            }
            return Compilestring(ReverseList(a2));
        }


    }
}