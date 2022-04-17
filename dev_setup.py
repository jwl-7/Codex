"""Dev Setup

This module contains the setup scripts for initializing dev environment.
"""


import os
import subprocess
import sys
import textwrap


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_PATH = (
    os.path.join(PROJECT_DIR, 'venv', 'bin', 'python')
    if os.name == 'posix'
    else os.path.join(PROJECT_DIR, 'venv', 'Scripts', 'python.exe')
)


def setup_script(name):
    """Decorator to format output when running setup scripts."""
    def wrap(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'{name:.<27}', end='')
            print('✓    ' if not result else f'✗    {result}')
            return result
        return wrapper
    return wrap


@setup_script('Creating config.py')
def create_config():
    """Create config.py file."""
    config = textwrap.dedent('''\
    """Config

    This module contains the configuration constants for the discord bot.
    """


    bot = {
        'prefix': 'ENTER_COMMAND_PREFIX',
        'token': 'ENTER_API_TOKEN',
        'owner': ENTER_OWNER_ID
    }

    dictionary = {
        'token': 'ENTER_API_TOKEN'
    }
    ''')
    try:
        with open('config.py', 'x') as file:
            file.write(config)
    except FileExistsError:
        return 'config.py already exists'


@setup_script('Creating virtual env')
def create_virtual_environment():
    """Create / Activate virtual environment."""
    if (
        hasattr(sys, 'base_prefix')
        or os.path.isdir('venv')
        or 'VIRTUAL_ENV' in os.environ
    ):
        return 'venv already exists'

    subprocess.run(
        'python -m venv venv',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


@setup_script('Installing requirements')
def install_requirements(venv):
    """Install dependencies from requirements.txt."""
    subprocess.run(
        f'{venv} -m pip install --upgrade pip',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    subprocess.run(
        f'{venv} -m pip install -r requirements.txt',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def setup():
    """Initialize all setup scripts."""
    os.chdir(PROJECT_DIR)
    create_config()
    create_virtual_environment()
    install_requirements(VENV_PATH)


def main():
    setup()


if __name__ == '__main__':
    main()
