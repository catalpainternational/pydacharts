import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydacharts",
    version="0.0.1",
    author="Joshua Brooks",
    author_email="josh@catalpa.io",
    description="Pydantic models for Python - ChartJS integration",
    url="https://github.com/joshbrooks/pydacharts",
    project_urls={"Bug Tracker": "https://github.com/joshbrooks/pydacharts/issues"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pydacharts"},
    packages=setuptools.find_packages(where="pydacharts"),
    python_requires=">=3.7",
    install_requires=[
        "pydantic",
    ],
)
