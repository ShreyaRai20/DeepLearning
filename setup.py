from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="Xray",
    version="0.0.1",
    author="Shreya Rai",
    author_email="shreya200199@gmail.com",
    install_requires=get_requirements("requirements.txt"),  # Pass file path here
    packages=find_packages(),
)
