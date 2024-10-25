from setuptools import setup, find_packages

setup(
    name="zibal_payment",
    version='0.1.0',
    author='Mohammad Eslami',
    description='A simple and secure Python package for integrating online payment processing in Django projects.',
    long_description=open('docs/pypi.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mohammad222PR/zibal_payment',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests>=2.25.0",
    ],
    keywords='payment gateway django integration online payments',
)
