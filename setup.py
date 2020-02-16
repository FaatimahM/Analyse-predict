from setuptools import setup, find_packages

setup(
    name='Analyse-predict',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Predict_2:analysing-eskom-data',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<Dominic-byte>/<Analyse-predict>',
    author='<Dominic Sadie>',
    author_email='<domi.sadie@gmail.com>'
)