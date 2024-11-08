RSD_simulator.py was the simulator used in this manuscript (https://www.science.org/doi/full/10.1126/sciadv.abl4354)

The README_SA.pdf file contains details about this simulator version.

All the simulations from this paper have been reimplemented with ctRSD-simulator-2.0. The scripts for this can be found as Examples in the ctRSD-simulator-2.0 folder.

A slightly updated version RSD_simulator (ctRSD_simulator_v101) is available in the ctRSD-simulator-2.0 folder. v101 corrects a few minor bugs, primarily with the comparator gate reactions. This version is the most reliable for comparing to simulator v2.0 across all reaction types. Note the implementation of v1.0.1 does not correctly handle fan-in and fan-out circuits (documented in SI Section 5 of the 2022 Science Advance manuscript). So the results of v2.0 and v1.0.1 will differ for those types of circuits.