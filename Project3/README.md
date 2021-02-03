Project 3 - Disaster Tweet Classification with Machine Learning.
===============================================================
This project uses machine learning techniques to [classify disaster tweets](https://www.kaggle.com/c/nlp-getting-started/data) between real and fake (metaphors, sarcasm, etc). It is a **sentiment analysis** problem.

A full report (in Portuguese) can be found in `report_ptbr.pdf`.

A shorter summary (in English) can be found in `presentation.pdf` and `video.mp4`.

The dataset, split into training and test sets, can be found in the `data` folder.

## Requirements
Install the required libraries (not all models require all libraries):

- Pandas
- NumPy
- MatPlotLib
- Tensorflow 2.0
- Scikit-Learn
- NLTK
- Six

You may also need IPython/Jupyter.

For some models, you need to download [GloVe](https://nlp.stanford.edu/projects/glove/) and add to the `src/machine_learning/Glove` folder.

## How to Run
In the `src/machine_learning` folder, there are a few Jupyter Notebooks, each one with a different machine learning technique.

These notebooks assume that they are being run in the Google Colaboratory environment, and paths are hardcoded for the team's Google Drive folder. Change at will, including the dataset path.

They may be a little hard to run, because they weren't developed with distribution in mind. The team recommends using the Google Colaboratory environment. The instructions and overall descriptions are in Portuguese.

The `src/machine_learning/Modelos` folder has some pre-trained models.
