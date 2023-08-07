//10/07/2023
//Verificar si un numero es primo
#include <iostream>
using namespace std;
int main()
{
    int numero, contador;
    bool Esprimo;
    contador = 0;
    // Solicita al usuario que ingrese un número
    cout << "Ingrese un número: ";
    cin >> numero;
    // Itera desde 1 hasta el número ingresado
    for (int i = 1; i <= numero; i++)
    { 
        if (numero % i == 0)
        {
            contador++;
        }
    }
    // Verifica si es primo o no según la cantidad de divisores encontrados
    if (contador == 2)
    { // Un número primo solo tiene dos divisores: 1 y el número mismo
        Esprimo = true;
    } else
    {
        Esprimo = false;
    }
    // Imprime en pantalla si es primo o no
    if (Esprimo == true)
    {
        cout << "El número " << numero << ": SI ES PRIMO" << endl;
    } else
    {
        cout << "El número " << numero << ": NO ES PRIMO" << endl;
    }

    return 0;
}
//COMPLETADO