//Nicolas Bahena Ostermaier
//Apunte 1. Arreglos
#include<iostream>
using namespace std;

int main(){

    //Arreglo con valores iniciales
    int c[] = {12,3,27,16,4,51,8,40};
    
    cout << c[0] << endl;
    cout << c[1] << endl;
    cout << c[2] << endl;
    cout << c[3] << endl;
    cout << c[4] << endl;
    cout << c[5] << endl;
    cout << c[6] << endl;
    cout << c[7] << endl;

    //Arreglo sin valores iniciales
    string materias[5];

    cout << "Ingrese la materia 1: ";
    cin >> materias[0];

    cout << "Ingrese la materia 2: ";
    cin >> materias[1];

    cout << "Ingrese la materia 3: ";
    cin >> materias[2];

    cout << "Ingrese la materia 4: ";
    cin >> materias[3];

    cout << "Ingrese la materia 5: ";
    cin >> materias[4];

    cout << materias[0] << endl;
    cout << materias[1] << endl;
    cout << materias[2] << endl;
    cout << materias[3] << endl;
    cout << materias[4] << endl;

    int i;
    cout << "Ingresa el numero de materia que quieres mostrar: ";
    cin >> i;
    cout << materias[i-1];

    return 0;
}