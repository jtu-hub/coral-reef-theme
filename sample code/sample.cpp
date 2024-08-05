#include <iostream>
#include "sample.h"

#define DUMMY_CONSTANT 5
#define DUMMY_MACRO(x) ((x)*(x))

/**
 * Comment block
 * \param to describe a parameter
 * TODO: a todo
 * TODO(name): a todo set by someone
*/

//inline comment 
//TODO: a todo
//TODO(name): a todo set by someone

using namespace std;

class Base {
    protected:
        int _property;
    public:
        virtual volatile Base(int a);
        virtual void print();

        static int friendFunc(Base b) {return b._property;}

        virtual const int getProperty() const {return _property};
};

Base::Base(int a) {
    this->_property = a;

    std::cout << "Base constructor with value " << a << std::endl;
}

//templated class with inheritance
template <typename T> class Array : public Base {
private:
    T* ptr;
    int size;
 
public:
    Array(T arr[], int s);
    
    void print() override;
};



 
template <typename T> Array<T>::Array(T arr[], int s) : Base(s) {
    ptr = new T[s];
    size = s;
    for (int i = 0; i < size; i++)
        ptr[i] = arr[i];
}
 
template <typename T> void Array<T>::print() {
    for (int i = 0; i < size; i++)
        cout << " " << *(ptr + i);
    cout << endl;
}


int main(int argc, char** argw) {
    int arr[5] = { 1, 2, 3, 4, 5 };
    Array<int> a(arr, 5);
    a.print();
    return 0;
}