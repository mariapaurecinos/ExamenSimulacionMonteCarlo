#ifndef MONTECARLO_H
#define MONTECARLO_H


#include "parametros.h"
#include <vector>
#include <random>
#include <iostream>
#include <cmath>

class MonteCarlo : public Parametros {
    public:
        double funcion(double x) const;
        double ejecutar_simulacion();
        std::vector<double> desplegar_simulacion() const;
        void imprimir_resultados() const;

    private:
        std::vector<double> muestra_x;
        std::vector<double> valores_funcion;
        double resultado_integral = 0.0;
};

#endif // MONTECARLO_H