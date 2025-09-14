
"""
Setup script for Agape Core Seed package
Makes the package installable via pip
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agape-core-seed",
    version="1.0.0",
    author="Agape Core AI Team", 
    author_email="info@agapecore.ai",
    description="Gospel-based AI ethics evaluation and guidance system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agapecore/agape-core-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies - pure Python
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "agape-core-analyze=agape_core_seed.seed_analyzer:main",
        ],
    },
    keywords="ai ethics gospel truth evaluation morality",
    project_urls={
        "Bug Reports": "https://github.com/agapecore/agape-core-ai/issues",
        "Source": "https://github.com/agapecore/agape-core-ai",
        "Documentation": "https://github.com/agapecore/agape-core-ai/docs",
    },
)
