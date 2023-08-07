//20/07/2023
//Programa para obtener el rango en la que esta una nota (A, B, C, D, E)
#include <iostream>
#include <cmath>

using namespace std;
// Función para obtener la calificación en base a la nota 
string calificarNota(float nota) {
    if (nota >= 19 && nota <= 20) {
        return "A";
    } else if (nota >= 16 && nota <= 18) {
        return "B";
    } else if (nota >= 13 && nota <= 15) {
        return "C";
    } else if (nota >= 10 && nota <= 12) {
        return "D";
    } else if (nota >= 1 && nota <= 9) {
        return "E";
    } else {
        return "Fuera de rango";
    }
}

// Función para ajustar la nota en base a su parte decimal 
void RedondearNota(float& nota) {
    nota = ceil(nota);
}

int main() {
    // Definición de 10 notas
    float notas[] = {14.5, 17.2, 8.9, 18.1, 6.3, 16.9, 7.8, 13.6, 19.3, 10.7};

    // Ajustar la nota y obtener la calificación para cada nota y mostrar el resultado
    for (int i = 0; i < 10; ++i) {
        RedondearNota(notas[i]);
        string calificacion = calificarNota(notas[i]);
        cout << "Alumno " << (i + 1) << ": " << calificacion << endl;
    }

    return 0;
}
//COMPLETADO