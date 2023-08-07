//10/07/2023
//Crear y mostrar una matriz de f*c
#include <iostream>
using namespace std;
int main() {
    //Declaracion de las variables
    int filas, columnas;

    // Solicita al usuario que ingrese el número de filas y columnas de la matriz
    cout << "Ingrese el número de Filas: ";
    cin >> filas;
    cout << "\nIngrese el número de Columnas: ";
    cin >> columnas;

    // Declaración y asignación del valor a la matriz
    float Matriz[filas][columnas];
    cout << "Ingrese los elementos de la Matriz:" << endl;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            cout << "Elemento(" << i + 1 << " , " << j + 1 << "): ";
            cin >> Matriz[i][j];
        }
    }
    // Mostrar la matriz ingresada
    cout << "La matriz ingresada es:" << endl;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            cout << Matriz[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
//COMPLETADO