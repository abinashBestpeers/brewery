from setuptools import find_packages, setup

setup(name="brewery",
      version = "0.1",
      description = "Microbrewery microservices",
      author = "Abinash Sinha",
      platforms = ["any"],
      license = "MIT",
      packages = find_packages(),
      install_requires = ["Flask==2.0.3", "requests==2.27.1"],
      )