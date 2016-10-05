# PUI 2016 HW 1.  

## On NYU classes please turn in your github account name where the repositories you will create in this and the following homework sets will be hosted.

## Create a directory HW1_\<netID> on your github repo and check the assignments there as directed. Remember to include a directory readme called README.md which briefly describes the homework, who you worked with, and what your contribution was. You will not be penalized if you had troubles, and you were mostly, or even entirely just trying to understand with your classmates help! But you must state so in the README.md. **If what you say is not consistent with what your classmates say in their README.md we will investigate the inconsistency, and you may loose points.**


# Assigned Reading:

What is the question? Jeff Leek & Roger D. Peng
http://moscow.sci-hub.bz/4d3cf57483ccf211f66cad18440023cd/10.1126%40science.aaa6146.pdf

### GRADING: questions on the readout will appear in the pre-class quizzez. 


# Assignment 1: Finish Lab 1

### Finish the lab started in the first lab session if you have not in class:
https://github.com/fedhere/PUI2016_fb55/blob/master/Lab1_fb55/githubCreateRepoCmds.md
At the end you should have a repository set up on your local machine (or on [compute](https://github.com/fedhere/PUI2016_fb55/blob/master/computationalResources.md)) as well as on your github account named gittest_\<netID>, with a single file in it named myfirstfile.txt, and you should have a resolved merge conflict. Because your repo is public we can access it, and see the history of your file, and the conflict in it. If you fell behind, please take yourself to this point, and feel free to work with others, but remember that it is your responsibility to learn, and be able to reproduce by yourself the work that you do in groups. 

### Work on a fork:

Pair with a classmate and fork each other’s repository. You are making your own copy of the repository, on which you can work independently. 

1. You need to first "fork" the repo, and then "clone" the fork of the repo on your machine. Further instructions on how to do it are on the Github website, if you need. 

2. Make changes to your local copy of your classmate file (whichever changes you wish to make). At the same time your class mate can make chnges of his or her own, as long as they do not affect __the same line__ as the one you are changing.

3. Both of you should commit your own modified file and push the changes to your won fork of the repo.

4. Request a merge from your classmate whose repo you forked. 

5. Each of you will get a pul request, and will merge your classmate fork. You should not have a conflict. if you do you have instructions in the same markdown on how to deal with it, though things can easily get very omplicated. Accept the merge request from your class mate.

### GRADING: 
- On your github account we must be able to see:
	1. your own repo, and in its history we need to see the merge. 

	2. your fork of your class mate repo and the changes you made to their file in its history

- On your classmate repo we need to see your merge request.

## Assignment 2: Set up your environment: 

1. Generate a directory on compute called PUI2016_\<netID>. 

2. Create an environmental variable on your compute account called PUI2016 that points to the directory PUI2016_<netID> by its full directory path: starting with /home [/home on a linux box, and with /Users on a mac if you want to replicate it on your machine] so that typing 
	```
	echo $PUI2016 
	```
returns the full path to the directory. Save  it in the .bashrc [.bashrc for (linux) or .bash_profile (OS X) if you want to replicate it on your machine] so that every time you open a new terminal the terminal knows what the $PUI2016 environmental variable (env var) is set to. To log into compute, as you know, you want to run the command 
	```
	ssh -X -A -t <netID>@gw.cusp.nyu.edu ssh -A -X compute 	
	```
on your terminal. Alternatively you can log in with the remote desktop into the green environment, and open a shell there.

3. Create an alias such that typing 
 	```
	pui2016 
	```
takes you to that directory. The alias must use the 'cd' command, and the env var $PUI2016 to do so. 

4. Take a screenshot of your .bashrc file so that we can see the alias and env var you created. 

6. Type this series of commands on the terminal:	
	```
	pwd
	pui2016
	pwd
	```
Take a screenshot of your terminal that shows this series of commands and their output. 

7. Once your environment is set up, go to github online and CREATE A NEW GITHUB REPO CALLED PUI2016_\<netID> ( this for me would be PUI2016_fb55: https://github.com/fedhere/PUI2016_fb55 ). Follow the github directions to create a repository on the command line on your local machine (https://help.github.com/articles/creating-a-new-repository/).  Notice that in this case you are working in the reverse order compared to the lab: you create the first instance of the repository on the remote server (on the web) and then you create a local repo to link to it on your machine. Follow the steps indicated by github to create the repo, a README.md file, and to link the online and the local repos. 

8. Inside the repository create a directory HW1_\<netid>

9. Inside this directory add a README.md file: edit the copy on your machine to have it describe what you did to set up your enviroment and upload the screenshots I directed you to take above, so that they are displayed in your README.md (like in the image below). The README.md is a “markdown” file. To see what the syntax to upload an image in a markdown file, or in general to format the text, you can look at this markdown and if you look at the raw file (by clicking the Raw button on the top right) you can see the syntax. 
Remember that you also need to upload the images in your remote directory for them to be displayed in your README! just like any file you add them by git add and git commit, git push.

NOTE: after you modify your .bashrc or .bash_profile you will have to rerun it:
	```
	source .bashrc 
	```
for the new set up to be incorporated in your environment. However, every new bash terminal you open will automatically read the .bashrc/.bash_profile and know about your new alias/env variables

### GRADING: 
We will grade you based on the README.md file you create in the github directory as described above. The README.mdfile **has to be your own!** While you can work in groups this must be written by you in your own words, to show you know what is going on. The screen shots need to show the appropriate lines in the .bashrc and that running the commands as requested takes you to the right directory.

![Screenshot 1 Assignment 2: my .bashrc](HW1_SS1.png)
![Screenshot 2 Assignment 2: my succesfull commands using $PUI2016 and the pui2016 alias](HW1_SS2.png)

## Assignment 3 - Extra Credit. 

##This may be hard, but figuring it out will greatly help you get the most out of the next several lectures. We keep track of your EC assignments and they will help your final grade. This homework is a notebook: this is the standard format of the homeworks in the future. To get full points your notebook must
## - be rendered (e.g. plots must be visible) so that we see what you intended to turn in
## - run: the TA must be able to download your notebook and run it without error. Failing to run will cost you 25% of the Assignment grade! 

1. Go to the PUI2015 directory you created in Assignment 1 and set up as a repo in Assignment 2.
2. Download the nontebook https://github.com/fedhere/PUI2016_fb55/blob/master/HW1_fb55/HW1_3_fb55.ipynb
. To do so click on Raw on the top right of the notebook. 
Now you have 2 choices: you can copy and paste the entire RAW Jupyter notebook (which is  a JSON file) onto a new file on your own machine (name the file HW1_3_<netID>.ipynb) or you can use the <i>wget</i> command on the terminal: typing 
	```
	wget https://raw.githubusercontent.com/fedhere/PUI2016_fb55/master/HW1_fb55/HW1_3_fb55.ipynb
	```
will save a version of the notebook in the directory where you were when you typed the command. wget, which stands for web get, downloads any files, or even entire directories, from a web URL. You must change the name of the notebook to HW1_3_\<netID>.ipynb

3. Fill in the code cells that I left empty following the directions. Run the check cells, which will help you to know that the cells you filled in were filled in correctly (you want to see the same output I saw, which is in the redered version of the notebook).

4. Once the notebook is done and rendered (you see the plots at the end of it) “stage it” so that git can track it: just follow the procedure in the lab assignment and use 
	```
	git add 
	git commit -m '<your message here>'
	```
5. Link the current directory to your new github repo (which you created in assignment 2) if you have not done so yet, (PUI2016_\<netID> on your github account, just like in the lab assignment you will need to use use 
 	```
	git remote add origin 
	git push -u  <url> 
	```
using the URL of your new repo.

6. Push the notebook into the github repo and check that it renders ok. Remember to check that it runs ok as well: before you commit open a new instance of Jupyter notebook (or restart your kernel!) and run through the notebook cell by cell to assure that there are no problems








## References: 
- markdown syntax - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet, http://daringfireball.net/projects/markdown/syntax
- basic bash commands - http://www.tldp.org/LDP/abs/html/basic.html
- environment setup - http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html#sect_03_01_02
- additional references were provided in the class slides.

Text Editors. 

#### -m

remember to add the -m “my commit message” when you commit to github, otherwise github will automatically open a text editor for you to type your message in , and then you have to deal with it. If github opened a text editor it is either emacs or vi, depending on your setup. If you are using emacs or vi, either because github opened them or to edit files, this is how you save your work and exit:

#### emacs 

Save: Ctrl+x Ctrl+s
Exit: Ctrl+x Ctrl+c
(if your emacs is running on the terminal you have to use these shortcuts, if it is running in its own X window you can use the dropdown menu)

#### vim (vi)

Save: esc :w
Exit: esc :q


## Key Concepts: 

- falsifiability and law of parsimony
- types of scientific questions
- reproducible research
- PEP8 and style standards 

- work with github 
- basic bash commands
- understand how to setup your environment
- creating and checking into github a Jupyter notebook


