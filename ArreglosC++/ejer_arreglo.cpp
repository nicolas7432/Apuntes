//Nicolas Bahena Ostermaier
//Pedir al usuario 5 numeros enteros, guardarlos en un arreglo y 
//mostrarlos en orden inverso al que fueron ingresados.
//Utilizar ciclos para pedir y mostrar valores

#include<iostream>
using namespace std;

int main(){

    int num[5];

    for(int i=0;i<5;i++){
        cout << "Ingrese un numero entero: ";
        cin >> num[i];
    }

    cout << endl << "Orden inverso:" << endl;


    for(int i=4;i>=0;i--){
        cout << num[i] << endl;
    }

    return 0;
}