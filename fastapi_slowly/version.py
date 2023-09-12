# fastapi_slowly/version.py

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import tomllib  # new in Python 3.11

def get_version():
    try:
        package_version = version(__package__)
    except PackageNotFoundError:
        pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
        with open(pyproject_path, "rb") as pyproject:
            toml = tomllib.load(pyproject)
            package_version = toml["tool"]["poetry"]["version"]
    return package_version
