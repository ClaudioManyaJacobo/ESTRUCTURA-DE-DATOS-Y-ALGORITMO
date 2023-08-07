//10/07/2023
//Sacar factorial de un numero
#include <iostream>
using namespace std;
int main()
{
    // Definimos las variables que se utilizaran
    int resultado, numero;
    // Soliticitamos al usuario que ingrese un numero
    cout << "Ingrese el número: ";
    cin >> numero;
    // Inicializamos la variables resultado en 1
    resultado = 1;
    // Iteramos desde 1 hasta el numero ingresado por el usuario
    for (int i = 1; i <= numero; i++)
    {
        resultado *= i; // Multiplicamos por i
    }
    // Imprimimos el valor de resultado
    cout << "El factorial de " << numero << " es: " << resultado << endl;

    return 0;
}
//COMPLETADO