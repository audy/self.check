from setuptools import setup

setup(
    name='self_check',
    version='0.0.0',
    description='Check your self',
    url='http://github.com/audy/self_check',
    author='Austin Davis-Richardson',
    author_email='harekrishna@gmail.com',
    packages=['self_check'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'self-check = self_check.__init__:main'
        ]
    }
)
