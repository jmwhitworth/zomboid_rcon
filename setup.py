from distutils.core import setup
setup(
    name = 'zomboid_rcon',
    packages = ['zomboid_rcon'],
    version = '0.2.0',
    license='GPL-3.0',
    description = 'Python class for interacting with Project Zomboid servers using RCON ',
    author = 'Jack Whitworth',
    author_email = 'jack@jackwhitworth.com',
    url = 'https://jackwhitworth.com',
    download_url = 'https://github.com/JMWhitworth/zomboid_rcon/archive/refs/tags/0.2.0.tar.gz',
    keywords = [
        'project-zomboid',
        'rcon',
        'project-zomboid-rcon'
    ],
    install_requires=[
        'python_dotenv',
        'rcon',
        'timeout_decorator'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',  # "3 - Alpha", "4 - Beta", "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)