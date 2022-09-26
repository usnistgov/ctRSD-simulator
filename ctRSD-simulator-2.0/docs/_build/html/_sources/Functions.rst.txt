.. _Functions:

Functions
=========

This section lists the different functions available within ctRSD-simulator-2.0.


.. admonition:: Note:

   Before all available functions can be accessed the model must be downloaded, imported, and instantiated!

   More information on these steps can be found :ref:`here <ImportSim>`.




.. _global_rate_constants:

global_rate_constants()
------------------------

**model.global_rate_constants** (*krz='False'*, *krsd='False'*, *krev='False'*, *krep='False'*, *krepr='False'*, 
*kth='False'*, *krzTG='False'*,*krsdF='False'*, *krevF='False'*,
*krsdA='False'*, *krzA='False'*, *krevCG='False'*, 
*krsdCGa='False'*, *krsdCGb='False'*, *krsdCG='False'*, *krzCG='False'*, 
*ktxnO='False'*, *ktxnG='False'*, *ktxnTG='False'* , *ktxnF='False'*, *ktxnAG='False'*, 
*ktxnCG='False'*, *ktxn='False'*, *kssdO='False'*, *kssdF='False'*, *kdsduG='False'*,
*kdsdG='False'*, *kdsdGO='False'*, *kdsduAG='False'*, *kdsdAG='False'*, *kdsduCG='False'*, 
*kdsdCG='False'*, *kdsduTG='False'*,*kdsdTG='False'*,*kdsdGF='False'*, 
*kdsdAGOa='False'*,*kdsdAGOb='False'*,*kdsdAGFb='False'*,*kdsdCGOa='False'*,*kdsdCGOb='False'*,
*kdrd='False'*, *kdeg='False'*, *kssd='False'*, *kdsd='False'*, 
*khybO='False'*, *khybR='False'*, *khyb='False'*, *leak='False'*, *leakA='False'*)

global_rate_constants is used to globally change rate constants for all species of the same type (single matrix), or certain groups of different types (multiple matrices), instead of changing a specific rate constant for just one individual species (index of a matrix).

**The defaults for the rate constants are initialized in the RSD_sim class. These values can be found** :ref:`here <class>`.

.. admonition:: Notes:
	
	Rate constant values should be supplied with units of *nM* and *seconds*

	More than one rate constant can be changed in a single call of *global_rate_constants()*. 

	The different transcription rates and degradation rates both have an input that will change all rates at once. *ktxn* changes all transcription rates in the simulator. *kdeg* changes all degradation rates in the simulator.

**Parameters:**
	krz: *float*, *optional* 
		Single ctRSD gate ribozyme cleavage rate constant.

	krsd: *float*, *optional* 
		Single ctRSD gate forward strand displacement rate constant.

	krev: *float*, *optional* 
		Output reverse strand displacement rate constant. This rate constant applies to outputs reacting with both GO and AGOb complexes.
		This rate constant is 0 for inputs because they only possess an output domain and cannot reverse a strand displacement reaction.

	krep: *float*, *optional* 
		Reporter forward strand displacement rate constant.

	krepr: *float*, *optional* 
		Reporter reverse strand displacement rate constant.

	kth: *float*, *optional* 
		Threshold gate forward strand displacement rate constant.

	krzTG: *float*, *optional* 
		Threshold gate ribozyme cleavage rate constant.

	krsdF: *float*, *optional* 
		Fuel forward forward strand displacement rate constant.

	krevF: *float*, *optional* 
		Fuel reverse strand displacement rate constant.

	krsdA: *float*, *optional* 
		ctRSD AND gate forward strand displacement rate constant.
		Changing this rate constant in *global_rate_constants()* will change the reaction rate for both input domains of an AG. To change these rates individually see *molecular_species()* below.

	krzA: *float*, *optional* 
		ctRSD AND gate ribozyme cleavage rate constant.

	krevCG: *float*, *optional* 
		Reverse strand displacement rate constant for outputs on a CG. These rates follow outputs, not CG gate indices.

	krsdCGa: *float*, *optional* 
		ctRSD comparator gate forward strand displacement rate constant for the first input domain of a CG (CG{i,_}).

	krsdCGb: *float*, *optional* 
		ctRSD comparator gate forward strand displacement rate constant for the second input domain of a CG (CG{_,j}).

	krsdCG: *float*, *optional* 
		ctRSD comparator gate forward strand displacement rate constant for both input domains.
		Changing this parameter will change both krsdCGa and krsdCGb.

	krzCG: *float*, *optional* 
		ctRSD comparator gate ribozyme cleavage rate constant.

	ktxnO: *float*, *optional* 
		Transcription rate constant for outputs (and inputs).
		This will change the transcription rates for both inputs (held along the diagonal of the ktxnO matrix) and the outputs.
		To change inputs individually change ktxnO in *molecular_species()* with the specific input.

	ktxnG: *float*, *optional* 
		Transcription rate constant for gates.

	ktxnTG: *float*, *optional* 
		Transcription rate constant for threshold gates.

	ktxnF: *float*, *optional* 
		Transcription rate constant for fuels.

	ktxnAG: *float*, *optional* 
		Transcription rate constants for AND gates.

	ktxnCG: *float*, *optional* 
		Transcription rate constant for comparator gates.


	kssdO: *float*, *optional* 
		Single stranded RNA degredation rate constant for outputs (and inputs).

	kssdF: *float*, *optional* 
		Single stranded RNA degredation rate constant for fuel strands.


	kdsduG: *float*, *optional* 
		Double stranded RNA degredation rate constant for uncleaved gates.

	kdsdG: *float*, *optional* 
		Double stranded RNA degredation rate constant for uncleaved gates.

	kdsdGO: *float*, *optional* 
		Double stranded RNA degredation rate constant for gate:output (GO) complexes.

	kdsduAG: *float*, *optional* 
		Double stranded RNA degredation rate constant for uncleaved AND gates.

	kdsdAG: *float*, *optional* 
		Double stranded RNA degredation rate constant for AND gates.

	kdsduCG: *float*, *optional* 
		Double stranded RNA degredation rate constant for uncleaved comparator gates.

	kdsdCG: *float*, *optional* 
		Double stranded RNA degredation rate constant for comparator gates.

	kdsduTG: *float*, *optional* 
		Double stranded RNA degredation rate constant for uncleaved threshold gates.

	kdsdTG: *float*, *optional* 
		Double stranded RNA degredation rate constant for threshold gates.

	kdsdGF: *float*, *optional* 
		Double stranded RNA degredation rate constant for gate:fuel (GF) complexes.

	kdsdAGOa: *float*, *optional* 
		Double stranded RNA degredation rate constant for AGOa complexes.

	kdsdAGOb: *float*, *optional* 
		Double stranded RNA degredation rate constant for AGOb complexes.

	kdsdAGFb: *float*, *optional* 
		Double stranded RNA degredation rate constant for AGFb complexes.

	kdsdCGOa: *float*, *optional* 
		Double stranded RNA degredation rate constant for CGOa complexes.

	kdsdCGOb: *float*, *optional* 
		Double stranded RNA degredation rate constant for CGOb complexes.


	kdrd: *float*, *optional* 
		Degredation rate constant for RNA in RNA:DNA hybrid duplexes.

	khybO: *float*, *optional* 
		Hybridization rate constant for output binding to the Q strand of the reporter.

	khybR: *float*, *optional* 
		Hybridization rate constant for the S strand to bind to the Q strand of the reporter.

	leak: *float*, *optional* 
		The percentage of leak transcription from a single input gate (G). This should be supplied as a decimal representing a percentage, *i.e.*, 0.05 to represent 5%.

	leakA: *float*, *optional* 
		The percentage of leak transcription from an AND gate (AG). This should be supplied as a decimal representing a percentage, *i.e.*, 0.05 to represent 5%.

**Changes to multiple classes of rate constants with a single input:**

	kssd: *float*, *optional* 
		To change the degredation rate consant for all single stranded species 

		(kssdO, kssdF).

	kdsd: *float*, *optional* 
		To change the degredation rate constant for all double stranded species 
		
		(kdsduG, kdsdG, kdsdGO, kdsduAG, kdsdAG, kdsduCG, kdsdCG, kdsduTG, kdsdTG, kdsdGF, kdsdAGOa, kdsdAGOb, kdsdAGFb, kdsdCGOa, kdsdCGOb).

	ktxn: *float*, *optional*
		To change change all transcription rate constants

		(ktxnO, ktxnG, ktxnTG, ktxnF, ktxnAG, ktxnCG)

	kdeg: *float*, *optional* 
		To change the degredation rate consant for all species

		(kssdO, kssdF, kdsduG, kdsdG, kdsdGO, kdsduAG, kdsdAG, kdsduCG, kdsdCG, kdrd).

	khyb: *float*, *optional* 
		To change the hybrdization rate constant for both output and reporter

		(khybO, khybR).




.. _molecular_species:

molecular_species()
--------------------

**model.molecular_species** (*name*, *DNA_con=0*, *ic='False'*, *krz='False'*, *krsd='False'*, *krev='False'*,
*krep='False'*, *krepr='False'*, *kth='False'*, *krzTG='False'*, *krsdF='False'*,
*krevF='False'*, *krsdA='False'*, *krzA='False'*, *krevCG='False'*, *krevCGa='False'*, *krevCGb='False'*,
*krsdCG='False'*, *krsdCGa='False'*, *krsdCGb='False'*, *krzCG='False'*, *ktxnO='False'*, *ktxnG='False'*,
*ktxnTG='False'*, *ktxnF='False'*, *ktxnAG='False'*, *ktxnCG='False'*, *kssdO='False'*, *kssdF='False'*,
*kdsduG='False'*, *kdsdG='False'*, *kdsdGO='False'*, *kdsduAG='False'*, *kdsdAG='False'*,
*kdsduCG='False'*, *kdsdCG='False'*, *kdsduTG='False'*, *kdsdTG='False'*, *kdsdGF='False'*,
*kdsdAGOa='False'*, *kdsdAGOb='False'*, *kdsdAGFb='False'*, *kdsdCGOa='False'*, *kdsdCGOb='False'*,
*kdrd='False'*, *khybO='False'*, *khybR='False'*, *leak='False'*, *leakA='False'*):

molecular_species is used to initialize all species involved in the system being simulated.

**Default DNA templates, initial conditions, and rate constants are initialized in RSD_sim. These values can be found** :ref:`here <class>`.


.. admonition:: Notes:

   Rate constant values should be supplied with units of *nM* and *seconds*

   More than one rate constant can be changed in a single call of *molecular_species()*. 

   Specifying an optional rate constant parameter in this function will only change the value for the individual species specified in *name*. The rest of the species will have the default values or the values specified in *global_rate_constants()* if called before *molecular_species()*. 

   Only rate constant values relevent to the species defined with *name* can be changed. For example, it is not possible to change krz for an input or output. Likewise it is not possible to change krsdA for a single input gate (G). A warning message will be issued if the specified rate constant cannot be changed for the named species. If multiple rate constants are changed in a single call the warning message will not specify which rate constant cannot be changed.


**Parameters:**
	name: *string*
		*name* inputs that show multiple options function with each of those options. All *name* inputs are also not case sensitive.
		
		Name of species being initialized
			* Input -> I{domain} / IN{domain} / INP{domain} / INPUT{domain} 
			* Gate -> G{domainI,domainO} / GATE{domainI,domainO} 
			* Reporter -> R{domain}, REP{domain}, REPORTER{domain} 
			* Output -> O{domainI,domainO} / OUT{domainI,domainO} / OUTPUT{domainI,domainO}
			* Uncleaved Gate -> uG{domainI,domainO} 
			* Gate-Input Complex -> GI{domain} (not case sensitive)
			* Gate-Output Complex -> GO{domainI,domainO} 
			* Reporter-Output Complex -> RO{domainI,domainO} 
			* Reporter Signal Strand -> S{domain} 
			* Reporter Signal Complement Strand -> Q{domain}
			* Uncleaved Threshold Gate -> uTG{domain} / uT{domains} / uTH{domain}
			* Threshold Gate -> TG{domain} / T{domains} / TH{domain}
			* Fuel -> F{domain} 
			* Gate-Fuel Complex -> GF{domain} 
			* Uncleaved AND Gate -> uAG{domainI,domainO}
			* AND Gate -> AG{domainI1.domainI2,domainO} / G{domainI1.domainI2,domainO} / GATE{domainI1.domainI2,domainO}
			* AND Gate-Output Complex A -> AGOa{domainI2,domainO} 
			* AND Gate-Output Complex B -> AGOb{domainI,domainO} 
			* AND Gate Fuel Complex B -> AGFb{domain} 
			* Uncleaved Comparator Gate -> uCG{domainI1,domainI2} 
			* Comparator Gate -> CG{domainI1,domainI2} 
			* Comparator Gate-Output Complex A -> CGOa{domainI,domainO} 
			* Comparator Gate-Output Complex B -> CGOb{domainI,domainO} 

	DNA_con: *float*, *if NONE,default=0*
		DNA concentration for inputed species. This and ic are the two ways a user can initialize a component being involved in the system. (Only applies to Input,Output,Gate,Fuel,AG,TG,CG,Reporter). Other than for Reporters this variable specifies the DNA template concentration for transcribable components in ctRSD circuits. For Reporter this is the same as a fixed initial concentration (ic).
		Other than for Reporter this represents the concentration of the DNA template that encodes for the transcription of the species specified in *name*.

	ic: *float*, *optional*, *if NONE,default=0*
		Initial Concentration for inputted species. This and DNA_con are the two ways a user can initialize a component being involved in the system. Other than for the Reporter, this refers to the initial concentration of the RNA species specified in *name*

	krz - leakA: *floats*, *optional*
		These optional rate constant parameters are defined as in the *global_rate_constants()* function. But changing them in *molecular_species()* will only change the value for the individual species specified in *name*
		Below are some additional paramaters and caveats unique to *molecular_species()*

		ktxnO: *float*, *optional* 
			Transcription rate constant for outputs (and inputs).

			To change the transcription rate of an indivdual input use this optional parameter. ktxnI is not a valid input.

			EX: model.molecular_species(I{3}, ktxnO=0.02)

		krsdA: *float*, *optional* 
			ctRSD AND gate forward strand displacement rate.

			If specified with AG, this will change the rate constant for the reaction with the first output in the AG. To change the rate constant for the reaction with the second output the user can specify an AGOa species anc change this rate constant.
			
			Ex: 

			.. code-block:: python

				model.molecular_species(AG{3.1,2}, krsdA=1e5/1e9) # changes krsdA for first input domain
				
				model.molecular_species(AGOa{1,2}, krsdA=1e5/1e9) # changes krsdA for second input domain

		krevCG: *float*, *optional*
			Reverse strand displacement rate constant for outputs on a CG. These rates follow outputs, not CG gate indices.
			This rate constant should be changed with specific outputs (or inputs) specified in *molecular_species()*, *e.g.*, 
			molecular_species(O{3,1},krevCG=0.4) or molecular_species(I{3},krevCG=0.4) which changes the rate these outputs/inputs dissociate from a CG.
			To change the reverse rates for all outputs that correspond to either domain of a CG use the *krevCGa* and *krevCGb* paramters below.

		krevCGa: *float*, *optional*
			Reverse strand displacement rate constant for all outputs (or inputs) that bind to the first index of a CG, *i.e.*, CG{i,_}.
			This changes the entire i-th column of the *krevCG* matrix.

		krevCGb: *float*, *optional*
			Reverse strand displacement rate constant for all outputs (or inputs) that bind to the second index of a CG, *i.e.*, CG{_,j}.
			This changes the entire j-th column of the *krevCG* matrix.

		If an AND gate (AG) is specified its leak transcription percentage can be changed with either *leak* or *leakA*.



.. _simulate: 

simulate()
-----------------

**model.simulate** (*t_vec*, *smethod='False'*, *iteration=1*)

simulate is used to run a simulation for a provided amount of time using the components previously initialized by molecular_species. simulate also includes the discontinuous feature of the simulator.

**Parameters:**
	t_vec: *array, type=float*
		Array of time points signifying the simulation run time and interval.

	smethod: *string*, *optional*, *if NONE, default='LSODA'*
		Solver method inputted into scipy.integrate.solve_ivp ODE integrator:
			* RK45
			* RK23
			* DOP853
			* Radau
			* BDF (recommended for comparator gate simulations)
			* LSODA

		For simulations using comparator gates (CG) the 'BDF' method is recommended. This can speed up the computation time.

	iteration: *int*, *if NONE,default=1*
		Controlling input for discontinuous feature. 

		Iteration signifies which step in a total simulation that the inputted simulation time and previously initialized species are tied to. For example, iteration=1 signifies first time step of simulation, iteration=2 signifies second time step of same simulation. There is no maximum in iteration, but must be positive integer. 

		Example of discontinuous feature can be found :ref:`here <discontinuous_simulation>`.


.. _output_concentration: 

output_concentration()
-----------------------

**model.output_concentration** (*name*)

output_concentration is used to pull out desired output concentrations created after running of the simulate function. 

.. admonition:: Note:

	Concentrations are output with *nM* units

	To compare to experiments with DNA reporters, the concentration of S{j} can be pulled out for plotting:
	*reacted_reporter = model.output_concentration('S{2}')*


**Parameters:**
	name: *string*
		*name* inputs that show multiple options function with each of those options. All *name* inputs are also not case sensitive.

		Name of species being initialized
			* Input -> I{domain} / IN{domain} / INP{domain} / INPUT{domain} 
			* Gate -> G{domainI,domainO} / GATE{domainI,domainO} 
			* Reporter -> R{domain}, REP{domain}, REPORTER{domain} 
			* Output -> O{domainI,domainO} / OUT{domainI,domainO} / OUTPUT{domainI,domainO}
			* Uncleaved Gate -> uG{domainI,domainO} 
			* Gate-Input Complex -> GI{domain} (not case sensitive)
			* Gate-Output Complex -> GO{domainI,domainO} 
			* Reporter-Output Complex -> RO{domainI,domainO} 
			* Reporter Signal Strand -> S{domain} 
			* Reporter Signal Complement Strand -> Q{domain}
			* Uncleaved Threshold Gate -> uTG{domain} / uT{domains} / uTH{domain}
			* Threshold Gate -> TG{domain} / T{domains} / TH{domain}
			* Fuel -> F{domain} 
			* Gate-Fuel Complex -> GF{domain} 
			* Uncleaved AND Gate -> uAG{domainI,domainO}
			* AND Gate -> AG{domainI1.domainI2,domainO} / G{domainI1.domainI2,domainO} / GATE{domainI1.domainI2,domainO}
			* AND Gate-Output Complex A -> AGOa{domainI2,domainO} 
			* AND Gate-Output Complex B -> AGOb{domainI,domainO} 
			* AND Gate Fuel Complex B -> AGF{domain} 
			* Uncleaved Comparator Gate -> uCG{domainI1,domainI2} 
			* Comparator Gate -> CG{domainI1,domainI2} 
			* Comparator Gate-Output Complex A -> CGOa{domainI,domainO} 
			* Comparator Gate-Output Complex B -> CGOb{domainI,domainO} 


.. _transcription_calibration: 

transcription_calibration()
----------------------------

**model.transcription_calibration** (*simTime*, *data* , *ktxn='False'*)

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

