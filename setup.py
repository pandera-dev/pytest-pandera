from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

version = {}
with open("pytest_pandera/version.py") as fp:
    exec(fp.read(), version)


setup(
    name="pytest-pandera",
    version=version["__version__"],
    author="Niels Bantilan",
    author_email="niels.bantilan@gmail.com",
    description="A pytest plugin for pandas data testing with pandera.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pandera-dev/pytest-pandera",
    project_urls={
        "Issue Tracker": "https://github.com/pandera-dev/pytest-pandera/issues",
    },
    keywords=["pandas", "validation", "data-structures"],
    license="MIT",
    data_files=[("", ["LICENSE.txt"])],
    packages=["pytest_pandera"],
    install_requires=[
        "pandera >= 0.5.0",
        "pytest",
    ],
    python_requires=">=3.6",
    platforms="any",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
    ],
)
