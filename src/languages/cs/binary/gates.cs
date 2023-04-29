namespace MinicallibGates{
    public partial class gates {
        
        public static bool Not(bool a) {
            bool o = true;
            if (a == true){
                o=false;
            }
            return o;
        }
        
        public static bool And(bool a, bool b) {
            bool o = false;
            if (a == true && b == true){
                o = true;
            }
            return o;
        }
        
        public static bool Nand(bool a, bool b) {
            return Not(And(a, b));
        }
        
        public static bool Nor(bool a, bool b) {
            return And(Not(a), Not(b));
        }
        
        public static bool Or(bool a, bool b) {
            return Not(And(Not(a), Not(b)));
        }
        
        public static bool Xor(bool a, bool b) {
            return Or(And(Not(a), b), And(a, Not(b)));
        }
        
        public static bool Xnor(bool a, bool b) {
            return Not(Or(And(Not(a), b), And(a, Not(b))));
        }
        

    }
}