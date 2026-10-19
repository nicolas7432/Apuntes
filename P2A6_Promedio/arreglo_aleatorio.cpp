//Nicolas Bahena Ostermaier
//Arreglo con valores aleatorios entre 50 y 100

#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

int main(){

    srand(time(0));

    int promedio, sum=0;
    int Aleatorios[5];

    for(int i=0; i<5; i++){
        Aleatorios[i] = rand() % 51 + 50;
        sum = sum + Aleatorios[i];
        cout << Aleatorios[i] << ", ";
    }

    promedio = sum / 5;
    cout << "\nEl promedio de los valores es: " << promedio << endl;
    

    return 0;
}