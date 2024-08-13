from setuptools import find_packages, setup
from typing import List

def get_requirements(fill_path:str)->List[str]:
    requirement = []

    with open('requirements.txt') as file_obj:
        requirement = file_obj.readlines()
        [reg.replace("\n", "") for reg in requirement]
        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    
    return requirement

HYPEN_E_DOT = "-e ."
setup(
name='mlproject',
version='0.0.1',
authur='Tien',
author_email='thegioigiaitri2608@gmail.com',
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)