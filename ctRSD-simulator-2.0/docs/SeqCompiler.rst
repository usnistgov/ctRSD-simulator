

Sequence Compiler
=================

Sequence compiler is a function avaliable in the simulator that takes in a species name as an input (same nomenclature used elsewhere in the simulator), among other function inputs, and outputs the strand sequence that fits that specified species name.

.. admonition:: Note:

	Although it is a function within the simulator, and is accessed in the same way as the other functins, it does not require a system to be simulated to be used. Hence why its documentation is being kept seperate from the other functions.

	Sequence compiler was included in the simulator so that users could all the useful tools in designing ctRSD circuits all in one place.


.. _DownloadDomainsList:

Download Domains List
---------------------

Below is a link to download a provided spreadhset that contains the list of domains for ctRSD reactions used to compile the sequences. The local file path on your computer will be an input into the sequence compiler function.

`ctRSD Domains List Spreadsheet can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Sequence Compiler/ctRSD_domains_list.xlsx>`_ 


Function Documentation
----------------------


.. admonition:: Warning!

   Before all available functions can be accessed the model must be downloaded, imported, and instantiated!

   More information on these steps can be found :ref:`here <ImportSim>`.




ctRSD_seq_compile(*name*,*filepath*,*Rz='Ro'*,*L='L'*,*term='T7t'*,*hp5='5hp'*,*eI=''*,*eO=''*,*s=''*,*invert=0*):

*name* inputs that show multiple options function with each of those options. All *name* inputs are also not case sensitive.

**Parameters:**
	name: *string*
		Name of species sequence will be compiled for.
			* Input -> I{domain} / IN{domain} / INP{domain} / INPUT{domain} 
			* Gate -> G{domainI,domainO} / GATE{domainI,domainO} 
			* Threshold -> T{domains} / TH{domain} / TG{domain}
			* Fuel -> F{domain} 
			* AND Gate -> G{domainI1.domainI2,domainO} / GATE{domainI1.domainI2,domainO} / AG{domainI1.domainI2,domainO} 
			* Comparator Gate -> CG{domainI,domainO} 
			* Comparator Gate-Output Complex A -> CGOa{domainI,domainO}
	
	filepath: *string*
		File path for ctRSD domains list excel sheet. Donwload :ref:`here <DownloadDomainsList>`.
	
	Rz: *string*, *optional*, *if NONE,default='Ro'*
		Ribozyme used.

	L: *string*, *optional*, *if NONE,default='L'*

	term: *string*, *optional*, *if NONE,default='T7t'*

	hp5: *string*, *optional*, *if NONE,default='5hp'*

	eI: *string*, *optional*

	eO: *string*, *optional*

	s: *string*, *optional*

	invert: *Boolean*, *optional*, *if NONE,0*



Examples
--------

First Steps:
	1. :ref:`Download, Import, and Initialize ctRSD-simulator-2.0 <ImportSim>`

	2. :ref:`Download ctRSD Domains List <DownloadDomainsList>`

	3. Use the example below for guidance!



.. figure:: /ExampleImages/SequenceCompilerExample.png
   :class: with-border
   :align: center

   **Sequence Compiler Example**



`Sequence Compiler Example Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Sequence Compiler/SequenceCompilerExample.py>`_ 