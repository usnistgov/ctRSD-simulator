

2022 Science Advances Paper
===========================

.. admonition:: Note:

   The following examples simulate figures from the 2022 Science Advances paper (Schaffter and Strychalski), `Cotranscriptionally encoded RNA strand displacement circuits <https://www.science.org/doi/10.1126/sciadv.abl4354>`_. See the paper for a detailed description of each experiment and/or simulation.

   In that paper a relatively weak output toehold was used with domain 2 for reportering. So in the following scripts, gates with output domain 2 have their reverse strand displacement rate constant decreased compared to the default in *molecular_species()*.


Figure 2D
-----------------------------
Figure 2D simulates a basic, one-layer ctRSD circuit with different input template concentrations.

Useful Features:
	* changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`

`Figure 2D Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/figure2D_simulations_v2.py>`_ 


Figure 4C
-----------------------------
Figure 4C simulates a ctRSD OR element.

Useful Features:
	* globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
	* changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`

`Figure 4C Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/figure4C_simulations_v2.py>`_ 



Figure 4F
-----------------------------
Figure 4F simulates a ctRSD AND gate.

Useful Features:
   * Specifying AND gates within :ref:`molecular_species() <molecular_species>`
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`


`Figure 4F Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/figure4C_simulations_v2.py>`_ 



Figure 4H
----------------------------
Figure 4H uses fuel reactions to simulate a signal amplification element.

Useful Features:
   * Specifying fuel strands within :ref:`molecular_species() <molecular_species>`
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`


`Figure 4H Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/figure4H_simulations_v2.py>`_ 



Figure 5B
----------------------------
Figure 5B simulates a one, two, three, and four layer ctRSD cascades.

Useful Features:
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`


`Figure 5B Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/figure5B_simulations_v2.py>`_ 



Figure 5C
----------------------------
Figure 5C simulates a 4-input ctRSD OR element.

Useful Features:
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`


`Figure 5C Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/figure5C_simulations_v2.py>`_ 



Figure 5D
----------------------------
Figure 5D simulates a two layer cascade of ctRSD AND gates.

Useful Features:
   * Specifying AND gates within :ref:`molecular_species() <molecular_species>`
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`


`Figure 5D Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/figure5D_simulations_v2.py>`_ 


Figure 5E
----------------------------
Figure 5E simulates a two layer cascade of a ctRSD OR gate leading to a ctRSD AND gate.

Useful Features:
   * Specifying AND gates within :ref:`molecular_species() <molecular_species>`
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`

.. admonition:: Warning!

   The original implementation of the model in ctRSD-simulator-1.0.1 overestimated the reverse rates for FAN-IN circuts. The new model implementation in ctRSD-simulator-2.0 corrected this issue. Therefore, the results can be slightly different between simulators. 

   More information on the imporved model implementation can be found :ref:`here <model_implementation>`.


`Figure 5E Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/figure5E_simulations_v2.py>`_ 


Figure 5F
----------------------------
Figure 5F simulates a two layer cascade of a ctRSD AND gate leading to a ctRSD OR element.

Useful Features:
   * Specifying AND gates within :ref:`molecular_species() <molecular_species>`
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`


`Figure 5F Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/figure5F_simulations_v2.py>`_ 


SI Figure 12
-----------------------------
SI Figure 12 simulates an experiment conducted to estimate ribozyme cleavage rate. In the experiment, G{1,2} is initially transcribed for 15 min by itself and given different krz values. After 15 min, the G{1,2} template is degraded (concentration set to 0) and the fraction of the cleaved gate as a function of time is observed in the absence of transcription.

Useful Features:
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`
   * Plotting species other than S{}
   * :ref:`Discontinuous simulation <discontinuous_simulation>` feature in simulate()

`SA22_SI_Figure12 Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/SA22_SI_figure12_v2.py>`_ 



SI Figure 16
-----------------------------
SI Figure 16 simulates mixing fixed concentations of I{1} and G{1,2} with a DNA reporter.

Useful Features:
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`
   * changing indiviudal initial conditions within :ref:`molecular_species() <molecular_species>`
   * :ref:`Discontinuous simulation <discontinuous_simulation>` feature in simulate()

`SA22_SI_Figure16 Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/SA22_SI_figure16_v2.py>`_ 



SI Figure 18
-----------------------------
SI Figure 18 simulates potential mechanims for uncleaved gates reacting slowly with inputs.

Useful Features:
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`


`SA22_SI_Figure18 Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/SA22_SI_figure18_v2.py>`_ 



SI Figure 19
-----------------------------
Figure 19 simulates the effect of increase reversing rates on one, two, three, and four layer cascades.

Useful Features:
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`

`SA22_SI_Figure19 Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/SA22_SI_figure19_v2.py>`_ 



SI Figure 26
-----------------------------
Figure 26 simulates steric hindrance between the leak products and ctRSD gates could reduce overall leak observed in longer cascades.

Useful Features:
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`

`SA22_SI_Figure26 Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/SA22_SI_figure26_v2.py>`_ 



SI Figure 27B
------------------------------
Figure 27B simulates lowering the forward strand displacement rate constant for I{4}.

Useful Features:
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`


`SA22_SI_Figure27B Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/SA22_SI_figure27B_v2.py>`_ 



SI Figure 30C
------------------------------
Figure 30C simulates how ctRSD circuit kinetics depend on toehold length and the length of a single-stranded spacer after the self-cleaving ribozyme.

Useful Features:
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`

`SA22_SI_Figure30C Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/SA22_SI_figure30C_v2.py>`_ 


SI Figure 31B
------------------------------
Figure 31B in the SI shows the influence of total template concentration and T7 RNAP concentration on transcriptional load. In terms, of the simulator, this example presents the need to be able to test different transcription rates to find the best rate for a set of data. The simulator uses :ref:`transcription_calibration <transcription_calibration>` for this purpose.

.. admonition:: Note:
   
   Click :ref:`here <calibration_simulation>` for full features of the *transcription_calibration()* function.
   

Useful Features:
   * calibration transcription rates using :ref:`transcription_calibration() <transcription_calibration>`
   * globally changing rate constants with :ref:`global_rate_constants() <global_rate_constants>`
   * changing indiviudal rate constants within :ref:`molecular_species() <molecular_species>`


`SA22_SI_Figure31B Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/2022%20Science%20Advances%20Paper/SA22_SI_figure31B_v2.py>`_ 

