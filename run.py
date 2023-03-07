import sys
from module import matlabAPI, wamitAPI, fastAPI, mdaoInterface, fileAPI, mainLoop, logger

# Check if all the folders exist.
fileAPI.init_check()


# error message for wrong commands
def error():
    logger.logger.info("\nCommand list:\n"
                       "1. run - run the simulation-optimization loop\n"
                       "2. openfast - run the openFAST simulation\n"
                       "3. matlab - run the matlab for generate the .gdf file\n"
                       "4. wamit - run WAMIT for calculating the hydrostatic data\n"
                       "5. openmdao - run openMDAO for optimization\n"
                       "6. help - for help")


if len(sys.argv) != 2:
    error()
    exit()

# command filter
if str(sys.argv[1]) == "run":
    mainLoop.Main().run()
elif str(sys.argv[1]) == "openfast":
    fastAPI.FAST().run()
elif str(sys.argv[1]) == "matlab":
    matlabAPI.MATLAB().run()
elif str(sys.argv[1]) == "wamit":
    wamitAPI.WAMIT().run()
elif str(sys.argv[1]) == "openmdao":
    mdaoInterface.MDAO().run()
else:
    error()
