Documentation for ctRSD-simulator-2.0 can be found here:

https://ctrsd-simulator.readthedocs.io/en/latest/

ctRSD_simulator_v101 is similar to v.1.0.0 used in the 2022 Science Advances manuscript. But v101 corrects a few minor bugs, primarily with the comparator gate reactions.
This version is the most reliable for comparing to simulator v2.0 across all reaction types. Note the implementation of v1.0.1 does not correctly handle fan-in and fan-out circuits (documented in SI Section 5 of the 2022 Science Advance manuscript).
So the results of v2.0 and v1.0.1 will differ for those types of circuits. 
