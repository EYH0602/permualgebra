import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="permualgebra",  
    version="0.0.1",
    author="Yifeng He",
    author_email="yfhe@ucdavis.edu",
    description="Calculate the permutations with Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EYH0602/permualgbra",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
