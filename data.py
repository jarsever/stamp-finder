'''
This file is to be called as an object and then passed around.

I didn't want to use global variables so I designed this class
to store all the data needed.

If you want to send data to other functions then you either pull
it out of the instance or send the whole "data" object.
'''

import os
from images import Image


class Data:

    def __init__(self):
        self.orig_path = os.getcwd()
        self.path = os.getcwd()
        self.set_file_list()


#-----------------------------------------------------------#
# Below are all the functions to "GET" data from the object #
#-----------------------------------------------------------#

    def get_file_list(self):
        return self.file_list

    def get_image_list(self):
        return self.image_list

    def get_path(self):
        return self.path


#---------------------------------------------------------#
# Below are all the functions to "SET" data to the object #
#---------------------------------------------------------#

    def set_file_list(self):
        os.chdir(self.path)
        self.file_list =  [f for f in os.listdir(self.path) if os.path.isfile(f)]


    # This function should not need to be called manually
    def set_image_list(self):
        self.image_list = []
        for f in self.file_list:
            x = Image(f)
            self.image_list.append(x)

    def set_path(self, path):
        self.path = path
        self.set_file_list()

    def go_home(self):
        self.set_path(self.orig_path)

