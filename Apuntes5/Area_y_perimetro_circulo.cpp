//Nicolas Bahena Ostermaier
//Apuntes 1 -Area y perimetro de un circulo
#include <iostream>
#include <cmath> //incluye funciones matematicas
#include <iomanip> //incluye funciones para formato de salida

using namespace std;

int main() {

    double radio, area, perimetro;

    cout << "Ingresa el radio del circulo: "; cin >> radio;

    //Calcular el area sin funciones matematicas
    area = 3.14151987552 * radio * radio;
    cout << "El area (sin funciones): " << area << endl;
    cout << "El area (sin funciones con formato): " << fixed << setprecision(1) << area << endl;

    area = M_PI * pow(radio, 2);
    cout << "El area (con funciones con formato): " << fixed << setprecision(1) << area << endl;

    perimetro = 2 * radio * M_PI;
    cout << "El perimetro es: " << fixed << setprecision(2) << perimetro << endl;

    return 0;
    

    
}