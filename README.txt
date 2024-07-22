Contents of this folder:
  - generators (folder) - This folder contains a Python source file for each implemented generator. 
                          It also contains a file called "__init__.py" which allows the files to be 
                          imported into other python programs.
  - .gitignore          - This file is a list of file names that should not be checked in to git
                          source control.
  - README.txt          - The file you're reading now!
  - diagnostics.ipynb   - This is a Python notebook that can be run with a runtime such as Jupyter, 
                          or within a code editor like Visual Studio Code. This code performs the
                          graphical diagnostics and statistical tests, and produces related 
                          visualizations.
  - requirements.txt    - A listing of the Python packages required to run the code in this project.
  - runtime.ipynb       - This is a Python notebook that may be run in the same manner as the 
                          diagnostics code. This code performs runtime data collection.
  
  How to run this code:
    0. This code was developed on Python 3.11.3. Any relatively recent version of Python should work.
    1. Install dependencies. If you use virtual environments for python, then do so. Otherwise, 
       you'll install the packages globally. Use the provided "requirements.txt" file to install
       these by running the following command in a terminal from within this project folder: 
           
           pip install -r ./requirements.txt
    
    2. View or run the ipynb files. If you have a Python editor or Jupyter installation that you are
       familiar with, you may view the files as-is, edit, or run them as you see fit. If you would 
       simply like to "run" these files and produce an output, then you may use the following 
       terminal commands from within the project folder.

       To run the diagnostics and statistical tests:

         jupyter nbconvert --to html --execute diagnostics.ipynb --output diagnostics.html

       To run the runtime data collection:
         
         jupyter nbconvert --to html --execute runtime.ipynb --output runtime.html

       These commands will produce the output files "diagnostics.html" and "runtime.html" which 
       display the results of the Python code.