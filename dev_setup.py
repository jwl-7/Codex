"""Dev Setup

This module contains the setup scripts for initializing dev environment.
"""


import os
import subprocess
import sys
import textwrap


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def setup_script(name):
    """Decorator to format output when running setup scripts."""
    def wrap(func):
        def wrapper(*args, **kwargs):
            print(f'{name}...', end='')
            result = func(*args, **kwargs)
            print('✓') if not isinstance(result, Exception) else print(f'✗ {result}')
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
        with open('config.py', 'w') as file:
            file.write(config)
    except OSError as error:
        return error


@setup_script('Creating virtual environment')
def create_virtual_environment():
    """Create / Activate virtual environment."""
    subprocess.run('python -m venv venv', shell=True)
    if not hasattr(sys, 'base_prefix') or 'VIRTUAL_ENV' not in os.environ:
        venv = os.path.join('venv', 'bin', 'python')
        if os.name == 'nt':
            venv = os.path.join('venv', 'Scripts', 'python.exe')
        return venv


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
    venv = create_virtual_environment()
    install_requirements(venv)


def main():
    setup()


if __name__ == '__main__':
    main()
