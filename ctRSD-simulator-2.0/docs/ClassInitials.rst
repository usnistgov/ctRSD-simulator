.. _class:

RSD_sim Class
=============

RSD_sim is a Python class that gives access to all of the simulator's built-in functions found :ref:`here <Functions>`. To have access to the features of the class you must first instantiate an object of the class, directions for this can be found :ref:`here <ImportSim>`.

This page gives info about the input of the object instantiation, and the initiaizations made for the class.


Class Object
------------

__init__(*domains=5*)


**Parameters:**
	domains: *int*, *if NONE, default=5* 
		The highest input or output index of the species indicated in *molecular_species()*. For example, if G{5,9} is specified, *domains* needs to be 9 or greater.
		This can be higher than the highest index in the system but it cannot be lower than the highest index in the system.



.. _initials_defaults: 

Initializations
---------------

All DNA template concentrations and initial conditions are initialized at 0.


Rate Constants:
	self.ktxnO = 0.013 (1/s)

	self.ktxnG = 0.013 (1/s)

	self.ktxnTG = 0.013 (1/s)

	self.ktxnF = 0.013 (1/s)

	self.ktxnAG = 0.013 (1/s)

	self.ktxnCG = 0.013 (1/s)

	self.leak = 0.03

	self.krz = 0.00417 (1/s)

	self.krsd = 1e3/1e9 (1/nM-s)

	self.krev = 270/1e9 (1/nM-s), 0 for inputs

	self.krep = 1e4/1e9 (1/nM-s)

	self.krepr = 0 (1/s)



	self.kth = 1e5/1e9 (1/nM-s)

	self.krzTG = 0.00417 (1/s)



	self.krsdF = 1e3/1e9 (1/nM-s)

	self.krevF = 1e3/1e9 (1/nM-s)



	self.krzA = 0.00417 (1/s)

	self.krsdA = 1e3/1e9 (1/nM-s)

	self.leakA = 0.06

	self.krzCG = 0.00417 (1/s)

	self.krsdCGa = 1e5/1e9 (1/nM-s)

	self.krsdCGb = 1e5/1e9 (1/nM-s)

	self.krevCG = 1 (1/s)
		
	self.kssdO = 0 (1/s)

	self.kssdF = 0 (1/s)

	self.kdsduG = 0 (1/s)

	self.kdsdG = 0 (1/s)

	self.kdsdGO = 0 (1/s)

	self.kdsdGF = 0 (1/s)

	self.kdsduTG = 0 (1/s)

	self.kdsdTG = 0 (1/s)

	self.kdsduAG = 0 (1/s)

	self.kdsdAG = 0 (1/s)

	self.kdsdAGOa = 0 (1/s)

	self.kdsdAGOb = 0 (1/s)

	self.kdsdAGFb = 0 (1/s)

	self.kdsduCG = 0 (1/s)

	self.kdsdCG = 0 (1/s)

	self.kdsdCGOa = 0 (1/s)

	self.kdsdCGOb = 0 (1/s)

	self.kdrd = 0 (1/s)

	self.khybO = 1e6/1e9 (1/nM-s)

	self.khybR = 1e6/1e9 (1/nM-s)



