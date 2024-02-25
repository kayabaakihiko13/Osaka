from setuptools import setup
from os import path
import io
import platform

info = path.abspath(path.dirname(__file__))
with io.open(path.join(info, "requirements.txt"), encoding="utf-8") as file:
    core_require = file.read().split("\n")
    if platform.system() == "Windows":
        core_require.append("pywin32")
install_require = [x.strip() for x in core_require if "git+" not in x]

setup(
    name="Osaka",
    version="0.0.1",
    author="Iqbal Ramadhan Anniswa",
    author_email="iqbalramad75@gmail.com",
    install_requires=install_require,
    packages=["Osaka"],
    python_requires=">=3.10",
)
