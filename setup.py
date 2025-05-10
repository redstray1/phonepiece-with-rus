from setuptools import setup,find_packages

requirements=[r.strip() for r in open("requirements.txt").readlines()]

setup(
   name='phonepiece',
   version='1.0.0',
   description='a multilingual phone tokenizer',
   author='Xinjian Li',
   author_email='xinjianl@cs.cmu.edu',
   url="https://github.com/redstray1/phonepiece-with-rus",
   packages=find_packages(),
   install_requires=requirements,
   package_data={'': ['*.csv', '*.tsv', 'tree.txt', 'pinyin2ipa.txt', 'model/latest/rus/*', 'model/latest/rus/g2p/*.csv']},
   include_package_data=True,
)
