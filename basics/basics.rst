Python for Atomistic Simulation
================================


Setting up a Virtual Environment
----------------------------------------

First, let's set up a virtual environment using `virtualenv`. If you haven't installed `virtualenv` yet, you can do it by running the following command:

.. code-block:: bash

    sudo apt install python3-pip
    sudo apt install python3-tk
    pip3 install virtualenv

Once `virtualenv` is installed, let's create the virtual environment named "envase":

.. code-block:: bash

   virtualenv envase

Next, activate the virtual environment (on macOS/Linux):

.. code-block:: bash

   source envase/bin/activate
   which python
   which pip

Installing ASE 
-----------------------

Now that we have the virtual environment set up, let's proceed to install ASE (Atomic Simulation Environment). We'll use `pip` to install it within the virtual environment:

.. code-block:: bash

   pip install ase

ASE is now successfully installed in your virtual environment and ready to use!

Part 3: Python Basics Review
----------------------------

Let's start with a brief review of some Python basics. We'll cover the introduction to Python, variables and data types, control flow, loops, functions, and an overview of NumPy and Matplotlib.

Introduction to Python
-----------------------

Python is a versatile, high-level programming language that's easy to learn and widely used in various fields, including scientific computing and data analysis.

Variables and Data Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Python, you can declare variables and assign values to them. Python is dynamically typed, meaning you don't need to specify the data type explicitly.

Python Code for Variables and Data Types:

.. code-block:: python

   # Variables and Data Types
   name = "John"
   age = 25
   height = 1.75
   is_student = True

Control Flow - Conditional Statements and Loops
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python provides various control flow constructs, such as if-else statements and loops (for and while), to control the program's flow based on conditions.

Python Code for Control Flow:

.. code-block:: python

   # Control Flow
   if age < 18:
       print("You are a minor.")
   elif age >= 18 and age < 60:
       print("You are an adult.")
   else:
       print("You are a senior citizen.")

   # Loops
   for i in range(5):
       print(f"Loop iteration: {i}")

   # While Loop
   counter = 0
   while counter < 5:
       print(f"While loop iteration: {counter}")
       counter += 1

Functions
---------

Functions allow us to group a block of code and execute it whenever needed. They promote code reusability and modularity.

Python Code for Functions:

.. code-block:: python

   # Functions
   def greet_user(username):
       print(f"Hello, {username}! Welcome to our course.")

   greet_user("Alice")

NumPy Basics
------------

NumPy is a fundamental library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with an extensive collection of high-level mathematical functions to operate on these arrays.

Python Code for NumPy Basics:

.. code-block:: python

   import numpy as np

   # Creating arrays
   arr1 = np.array([1, 2, 3, 4, 5])
   arr2 = np.arange(10, 21, 2)
   arr3 = np.zeros((2, 3))
   arr4 = np.ones((3, 2))

   # Array operations
   sum_array = arr1 + arr2
   dot_product = np.dot(arr3, arr4)

Introduction to Matplotlib
--------------------------

Matplotlib is a widely-used library for creating static, interactive, and animated plots in Python. It enables data visualization with a wide range of customization options.

Python Code for Matplotlib:

.. code-block:: python

   import matplotlib.pyplot as plt

   # Creating simple plots
   x = np.linspace(0, 10, 100)
   y = np.sin(x)
   plt.plot(x, y)
   plt.xlabel("x-axis")
   plt.ylabel("y-axis")
   plt.title("Sine Function")
   plt.grid(True)
   plt.show()

Conclusion
----------

Congratulations! You've completed the Python basics review and set up the ASE environment within your virtual environment. In the next section, we'll delve deeper into atomistic simulations with ASE and Python.

Remember to activate the virtual environment whenever you work on the course materials related to ASE to ensure a clean and isolated environment for your simulations.

Happy learning and happy experimenting with Python for Atomistic Simulation!
