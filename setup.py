from setuptools import setup, find_packages

setup(
    author="Anna Vidal Perez",
    description="Technical test for Clarity AI",
    name="clarity",
    version="0.1.0",
    packages=find_packages(include=["clarity", "clarity.*"]),
    install_requires=['datetime', 'pandas', 'time'],
    setup_requires=['wheel']
)