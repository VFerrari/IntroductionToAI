Project 2 - Image Reconstruction with Genetic Algorithms.
=========================================================
This project uses genetic algorithms (with many variations) for image reconstruction.

The problem consists of, given the original image, recreating an image from scratch. The original is only used for fitness purposes (how good is the image generated). This is not particularly useful in many applications, but can be used as basis for other problems, and is good for the purpose of this project: test different methods of reproduction, mutation, etc.

The motivation came from [Roger Johansson's "Evolution of Mona Lisa"](https://rogerjohansson.blog/2008/12/07/genetic-programming-evolution-of-mona-lisa/), but instead of using polygons, the pixel values are directly used.

## Requirements
Install the required libraries:

- Pandas
- NumPy
- OpenCV2
- MatPlotLib

You may also need IPython/Jupyter.

## How to Run
Open the Jupyter Notebook `project2.ipynb`, which contains a report on the entire project and all variations, structured in a didactic manner.

The results can also be seen in the notebook, but a summary is available in `result_summary.pdf`.
