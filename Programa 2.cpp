//10/07/2023
//Calculadora Basica
#include <iostream>
using namespace std;
int main()
{
    // Definimos nuestras variables
    float num1, num2, resultado;
    char operation;
    // Solicitamos los datos al usuario
    cout << "Ingrese el primer numero: ";
    cin >> num1;
    cout << "Ingrese el segundo numero: ";
    cin >> num2;
    cout << "Ingrese la operacion (+,-,* o /):";
    cin >> operation;
    // Realizamos la operacion correspondiente para la opcion seleccionada
    switch (operation)
    {
    case '+': resultado = num1 + num2;
        break;
    case '-':
        resultado = num1 - num2;
        break;
    case '*':
        resultado = num1 * num2;
        break;
    case '/':
        // Validamos el divisior entre 0
        if (num2 != 0)
        {
            resultado = num1 / num2;
        }
        else
        {
            cout << "Error! Division por cero" << endl;
        }
        break;
    default:
        cout << "Operador invalido" << endl;
        break;
    }
    // Mostramos el resultado
    cout << "\nEl Resultado es:" << resultado << "\n\n";

    return 0;
}
//COMPLETADO