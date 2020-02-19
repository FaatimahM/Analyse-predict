from setuptools import setup, find_packages

setup(
    name='Analyse-predict',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Predict_2:analysing-eskom-data',
    long_description=open('README.md').read(),
    install_requires=['numpy<=1.18.1','pandas<=1.0.1'],
    url='https://github.com/FaatimahM/Analyse-predict.git',
    author='Dominic Sadie Sizwe Bhembe Faatimah Mansoor Rirhandzu Mahlaule'
    author_email='domi.sadie@gmail.com sjbhembe@hotmail.com faatimahmansoor@gmail.com melva.rirhandzu@gmail.com'
)