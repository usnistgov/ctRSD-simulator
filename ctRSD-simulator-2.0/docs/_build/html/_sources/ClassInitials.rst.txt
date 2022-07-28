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
		Numbers of domains present in the simulated system.




Initializations
---------------

All DNA templates and initial conditions are initialized at 0.


Rate Constants:
	self.ktxnO = 0.013 1/s
	
	self.ktxnG = 0.013 1/s
	
	self.ktxnTh = 0.013 1/s
	
	self.ktxnF = 0.013 1/s
	
	self.ktxnAG = 0.013 1/s
	
	self.ktxnCG = 0.013 1/s
	

	
	self.krz = .25/60 1/s
	
	self.krsd = 1e3/1e9 1/nM-S
	
	self.krev = 270/1e9 1/nM-S
	

	
	self.krep = 1e4/1e9 1/nM-S
	
	self.krepr = 0 1/s
	

	
	self.kth = 1e5/1e9 1/nM-S
	
	self.krzTh = .00417 1/s
	

	
	self.krsdF = 1e3/1e9 1/nM-S
	
	self.krevF = 270/1e9 1/nM-S
	
	self.krevF = 1e3/1e9 1/nM-S
	

	
	self.krzA = .25/60 1/s
	
	self.krsdA = 1e3/1e9 1/nM-S
	
	self.krevA = 270/1e9 1/nM-S
	

	
	self.krzCG = .00417 1/s
	
	self.krsdCG = 1e5/1e9 1/nM-S
	
	self.krevCG = 1 1/s
	

	
	self.kssdO = 0 1/s
	
	self.kssdF = 0 1/s
	

	
	self.kdsduG = 0 1/s
	
	self.kdsdG = 0 1/s
	
	self.kdsdGO = 0 1/s
	
	self.kdsduAG = 0 1/s
	
	self.kdsdAG = 0 1/s
	
	self.kdsduCG = 0 1/s
	
	self.kdsdCG = 0 1/s
	
	self.kdrd = 0 1/s
	

	
	self.khybO = 1e6/1e9 1/nM-S
	
	self.khybR = 1e6/1e9 1/nM-S



