"""
File: Asset.py
Description: This module handles all of the Rig class code. This has not been implemented
Author: Dyllan Reid
ID: reidy015@mymail.unisa.edu.au
Username: reidy015
This is my own work as defined by the University's Academic Misconduct Policy.
"""
## There's not alot here as I managed most of the work in Hacker and Rig. The Asset class definitely has a place
## for deeper usage, but the current implementation I was able to achieve without using this class.
class Asset:
    def __init__(self, name, description, is_encrypted, container):
        self.__name = name
        self.__description = description
        self.__is_encrypted = False
        self.__container = container

    def __str__(self):
        name = str(self.__name)
        description = str(self.__description)
        output = ''

        if self.__is_encrypted:
            output = f'{name}: {description} (encrypted)'

        else:
            output = f'{name}: {description}'

        print(output)

    def get_name(self):
        return self.__name
    def get_description(self):
        return self.__description
    def get_is_encrypted(self):
        return self.__is_encrypted

