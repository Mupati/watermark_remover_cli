from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="watermark_remover_cli",
    version="0.0.1",
    author="Kofi Mupati",
    author_email="scientificgh@gmail.com",
    description="Watermark Remover for PDFs and Images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mupati/watermark_remover_cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    zip_safe=False
)
