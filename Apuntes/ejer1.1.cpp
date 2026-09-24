//Nicolas Bahena Ostermaier
#include <iostream>
using namespace std;

int main() {

    //Definición o declaración de las variables
    double val1, val2, res;

    //Datos de entrada
    cout << "Valor No. 1: ";
    cin >> val1;
    cout << "Valor No. 2: ";
    cin >> val2;

    //Procesos parciales
    if (val1 < val2) {              //Si____________Entonces
        res = val1 + val2;
    }
    else {                          //SiNo
        if (val1 > val2) {          //Si____________Entonces
            res = val1 - val2;
        }
        else {                     //SiNo
            res = val1 * val2;
        }                          //FinSi
    }                              //FinSi
    
    //Datos de salida parciales
    cout << "Resultado = " << res;


    return 0;
}