from setuptools import setup

setup(
        name='barecli',
        version='0.0.5',
        description='barecli description',
        author='Author Name',
        author_email='author@email.xyz',
        url='project.url.org',
        license='Apache 2.0',
        py_modules=['barecli.cli'],
        install_requires=[
            'Click',
        ],
        entry_points='''
            [console_scripts]
            barecli=barecli:cli
        ''',
)
