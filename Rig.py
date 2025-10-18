"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Dyllan Reid
ID: reidy015@mymail.unisa.edu.au
Username: reidy015
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
class Rig:
    def __init__(self, name, owner):
        self.__name = name
        self.__damage = 0
        self.__is_broken = False
        self.__storage = {'CryptoToken': 0,
                          'Data Spike': 2,
                          'Removable Drive': 1,
                          'Security Chip': 0,
                          'Hardware Patch': 0}
        self.__upgrade_level = 0
        self.__owner = owner

    def __str__(self):
        counter = 0
        condition = condition()
        output = f'Rig: {self.__name}\n'
        output += f'Condition: {condition}\n'
        output += f'Upgrade Level: {self.__upgrade_level}\n'

        for item in self.__storage:

            if self.__storage[item] > 0:
                counter += 1

        if counter > 0:
            output += f'Stored Assets:\n'

        elif counter == 0:
            output += f'Nothing is stored in this rig'

        for item in self.__storage:

            if self.__storage[item] > 0:
                output += f'{item}: {self.__storage[item]}\n'

        return output

    def condition(self):
        output = ''
        max_hp = (self.get_upgrade_level() * 2) + 2
        level = self.get_upgrade_level()

        if self.get_damage() == 0:
            output += f'Pristine'

        elif self.get_damage() > 0 and self.get_damage() < max_hp:
            output += f'Damaged'

        else:
            output += f'Broken'

        output += f'( {level})'

    def repair(self):
        token_in_storage = self.get_storage()
        token_in_inv = self.__owner.get_inventory()

        if 'CryptoToken' in token_in_storage and token_in_storage['CryptoToken'] > 0:
            token_in_storage['CryptoToken'] -= 1
            self.set_damage('repair')

        elif 'CryptoToken' in token_in_inv and token_in_inv['CryptoToken'] > 0:
            token_in_inv['CryptoToken'] -= 1
            self.set_damage('repair')

    def upgrade(self):
        # This and the repair function use different methodology to update the hacker inventories.
        # Need to confirm which method works, and if both do which I prefer
        patch_in_storage = self.get_storage()
        patch_in_inv = self.__owner.get_inventory()

        if 'Hardware Patch' in patch_in_storage and patch_in_storage['Hardware Patch'] > 0:
            self.set_storage('Hardware Patch', 1, 'spend')
            self.set_upgrade_level(1)

        elif 'Hardware Patch' in patch_in_inv and patch_in_inv['Hardware Patch'] > 0:
            self.__owner.set_storage('Hardware Patch', 1, 'spend')
            self.set_upgrade_level(1)

    def generate_asset(self):

    #def current_condition(self):

    #def get_name(self):
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

        elif change == 'repair' and self.__damage == 0:
            return 'No repair is needed'

        elif change == 'repair':
            self.__damage = 0
            self.__is_broken = False

    def set_upgrade_level(self, change):
        self.__upgrade_level += change
    def set_storage(self, item, change, spend_or_create):
        if spend_or_create == 'spend':
            self.__storage[item] -= change

        elif spend_or_create == 'create':
            self.__storage[item] += change