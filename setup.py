from setuptools import find_packages, setup

setup(
    name="xdays_journey",
    version="0.3.0",
    packages=find_packages(include=["xdays_journey"]),
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Japanese",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    url="https://github.com/pyconjp/x-days-journey",
    author="PyCon JP 2021 staff",
    author_email="pyconjp@pycon.jp",
    license="MIT license",
    zip_sage=False,
)
