from setuptools import find_packages,setup
from typing  import List 

x='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if x in requirements:
            requirements.remove(x)
            


setup(
    name='mlproject',
    version='0.0.1',
    author='srikeerthi',
    author_email='srikeerthibandi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)