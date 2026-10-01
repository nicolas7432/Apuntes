//Nicolas Bahena Ostermaier
//Apunte3
/* Un almacen de pedidos por correo vende cinco productos, 
los precios son los siguientes:
-producto 1: $2.98
-producto 2: $4.50
-producto 3: $9.98
-producto 4: $4.49
-producto 5: $6.87

Escriba un programa que solicite el numero del producto y la cantidad vendida.
El programa debe determinar el precio de venta de cada producto, calcular y 
mostrar el valor total del producto vendido */

#include <iostream>
using namespace std;

int main() {

    int numPro, canVen;
    float preVen, valTot;

    cout << "Ingrese el numero del producto (1 al 5): ";
    cin >> numPro;
    cout << "Ingrsa la cantidad vendida: ";
    cin >> canVen;

    switch(numPro) {
        case 1: preVen = 2.98; break;
        case 2: preVen = 4.50; break;
        case 3: preVen = 9.98; break;
        case 4: preVen = 4.49; break;
        case 5: preVen = 6.87; break;
        default: preVen = 0; cout << "Error: El numero del producto debe estar entre 1 y 5" << endl;
    }

    cout << "El precio de venta del producto " << numPro << " es: $" << preVen << endl; 
    valTot = preVen * canVen;
    cout << "El total de la venta es: $" << valTot << endl;

    return 0;
}
