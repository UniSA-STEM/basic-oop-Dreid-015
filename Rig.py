"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Dyllan Reid
ID: reidy015@mymail.unisa.edu.au
Username: reidy015
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
import random

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__is_broken = False
        self.__storage = {'CryptoToken': 1,
                          'Data Spike': 2,
                          'Removable Drive': 1,
                          'Security Chip': 0,
                          'Hardware Patch': 0}
        self.__upgrade_level = 0
        self.__max_hp = (self.get_upgrade_level() * 2) + 2

    def __str__(self):
        counter = 0
        condition = self.condition()

        output = f'Rig: {self.__name}\n'
        output += f'Condition: {condition}\n'
        output += f'Upgrade Level: {self.__upgrade_level}\n'

        for item in self.__storage:

            if self.__storage[item] > 0:
                counter += 1

        if counter > 0:
            output += '\n'
            output += f'Stored Assets:\n'

        elif counter == 0:
            output += f'Nothing is stored in this rig'

        for item in self.__storage:

            if self.__storage[item] > 0:
                output += f'{item}: {self.__storage[item]}\n'

        output += '*********************************'

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

        output += f' (Level {level})'
        return output

    def repair(self, hacker):
        token_in_storage = self.get_storage()
        token_in_inv = hacker.get_inventory(hacker)

        if self.get_damage() == 0:
            print('No repair required')

        elif 'CryptoToken' in token_in_storage and token_in_storage['CryptoToken'] > 0:
            token_in_storage['CryptoToken'] -= 1
            self.__damage = 0

        elif 'CryptoToken' in token_in_inv and token_in_inv['CryptoToken'] > 0:
             token_in_inv['CryptoToken'] -= 1
             self.__damage = 0

    def upgrade(self, hacker):
        patch_in_storage = self.get_storage()
        patch_in_inv = hacker.get_inventory(hacker)

        if 'Hardware Patch' in patch_in_storage and patch_in_storage['Hardware Patch'] > 0:
            self.set_storage('Hardware Patch', 1, 'spend')
            self.set_upgrade_level(1)

        elif 'Hardware Patch' in patch_in_inv and patch_in_inv['Hardware Patch'] > 0:
            hacker.set_inventory('Hardware Patch', 1, 'spend')
            self.set_upgrade_level(1)

    def generate_asset(self):
        asset_nums = ['CryptoToken', 'Data Spike', 'Removable Drive', 'Security Chip', 'Hardware Patch']
        random_num = random.randint(1, 4)
        random_asset = asset_nums[random_num]

        self.__storage[random_asset] += 1

        print(f'{random_asset}has been generated and stored in this rig')

    def get_name(self):
        return self.__name
    def get_damage(self):
        return self.__damage
    def get_is_broken(self):
        return self.__is_broken
    def get_storage(self):
        return self.__storage
    def get_upgrade_level(self):
        return int(self.__upgrade_level)
    def get_max_hp(self):
        return self.__max_hp

    def set_damage(self, amount):
            self.__damage += amount

            if self.__damage > self.get_max_hp():
                self.__is_broken = True
    def set_upgrade_level(self, change):
        self.__upgrade_level += change
    def set_storage(self, item, change, spend_or_create):
        if spend_or_create == 'spend':
            self.__storage[item] -= change

        elif spend_or_create == 'create':
            self.__storage[item] += change