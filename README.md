# WOW-tool

## Introduction

This is an interface for connecting the OpenFAST, OpenMDAO, WAMIT, and Matlab. This tool allows an automatic loop between simulation and optimisation. The tool is contributed by Wind Over Wave society in the University of Edinburgh.

## Structure

![structure](https://cdn.ussjackdaw.com/image/interface.png)

## Environment

1. MATLAB Engine API for Python [(Install)](https://uk.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
2. MATLAB R2022b
3. WAMIT
4. OpenFAST
5. OpenMDAO
6. Python 3.9

## Commands

To run this tool, you need to run the below command in terminal:

    # python run.py [command]

Command list:

1. run - run the simulation-optimization loop
2. openfast - run the openFAST simulation
3. matlab - run the matlab for generate the .gdf file
4. wamit - run WAMIT for calculating the hydrostatic data
5. openmdao - run openMDAO for optimization
6. help - for help

## Acknowledgement

The University of Edinburgh, Engineering for Change Association;

**Supervisor:**

[Prof. Alasdair McDonald](https://www.eng.ed.ac.uk/about/people/prof-alasdair-mcdonald)

**Software License:**

The University of Edinburgh

**Sponsor:** 

[offshorewind4kids](https://www.offshorewind4kids.com/)

## About us

We are a team made up of students, who aim to build up a floating structure to support a small wind turbine to operate over the water, and bring it to competition in the Netherlands in May. For more details of the competition please visit the official website:

[Floating Wind Challenge](https://www.offshorewind4kids.com/floating-wind-challenge)

Our website:

[Wind Over Wave](http://woc.uss1.cn)

If you have any question, please contact us through:

engineering4change.ed@gmail.com