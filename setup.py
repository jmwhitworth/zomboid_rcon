from distutils.core import setup
setup(
    name = 'zomboid_rcon',
    packages = ['zomboid_rcon'],
    version = '0.1.0',
    license='GPL-3.0',
    description = 'Python class for interacting with Project Zomboid servers using RCON ',
    author = 'Jack Whitworth',
    author_email = 'jack@jackwhitworth.com',
    url = 'https://jackwhitworth.com',
    download_url = '',
    keywords = [
        'project-zomboid',
        'rcon',
        'project-zomboid-rcon'
    ],
    install_requires=[
        'dotenv',
        'rcon',
        'timeout_decorator'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)