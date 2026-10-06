//Nicolas Bahena Ostermaier
//Apunte 3 - Calcular el desglose de precio con IVA (16%)
#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    float precio, iva, subtotal, total;
    int cantidad;

    cout << "Precio del producto: $"; cin >> precio;
    cout << "Cantidad del producto: "; cin >> cantidad;

    subtotal = precio * cantidad;
    iva = subtotal * 0.16;
    total = subtotal + iva;

    cout << "Subtotal: $" << fixed << setprecision(2) << subtotal << endl;
    cout << "IVA: $" << fixed << setprecision(2) << iva << endl;
    cout << "Total: $" << fixed << setprecision(2) << total << endl;


    return 0;
}
