#!/usr/bin/env python3

"""Tpatrick | Alta3 Research
   A simple script to move a file for me, and rename another."""

# standard library imports   
import shutil
import os


def main():
    # setting the starting point for our program
    os.chdir('/home/student/slop/')
    # moving the raynor.obj to its proper place
    shutil.move('raynor.obj', 'ceph_storage/')

    # renaming a file - calling for input from user
    xname = input('What is the new name for kerrigan.obj? ')
    # performing the move which will simply replace/rename the obj.
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
