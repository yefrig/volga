import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="volga",
    version="0.0.1",
    author="Yefri Gaitan <yg2548@columbia.edu>, Ecenaz Jen Ozmen <eo2419@columbia.edu>",
    description="A python framework for deserealization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yefrig/coms4995-volga",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed"
    ],
    python_requires='>=3.8',
)
