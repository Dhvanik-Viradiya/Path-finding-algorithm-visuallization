import setuptools

setuptools.setup(
    name="visualize-algos",
    version="0.0.4",
    author="Dhvanik Viradiya",
    author_email="viradiyadhvanik@gmail.com",
    description="Visualize path finding algorithms simultaneously for the same condition in UI.",
    long_description="There are only limited algorithms implemented. In follow up versions more algorithms will be added and will be used to visualize the algorithms easily.",
    long_description_content_type="text/markdown",
    url="https://github.com/Dhvanik-Viradiya/Path-finding-algorithm-visuallization",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
