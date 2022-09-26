Overview
===============================================
Welcome to the documentation for ctRSD-simulator-2.0! 

ctRSD-simulator-2.0 was designed to be a comprehensive, scalable, and user-friendly model for simulating the kinetics of contranscriptionally encoded RNA strand displacement (ctRSD) circuits. 

ctRSD circuits are an emerging technology for programmabale and scalable molecular computations. ctRSD circuits can execute multilayer cascades, logic, and signal amplification, and these elementary functions can be integrated to orchestrate sophisticated information processing tasks like digital calculations and pattern recognition. 

The goal of the simulator is to aid the user to design, predict, and understand the behavior of ctRSD circuits. Also, providing experimentalists with a functional model allowing for the efficient *in silico* prototyping of ctRSD systems.

In addition to the kinetic simulations, the simulator package also has a :ref:`sequence compiler function <seq_compile>` that can be used to assemble the DNA sequences necessary to test a specific component / design in experiments.

**The simulator requires the following Python packages for full capabilities:** *numpy*, *scipy*, *matplotlib*, *re*, *math*, *xlrd*