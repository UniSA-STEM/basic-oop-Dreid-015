"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Dyllan Reid
ID: reidy015@mymail.unisa.edu.au
Username: reidy015
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import Hacker
class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__is_broken = False
        self.__storage = {'CryptoToken': 0,
                          'Data Spike': 2,
                          'Removable Drive': 1,
                          'Security Chip': 0,
                          'Hardware Patch': 0}
        self.__upgrade_level = 0

    def repair(self):
        token_in_storage = self.get_storage()
        token_in_inv = Hacker.get_inventory()

        if 'CryptoToken' in token_in_storage and token_in_storage['CryptoToken'] > 0:
            token_in_storage['CryptoToken'] -= 1
            self.set_damage('repair')

        elif 'CryptoToken' in token_in_inv and token_in_inv['CryptoToken'] > 0:
            token_in_inv['CryptoToken'] -= 1
            self.set_damage('repair')

    def upgrade(self):
        ## Hackers can upgrade their rig using a Hardware Patch. This increases the rig’s upgrade level,
        ## which improves storage size and reduces damage taken in batles. Upgrades require a rig and
        ## a Hardware Patch in inventory.

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

    def set_damage(self, change, amount):
        ## Big note here is that this function is designed to handle both damaging and repairing a rig
        ## change should only ever be set as 'damage', or 'repair'. This is used in comparisons to determine functionality

        if change == 'damage':
            self.__damage += amount

            if self.__damage > self.__upgrade_level + 2:
                self.__is_broken = True

        elif change == 'repair':
            self.__damage = 0
            self.__is_broken = False

    def set_is_broken(self, is_broken):
