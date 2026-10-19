//Nicolas Bahena Ostermaier
/****************

-Realizar un programa que simule la boleta de un estudiante.
-El nombre de las materias y la calificacion de las materias deberan
almacenarse en un arreglo string y otro int respectivamente.
-Las calificaciones de la materia se deberan generar de forma aleatoria
en un rango 5 a 10
-Al final debera mostrar la suma y el promedio de las calificaciones
-Imprimir un grafico de frecuencia por cada calificacion y el promedio final
Ejemplo:
Materia 1,9: ********
Materia 2,5: *****
Materia 3,7: ****
promedio 7: *******
*******************/

#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

int main(){

    srand(time(0));

    int i;
    cout << "Ingrese el numero de materias: ";
    cin >> i; cout << endl;

    string Materias[i];
    int Calificaciones[i], sum=0, promedio;

    for(int j=0; j<i; j++){
        cout << "Ingrese el nombre de la materia " << j+1 << ": ";
        cin >> Materias[j];
        Calificaciones[j] = rand() % 6 + 5;
        sum += Calificaciones[j];
    }

    promedio = sum / i;

    cout << endl;

    for(int j=0; j<i; j++){
        cout << Materias[j] << ": " << Calificaciones[j] << ": ";
        for(int n=0; n<Calificaciones[j]; n++){
            cout << "*";
        }
        cout << endl;
    }
    cout << "Promedio: " << promedio << ": ";
    for(int n=0; n<promedio; n++){
        cout << "*";
    }
    cout << endl;

    return 0;
}