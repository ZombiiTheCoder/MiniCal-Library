package binary.converter;

import binary.config.config;

public class converter {
    
    public static String BoolToString(boolean a) {

        String o = "0";
        if (a == true) { o = "1"; }
    
        return o;
    
    }
    
    public static String CompileString(boolean ... bool) {
    
        String[] ns = new String[config.BitLimit];
    
        for (int i = 0; i < bool.length; i++) {
    
            ns[i] = BoolToString(bool[i]);
    
        }
    
        StringBuilder s = new StringBuilder();

        for (String ch : ns) {
            s.append(ch);
        }
 
        // convert in string
        String string = s.toString();

        return string;
    
    }
    

}
