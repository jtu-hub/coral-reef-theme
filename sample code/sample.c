#include <stdlib.h>
#include "sample.h"

#define DUMMY_CONSTANT 5
#define DUMMY_MACRO(x) ((x)*(x))

/**
 * Comment block
 * \param to describe a parameter
 * TODO: a todo 
 * TODO(name): a todo set by someone
 * Note():
*/

//inline comment 
//TODO: a todo
//TODO(name): a todo set by someone

//struct
struct MyStruct {
    double a;
    char a1 : 3;
    char a2 : 5;
};

enum TestEnum {
    ZERO = 0,
    ONE,
    TWO
};

//function
int foo(int a, custom_t b) {
    printf("print something in %s, %d\n", a, __func__);

    int i = ZERO;

    return a + DUMMY_CONSTANT + i;
}

int main(int argc, char** argw) {
    custom_t temp = {5.2, 2, 10};
    int i;

    foo(20, temp);

    if(temp.a1 < 4) {
        temp.a = DUMMY_MACRO((double)temp.a1);
    } else {
        exit(EXIT_FAILURE);
    }

    for(int i=0; i<(int)temp.a2; i++) {
        printf("iter %d", i);
    }

    return EXIT_SUCCESS;
}