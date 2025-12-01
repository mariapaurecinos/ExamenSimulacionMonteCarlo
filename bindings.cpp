#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "montecarlo.h"

namespace py = pybind11;

PYBIND11_MODULE(montecarlo_cpp, m) {
    m.doc() = "Bindings C++ para MonteCarlo";

    py::class_<MonteCarlo>(m, "MonteCarlo")
        .def(py::init<>())
        .def("set_parametros", &MonteCarlo::set_parametros)
        .def("ejecutar_simulacion", &MonteCarlo::ejecutar_simulacion)
        .def("get_muestra_x", &MonteCarlo::get_muestra_x)
        .def("get_valores_funcion", &MonteCarlo::get_valores_funcion)
        .def("get_resultado_integral", &MonteCarlo::get_resultado_integral);
}
