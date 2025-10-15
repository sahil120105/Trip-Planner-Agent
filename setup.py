from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    """

    requirements_list: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirements_list

print(get_requirements()) 


setup(
    name="trip_planner_agent",
    version="0.1.0",
    author="Sahil Ranadive",
    author_email="sahilranadive12@gmail.com",
    packages = find_packages(),             # Automatically finds and includes all Python sub-packages in the project.
    install_requires = get_requirements()
)