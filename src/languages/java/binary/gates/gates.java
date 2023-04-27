package binary.gates;

public class gates {
    
    public static boolean Not(boolean a) {
        return !a;
    }
    
    public static boolean And(boolean a, boolean b) {
        return a == b;
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
