namespace minicallib_gates{
    public class gates {
        
        public static boolean Not(boolean a) {
            boolean o = true;
            if (a == true){
                o=false;
            }
            return o;
        }
        
        public static boolean And(boolean a, boolean b) {
            boolean o = false;
            if (a == true && b == true){
                o = true;
            }
            return o;
        }
        
        public static boolean Nand(boolean a, boolean b) {
            return Not(And(a, b));
        }
        
        public static boolean Nor(boolean a, boolean b) {
            return And(Not(a), Not(b));
        }
        
        public static boolean Or(boolean a, boolean b) {
            return Not(And(Not(a), Not(b)));
        }
        
        public static boolean Xor(boolean a, boolean b) {
            return Or(And(Not(a), b), And(a, Not(b)));
        }
        
        public static boolean Xnor(boolean a, boolean b) {
            return Not(Or(And(Not(a), b), And(a, Not(b))));
        }
        

    }
}