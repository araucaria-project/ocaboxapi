"""Setup Alpyca for distribution."""
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="ocabox",
    description="Python interface for OCA Telescopes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/araucaria-project/ocabox",
    version="2.0.0",
    license="LICENSE.txt",
    py_modules=["ocabox"],
    install_requires=["requests", "python-dateutil", 'pyyaml'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Astronomy",
        "License :: OSI Approved :: Apache Software License",
    ],
)
