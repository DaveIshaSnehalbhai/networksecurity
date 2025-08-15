'''
 The setup.py file is an essential  of packaging and distributing python projects.
 It is used by setuptools to define the configuration of your project, such as its
 metadata, dependencies and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                # Ignore empty lines and -e.
                if requirements and requirements!= '-e .':
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Isha Dave",
    author_email="ISDave003@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)