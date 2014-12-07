# Computer Setup and Data Handling

For this course, we will be using the [**Data Science Toolbox**](http://datasciencetoolbox.org/), which is a virtual environment based on Ubuntu Linux that is specifically configured for doing data science.

### Step 1: Download and install VirtualBox

- Go to the [Virtualbox download page](https://www.virtualbox.org/wiki/Downloads) and download the appropriate binary. Open the binary and follow the installations instructions.

### Step 2: Download and install Vagrant

- Go the [Vagrant download page](http://www.vagrantup.com/downloads.html) and download the appropriate binary. Open the binary and follow the installations instructions.

### Step 3a: Download and initialize the Data Science Toolbox Vagrant environment

- Open a terminal (also known as the command prompt in Microsoft Windows). Create a directory, for example "gadatasciencetoolbox", and navigate to it:

```
$ mkdir gadatasciencetoolbox
$ cd gadatasciencetoolbox
```

- Next, run the following command:
```
$ vagrant init data-science-toolbox/dst
```

### Step 3b: Update the Vagrant config file to forward port 8888

- Step 3a created in your gadatasciencetoolbox folder a file named `Vagrantfile`, which is a config file used by Vagrant. Open the file in your favorite text editor (e.g. vim, notepad) and add the following text somewhere around line 22:

```
config.vm.network "forwarded_port", guest: 8888, host: 8888
```

This line instructs Vagrant to open up port 8888 so that the IPython Notebook server is accessible from your browser.

### Step 3c: Start the Data Science Toolbox!

```
$ vagrant up
```

### Step 4 (Mac OS X and Linux): Connect to the Data Science Toolbox via ssh: 

- If you are running Mac OS X or some other UNIX-like operating system, you can log in to the Data Science Toolbox by simply running the following command in a terminal:

```
$ vagrant ssh
```

### Step 4 (Windows): Connect to the Data Science Toolbox via ssh: 

- If you are running Microsoft Windows, you need to use a third-party application in order to log in to the Data Science Toolbox. We recommend **Putty** for this. Go to its [download page](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) and download `putty.exe`. Run `putty.exe` and enter the following values:

```
Host Name (or IP address): 127.0.0.1 
Port: 2222
Connection type: SSH
```
(If you want, you can save these values as a session by clicking the "Save" button, so that you do not need to enter these values again.)

Next, click the "Open" button and enter "vagrant" for both the username and the password.

### Step 5: Install GA Data Science Bundle

- Now that you are logged into your new virtual machine, run the following commands:

(Note that `vagrant@data-science-toolbox:~` indicates that this command should be run on the Data Science Toolbox.)

```
vagrant@data-science-toolbox:~$ dst update
vagrant@data-science-toolbox:~$ dst add gads
```

Invoke the following command to create a password-protected profile:

```
vagrant@data-science-toolbox:~$ dst setup base
```

### Step 6: Set up IPython Notebook

To start the IPython Notebook server, run:

```
vagrant@data-science-toolbox:~$ sudo ipython notebook --profile=dst
```

- You can now access the IPython Notebook server at https://localhost:8888. Because the SSL certificate is self-signed, you may get a warning message from your browser. The image below shows how Chrome complains about this. Because you know what's on the server-side, you can just click on the "Proceed anyway" button.


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
