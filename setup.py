from setuptools import setup, find_packages

setup(
    name="ML_DL_coursework",
    version="0.0.1",
    description="A project with Flask backend and ML service for generating haiku.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alexander Dedov",
    author_email="m2313016@edu.misis.ru",
    url="https://github.com/nelina1r/ML_DL_coursework",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "jinja2",
        "requests",
        "diffusers",
        "torch",
        "GPUtil",
        "numba",
        "flask-cors"
    ],
    entry_points={
        "console_scripts": [
            "backend = backend.app.main:app",
            "ml = ml.app.main:app"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
