#include "parametros.h"
#include <iostream>

void Parametros::entrada_datos() {
    std::cout << "Limite inferior (a): ";
    std::cin  >> limite_inferior;

    std::cout << "Limite superior (b): ";
    std::cin  >> limite_superior;

    std::cout << "Número de simulaciones: ";
    std::cin  >> tamano_muestra;

    std::cout << "Selecciona la funcion:\n";
    std::cout << "  1) f(x) = 1 / (e^x + e^-x)\n";
    std::cout << "  2) f(x) = 2 / (e^x + e^-x)\n";
    std::cout << "Opcion: ";
    std::cin  >> opcion_funcion;
}
