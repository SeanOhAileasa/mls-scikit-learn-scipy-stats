< [GMIT Data Analytics](https://web.archive.org/web/20201029063153/https://www.gmit.ie/computer-science-and-applied-physics/higher-diploma-science-computing-data-analytics-ict) | [Home](https://github.com/SeanOhAileasa) | [README](https://github.com/SeanOhAileasa/mls-scikit-learn-scipy-stats/blob/main/README.md) >

[![GMIT](https://github.com/SeanOhAileasa/SeanOhAileasa/blob/master/rc/gmit.png?raw=true)](https://web.archive.org/web/20201029063153/https://www.gmit.ie/computer-science-and-applied-physics/higher-diploma-science-computing-data-analytics-ict)

## Machine Learning & Statistics, Winter 21/22
### Due: last commit on or before January 2nd, 2022

Winter 21/22 assessment for the ``Machine Learning & Statistics`` module (5 Credits) of the ``Higher Diploma in Science in Computing (Data Analytics) (H.Dip)`` programme (75 Credits) at **Galway-Mayo Institute of Technology (GMIT)**.

## Learning Outcomes

i. Describe the stochastic nature of real-world measurements. 

Stochastic is the opposite of deterministic. Something is deterministic if you know the outcome or can figure out the right outcome for definite ahead of time. Unfortunately, nothing is deterministic; therefore, almost everything is stochastic. Refers to events whereby chance is accepted.

ii. Select an appropriate mathematical model of a real-world problem.

Analysis of a real-world problem that might identify has a stochastic basis, and that there's some chance involved. On top of that, the next step is to determine the right way to look at that real-world problem. Is there a way of formulating it or modelling it using an off the shelf Statistical or Machine Learning ``Python`` library to frame that problem correctly?

iii. Select an appropriate cost function for a given Machine Learning task.

The keyword here is optimisation, based on calculus, which is the basis for most Machine Learning. So, for example, having a function that measures the cost of something, is there a way to find the minimum cost resulting in the lowest possible price—selecting an appropriate cost function. The real-world problem is formulated in the correct terminology, identifying the correct parameters or setup, then applying Data Analytics (Machine Learning) techniques.

iv. Apply an optimisation technique to the parameters of a model.

The cost function is identified, then changing the problem's parameters to determine the cost. Finally, an optimisation technique is applied to the cost function to determine the minimum cost.

![meme](https://github.com/SeanOhAileasa/SeanOhAileasa/blob/master/rc/meme/pdf.png?raw=true)

The terminology and concepts introduced thus far can be considered wordy and of a high level conceptually, but these can be nebulous. 

It turns out that it involved just one or two commands from a Machine Learning ``Python`` library, which does most of the heavy lifting for you. So it's the formulation of the problem, the way you look at it, in terms of Machine Learning etc that's important. It is how to set up the model and then apply one of the off-the-shelf techniques to get the desired results.

#### Use ``Binder`` ![Binder](https://mybinder.org/badge_logo.svg)

This repository can be interacted in an executable environment, making the code immediately reproducible for experimentation using ``Docker`` in the background. The ``Binder`` badge creates a virtual machine in the cloud that runs the Jupyter Notebook enabling live interaction. Note it does not change the original Jupyter Notebook as it cannot sync with GitHub. The ``requirements.txt`` (python convention) file includes the packages required to run each Jupyter Notebook.

## Instructions

The purpose of the assessment is to ensure the module's learning outcomes are achieved while also providing sample work to show prospective employers. The overall assessment is split into the three components detailed below.

#### i. GitHub Repository:

Containing two Jupyter Notebooks described further down and in addition to:

- A clear and informative ``README.md`` explaining why the repository exists, what is in it, and how to run the notebooks.

- A ``requirements.txt`` file enables someone to quickly run the notebooks with minimal configuration. Of course, also include any required files such as data files and image files.

#### ii. [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/SeanOhAileasa/mls-scikit-learn-scipy-stats/blob/main/scikit-learn.ipynb) ``sklearn`` Jupyter Notebook [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SeanOhAileasa/mls-scikit-learn-scipy-stats/HEAD?labpath=scikit-learn.ipynb):

- A clear and concise overview of the ``scikit-learn`` Python library.

- Demonstrate three interesting ``scikit-learn`` algorithms. The choice may be based on the module content or otherwise - may have an overall spread of examples across the library or pick a particularly interesting part.

- Appropriate plots and other visualisations to enhance the notebook for viewers.

###### Motivation

Initially, I proposed to apply the three algorithms of interest (Machine Learning) to ``Cybersecurity`` problems. However, given the background knowledge required by viewers of the Jupyter Notebook instead will introduce a theoretical application to ``Cybersecurity`` where appropriate. The overall objective is to ensure the module's learning outcomes are achieved (best done by using the datasets introduced).

###### Description
&#x1F6A7;

###### Conclusion
&#x1F6A7;

#### iii. [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/SeanOhAileasa/mls-scikit-learn-scipy-stats/blob/main/scipy-stats.ipynb) ``scipy.stats`` Jupyter Notebook [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SeanOhAileasa/mls-scikit-learn-scipy-stats/HEAD?labpath=scipy-stats.ipynb):

- A clear and concise overview of the ``scikit-stats`` Python library.

- An example hypothesis test using ``ANOVA``. The dataset used must be appropriate to use ``ANOVA``, ensuring the assumptions underlying ``ANOVA`` are met, and then perform and display the results of ``ANOVA`` using ``scipy.stats``.

- Appropriate plots and other visualisations to enhance the notebook for viewers [0].

###### Motivation

From medical studies to research experiments, from polling organizations to United Nations observers and ``Cybersecurity``, data is being collected everywhere and all the time. Knowledge in statistics provides the tools and conceptual foundations in quantitative reasoning to extract information intelligently from this sea of data.

###### Description

&#x1F6A7;

###### Conclusion

&#x1F6A7;

## Installation

- Require Python to be loaded on your local machine. Recommend downloading and installing Anaconda.

https://www.anaconda.com/download/

## Execute Jupyter Notebook

- The software must be downloaded and run on a machine as follows:

	- Clone the repository with the following command:

	``git clone https://github.com/SeanOhAileasa/mls-scikit-learn-scipy-stats.git``

  - Run Jupyter Notebooks from the command line with the following:

	``jupyter notebook``

  - Open notebook - ``scikit-learn.ipynb``
  
  - Open notebook - ``scipy-stats.ipynb``  

  - Once running within the Jupyter environment can navigate with ease - links are plentiful.

	- ***Notebook links will not work on github given that github renders as static HTML - also not able to view equation tag numbers. Please run on a local machine or use nbviewer (see below).***

- An alternative to downloading and running on a local machine with all features included (links/equation tag number etc) can view via [[``scikit-learn``](https://nbviewer.jupyter.org/github/SeanOhAileasa/mls-scikit-learn-scipy-stats/blob/main/scikit-learn.ipynb)][[``scipy-stats``](https://nbviewer.jupyter.org/github/SeanOhAileasa/mls-scikit-learn-scipy-stats/blob/main/scipy-stats.ipynb)].

## Troubleshoot

&#x1F6A7;

## Credits

&#x1F6A7;

## Contact

&#x1F6A7;

## END