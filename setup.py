"""Setup ocaboxapi for distribution."""
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="ocaboxapi",
    description="Python interface for OCA Telescopes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/araucaria-project/ocaboxapi",
    version="3.0.2",
    license="LICENSE.txt",
    py_modules=["ocaboxapi"],
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
