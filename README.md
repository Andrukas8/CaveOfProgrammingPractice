python -m venv venv #installs new virtual environment called venv in active folder

.\venv\Scripts\activate.ps1 #activates the virtual environment

deactivate #deactivates the virtual environment

pip install <...> #installs a library

pip freeze #shows libraries installed in a particular virtual environment. Use this command and then copy all libraries as they are into requirements.txt file (use Ctrl+C from terminal).

#Do not commit venv folder. Use .gitignore

#When cloning from GitHub - need to install libraries from requirements.txt file

pip install -r requirements.txt

rmdir /s /q venv #deletes the virtual environment folder

dir /s venv #shows information about the venv folder

.gitignore #list of directories and files that git will ignore when we push changes. use venv/ in .gitignore to ignore venv.

git add --all #adds all changed files to a stage

#Useful git commands

touch README.md

git init

git add README.md

git commit -m "first commit"

git remote add origin git@github.com:Andrukas8/<reponame>.git

git push -u origin master