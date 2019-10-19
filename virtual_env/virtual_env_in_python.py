#  Virtual Environment

"""
Steps

1. pip install virtualenv
2. create virtual env using command
    virtaulenv kuldeep -- kuldeep is env folder name
3. activate the virtual env using command
    in-windows -- .\foldername\Scripts\activate (if errror set-executionpolicy remotesigned)
    in-Linux --  source foldername/bin/activate

    For Deactivate  -- deactivate

4. install all modules in new ENV 

"""


# Create requirement txt for all packages intalled to your env

# this step after activate the virtual env
"""
Steps

1. pip freeze >requirement.txt (Create text file)



"""

# Install all packages through requirement.txt
"""
Steps

1. pip install -r .\requirement.txt

"""



# Create Virtual Environment but load all side packages(local python packages)

"""
Steps

1. 2. create virtual env using command
    virtaulenv --system-site-packages kuldeep1 -- kuldeep is env folder name

"""