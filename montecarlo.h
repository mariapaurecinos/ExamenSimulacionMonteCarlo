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

        void set_parametros(double a, double b, int n, int opcion);
        std::vector<double> get_muestra_x() const;
        std::vector<double> get_valores_funcion() const;
        double get_resultado_integral() const;

    private:
        std::vector<double> muestra_x;
        std::vector<double> valores_funcion;
        double resultado_integral = 0.0;
};

#endif // MONTECARLO_H