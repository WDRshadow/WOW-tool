import os
import sys

# Check if all the folders exist.
folder_list = ["temp", "logs"]
for i in folder_list:
    folder = os.path.exists(i)
    if not folder:
        os.makedirs(i)

from module import logger


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
    from module import mainLoop

    mainLoop.Main().run()
elif str(sys.argv[1]) == "openfast":
    from module import fastAPI

    fastAPI.FAST().run()
elif str(sys.argv[1]) == "matlab":
    from module import matlabAPI

    matlabAPI.MATLAB().run()
elif str(sys.argv[1]) == "wamit":
    from module import wamitAPI

    wamitAPI.WAMIT().run()
elif str(sys.argv[1]) == "openmdao":
    from module import mdaoInterface

    mdaoInterface.MDAO().run()
else:
    error()
