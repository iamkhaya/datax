"""setup file"""


from setuptools import find_packages, setup

with open("requirements.txt", encoding="utf-8") as f:
    REQUIREMENTS = [dependency.strip() for dependency in f if dependency.strip()]

with open("version", encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(
    name="datax",
    version=VERSION,
    description="datax",
    long_description="datax library",
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
    ],
    author="Khayelihle Tshuma",
    author_email="khayelihle.tshuma@gmail.com",
    url="https://datax.com",
    keywords="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
)
