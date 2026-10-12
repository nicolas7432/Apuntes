//Nicolas Bahena Ostermaier
//Apunte 1
//Estructuras cíclicas
//1. do-while  (Repetir-Mientras)
//2. while     (Mientras)
//3.for        (Para)

#include <iostream>
using namespace std;

//Imprimir los numeros del 1 al 10
int main(){
    
    int numero;
    numero = 1;

    do{
        cout << numero << endl;
        numero = numero+1;
    }while(numero <= 10);

    return 0;
}