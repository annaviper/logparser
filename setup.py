from setuptools import setup, find_packages

setup(
    author="Anna Vidal Perez",
    description="Parses log and returns connections to a host.",
    name="logparser",
    version="0.1.0",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['datetime', 'pandas', 'build', 'pytest'],
    setup_requires=['wheel'],
    test_requires=['pytest']
)