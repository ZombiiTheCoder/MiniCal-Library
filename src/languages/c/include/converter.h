#ifndef converter_h
#define converter_h
#include <stdbool.h>

char BoolToStr(bool a);
char* CompileString(const bool * bits, ...);
bool StrToBool(char a);
bool* DecompileString(char* a);

#endif