from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "montecarlo_cpp",
        ["bindings.cpp", "montecarlo.cpp", "parametros.cpp"],
        cxx_std=17,
    ),
]

setup(
    name="montecarlo_cpp",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
