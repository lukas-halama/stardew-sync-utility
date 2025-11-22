# setup.py

from setuptools import setup, find_packages

# Load the version from sdv_sync/__init__.py
with open("sdv_sync/__init__.py", "r") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.strip().split("=")[1].strip().strip('"')
            break
    else:
        version = "0.0.0"

setup(
    name='stardew-sync-utility',
    version=version,
    packages=find_packages(),
    description='A utility to synchronize Stardew Valley saves between PC and mobile via cloud services.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name or GitHub Handle',
    url='https://github.com/lukas-halama/stardew-sync-utility',
    license='MIT',
    install_requires=[
        # No external dependencies needed yet, only standard library modules (os, subprocess, shutil)
    ],
    entry_points={
        # This creates the command 'sdv-sync-tool' that executes the main function in cli.py
        'console_scripts': [
            'sdv-sync-tool=sdv_sync.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Games/Entertainment',
        'Development Status :: 3 - Alpha',
    ],
)
