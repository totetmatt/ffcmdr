from pathlib import Path
from setuptools import setup, find_packages

setup(
    name='ffcmdr',  # Replace with your package’s name
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    project_urls={
        "Source Code": "https://github.com/totetmatt/ffcmdr",
    },
    author='Matthieu Totet',  
    author_email='matthieu.totet@gmail.com',
    description='A helper library to manipulate and run FFmpeg command and filter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",

)