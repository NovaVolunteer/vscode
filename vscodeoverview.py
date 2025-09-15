# %%
import pandas as pd
# import math
# import simple_math # (Assuming simple_math.py is in the same directory)
import plotly.express as px
import numpy as np
import statsmodels
# %%
# Small Python script example: Calculate the area of a circle

def area_of_circle(radius):
    """Return the area of a circle given its radius."""
    return math.pi * radius ** 2

if __name__ == "__main__":
    r = 50
    print(f"Area of circle with radius {r}: {area_of_circle(r):.2f}")


# %% [markdown]
# ## Overview
# This notebook provides an overview of the Visual Studio Code (VSCode) interface, focusing on its key 
# features and functionalities.
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
# - **Command Palette**: Accessed via `F1`, it allows users to execute commands quickly.

# %%
# Example: Scatter plot of hours of sleep vs GPA

# Generate synthetic data showing positive correlation between sleep and GPA
np.random.seed(42)
sleep_hours = np.random.normal(loc=6.5, scale=1.0, size=100)
sleep_hours = np.clip(sleep_hours, 4, 9)
gpa = 2.0 + (sleep_hours - 4) * 0.5 + np.random.normal(0, 0.15, size=100)
gpa = np.clip(gpa, 2.0, 4.0)

df_sleep_gpa = pd.DataFrame({
    "Sleep Hours": sleep_hours,
    "GPA": gpa
})

fig = px.scatter(
    df_sleep_gpa,
    x="Sleep Hours",
    y="GPA",
    title="Relationship Between Hours of Sleep and GPA",
    trendline="ols"
)
fig.show()


# %% [markdown]
# Overview of Python Packages
#

# A package in Python is a way of organizing related modules into a directory hierarchy.
# It is simply a directory containing a special `__init__.py` file and one or more module files.
#
# Packages help structure code, promote reuse, and make it easier to maintain large projects.
#
# A module in Python is a file containing Python code (functions, classes, variables, etc.) 
# that can be imported and used in other Python programs.
#
# Modules help organize code into reusable components. For example, `pandas` is a module that 
# provides data analysis tools. You can create your own modules by saving Python code in 
# a `.py` file and importing it using the `import` statement.

# %%
# Example: Creating a simple math module

# Save the following code in a file named simple_math.py
# simple_math.py


# %%
# Example usage:

print(simple_math.add(2, 3))
print(simple_math.subtract(5, 2))   
print(simple_math.multiply(4, 6))   
print(simple_math.divide(10, 2))    


# %%

# Example: Accessing documentation for a package

# 1. Using the built-in `help()` function
help(pd)

# 2. Using the `.__doc__` attribute
print(pd.__doc__)

# 3. Accessing online documentation
# You can open the official pandas documentation in your browser:
# $BROWSER https://pandas.pydata.org/docs/

# 4. Using IPython/Jupyter magic commands (in a notebook or IPython shell)
# ?pandas           # Shows summary documentation
# ??pandas          # Shows detailed documentation including source code (if available)



# %%

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
# Four different ways to load data in Python

# 1. Using pandas to read a CSV file from a URL
df_csv_url = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# 2. Using pandas to read a local CSV file
# df_csv_local = pd.read_csv("local_titanic.csv")  # Uncomment and provide path to use

# 3. Using pandas to read from an Excel file
# df_excel = pd.read_excel("local_titanic.xlsx")  # Uncomment and provide path to use

# 4. Using pandas to read from a SQL database
# import sqlite3
# conn = sqlite3.connect("titanic.db")
# df_sql = pd.read_sql_query("SELECT * FROM passengers", conn)
# conn.close()



# %%
# Example: Using Data Wrangler in VSCode

# Load a complex dataset: Titanic passenger data
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Preview the data
print(df.head())


# %% 









