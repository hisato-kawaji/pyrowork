from setuptools import setup, find_packages

import os
import re

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()
CHANGES = open(os.path.join(HERE, 'CHANGES.rst')).read()
# Remove custom RST extensions for pypi
CHANGES = re.sub(r'\(\s*:(issue|pr|sha):.*?\)', '', CHANGES)
CHANGES = re.sub(r':ref:`(.*?) <.*>`', r'\1', CHANGES)

REQUIREMENTS = [
]

TEST_REQUIREMENTS = [
]

if __name__ == "__main__":
    setup(
        name='pyrowork',
        version='0.1.0',
        description='A simple devops framework to structurize AWS Serverless Architecture',
        long_description=README + '\n\n' + CHANGES,
        classifiers=[
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Development Status :: 4 - Beta',
            'Framework :: Pyramid',
            'Intended Audience :: System Administrators',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: System :: Systems Administration',
        ],
        license='MIT',
        author='Hisato Kawaji',
        author_email='hisato.kawaji@gmail.com',
        url='http://',
        keywords='pypi s3 cheeseshop package',
        platforms='any',
        zip_safe=False,
        include_package_data=True,
        packages=find_packages(exclude=('tests',)),
        ={
            'console_scripts': [
                'pyro = pyrowork.command:main'
            ],
        },
        install_requires=REQUIREMENTS,
        tests_require=REQUIREMENTS + TEST_REQUIREMENTS,
        test_suite='tests',
        extras_require={
        },
    )
