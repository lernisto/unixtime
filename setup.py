import subprocess
from glob import glob
from os.path import splitext, basename

import setuptools


def get_version():
    try:
        git = subprocess.Popen(
            ["git", "describe", "--always", "--dirty"], stdout=subprocess.PIPE
        )
        stdout, stderr = git.communicate()
        gitlabel = stdout.decode().strip()
        with open("VERSION", "w") as fo:
            fo.write(gitlabel)
    except OSError:
        with open("VERSION", "r") as fo:
            gitlabel = fo.read()

    return gitlabel


setuptools.setup(
    version=get_version(),
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
)
