from setuptools import setup, Extension
import sysconfig
import pybind11

functions_module = Extension(
    name='EntropyCodec',
    sources=['wrapper.cpp'],
    include_dirs=[
        sysconfig.get_paths()['include'],
        pybind11.get_include()
    ]
)

setup(
    ext_modules=[functions_module],
    options={"build_ext": {"build_lib": ".."}}
)