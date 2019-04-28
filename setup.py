from distutils.core import setup
setup(
    name='igloo',         # How you named your package folder (MyLib)
    packages=['igloo-python'],   # Chose the same as "name"
    version='0.9',
    license='MIT',
    description='Python client for igloo',
    author='Igloo Team',
    author_email='hello@igloo.ooo',
    url='https://github.com/IglooCloud/igloo_python',
    download_url='https://github.com/IglooCloud/igloo_python/archive/v_09.tar.gz',
    keywords=['iot', 'igloo'],
    install_requires=[
        'requests', 'asyncio', 'pathlib', 'websockets', 'aiodataloader'
    ],
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development ',
        'License :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
