//10/07/2023
//Conversion de grados
#include <iostream>
using namespace std;
int main()
{
    //Definicion de las variables
    float grados;
    int opcion1, opcion2;
    // Solicitar al usuario que elija la escala de temperatura de entrada
    cout << "Por favor, elige la escala de temperatura de entrada:" << endl;
    cout << "1. Celsius\n2. Fahrenheit\n3. Kelvin"<< endl; cin >> opcion1;
    // Realizamos las conversiones basadas en la opción de entrada
    switch (opcion1)
    {
    case 1:
        cout << "Has elegido Celsius. Ahora elige la escala a la que       deseas convertir:" << endl;
        cout << "1. Fahrenheit\n2. Kelvin"<< endl; cin >> opcion2;
        // Realizamos las conversiones basadas en la opción de salida
        switch (opcion2){
        case 1:
            cout << "Por favor, introduce los grados que deseas convertir:"; cin >> grados;
            cout << grados << " grados Celsius son " << grados * 9 / 5 + 32 << " grados Fahrenheit." << endl;
            break;
        case 2:
            cout << "Por favor, introduce los grados que deseas convertir:"; cin >> grados;
            cout << grados << " grados Celsius son " << grados + 273.15 << " grados Kelvin." << endl;
            break;}
        break;
    case 2:
        cout << "Has elegido Fahrenheit. Ahora elige la escala a la que deseas convertir:" << endl;
        cout << "1. Celsius\n2. Kelvin"<< endl; cin >> opcion2;
        // Realizamos las conversiones basadas en la opción de salida
        switch (opcion2){
        case 1:
            cout << "Por favor, introduce los grados que deseas convertir:"; cin >> grados;
            cout << grados << " grados Fahrenheit son " << (grados - 32) * 5 / 9 << " grados Celsius." << endl;
            break;
        case 2:
            cout << "Por favor, introduce los grados que deseas convertir:"; cin >> grados;
            cout << grados << " grados Fahrenheit son " << (grados - 32) * 5 / 9 + 273.15 << " grados Kelvin." << endl;
            break;}
        break;
    case 3:
        cout << "Has elegido Kelvin. Ahora elige la escala a la que deseas convertir:" << endl;
        cout << "1. Celsius\n2. Fahrenheit"<< endl; cin >> opcion2;
        // Realizamos las conversiones basadas en la opción de salida
        switch (opcion2){
        case 1:
            cout << "Por favor, introduce los grados que deseas convertir:"; cin >> grados;
            cout << grados << " grados Kelvin son " << grados - 273.15 << " grados Celsius." << endl;
            break;
        case 2:
            cout << "Por favor, introduce los grados que deseas convertir:"; cin >> grados;
            cout << grados << " grados Kelvin son " << (grados - 273.15) * 9 / 5 + 32 << " grados Fahrenheit." << endl;
            break;}
        break;
    default:
        cout << "Opción no válida. Por favor, elige una opción entre 1 y 3." << endl;
    }
    return 0;
}
//COMPLETADO