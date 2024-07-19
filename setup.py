# setup.py

from setuptools import setup, find_packages

setup(
    name="uvcl",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    tests_require=[
        'pytest',
    ],
    author="Andy Gatza",
    author_email="andy.gatza@gmail.com",
    description="UVCL, or the Universal VTR Control Library, is a serial control library to communicate with legacy VTRs and VCRs for integration in both small and large digitization projects",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/144a/Universal-VTR-Control-Library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)