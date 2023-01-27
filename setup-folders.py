# Import required libraries
from pathlib import Path
import os, sys

# If the first folder (Les 01) exists, there is probably no need to execute the rest of the script.
if Path(Path.cwd() / Path("Les 01")).exists():
    print("It seems this script has already been executed. Stopping further actions... Done.")
    sys.exit()

for i in range(1, 6):
    # Step 1: Construct the to-be-created name of the folder
    folderName = "Les 0%d" % i

    # Step 2: Construct the complete path of the folder
    folderPath = Path(Path.cwd() / Path(folderName))
    # (if you want to see what the path is going to be, do:)
    # print(folderPath)

    # Step 3: Make the new folder (directory)
    folderPath.mkdir()
    if folderPath.exists():
        print("%s has been created!" % folderName)