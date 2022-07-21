
Simulator Features
==================

.. admonition:: Note:

   All following examples are important features of the ctRSD-simulator-2.0.




.. _calibration_simulation:

Calibration Simulation
----------------------

Calibration simulation shows the functionalities of the :ref:`transcription_calibration <transcription_calibration>` function. The function is used for testing different transcription rates in order to find the best fit rate for an inputted data set. The user can test their data against a base set of transcription rates provided by the function, or specify what specfic rate(s) they would like to test.

.. admonition:: Note:

   The provided Python script includes the creation of a set of test data inputted into the function.


Some Functionalities used:
	* calibration transcription rates using :ref:`transcription_calibration <transcription_calibration>`



`Calibration Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/calibration_simulation.py>`_ 



.. figure:: /ExampleImages/calibration_simulation_baserates.svg
   :align: center



   **Calibration Against Base Rates**



.. figure:: /ExampleImages/calibration_simulation_specifiedrates.svg
   :align: center

   **Calibration Against Specified Rates**







.. _discontinuous_simulation:


Discontinuous Simulation
------------------------

Discontinuous Simulation provides guidance for the usage of discontinuous feature of ctRSD-simulator-2.0. This feature allows the user to run a simulation for a specific amount of time using any desired conditions, and then apply a different set of conditions for the next time span, till the given end of the simulation. The user has the ability to change the conditions for a given amount of time across the entire length of the simulation as many times as needed. Also, full function of the different features of the simulator are available to be changed for different time spans of the total simulaton time.

.. admonition:: Note:
   
   The discontinuous feature is a part of the simulate function. More information on using simulate for discontinuous simulations can be found :ref:`here <simulate>`.



Some Functionalities used:
	* globally changing rates with :ref:`global_rate_constants <global_rate_constants>`
	* changing initial condtions/indiviudal rates within :ref:`molecular_species <molecular_species>`
	* launching simulation using :ref:`simulate <simulate>`
	* discontinuous feature available using :ref:`simulate <simulate>`
	* pulling out desired output concentrations using :ref:`output_concentration <output_concentration>`



Comparison to ctRSD-simulator-1
+++++++++++++++++++++++++++++++
`Discontinuous Simulation Comparison Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/discontinuous_simulationsCompar.py>`_ 

.. figure:: /ExampleImages/discontinuous_simulationsCompar.svg
   :class: with-border
   :align: center

   **Discontinuous Simulation Comparison**



Usage in ctRSD-simulator-2.0
++++++++++++++++++++++++++++
`Discontinuous Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/discontinuous_simulations.py>`_ 

.. figure:: /ExampleImages/discontinuous_simulations.svg
   :class: with-border
   :align: center

   **Discontinuous Simulation**











Comparator Gate Simulation
--------------------------

Comparator Gate simulation shows a basic comparator gate reaction. This features shows the ability for a ctRSD circuit to be designed so that one output over the other is made depending on which input has a higher concentration.



Some Functionalities used:
	* globally changing rates with :ref:`global_rate_constants <global_rate_constants>`
	* changing initial condtions/indiviudal rates within :ref:`molecular_species <molecular_species>`
	* launching simulation using :ref:`simulate <simulate>`
	* pulling out desired output concentrations using :ref:`output_concentration <output_concentration>`



Comparison to ctRSD-simulator-1
+++++++++++++++++++++++++++++++
`CG Simulation Comparison Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/CG_simulationsCompar.py>`_ 

.. figure:: /ExampleImages/CG_simulationsCompar.svg
   :class: with-border
   :align: center

   **CG Simulation Comparison**



Usage in ctRSD-simulator-2.0
++++++++++++++++++++++++++++
`CG Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/CG_simulations.py>`_ 

.. figure:: /ExampleImages/CG_simulations.svg
   :class: with-border
   :align: center

   **CG Simulation**


The CG grid simulation is another example using a basic CG system. However, a grid is made using two sets of changing input concentrations. The x-axis shows changing IN{6}, whereas the y-axis shows increasing IN{7}. The grid example efficiently demonstrates the consistent functionality of the comparator gates.


`CG Grid Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/CG_simulationsGRID.py>`_ 

.. figure:: /ExampleImages/CG_simulationsGRID.svg
   :class: with-border
   :align: center

   **CG Grid Simulation**




Three Comparator Gate Simulation
--------------------------------

Three Comparator Gate Simulation is a system of three comparator gates and three inputs where only the highest input concentration will create the corresponding output reporter.


Some Functionalities used:
	* globally changing rates with :ref:`global_rate_constants <global_rate_constants>`
	* changing initial condtions/indiviudal rates within :ref:`molecular_species <molecular_species>`
	* launching simulation using :ref:`simulate <simulate>`
	* pulling out desired output concentrations using :ref:`output_concentration <output_concentration>`



Comparison to ctRSD-simulator-1
+++++++++++++++++++++++++++++++
`Three CG Simulation Comparison Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/threeCG_simulationsCompar.py>`_ 

.. figure:: /ExampleImages/threeCG_simulationsCompar.svg
   :class: with-border
   :align: center

   **Three CG Simulation Comparison**



Usage in ctRSD-simulator-2.0
++++++++++++++++++++++++++++
`Three CG Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/threeCG_simulations.py>`_ 

.. figure:: /ExampleImages/threeCG_simulations.svg
   :class: with-border
   :align: center

   **Three CG Simulation**








Thresholding Simulation
--------------------------------

Thresholding Simulation showcases a simple thresholding reaction, where a threshold can be added to a given system to effectively annihlate corresponding input concentrations.


Some Functionalities used:
	* changing initial condtions/indiviudal rates within :ref:`molecular_species <molecular_species>`
	* launching simulation using :ref:`simulate <simulate>`
	* pulling out desired output concentrations using :ref:`output_concentration <output_concentration>`



Comparison to ctRSD-simulator-1
+++++++++++++++++++++++++++++++
`Thresholding Simulation Comparison Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/threshold_simulationCompar.py>`_ 

.. figure:: /ExampleImages/threshold_simulationCompar.svg
   :class: with-border
   :align: center

   **Thresholding Simulation Comparison**



Usage in ctRSD-simulator-2.0
++++++++++++++++++++++++++++
`Thresholding Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/threshold_simulation.py>`_ 

.. figure:: /ExampleImages/threshold_simulation.svg
   :class: with-border
   :align: center

   **Thresholding Simulation**







Degradation Simulation
--------------------------------

Degradation Simulation shows the ability to use :ref:`global_rate_constants <global_rate_constants>` to raise degradation rates from their 0 default to initialize degradation reactions in a system. 

:ref:`global_rate_constants <global_rate_constants>` gives the user the ability to change all degradation rates at once using "kdeg" as an argument, to just change degradation rates for single stranded species,"kssd," double stranded species,"kdsd," or RNA:DNA hyrbids,"kdrd," and finally to change the degrdation rates for any given individual species.

The following two figures change all degradation rates simultaneously.


Some Functionalities used:
	* globally changing rates with :ref:`global_rate_constants <global_rate_constants>`
	* changing initial condtions/indiviudal rates within :ref:`molecular_species <molecular_species>`
	* launching simulation using :ref:`simulate <simulate>`
	* pulling out desired output concentrations using :ref:`output_concentration <output_concentration>`



Comparison to ctRSD-simulator-1
+++++++++++++++++++++++++++++++

`Degradation Simulation Comparison Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/degradation_simulationsCompar.py>`_ 

.. figure:: /ExampleImages/degradation_simulationsCompar.svg
   :class: with-border
   :align: center

   **Degradation Simulation Comparison**



Usage in ctRSD-simulator-2.0
++++++++++++++++++++++++++++

`Degredation Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/degradation_simulations.py>`_ 

.. figure:: /ExampleImages/degradation_simulations.svg
   :class: with-border
   :align: center

   **Degradation Simulation**


The final degredation example simulates a system with degradation rates where single stranded species, double stranded species, and RNA:DNA hyrbids were given altering degradation rates.


`Degradation Simulation with changing groups of rates Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/degradationIndividRates_simulations.py>`_ 

.. figure:: /ExampleImages/degradationIndividRates_simulation.svg
   :class: with-border
   :align: center

   **Degradation Simulation (Changing Groups of Degradation Rates**





Seesaw Simulations
-------------------

A simulation of an AND gate using the seesaw gate design from `Scaling Up Digital Circuit Computation with DNA Strand Displacement Cascades (Qian and Winfree Science 2011) <https://www.science.org/doi/10.1126/science.1200520>`_.


Some Functionalities used:
   * globally changing rates with :ref:`global_rate_constants <global_rate_constants>`
   * changing initial condtions/indiviudal rates within :ref:`molecular_species <molecular_species>`
   * launching simulation using :ref:`simulate <simulate>`
   * pulling out desired output concentrations using :ref:`output_concentration <output_concentration>`



ctRSD Seesaw Simulation
+++++++++++++++++++++++++++++++
`ctRSD Seesaw Simulation Comparison Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/seesaw_simulation_ctRSD.py>`_ 

.. figure:: /ExampleImages/seesaw_simulation_ctRSD.svg
   :class: with-border
   :align: center

   **ctRSD Seesaw Simulation Comparison**



DNA Seesaw Simulation
++++++++++++++++++++++++++++
`DNA Seesaw Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/seesaw_simulation_DNA.py>`_ 

.. figure:: /ExampleImages/seesaw_simulation_DNA.svg
   :class: with-border
   :align: center

   **DNA Seesaw Simulation**







Two-Toehold Simulation
----------------------------
Two-Toehold Simulation shows the differing results of a multi toehold system.

Some Functionalities used:
   * globally changing rates with :ref:`global_rate_constants <global_rate_constants>`
   * changing initial condtions/indiviudal rates within :ref:`molecular_species <molecular_species>`
   * launching simulation using :ref:`simulate <simulate>`
   * pulling out desired output concentrations using :ref:`output_concentration <output_concentration>`



`Two Toehold Sim Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/TwoToehold_simulation.py>`_ 

.. figure:: /ExampleImages/TwoToehold_simulation.svg
   :class: with-border
   :align: center

   **Two-Toehold Simulation**




AND Gate with Fuel Simulation
------------------------------
This simulation shows a basic ctRSD AND gate system, but with fuel added to one of the inputs using :ref:`molecular_species <molecular_species>`

Some Functionalities used:
   * globally changing rates with :ref:`global_rate_constants <global_rate_constants>`
   * changing initial condtions/indiviudal rates within :ref:`molecular_species <molecular_species>`
   * launching simulation using :ref:`simulate <simulate>`
   * pulling out desired output concentrations using :ref:`output_concentration <output_concentration>`



`AG Fuel Sim Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/AGfuel_simulations.py>`_ 

.. figure:: /ExampleImages/AGfuel_simulations.svg
   :class: with-border
   :align: center

   **AG Fuel Simulation**




Two Minterm Simulation
----------------------------
Two Minterm Simulation shows a 4-input, 2 ctRSD AND gate system. (ex. AB + CD)

Some Functionalities used:
   * globally changing rates with :ref:`global_rate_constants <global_rate_constants>`
   * changing initial condtions/indiviudal rates within :ref:`molecular_species <molecular_species>`
   * launching simulation using :ref:`simulate <simulate>`
   * pulling out desired output concentrations using :ref:`output_concentration <output_concentration>`



`Two Minterm Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator-2.0/blob/main/Examples/AB+CD_simulations.py>`_ 

.. figure:: /ExampleImages/AB+CD_simulations.svg
   :class: with-border
   :align: center

   **Two Minterm Simulation**