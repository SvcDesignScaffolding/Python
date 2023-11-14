from setuptools import setup

setup(
    name="example_pkg",
    version="0.1.0",
    packages=["example_pkg"],
    package_dir={"example_pkg": "src/example_pkg"},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["fastapi", "pydantic", "pytest"],
    tests_require=["pytest", "pytest-cov"],
    package_data={
      "example_pkg": [ "tests/*.py" ],
    },
)
