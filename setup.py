import pathlib

from setuptools import find_packages, setup


here = pathlib.Path(__file__).parent.resolve()

readme = (here / "README.md").read_text(encoding="utf-8")
reqs = (here / "requirements.txt").read_text()
dev_reqs = (here / "requirements-dev.txt").read_text()


setup(
    name="python-project-template",
    version="0.0.1",
    author="JordanCHW",
    url="https://github.com/JordanCHW/python-project-template",
    description="Python sample project",
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=find_packages(exclude=("tests")),
    python_requires=">=3.9",
    install_requires=reqs,
    extras_require={"dev": dev_reqs},
)
