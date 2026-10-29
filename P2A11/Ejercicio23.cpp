//Nicolas Bahena Ostermaier
/*
 Realizar un programa para calcular la velocidad (en m/s) de los corredores de la carrera de 1.500
metros. La entrada consistirá en los minutos y segundos, que dan el tiempo del corredor; por
cada corredor, el programa debe visualizar el tiempo en minutos y segundos, así como la
velocidad media.
*/

#include<iostream>
using namespace std;

int main(){

    int min;
    int seg;
    int s2;
    float v;
    int i = 1;
    
    cout << "Carrera de 1500m" << endl << endl;

    while(true){
        cout << "Jugador " << i << endl;
        cout << "minutos: ";
        cin >> min;
        cout << "segundos: ";
        cin >> seg;

        if (min == 0 && seg == 0) {
            break; 
        }

        s2 = min * 60 + seg;
        v = 1500.0 / s2; 
        
        cout << "Velocidad media: " << v << " m/s" << endl << endl;
        
        i += 1;
    }

    cout << "Programa finalizado." << endl;
    return 0;
}