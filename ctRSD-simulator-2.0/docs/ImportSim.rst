.. _ImportSim:

Installing and Initializing Simulator
=====================================

**The following packages are used internally within the simulator and will need to be installed and available in the Python environment the simulator is running within:**
*numpy*, *scipy*, *matplotlib*, *re*, *math*, *xlrd*

If you are new to Python we recommend downloading Anaconda <https://www.anaconda.com/>`, which should automatically have the necessary auxiliary Python packages/libraries installed. We primarily used the Spyder IDE to develop this code and would also recommend that for new users of Python. However, there can be issues with getting Spyder to launch from Anaconda, particularly for Mac users. 

Jupyter Notebook is another good option running routine simulations - the simulation code can be split into small managable chucks that typically only need minor edits across simulations: initialize model, change rate constants and populate molecular species / conditions, simulate, and plotting. 


**Before you can use all the functions and features of ctRSD-simulator-2.0, you must first follow these steps:**
	1. :ref:`download <download_simulator>` ctRSD-simulator-2.0
	2. import the simulator in your Python script
	3. Instantiate the simulator's :ref:`class <class>` -> input is # of domains (default=5)
	4. Now use all the functions/features available in ctRSD-simulator-2.0!

.. admonition:: Note:

   You will need to import the simulator package in your local script to use it. After downloading a local copy of the package you can import the package with the code below. Note *ctRSD_simulator_200* refers to the name of latest simulator package downloaded from GitHub


   .. code-block:: python

		import sys
		sys.path.insert(1,'filepath of simulator on your computer')
		import ctRSD_simulator_200 as RSDs



Please use figure below as an example:

.. code-block:: python
	
	# importing any additional packages for specific use in this script
	import numpy as np
	import matplotlib.pyplot as plt

	# STEP 2 - add the path to the local copy of the simulator (an example path is shown below)
	# 			- import the simulator
	import sys
	sys.path.insert(1,'C:\\Users\\Name\\Documents\\SimFolder')
	import ctRSD_simulator_200 as RSDs

	'''
	As will most Python classes, the model must be instantiated before accessing its functions/features.

	The model's class has an input that is the number of domains necessary for simulating a system 
	(the default if no input is provided is 5 domains)
	The number of domains needs to be >= the highest domain index of the components specified in molecular_species() for a given simulation
	'''

	# STEP 3 - create a model instance
	model = RSDs.sim() # default number of domains (5)

	'''
	Now that a model instance has been created the model functions can be used
	'''

	# STEP 4 - set up a simulation

	# molecular_species() function
	model.molecular_species(I{1},DNA_con=25)
	model.molecular_species(G{1,2},DNA_con=25)
	model.molecular_species(R{2},ic=500)

	# simulate() function
	sim_time = np.linspace(0,3,1001)*3600 # seconds of simulation time
	model.simulate(sim_time)

	# output_concentration() function
	S2 = model.output_concentration('S{2}')

	# plotting
	plt.plot(sim_time,S2)
	plt.xlabel('Time (seconds)')
	plt.ylabel('Reacted reporter (nM)')




