Quantum ESPRESSO Calculations
====================================

.. raw:: html

   <h2 style="text-align: center;">Course Material</h2>

Welcome to the course on "Introduction to Quantum ESPRESSO Calculations and Materials Simulation" using the Atomic Simulation Environment (ASE). In this course, you will learn the basics of quantum mechanical calculations using the Quantum ESPRESSO software package and how to perform materials simulations with ASE.

Prerequisites
-------------

Before starting this course, make sure you have the following installed on your system:

1. Python with pip (to install ASE).
2. Quantum ESPRESSO (installed separately from the ASE).

Downloading Crystal Structures from Materials Project
-----------------------------------------------------

In this section, we will download crystal structures of GaAs, Si, and Al from the Materials Project database and read them using ASE.

1. Install ASE
   - You can install ASE using pip with the following command:

     .. code-block:: bash

        pip install ase

2. Import ASE modules
   - Import the necessary ASE modules to work with crystal structures:

     .. code-block:: python

        from ase.io import read

3. Download CIF files
   - Download the CIF files for GaAs, Si, and Al from the Materials Project website (https://materialsproject.org/).
   - Save the CIF files in your working directory.

4. Read CIF files
   - Use the `read` function from ASE to read the CIF files and create ASE `Atoms` objects:

     .. code-block:: python

        gaas = read('gaas.cif')
        si = read('si.cif')
        al = read('al.cif')

Creating Quantum ESPRESSO Calculator in ASE
-------------------------------------------

Now that we have our crystal structures loaded as `Atoms` objects, we will create Quantum ESPRESSO calculators to perform electronic structure calculations.

1. Import Quantum ESPRESSO calculator
   - Import the `Espresso` calculator from ASE to interface with Quantum ESPRESSO:

     .. code-block:: python

        from ase.calculators.espresso import Espresso

2. Set up Quantum ESPRESSO calculator
   - Create a Quantum ESPRESSO calculator for GaAs:

     .. code-block:: python

        # Set up the Quantum ESPRESSO calculator for GaAs
        gaas_calc = Espresso(pw=400,       # Plane wave cutoff energy in eV
                             calculation='scf', # Self-consistent field calculation
                             kpts=(4, 4, 4), # Monkhorst-Pack k-point mesh
                             xc='PBE',     # Exchange-correlation functional (PBE for Perdew-Burke-Ernzerhof)
                             outdir='gaas_calculation', # Output directory for Quantum ESPRESSO
                             pseudo_dir='pseudo',  # Directory containing pseudopotential files
                             pseudopotentials={'Ga': 'Ga.pbe-n-kjpaw.UPF', 'As': 'As.pbe-n-kjpaw.UPF'} # Pseudopotentials for elements
                             )

        # Attach the calculator to the GaAs structure
        gaas.set_calculator(gaas_calc)

   - Repeat the above steps to create calculators for Si and Al with appropriate pseudopotential files.

Running Quantum ESPRESSO Calculations
-------------------------------------

Now that we have set up the Quantum ESPRESSO calculators, let's run the electronic structure calculations for GaAs, Si, and Al.

1. Calculate the potential energy of GaAs
   - Use the `get_potential_energy()` method of the `Atoms` object to perform the calculation:

     .. code-block:: python

        gaas_energy = gaas.get_potential_energy()
        print('GaAs total energy:', gaas_energy, 'eV')

   - Repeat the above step for Si and Al.

2. Accessing Additional Results
   - ASE allows us to extract additional results from the Quantum ESPRESSO calculations, such as forces, stress tensor, and electronic structure information.

   .. note::

      Students are encouraged to explore the ASE documentation to learn how to extract and analyze additional information from Quantum ESPRESSO calculations.


Density of States
---------------------------

The density of states (DOS) is a fundamental concept in condensed matter physics and quantum mechanics. It provides valuable insights into the distribution of energy levels available to electrons in a material. The DOS is defined mathematically as:

.. math::

    g(\varepsilon) = \sum\limits_n \langle\psi_n|\psi_n\rangle \delta(\varepsilon-\varepsilon_n),

where :math:`\varepsilon_n` represents the eigenvalue of the eigenstate :math:`|\psi_n\rangle`.

In a given orthonormal basis, the DOS can be expressed as a sum over basis functions:

.. math::

    \begin{align*}
    g(\varepsilon) &= \sum\limits_i g_i(\varepsilon), \\
    g_i(\varepsilon) &= \sum\limits_n \langle \psi_n | i \rangle \langle i | \psi_n \rangle \delta(\varepsilon - \varepsilon_n),
    \end{align*}

where :math:`g_i(\varepsilon)` is called the *projected density of states* (PDOS). Additionally, the DOS can also be represented as an integral over the spatial coordinates:

.. math::

    \begin{align*}
    g(\varepsilon) &= \int\!\mathrm{d}r g(r, \varepsilon), \\
    g(r, \varepsilon) &= \sum\limits_n \langle\psi_n | r \rangle \langle r | \psi_n \rangle \delta(\varepsilon - \varepsilon_n),
    \end{align*}

where :math:`g(r, \varepsilon)` is known as the *local density of states* (LDOS).

It is important to note that the completeness of the selected basis sets is crucial in defining the DOS. We have :math:`1 = \sum\limits_i | i \rangle\langle i |` for discrete basis sets and :math:`1 =\int\!\mathrm{d}r |r\rangle\langle r|` for continuous basis sets.

The DOS has several important properties that make it a valuable tool for understanding electronic structure:

1. **Total Number of Electrons (N):** The integral of DOS below the Fermi energy gives the total number of electrons (N) in the system:

   .. math::

       \int\!\mathrm{d}\varepsilon\, n_F(\varepsilon) g(\varepsilon) = N,

   where :math:`n_F(\varepsilon)` is the Fermi distribution function.

2. **Electron Density (n(r)):** The integral of LDOS multiplied by the Fermi distribution provides the electron density at a given point in space (r):

   .. math::

       \int\!\mathrm{d}\varepsilon\, n_F(\varepsilon) g(r, \varepsilon) = n(r).

The DOS is a powerful tool in solid-state physics and materials science for understanding the electronic properties of materials and predicting their behavior under different conditions.

.. note::
   In the above definition, the k-dependence of eigenfunctions has been dropped for simplicity. For a more accurate definition, one can refer to "*Quantum Chemistry of Solids: The LCAO First Principles Treatment of Crystals*" by Robert A. Evarestov.

To summarize, the DOS provides crucial information about the distribution of energy levels and electronic states in a material, making it a fundamental concept in the study of condensed matter and quantum systems.
