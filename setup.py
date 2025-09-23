from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''This full will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != ""]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="ML",                # your project name
    version="0.1.0",
    author="Kamran Ansari",
    author_email="your_email@example.com",
    description="My ML project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)