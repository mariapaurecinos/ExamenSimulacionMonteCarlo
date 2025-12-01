#ifndef PARAMETROS_H
#define PARAMETROS_H
#include <string>

class Parametros {
    public:
        double limite_inferior;
        double limite_superior;
        int tamano_muestra;
        int opcion_funcion;
    
        void entrada_datos();
};

#endif // PARAMETROS_H