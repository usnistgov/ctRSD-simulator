.. _troubleshooting:


Troubleshooting
===============


This page offers some useful tips to troubleshoot based off some of the problems we encountered when building the simulator.



Speeding Up Comparator Gate Simulations
---------------------------------------


Due to comparator gate reactions utilizing very disparate time scales, simulations using comparator gates may have a much slower time efficiency than the other reactions. Below are some different options for reducing the simulation time when using comparator gates.

Troubleshooting options:
	1. Utilize the BDF solving method. BDF is an implicit method meant for stiff equations, so it can help to process the CG reactions	quicker. The solving method used can be changed in :ref:`simulate <simulate>`.

	2. If you are looping through the simulator many times, parallelizing these loops can also greatly speed time efficiency. Python offers many different ways to create parallel loops, such as the *multiprocessing* package.



Overriding Rate Constants
------------------------------


Since both :ref:`molecular_species <molecular_species>` and :ref:`global_rate_constants <global_rate_constants>` offer the ability to change the rate constants available in the simulator, you may find one function overriding changes you made in the other.

Troubleshooting Tips (Examples Below):
	1. Both functions will only alter rate constants that are specified in the call of the function. If you do not specify a particular rate constant, then neither functions will change it from its most recent value.


	2. The order of the changes made by the two functions depends on the order in which the functions are called in the script. Whichever function is called first will have its changes come into effect first. Therefore, if you call both functions for the same rate constant, or either functions multiple times for the same rate constant, then the last function call will reflect the most recent value of that rate constant.


.. figure:: /ExampleImages/Troubleshooting-overriding1.png
   :class: with-border
   :align: center

   **global_rate_constants before molecular species**


.. figure:: /ExampleImages/Troubleshooting-overriding2.png
   :class: with-border
   :align: center

   **molecular_species before global_rate_constants**




Accessing Variables in the Simulator
------------------------------------

In order to troubleshoot a script utilizing the simulator, you may want to access different variables that are found in the simulator, but not locally available in your script. 

.. admonition:: Note:

   Only varibles that have the "self" attachment are available to be accessed from outside the simulator (Ex: self.variable_name).

   If you wish to pull out a variable that does not currently have the self attachment, simply add "self." before every occurence of that variable in the simulator.


In order to access any variable with the "self" attachment (Example Below):

	1. The bulk of the simulator's code (excluding the rate equations function) exists in the RSDs_sim Python class. Therefore, as you would to run a simulation, you must first instantiate an object of the RSD_sim class. Details to do this can be found :ref:`here <ImportSim>`.

	2. Assuming the model is downloaded, imported, and instantiated accessing a variable is very similar to calling one of the functions. You simply the call the variable name with the name of the class object's attachment. For example, if you defined the model instantiation as "model", then the format for accessing a variable would be "model.variable_name".


.. figure:: /ExampleImages/Troubleshooting-accessingvariables.png
   :class: with-border
   :align: center

   **How to access variables present in simulator**

**Critical values to check for customized simulations include:**

   The matrices holding DNA template concentrations
      These are specified as *model.[name]temp_con*, where [name] can be G, O, TG, F, AG, CG

   The matrices holding initial concentrations if these were changed in *molecular_species()*
      These are specified as *model.[name]_ic*, where [name] can be uG, G, GO, O, TG, F, AG, CG, R, S, Q, AGOa, AGOb, AGFb, CGOa, CGOb

   The matrices holding rate constants if these were changed in *global_rate_constants()* *molecular_species()*
      These are specified as *model.[name]*, where [name] is the name of the rate constant (ktxnO, krsd, krz, kdrd, kssdO, etc)
