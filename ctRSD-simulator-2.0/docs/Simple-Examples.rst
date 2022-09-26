
.. _simple_examples:

Simple Examples
===============


.. _single_layer:

Single ctRSD Gate Reaction
---------------------------

Simulating the system below:


.. figure:: /ExampleImages/single_gate_reaction.png
   :align: center

   **Single ctRSD Gate Reaction**


`Single ctRSD Gate Reaction Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/Simple Examples/single_gate_reaction.py>`_ 


.. code-block:: python

   import ctRSD_simulator_200 as RSDs # import latest simulator version

   # create the model instance
   model = RSDs.RSD_sim() # default # of domains (5 domains)

   # specify species involved in the system
   model.molecular_species('I{1}',DNA_con=25)
   model.molecular_species('G{1,2}',DNA_con=25)
   model.molecular_species('R{2}',ic=500)

   # simulating the model
   t_sim = np.linspace(0,6,1001)*3600 # seconds
   model.simulate(t_sim) # simulate the model

   # pull out the species from the model solution to plot
   S2 = model.output_concentration('S{2}')



.. _two_layer:

Two-Layer Cascade Simulation
----------------------------

Simulating the system below:


.. figure:: /ExampleImages/two_layer_simulation.png
   :class: with-border
   :align: center

   **Two-Layer Cascade Simulation**

`Two Layer Cascade Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/Simple Examples/two_layer_simulation.py>`_ 


.. code-block:: python

   import ctRSD_simulator_200 as RSDs # import latest simulator version

   # create the model instance
   model = RSDs.RSD_sim() # default # of domains (5 domains)

   model.global_rate_constants(ktxn=0.02) # changing the global transcription rate constant

   # specify species involved in the system
   model.molecular_species('I{3}',DNA_con=25)
   model.molecular_species('G{3,1}',DNA_con=25)
   model.molecular_species('G{1,2}',DNA_con=10)
   model.molecular_species('R{2}',ic=500)

   # simulating the model
   t_sim = np.linspace(0,6,1001)*3600 # seconds
   model.simulate(t_sim) # simulate the model

   # pull out the species from the model solution to plot
   S2 = model.output_concentration('S{2}')



.. _fan_out_simulation:


Fan-Out Simulation
--------------------------

Simulating the system below:


.. figure:: /ExampleImages/fan_out_simulation.png
   :class: with-border
   :align: center

   **Fan-Out Simulation**


`Fan Out Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/Simple Examples/fan_out_simulation.py>`_ 


.. code-block:: python

   import ctRSD_simulator_200 as RSDs # import latest simulator version

   # create the model instance
   model = RSDs.RSD_sim() # default # of domains (5 domains)

   model.global_rate_constants(ktxn=0.02) # changing the global transcription rate constant

   # specify species involved in the system
   model.molecular_species('O{4,3}',DNA_con=25)
   model.molecular_species('G{3,1}',DNA_con=15)
   model.molecular_species('G{3,5}',DNA_con=15,krsd=5e-6) # changing krsd{3,5} 
   model.molecular_species('R{1}',ic=500,krep=5e-5) # changing krep{1}
   model.molecular_species('R{5}',ic=500)

   # simulating the model
   t_sim = np.linspace(0,6,1001)*3600 # seconds
   model.simulate(t_sim) # simulate the model

   # pull out the species from the model solution to plot
   S1 = model.output_concentration('S{1}')
   S5 = model.output_concentration('S{5}')



Fan-Out Fan-In Simulation
--------------------------

Simulating the system below:


.. figure:: /ExampleImages/fan_out_fan_in_simulation.png
   :class: with-border
   :align: center

   **Fan-Out Fan-In Simulation**

`Fan Out Fan In Simulation Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/Simple Examples/fan_out_fan_in_simulation.py>`_ 


.. code-block:: python

   import ctRSD_simulator_200 as RSDs # import latest simulator version

   # create the model instance
   model = RSDs.RSD_sim(8) # increasing # of domains to match highest index in system

   model.global_rate_constants(ktxn=0.02) # changing the global transcription rate constant

   # specify species involved in the system
   model.molecular_species('O{4,3}',DNA_con=25)
   model.molecular_species('G{3,8}',DNA_con=15)
   model.molecular_species('G{3,5}',DNA_con=15,krsd=5e-6) # changing krsd{3,5} 
   model.molecular_species('G{8,2}',DNA_con=10,krev=1e-8) # changing krev{8,2}
   model.molecular_species('G{5,2}',DNA_con=10,krsd=3e-6,krev=1e-8) # changing krsd{5,2} and krev{5,2} 
   model.molecular_species('R{2}',ic=500)

   # simulating the model
   t_sim = np.linspace(0,6,1001)*3600 # seconds
   model.simulate(t_sim) # simulate the model

   # pull out the species from the model solution to plot
   S2 = model.output_concentration('S{2}')


Experimental Nomenclature
--------------------------

Simulating the systems below:


.. figure:: /ExampleImages/exp_nomenclature_examples.png
   :class: with-border
   :align: center

   **Single gate reaction and two layer cascade with experimental nomenclature** In ctRSD circuit experiments different input and output toeholds are often used. This, and the inclusion of other additional domains, leads to an expanded nomenclature compared to what is used in the simulator. Experimentalists may want to use the expanded nomenclature in their simulations to keep track of how circuits are linked together. The simulator allows for this expanded nomenclature by ignoring any letters before or after the input-output indices of a component. The code below highlights this feature. 

Note using the expanded nomenclature below does not change anything about the simulation. The simulator ignores the letters before or after the indices. This is merely a way to keep track of the experimental components in a simulation. If the different toeholds have different rate constants, these can be changed when each component is defined in *molecular_species()*, see :ref:`Two toehold cascade simulation <two_toehold>`


`Single ctRSD Gate Reaction with Experimental Nomenclature Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/Simple Examples/single_gate_reaction_exp_nomenclature.py>`_ 


.. code-block:: python

   # create the model instance
   model = RSDs.RSD_sim() # default # of domains (5 domains)

   # specify species involved in the system
   model.molecular_species('I{u1}',DNA_con=25)
   model.molecular_species('G{u1,w2r}',DNA_con=25)
   model.molecular_species('R{w2}',ic=500)

   # simulating the model
   t_sim = np.linspace(0,6,1001)*3600 # seconds
   model.simulate(t_sim) # simulate the model

   # pull out the species from the model solution to plot
   S2 = model.output_concentration('S{w2}')

`Two Layer Simulation with Experimental Nomenclature Python Script can be found here <https://github.com/usnistgov/ctRSD-simulator/blob/main/ctRSD-simulator-2.0/Examples/Simple Examples/two_layer_simulation_exp_nomenclature.py>`_ 


.. code-block:: python

   # create the model instance
   model = RSDs.RSD_sim() # default # of domains (5 domains)

   model.global_rate_constants(ktxn=0.02) # changing the global transcription rate constant

   # specify species involved in the system
   model.molecular_species('I{u3}',DNA_con=25)
   model.molecular_species('G{u3,v1}',DNA_con=25)
   model.molecular_species('G{v1,u2r}',DNA_con=10)
   model.molecular_species('R{u2}',ic=500)

   # simulating the model
   t_sim = np.linspace(0,6,1001)*3600 # seconds
   model.simulate(t_sim) # simulate the model

   # pull out the species from the model solution to plot
   S2 = model.output_concentration('S{u2}')

