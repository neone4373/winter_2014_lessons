# General Assembly Data Science Course 14 - Winter 2014

*This repo includes materials for the General Assembly Data Science course in NYC. Navigate the directory structure to find what you're looking for. The `README.md` files are often the most central in a directory, and will display by default when you navigate on github.*


## Upcoming Activity:

* 12/10/2014 - First class Intro to Data Science
* 12/15/2014 - Intro to Machine Learning
* 12/17/2014 - Linear Regression

## Office Hours

Neo will be available by appointment, neo@fixitwithcode.com

Katie will hold regular office hours 

Katie: M,W - 9:30-10:30PM  ktbarnwell@gmail.com

### Syllabus

| Date      | Location | Topic | Assignment Due 
|:----------|:--------|:------|:------|:------
| 12/10/2014 | GA East (902 Broadway, 4th Floor) |Intro to Intro to Data Science | Finish computer setup (lab01)
| **12/15/2014** || Intro to Machine Learning | Chicago housing price predictor (*dataexplor01*)
| 12/17/2014  | | Linear Regression | lab02 iPython notebooks
| **12/22/2015**| | **Winter Break (Holiday/ No class)** | |
| **12/25/2015**| | **Winter Break (Holiday/ No class)** | |
| **12/29/2015**| | **Winter Break (Holiday/ No class)** | |
| **12/31/2015**| | **Winter Break (Holiday/ No class)** | |
| 1/5/2015 | | Data Visualization and EDA | 
| **1/7/2015**  | | Model Selection | *dataexplor02*
| 1/12/2015 | | Regularization, Dimensionality Reduction | *dataexplor03* 
| **1/14/2015** | | Classification, Logistic Regression | *dataexplor04*
| 1/19/2015 | | Probability and Bayes Theorem, Naive Bayes Classifiers | 
| **1/21/2015** | | Evaluating Classifier Models | *dataexplor05*
| 1/26/2015 | | Project Lightning Talks | Project Update |
| **1/28/2015**  | | Time Series Analysis | *dataexplor06*
| 2/2/2015 | | Clustering, k-means | *dataexplor07*
| **2/4/2015** | | Review | 
| 2/9/2015 | | Natural Language Processing | *dataexplor08*
| **2/11/2015** | | Bayesian A/B Testing | 
| 2/16/2015 | | Decision Trees and Ensemble Methods |
| **2/18/2015** | | Data Engineering: Distributed Computing, Hadoop, Storm |
| 2/23/2015 | | TBA |
| **2/25/2015** | | TBA | 
| 3/2/2015  | | Review | 
| **3/4/2015**  | | Presentation Workshop | Presentation Slides/Outline
| 3/9/2015  | | Final Presentations | Final Project Due


### Getting Help

**Github Issues**

For general or specific course help, students can get the fastest response by posting an issue, to the [issues page for this repository](https://github.com/neone4373/winter_2015_lessons/issues)

* Katie will be reviewing each issue
* Students and other instructors following the repository will also be able to address the issue, improving response time.

## TODO - probably will just use email
### Submitting Assignments

We will be using the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull</a> git model for submitting labs and some assignments.

For the **first assignment**:

1. Fork the assignments repo for the class:

2. clone the repo to your newly created Data Science Toolbox

```sh
vagrant@data-science-toolbox:~$git clone git@github.com:<yourgithubusername>/fall_2014_assignments.git
```

in `<yourgithubusername>/fall_2014_assignments/lab01`, make a directory with your first initial/full last name.

```sh
vagrant@data-science-toolbox:~$export DIR=<"flastname">
vagrant@data-science-toolbox:~$mkdir $DIR; cd <yourgithubusername>/fall_2014_assignments/lab01/$DIR;
```

With a text editor, create and save a markdown file with the following content:

* Your name and what you do
* One liner about your coding and math background
* Any social web you use and don't mind sharing (e.g. linkedin, twitter)
* A data blog post you read recently for sharing with the class
create a branch of the repository with a unique name, and then commit to that repo

```sh
vagrant@data-science-toolbox:~$git checkout -b my_name_class_1
vagrant@data-science-toolbox:~$git add .
vagrant@data-science-toolbox:~$git commit -m 'my first git commit!'
vagrant@data-science-toolbox:~$git push origin my_name_class_1
```

Add a pull request. This is the actual submission of your work. You can do this on github by finding your branch and clicking "Create pull request." Developers, feel free to use some command line tool for this if you prefer it.

Again, a link to github documentation on the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork and Pull git model</a>.


