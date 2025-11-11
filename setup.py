from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement_lst = []  # ✅ Initialize the list

    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and '-e' lines
                if requirement and not requirement.startswith('-e'):
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

# print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Swaleha',
    author_email='swaleha@example.com',
    description='A package for Network Security',
    packages=find_packages(),
    install_requires=get_requirements()
)

