# Computer Setup and Data Handling

There are a number of tools that are very useful to have installed on your machine.

The minimum set of tools to start exploring data science with Python are

* Python Environment
* Text Editor
* Version Control

If you have a preference for a particular software that meets one of these requirements, then by all means, stick to what you are familiar with. But if you don't have a prefence I'd suggest you start off with following the install instructions for:

* Python Environment : [**Anaconda**](http://docs.continuum.io/anaconda/install.html),  is a collection of the most popular modules used for scientific computing. It's the one-stop shop to get all the python modules for doing data science
* Text Editor : [**SublimeText3**](http://www.sublimetext.com/3), is a sophisticated text editor for code, markup and prose. You'll love the slick user interface, extraordinary features and amazing performance.
* Version Control : [**Git**](http://nbviewer.ipython.org/github/ga-students/DS_HK_2/blob/gh-pages/notebooks/Guides%20-%20Git%20&%20GitHub.ipynb), saves 'snapshots' of your work and lets you share it with others.

Once you've installed the minimum requirements, consider beefing up your system with additional instructions for

* [Mac OSX](#Mac-OSX)
* [Linux](#Linux)
* [Windows](#Windows)

# Mac OSX

Once you have the [minimal setup](#Developer-Setup-Instructions), you might also consider improving your developer experience with the follow. In order of importance:

* Update to the [latest version of OSX](http://www.apple.com/hk/en/osx/)
* [Install XCode](https://developer.apple.com/xcode/) for its command-line tools, and open it at least once - then never again.
* Install a package manager for OSX. [Homebrew](http://brew.sh/) is installed by pasting the following into a terminal (search for the `terminal` app in spotlight) and follow the instructions

    > ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
        
* If you've installed Homebrew, you now have the `brew` command which allows you to install a better 'shell' called `ZSH`, this gives you better auto-completion options so you'll have to type less in the terminal. Paste the follow into the terminal.
    
    > brew install zsh

* Once you've installed ZSH, be sure to also get this community curated collection of extensions for ZSH, called `oh-my-zsh`. Paste into the terminal.

   > curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | ZSH=~/.dotfiles/zsh sh

* Install [iTerm2](http://www.iterm2.com/#/section/home) as a superior Terminal Emulator.

# Linux

Once you have the [minimal setup](#Developer-Setup-Instructions), you should be ready to go.

* If you'd like to have a more customisable shell, consider installing zsh with your package manager of choice, e.g.

> sudo apt-get install zsh
    
    or

> sudo yum install zsh

* Once you've installed ZSH, be sure to also get this community curated collection of extensions for ZSH, called `oh-my-zsh`. Paste into the terminal.

   > curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | ZSH=~/.dotfiles/zsh sh

* If you are looking to replace your default Terminal Emulator, give [Terminator](http://gnometerminator.blogspot.hk/p/introduction.html) a try.

# Windows

Make sure you have followed the [minimal setup](#Developer-Setup-Instructions), and now have a programme called 'Git Bash'. 

Whenever we refer to 'the terminal' or you see `command line` instructions, you are expected to open `Git Bash` and paste/run them there.

If you have more tips on doing data science under windows, feel free to [contact me](http://type.hk) and I'll add your suggestions here.

# iPython Notebook

iPython Notebooks are fantastic ways to distribute 'literate code'. That is, code which is annotated with a more extensive explanation of what it does. In the notebook's case, the explanation might also include graphics, plots and videos. 

To run the notebooks locally, run 

```bash
$ ipython notebook --pylab=inline
```


## Next Steps

If you find yourself all setup and itching to see what iPython can do check out the `more.md` file for some pretty nifty examples.

Additionally, we will always recommend 4 or 5 readings or other support materials for every class, either to supplement the current material, prep for the next class, or covering previous material that students still have questions on.

**Reading and other Materials**

* <a href="http://nbviewer.ipython.org/urls/gist.github.com/fonnesbeck/5850375/raw/c18cfcd9580d382cb6d14e4708aab33a0916ff3e/1.+Introduction+to+Pandas.ipynb">Pandas Tutorial</a>
* <a href="http://www.quora.com/Data-Science/What-is-it-like-to-be-a-data-scientist">Quora: What is it like to be a data scientist?</a>
* <a href="http://www.youtube.com/watch?v=h9vQIPfe2uU"> Josh Wills: The Life of a Data Scientist</a>
* <a href="http://www.p-value.info/"> P-Value.info, Carl Anderson's blog (Director of Data at Warby Parker)</a>
* <a href="http://blog.okcupid.com/"> A look at OKCupid and their detailed work in trends</a>
* <a href="http://radar.oreilly.com/2011/09/building-data-science-teams.html">DJ Patil, Building Data Science Teams</a>
* <a href="http://benfry.com/phd/">Ben Fry's Dissertation: Computational Information Design </a>
