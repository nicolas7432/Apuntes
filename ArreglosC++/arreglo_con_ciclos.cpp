//Nicolas Bahena Ostermaier
//Apunte 2. Arreglos con ciclos

#include<iostream>
using namespace std;

int main(){

    //Arreglo con valores iniciales
    int c[] = {12,3,27,16,4,51,8,40};

    for(int i=0;i<8;i++){
        cout << c[i] << endl;
    }

    //Areglo sin valores iniciales
    string materias[5];

    for(int i=0;i<5;i++){
        cout << "Ingrese la materia " << i+1 << ": ";
        cin >> materias[i];
    }

    for(int i=0;i<5;i++){
        cout << materias[i] << ", ";
    }

    return 0;
}