from setuptools import setup, find_packages

setup(
    name="comcat-cli",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'comcat=comcat.cli:main',
        ],
    },
    install_requires=[
        # List dependencies here, if any
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to concatenate text files from a folder into a single markdown file with stylish dividers.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/comcat-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
