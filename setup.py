"""

The setup.py file is essential part of packaging and distributing Python projects.
It is used by setuptool (or distutils in older Python versions) to define the
configuration of your project, such as its metadata, dependencies, and more

"""

# setup is a function from setuptools module that is used to define the configuration of your project
# find_packages is a function from setuptools module that automatically finds all packages in the project
from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    """
    This function returns a list of required packages for the project.
    """
    requirements: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore the empty lines and -e .
                if requirement and requirement != "-e .":
                    requirements.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirements


print(get_requirements())
setup(
    name="networkSystemML",
    version="0.0.1",
    author="Mohamed Tamer",
    author_email="mohamed.tamer.mtn@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
