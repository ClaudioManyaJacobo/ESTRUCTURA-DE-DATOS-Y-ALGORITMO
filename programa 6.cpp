//10/07/2023
//Sacar serie fibonacci
#include <iostream>
using namespace std;

int main() {
    //Declaracion de las variables y asignacion
    int numero, num1 = 0, num2 = 1, suma;

    // Solicita al usuario que ingrese un número
    cout << "Ingrese un número: ";
    cin >> numero;

    cout << "La serie Fibonacci hasta el numero " << numero << " es: " << endl;

    // Imprime el primer número de la serie Fibonacci, que es 0
    cout << num1 << endl;

    // Verifica si el número ingresado es mayor a 1 para continuar con la serie Fibonacci
    if (numero > 1) {
        
        // Imprime el segundo número de la serie Fibonacci, que es 1
        cout << num2;

        // Calcula y muestra los siguientes números de la serie Fibonacci hasta el número ingresado
        for (int i = 3; i <= numero; i++) {
            suma = num1 + num2; // Calcula el siguiente número de la serie sumando los dos números anteriores
            cout << suma << endl; // Imprime el número calculado
            num1 = num2; // Actualiza el valor de num1 con el valor actual de num2
            num2 = suma; // Actualiza el valor de num2 con el valor actual de la suma
        }
    } 
    else 
    {
        cout << "El valor ingresado debe de ser mayor a 1."; // Mensaje de error si el número ingresado es 1 o menor
    }

    return 0;
}
//COMPLETADO