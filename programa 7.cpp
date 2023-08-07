//10/07/2023
//Sacar la sumatoria de un numero
#include <iostream>
using namespace std;

int main() {
    //Declaracion de las variables y asigancion
    int numero, suma;
    suma = 0;

    // Solicita al usuario que ingrese un número
    cout << "Ingrese un número: ";
    cin >> numero;

    // Calcula la sumatoria de los divisores del número ingresado
    for (int i = 1; i <= numero; ++i) {
        if (numero % i == 0) {
            suma = suma + i; // Si el número i es divisor del número ingresado, se agrega a la sumatoria
        }
    }

    // Muestra el resultado de la sumatoria de los divisores
    cout << "\nLa sumatoria de sus divisores es " << suma;

    return 0;
}
//COMPLETADO