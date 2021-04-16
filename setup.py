from setuptools import setup, find_packages, Extension
from numpy.distutils.misc_util import get_numpy_include_dirs


def grid_subsampling_ext():
    SOURCES = [
        "cpp_wrappers/cpp_utils/cloud/cloud.cpp",
        "cpp_wrappers/cpp_subsampling/grid_subsampling/grid_subsampling.cpp",
        "cpp_wrappers/cpp_subsampling/wrapper.cpp",
    ]

    ext = Extension(
        name="kpconv.grid_subsampling",
        sources=SOURCES,
        extra_compile_args=["-std=c++11", "-D_GLIBCXX_USE_CXX11_ABI=0"],
    )
    return ext


def radius_neighbors_ext():
    SOURCES = [
        "cpp_wrappers/cpp_utils/cloud/cloud.cpp",
        "cpp_wrappers/cpp_neighbors/neighbors/neighbors.cpp",
        "cpp_wrappers/cpp_neighbors/wrapper.cpp",
    ]

    ext = Extension(
        name="kpconv.radius_neighbors",
        sources=SOURCES,
        extra_compile_args=["-std=c++11", "-D_GLIBCXX_USE_CXX11_ABI=0"],
    )
    return ext


setup(
    name="kpconv",
    version="0.1.0",
    author="Hugues THOMAS",
    license="MIT",
    install_requires=[
        "matplotlib",
        "numpy",
        "torch",
        "scikit-learn",
    ],
    extras_require=dict(visualizer="mayavi"),
    packages=find_packages(),
    ext_modules=[
        grid_subsampling_ext(),
        radius_neighbors_ext(),
    ],
    include_dirs=get_numpy_include_dirs(),
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
    ],
)
