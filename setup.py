from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(name='Covid-19-Vigia',
      version='0.1',
      description='Aplicação de vigilância em tempo real do Coronavírus covid-19.',
      url='https://github.com/hudsonbrendon/calculator',
      author='Strong Moves Brothers',
      author_email='holzhausen.vitor@gmail.com',
      license='MIT',
      packages=['covid19Vigia', 'vigia'],
      zip_safe=False)
