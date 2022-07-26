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
	self.ktxnO = 0.013
	
	self.ktxnG = 0.013
	
	self.ktxnTh = 0.013
	
	self.ktxnF = 0.013
	
	self.ktxnAG = 0.013
	
	self.ktxnCG = 0.013
	

	
	self.krz = .25/60
	
	self.krsd = 1e3/1e9
	
	self.krev = 270/1e9
	

	
	self.krep = 1e4/1e9
	
	self.krepr = 0
	

	
	self.kth = 1e5/1e9
	
	self.krzTh = .00417
	

	
	self.krsdF = 1e3/1e9
	
	self.krevF = 270/1e9
	
	self.krevF = 1e3/1e9
	

	
	self.krzA = .25/60
	
	self.krsdA = 1e3/1e9
	
	self.krevA = 270/1e9
	

	
	self.krzCG = .00417
	
	self.krsdCG = 1e5/1e9
	
	self.krevCG = 1
	

	
	self.kssdO = 0
	
	self.kssdF = 0
	

	
	self.kdsduG = 0
	
	self.kdsdG = 0
	
	self.kdsdGO = 0
	
	self.kdsduAG = 0
	
	self.kdsdAG = 0
	
	self.kdsduCG = 0
	
	self.kdsdCG = 0
	
	self.kdrd = 0
	

	
	self.khybO = 1e6/1e9
	
	self.khybR = 1e6/1e9



