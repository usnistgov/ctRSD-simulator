.. _Functions:

Functions
=========

This section lists the different functions available within ctRSD-simulator-2.0.


.. admonition:: Note:

   Before all available functions can be accessed the model must be downloaded, imported, and instantiated!

   More information on these steps can be found :ref:`here <ImportSim>`.




.. _global_rate_constants:

global_rate_constants
---------------------

global_rate_constants(*krz='False'*, *krsd='False'*, *krev='False'*, *krep='False'*, *krepr='False'*, *kth='False'*, *krzTh='False'*
, *krsdF='False'*, *krevF='False'*, *krevA='False'*, *krsdA='False'*, *krzA='False'*, *krevCG='False'*, 
*krsdCG='False'*, *krzCG='False'*, *ktxnO='False'*, *ktxnG='False'*, *ktxnTh='False'* , *ktxnF='False'*, *ktxnAG='False'*
, *ktxnCG='False'*, *ktxn='False'*, *kssdO='False'*, *kssdF='False'*, *kdsduG='False'*, *kdsdG='False'*, *kdsdGO='False'*
, *kdsduAG='False'*, *kdsdAG='False'*, *kdsduCG='False'*, *kdsdCG='False'*, *kdrd='False'*, *kdeg='False'*, *kssd='False'*, *kdsd='False'*
, *khybO='False'*, *khybR='False'*, *khyb='False'*)

global_rate_constants is used to globally change rate constants for all species of the same type (single matrix), or certain groups of different types (multiple matrices), instead of changing a specific rate constant for just one individual species (index of a matrix).

Rate Constant initializations can be found :ref:`class <class>`.

**Parameters:**
	krz: *float*, *optional* 
		Base ctRSD gate ribozymal cleavage rate.

	krsd: *float*, *optional* 
		Base ctRSD gate forward reaction rate.

	krev: *float*, *optional* 
		Base ctRSD output reverse reaction rate.

	krep: *float*, *optional* 
		Reporter reaction rate.

	krepr: *float*, *optional* 
		Reverse reporter reaction rate.

	kth: *float*, *optional* 
		Thresholding reaction rate.

	krzTh: *float*, *optional* 
		Thresholding ribozymal cleavage rate.

	krsdF: *float*, *optional* 
		Fuel forward reaction rate.

	krevF: *float*, *optional* 
		Fuel reverse reaction rate.

	krz: *float*, *optional* 
		Ribozymal cleavage rate.

	krevA: *float*, *optional* 
		ctRSD AND gate reverse reaction rate.

	krsdA: *float*, *optional* 
		ctRSD AND gate forward reaction rate.

	krzA: *float*, *optional* 
		ctRSD AND gate ribozymal cleavage rate.

	krevCG: *float*, *optional* 
		ctRSD comparator gate reverse reaction rate.

	krsdCG: *float*, *optional* 
		ctRSD comparator gate forward reaction rate.

	krzCG: *float*, *optional* 
		ctRSD comparator gate ribozymal cleavage rate.

	ktxnO: *float*, *optional* 
		Transcription rate for output.

	ktxnG: *float*, *optional* 
		Transcription rate for gate.

	ktxnTh: *float*, *optional* 
		Transcription rate for threshold.

	ktxnF: *float*, *optional* 
		Transcription rate for fuel.

	ktxnAG: *float*, *optional* 
		Transcription rate for AND gate.

	ktxnCG: *float*, *optional* 
		Transcription rate for comparator gate.

	ktxn: *float*, *optional*
		Globally change all transcription rates (ktxnO,ktxnG,ktxnTh,ktxnF,ktxnAG,ktxnCG)

	kssdO: *float*, *optional* 
		Degredation rate for output (single stranded).

	kssdF: *float*, *optional* 
		Degredation rate for fuel (single stranded).

	kdsduG: *float*, *optional* 
		Degredation rate for uncleaved gate (double stranded).

	kdsdG: *float*, *optional* 
		Degredation rate for gate (double stranded).

	kdsdGO: *float*, *optional* 
		Degredation rate for gate-output complex (double stranded).

	kdsduAG: *float*, *optional* 
		Degredation rate for uncleaved AND gate (double stranded).

	kdsdAG: *float*, *optional* 
		Degredation rate for AND gate (double stranded).

	kdsduCG: *float*, *optional* 
		Degredation rate for uncleaved comparator gate (double stranded).

	kdsdCG: *float*, *optional* 
		Degredation rate for comparator gate (double stranded).

	kdrd: *float*, *optional* 
		Degredation rate for RNA:DNA hybrids.

	kssd: *float*, *optional* 
		Degredation rate for all single stranded species (kssdO,kssdF).

	kdsd: *float*, *optional* 
		Degredation rate for all double stranded species (kdsduG,kdsdG,kdsdGO,kdsduAG,kdsdAG,kdsduCG,kdsdCG).

	kdeg: *float*, *optional* 
		Degredation rate for all species (kssdO,kssdF,kdsduG,kdsdG,kdsdGO,kdsduAG,kdsdAG,kdsduCG,kdsdCG,kdrd).

	khybO: *float*, *optional* 
		Hybridization rate for output.

	khybR: *float*, *optional* 
		Hybridization rate for reporter.

	khyb: *float*, *optional* 
		Hybrdization rate for both output and reporter (khybO,khybR).




.. _molecular_species:

molecular_species
-----------------

molecular_species(*name*, *DNA_con=0*, *ic='False'*, *krz='False'*, *krsd='False'*, *krev='False'*, *krep='False'*, *krepr='False'*, *kth='False'*, *krzTh='False'*, *krsdF='False'*, *krevF='False'*, *krevA='False'*, *krsdA='False'*, *krzA='False'*, *krevCG='False'*, *krsdCG='False'*, *krzCG='False'*, *ktxnO='False'*, *ktxnG='False'*, *ktxnTh='False'*, *ktxnF='False'*, *ktxnAG='False'*, *ktxnCG='False'*, *kssdO='False'*, *kssdF='False'*, *kdsduG='False'*, *kdsdG='False'*, *kdsdGO='False'*, *kdsduAG='False'*, *kdsdAG='False'*, *kdsduCG='False'*, *kdsdCG='False'*, *kdrd='False'*, *khybO='False'*, *khybR='False'*, *khyb='False'*)

molecular_species is used to initialize all species involved in the system being simulated.

DNA template, initial condition, and rate constant initializations can be found :ref:`class <class>`.


.. admonition:: Warning!

   All optional rate constant inputs can only change corresponding species when inputted with those specific species. A warning message will be issued otherwise.

**Parameters:**
	name: *string*
		Name of species being initialized
			* Input -> I{domain} / IN{domain} / INP{domain} / INPUT{domain} (all options work, not case sensitive)
			* Gate -> G{domainI,domainO} / GATE{domainI,domainO} (all options work, not case sensitive)
			* Reporter -> R{domain}, REP{domain}, REPORTER{domain} (all options work, not case sensitive)
			* Output -> O{domainI,domainO} / OUT{domainI,domainO} / OUTPUT{domainI,domainO} (all options work, not case sensitive)
			* Uncleaved Gate -> uG{domainI,domainO} (not case sensitive)
			* Gate-Input Complex -> GI{domain} (not case sensitive)
			* Gate-Output Complex -> GO{domainI,domainO} (not case sensitive)
			* Reporter-Output Complex -> RO{domainI,domainO} (not case sensitive)
			* Output Reporter -> S{domain} (not case sensitive)
			* Uncleaved Threshold -> uTH{domain} (not case sensitive)
			* Threshold -> TH{domain} (not case sensitive)
			* Fuel -> F{domain} (not case sensitive)
			* Fuel Gate -> GF{domain} (not case sensitive)
			* Uncleaved AND Gate -> uAG{domainI,domainO} (not case sensitive)
			* AND Gate -> G{domainI1.domainI2,domainO} / GATE{domainI1.domainI2,domainO} / AG{domainI1.domainI2,domainO} (all options work, not case sensitive)
			* AND Gate-Output Complex A -> AGOa{domainI,domainO} (not case sensitive)
			* AND Gate-Output Complex B -> AGOb{domainI,domainO} (not case sensitive)
			* AND Gate Fuel Complex B -> AGF{domain} (not case sensitive)
			* Uncleaved Comparator Gate -> uCG{domainI,domainO} (not case sensitive)
			* Comparator Gate -> CG{domainI,domainO} (not case sensitive)
			* Comparator Gate-Output Complex A -> CGOa{domainI,domainO} (not case sensitive)
			* Comparator Gate-Output Complex B -> CGOb{domainI,domainO} (not case sensitive)

	DNA_con: *float*, *if NONE,default=0*
		DNA template concentration for inputed species. This and ic are the two ways a user can initialize a component being involved in the system. (Only applies to Input,Gate,Reporter,Output,Threshold,Fuel,GF,AG,CG)

	ic: *float*, *optional*
		Initial Concentration for inputted species. This and DNA_con are the two ways a user can initialize a component being involved in the system.

	krz: *float*, *optional* 
		Base ctRSD gate ribozymal cleavage rate.

	krsd: *float*, *optional* 
		Base ctRSD gate forward reaction rate.

	krev: *float*, *optional* 
		Base ctRSD output reverse reaction rate.

	krep: *float*, *optional* 
		Reporter reaction rate.

	krepr: *float*, *optional* 
		Reverse reporter reaction rate.

	kth: *float*, *optional* 
		Thresholding reaction rate.

	krzTh: *float*, *optional* 
		Thresholding ribozymal cleavage rate.

	krsdF: *float*, *optional* 
		Fuel forward reaction rate.

	krevF: *float*, *optional* 
		Fuel reverse reaction rate.

	krz: *float*, *optional* 
		Ribozymal cleavage rate.

	krevA: *float*, *optional* 
		ctRSD AND gate reverse reaction rate.

	krsdA: *float*, *optional* 
		ctRSD AND gate forward reaction rate.

	krzA: *float*, *optional* 
		ctRSD AND gate ribozymal cleavage rate.

	krevCG: *float*, *optional* 
		ctRSD comparator gate reverse reaction rate.

	krsdCG: *float*, *optional* 
		ctRSD comparator gate forward reaction rate.

	krzCG: *float*, *optional* 
		ctRSD comparator gate ribozymal cleavage rate.

	ktxnO: *float*, *optional* 
		Transcription rate for output.

	ktxnG: *float*, *optional* 
		Transcription rate for gate.

	ktxnTh: *float*, *optional* 
		Transcription rate for threshold.

	ktxnF: *float*, *optional* 
		Transcription rate for fuel.

	ktxnAG: *float*, *optional* 
		Transcription rate for AND gate.

	ktxnCG: *float*, *optional* 
		Transcription rate for comparator gate.

	kssdO: *float*, *optional* 
		Degredation rate for output (single stranded).

	kssdF: *float*, *optional* 
		Degredation rate for fuel (single stranded).

	kdsduG: *float*, *optional* 
		Degredation rate for uncleaved gate (double stranded).

	kdsdG: *float*, *optional* 
		Degredation rate for gate (double stranded).

	kdsdGO: *float*, *optional* 
		Degredation rate for gate-output complex (double stranded).

	kdsduAG: *float*, *optional* 
		Degredation rate for uncleaved AND gate (double stranded).

	kdsdAG: *float*, *optional* 
		Degredation rate for AND gate (double stranded).

	kdsduCG: *float*, *optional* 
		Degredation rate for uncleaved comparator gate (double stranded).

	kdsdCG: *float*, *optional* 
		Degredation rate for comparator gate (double stranded).

	kdrd: *float*, *optional* 
		Degredation rate for RNA:DNA hybrids.

	khybO: *float*, *optional* 
		Hybridization rate for output.

	khybR: *float*, *optional* 
		Hybridization rate for reporter.

	khyb: *float*, *optional* 
		Hybrdization rate for both output and reporter (khybO,khybR).




.. _simulate: 

simulate
-----------------

simulate(*t_vec*, *leak=0.03*, *leakA=0.06*, *smethod='False'*, *iteration=1*)

simulate is used to run a simulation for a provided amount of time using the components previously initialized by molecular_species. simulate also includes the discontinuous feature of the simulator.

**Parameters:**
	t_vec: *array, type=float*
		Array of time points signifying the simulation run time.
	leak: *float*, *if NONE,default=0.03*
		Transcription leak rate from ctRSD gate.
	leakA: *float*, *if NONE,default=0.06*
		Transcription leak rate from ctRSD AND gate.
	smethod: *string*, *optional*, *if NONE, default='LSODA'*
		Solver method inputted into scipy.integrate.solve_ivp ODE integrator:
			* RK45
			* RK23
			* DOP853
			* Radau
			* BDF (recommended for comparator gate simulations)
			* LSODA
	iteration: *int*, *if NONE,default=1*
		Controlling input for discontinuous feature. 

		Iteration signifies which step in a total simulation that the inputted simulation time and previously initialized species are tied to. For example, iteration=1 signifies first time step of simulation, iteration=2 signifies second time step of same simulation. There is no maximum in iteration, but must be positive integer. 

		Example of discontinuous feature can be found :ref:`here <discontinuous_simulation>`.


.. _output_concentration: 

output_concentration
--------------------

output_concentration(*name*)

output_concentration is used to pull out desired output concentrations created after running of the simulate function.

**Parameters:**
	name: *string*
		Name of species being initialized
			* Input -> I{domain} / IN{domain} / INP{domain} / INPUT{domain} (all options work, not case sensitive)
			* Gate -> G{domainI,domainO} / GATE{domainI,domainO} (all options work, not case sensitive)
			* Reporter -> R{domain}, REP{domain}, REPORTER{domain} (all options work, not case sensitive)
			* Output -> O{domainI,domainO} / OUT{domainI,domainO} / OUTPUT{domainI,domainO} (all options work, not case sensitive)
			* Uncleaved Gate -> uG{domainI,domainO} (not case sensitive)
			* Gate-Input Complex -> GI{domain} (not case sensitive)
			* Gate-Output Complex -> GO{domainI,domainO} (not case sensitive)
			* Reporter-Output Complex -> RO{domainI,domainO} (not case sensitive)
			* Output Reporter -> S{domain} (not case sensitive)
			* Uncleaved Threshold -> uTH{domain} (not case sensitive)
			* Threshold -> TH{domain} (not case sensitive)
			* Fuel -> F{domain} (not case sensitive)
			* Fuel Gate -> GF{domain} (not case sensitive)
			* Uncleaved AND Gate -> uAG{domainI,domainO} (not case sensitive)
			* AND Gate -> G{domainI1.domainI2,domainO} / GATE{domainI1.domainI2,domainO} / AG{domainI1.domainI2,domainO} (all options work, not case sensitive)
			* AND Gate-Output Complex A -> AGOa{domainI,domainO} (not case sensitive)
			* AND Gate-Output Complex B -> AGOb{domainI,domainO} (not case sensitive)
			* AND Gate Fuel Complex B -> AGF{domain} (not case sensitive)
			* Uncleaved Comparator Gate -> uCG{domainI,domainO} (not case sensitive)
			* Comparator Gate -> CG{domainI,domainO} (not case sensitive)
			* Comparator Gate-Output Complex A -> CGOa{domainI,domainO} (not case sensitive)
			* Comparator Gate-Output Complex B -> CGOb{domainI,domainO} (not case sensitive)
			* Q -> Q{domain} (not case sensitive)


.. _transcription_calibration: 

transcription_calibration
-------------------------

transcription_calibration(*simTime*, *data* , *ktxn='False'*)

transcription_calibration is used to test different transcription rates against an inputted set of data and its corresponding time values. The user can test their data against a base set of rates set in the function, or can specify their own rate(s).

**Parameters:**
	simTime: *array, type=float*
		Array of time points corresponding to the inputted data set.

	data: *array, type=float*
		User data set.

	ktxn: *Multiple Inputs: list(type=float), Single Input: float*, *optional*
		Transcription rate(s) the user wishes to calibrate using the dataset. If more than one transcription rate is being inputted, the rates must be formatted as a list, which can be of any length.

		If NONE, simulator will use a base set of transcription rates. (k_txn = [0.005,0.0075,0.01,0.0125,.015,.02])

		Example of transcription_calibration can be found :ref:`here <calibration_simulation>`.

