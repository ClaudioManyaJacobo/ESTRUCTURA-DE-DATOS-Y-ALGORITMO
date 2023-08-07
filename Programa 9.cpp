//10/07/2023
//Resolver una ecuacion simple
#include <iostream>
using namespace std;

int main()
{
    // Definicion de las variables
    int x, resultado;

    // Obtener el valor para x
    cout << "RESOLVER LA SIGUIENTE ECUACION 2X(5X+3)+7X+(3X-2)" << endl;
    cout << "Ingrese el valor de X: ";
    cin >> x;

    // Resolvemos la ecuacion
    resultado = 2 * x * (5 * x + 3) + 7 * x + (3 * x - 2);

    // Mostrar el resultado
    cout << "El resultado es: " << resultado << endl;

    return 0;
}
//COMPLETADO