import ast
import os
from typing import Optional

from setuptools import find_packages, setup


def get_version(file_name: str, version_name: str = "__version__") -> Optional[str]:
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                if node.targets[0].id == version_name:
                    return node.value.s
    raise ValueError(
        f"Couldn't find assignment to variable {version_name} in file {file_name}"
    )


class About(object):
    NAME = "contextual-logger"
    VERSION = get_version("contextual_logger/__init__.py")
    AUTHOR = "blester125"
    EMAIL = f"{AUTHOR}@gmail.com"
    URL = f"https://github.com/{AUTHOR}/{NAME}"
    DL_URL = f"{URL}/archive/{VERSION}.tar.gz"
    LICENSE = "MIT"
    DESCRIPTION = "Contextual Logger"


ext_modules = []


setup(
    name=About.NAME,
    version=About.VERSION,
    description=About.DESCRIPTION,
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    long_description_content_type="text/markdown",
    author=About.AUTHOR,
    author_email=About.EMAIL,
    url=About.URL,
    download_url=About.DL_URL,
    license=About.LICENSE,
    python_requires=">=3.6",
    packages=find_packages(),
    package_data={
        "contextual_logging": [],
    },
    include_package_data=True,
    install_requires=[],
    extras_require={
        "test": ["pytest"],
    },
    keywords=[],
    ext_modules=ext_modules,
    entry_points={
        "console_scripts": [],
    },
    classifiers={
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
    },
)
