from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from a given file,
    excluding any lines like "-e ."
    '''
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            if line and not line.startswith('-e'):
                requirements.append(line)
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Hamza',
    author_email='hamzaa.arifii@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
