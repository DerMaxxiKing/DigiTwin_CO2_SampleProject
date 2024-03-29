#!/usr/bin/env python3

from pathlib import Path

import setuptools

project_dir = Path(__file__).parent

setuptools.setup(
    name="DigiTwin_CO2_SampleProject",
    version="2",
    description="Project which shows the use of the SIMULTAN data model and Python for digital twins",
    # Allow UTF-8 characters in README with encoding argument.
    long_description=project_dir.joinpath("README.rst").read_text(encoding="utf-8"),
    keywords=["python"],
    author="Max Buehler",
    url="",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    # pip 9.0+ will inspect this field when installing to help users install a
    # compatible version of the library for their Python version.
    python_requires=">=3.7",
    setup_requires=["wheel"],
    # There are some peculiarities on how to include package data for source
    # distributions using setuptools. You also need to add entries for package
    # data to MANIFEST.in.
    # See https://stackoverflow.com/questions/7522250/
    include_package_data=True,
    # This is a trick to avoid duplicating dependencies between both setup.py and
    # requirements.txt.
    # requirements.txt must be included in MANIFEST.in for this to work.
    # It does not work for all types of dependencies (e.g. VCS dependencies).
    # For VCS dependencies, use pip >= 19 and the PEP 508 syntax.
    #   Example: 'requests @ git+https://github.com/requests/requests.git@branch_or_tag'
    #   See: https://github.com/pypa/pip/issues/6162
    install_requires=project_dir.joinpath("requirements.txt").read_text().split("\n"),
    zip_safe=False,
    license="MIT",
    license_files=["LICENSE.txt"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["run_measurement_generator=DigiTwin_CO2_SampleProject.MonitoringFaker.fake_measurement_data:fake_measurement_data",
                                      "run_co2_prediction=DigiTwin_CO2_SampleProject.main:run_predictions"]},
)
