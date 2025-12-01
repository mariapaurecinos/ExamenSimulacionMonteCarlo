#include "montecarlo.h"

double MonteCarlo::funcion(double x) const {
    double ex = std::exp(x);
    double emx = std::exp(-x);
    double denom = ex + emx;

    if (opcion_funcion == 2) {
        return 2.0 / denom;
    }
    return 1.0 / denom;
}

double MonteCarlo::ejecutar_simulacion() {
    muestra_x.clear();
    valores_funcion.clear();

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<double> dist(limite_inferior, limite_superior);

    double suma = 0.0;

    for (int i = 0; i < tamano_muestra; ++i) {
        double x = dist(gen);
        double fx = funcion(x);
        muestra_x.push_back(x);
        valores_funcion.push_back(fx);
        suma += fx;
    }

    const double PI = std::acos(-1.0);
    resultado_integral =
        (limite_superior - limite_inferior) *
        (suma / static_cast<double>(tamano_muestra)) *
        (2.0 / PI);

    return resultado_integral;
}

std::vector<double> MonteCarlo::desplegar_simulacion() const {
    return valores_funcion;
}

void MonteCarlo::imprimir_resultados() const {
    std::cout << "Resultado aproximado: "
              << resultado_integral << std::endl;
}
