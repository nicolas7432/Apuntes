//Nicolas Bahena Ostermaier
/**********************************
Funciones con return / con parametros
***********************************/
#include<iostream>
using namespace std;

int potencia2(int num){
    return num*num;
}
bool esPar(int num){
    if(num%2==0){
        return true;
    }
    else{
        return false;
    }
}
string calcularEdad(int anio){
    int edad = 2026 - anio;
    return "Tu edad es: " + to_string(edad) + " años";
}

int main(){

    //---- Funcion potencia2
    int x;
    x = potencia2(9); //llamada de funcion
    cout << "Potencia 2 de (9): " << x << endl;

    cout << "Potencia 2 de (15): " << potencia2(15) << endl;

    int numero;
    cout << "Ingresa un valor: "; cin >> numero;
    cout << "Potencia 2 de (" << numero << "): " << potencia2(numero) << endl;

    //--- Funcion esPar
    cout << "9 es par: " << esPar(9) << endl;
    cout << "62 es par: " << esPar(62) << endl;

    cout << boolalpha << "71 es par: " << esPar(71) << endl;
    cout << boolalpha << "28 es par: " << esPar(28) << endl;

    //--- Funcion calcularEdad
    int anioNac;
    cout << "Ingresa tu año de nacimiento: "; cin >> anioNac;
    cout << calcularEdad(anioNac) << endl;


    return 0;
}