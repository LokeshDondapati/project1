from setuptools import setup, find_packages

setup(
    name='Project1',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'pandas',
        # Other dependencies
    ],
    entry_points={
        'console_scripts': [
            # If your package includes any command-line scripts, you can define them here
        ],
    },
    author='Lokesh Dondapati',
    description='Project1',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/your-repository',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
