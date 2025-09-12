# %% [markdown]
# ## Overview
# This notebook provides an overview of the Visual Studio Code (VSCode) interface, focusing on its key features and functionalities.
#
# ## Key Features
# - **Integrated Terminal**: VSCode includes a built-in terminal for running commands and scripts.
# - **Extensions Marketplace**: Users can enhance functionality by installing extensions from the marketplace.
# - **Debugging Tools**: VSCode offers powerful debugging tools for various programming languages.
# - **Version Control Integration**: Built-in support for Git allows for seamless version control.
#
# ## User Interface
# The VSCode interface is divided into several key areas:
# - **Activity Bar**: Located on the side, it provides access to different views like Explorer, Search, and Extensions.
# - **Editor Area**: The central part of the interface where files are opened and edited.
# - **Status Bar**: Displays information about the current project and file, including branch name and errors.
#

# %% [python]
def divide(a, b):
    # This will raise a ZeroDivisionError if b is 0
    return a / b

# Example usage that causes an error
result = divide(10, 1)  # Debugger can be used here to inspect the error
#to inspect the error
result

# ### Difference between Python script, IPython, and Jupyter Notebook

# %% [markdown]
# **Python Script**: A plain `.py` file containing Python code. 
# It is executed from start to finish by the Python interpreter. 
# There is no built-in support for interactive execution or rich
# output.

# **IPython**: An enhanced interactive Python shell. 
# It provides features like tab completion, object introspection, 
# and magic commands. IPython files can be `.py` or `.ipynb` 
# (notebooks), and code can be run interactively, line by line or 
# cell by cell.

# **Jupyter Notebook**: A web-based interactive environment for 
# writing and running code in cells. Notebooks (`.ipynb` files) 
# support mixing code, markdown, and rich outputs (plots, images).
# They are ideal for data exploration, visualization, and sharing results.
# %%




