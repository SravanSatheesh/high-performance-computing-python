from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "dft_openmp_win",
        sources=["dft_openmp_win.pyx"],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-fopenmp"],
    )
]

setup(
    name="dft_openmp_win",
    ext_modules=cythonize(
        extensions,
        compiler_directives={'language_level': "3"}
    )
)