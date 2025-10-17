"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Dyllan Reid
ID: reidy015@mymail.unisa.edu.au
Username: reidy015
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self, name, damage, is_broken, storage, upgrade_level):
        self.__name = name
        self.__damage = damage
        self.__is_broken = False
        self.__storage = ['Data Spike', 'Data Spike', 'Removable Drive']
        self.__upgrade_level = 0

    def repair(self):

    def upgrade(self):

    def take_damage(self, damage):

    def generate_asset(self):

    def current_condition(self):



    def get_name(self):
        return self.__name
    def get_damage(self):
        return self.__damage
    def get_is_broken(self):
        return self.__is_broken
    def get_storage(self):
        return self.__storage
    def get_upgrade_level(self):
        return self.__upgrade_level
