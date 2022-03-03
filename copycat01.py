#!/usr/bin/env python3
""" TPatrick | Alta3 Research
    Doing stuff in class and things - But also backing up files"""

# importing additional code because I can't be bothered
import shutil
import os

# def main because I'm told this is best practice
def main():

    """ code to move files around """
    # move into the working directory
    os.chdir("/home/student/slop/")
    # copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    
    #copy the entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main ()
