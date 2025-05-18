from setuptools import setup, find_packages

setup(
    name="safe_runner",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["psutil"],
    author="Mito",
    description="Safely run Python code under resource and time constraints.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)