//Nicolas Bahena Ostermaier
//Valores pseudo-aleatorios

#include<iostream>
#include<cstdlib> //funciones rand()
#include<ctime> //tiempo del sistema
using namespace std;

int main(){

    srand(time(NULL)); //semilla 

    int num;

    num = rand(); //genera un valor aleatorio y lo asigna a num

    cout << "Valor pseusdo-aleatorio: " << num << endl;

    //Valores entre 0 y 10
    num = rand() % 11;
    cout << "Valores entre 0 y 10: " << num << endl;

    //Valor entre 1 y 10
    num = rand() % 10 + 1;
    cout << "Valor entre 1 y 10: " << num << endl;

    //Valor entre 5 y 15
    num = rand() % 11 + 5;
    cout << "Valor entre 5 y 15: " << num << endl;

    //Valor enntre 180 y 220
    num = rand() % 41 + 180;
    cout << "Valor entre 180 y 220: " << num << endl;

    return 0;
}