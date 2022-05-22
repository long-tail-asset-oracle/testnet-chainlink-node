import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testnet-chainlink-node",
    version="0.0.1",
    author="Nodemadic",
    author_email="nodemadic@gmail.com",
    description="ChainLink automated job deployment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/long-tail-asset-oracle/testnet-chainlink-node",
    project_urls={
        "Node Deployment": "https://github.com/orgs/long-tail-asset-oracle/projects/1",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
