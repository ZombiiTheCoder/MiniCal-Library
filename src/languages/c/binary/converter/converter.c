#include "../../include/converter.h";
#include "../../include/config.h";

char BoolToStr(bool a){
    char o = '0';
    if (a == true) o = "1";
}

char* CompileString(const bool * bits, ...){

    char* out[BitLimit];

    for (int i = 0; i < BitLimit; i++) {

        out[i] = bits[i];

    }

    return out;
}

bool StrToBool(char a){
    bool o = false;
    if (a == "1") o = true;
}

bool* DecompileString(char* a){

}