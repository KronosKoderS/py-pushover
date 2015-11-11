from setuptools import setup, find_packages

install_requires = ['requests', 'websocket-client']

version = '0.1'

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description=''

setup(
    name='py_pushover',
    packages=['py_pushover'],
    version=version,
    description='Object Oriented API calls to the Pushover Service',
    long_description=long_description,
    url='https://github.com/KronosKoderS/py_pushover',
    download_url='https://github.com/KronosKoderS/py_pushover/tarball/v' + version,
    author='KronoSKoderS',
    author_email='superuser.kronos@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=install_requires,
    test_suite="tests.get_tests"
)
