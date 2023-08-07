//10/07/2023
//Sacar promedio de 3 numeros
#include <iostream>
using namespace std;
int main()
{
    // Definimos las variables
    int numero1, numero2, numero3;
    float promedio;
    // Pedimos y guardamos los datos
    cout << "Ingrese el primer número: ";
    cin >> numero1;
    cout << "Ingrese el segundo número: ";
    cin >> numero2;
    cout << "Ingrese el tercer número: ";
    cin >> numero3;
    // Promediando los tres números ingresados.
    promedio = (numero1 + numero2 + numero3) / 3;
    // Imprimiendo la media aritmética de los tres números
    cout << "El promedio es: " << promedio;
    return 0;
}
//COMPLETADO