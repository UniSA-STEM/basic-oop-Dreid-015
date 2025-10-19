"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Dyllan Reid
ID: reidy015@mymail.unisa.edu.au
Username: reidy015
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

import Rig
class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = {'CryptoToken': 1,
                          'Data Spike': 0,
                          'Removable Drive': 0,
                          'Security Chip': 0,
                          'Hardware Patch': 0,
                          'Rig': False}
        self.__encrypted_assets = {'CryptoToken': 0,
                                   'Data Spike': 0,
                                   'Removable Drive': 0,
                                   'Security Chip': 0,
                                   'Hardware Patch': 0}
        self.__trace_level = 0
        self.__exposed = False
        self.__rig = None

    #def __str__(self):
    #    name = str(self.__name)

    def acquire_rig(self, rig_name):
        inventory = self.get_inventory()
        rig_status = inventory['Rig']

        if rig_status == False and inventory['CryptoToken'] > 0:
            self.set_inventory('Rig', True, 'create')
            self.set_inventory('CryptoToken', 1, 'spend')
            created_rig = Rig.Rig(rig_name)
            print(f'{rig_name} ready to hack the planet.')
            self.__rig = created_rig

        elif rig_status == True:
            print("Hackers can only have 1 rig")
        elif inventory['CryptoToken'] == 0:
            print('No CryptoToken, No rig.')

    def data_spike(self, source, target):
        rig_inventory = source.get_storage()
        damage = source.get_upgrade_level() + 1
        result = []

        if 'Data Spike' in rig_inventory and rig_inventory['Data Spike'] > 0:
            source.set_storage('Data Spike', 1, 'spend')
            target.set_damage(damage)
            self.set_trace_level(1)

            result.append(f'Data Spike from {source.get_name()} has done {damage} to {target.get_name()}.\n')
            result.append(f'{target} has taken {target.get_damage} damage.\n')

            if target.get_is_broken() == True and rig_inventory['Removable Drive'] > 0:
                extract = input(f'Would you like to extract unencrypted assets from {source.get_name()}? (y/n)')

                if extract == 'y':
                    self.extract_assets(source, target)

        elif rig_inventory['Data Spike'] <= 0:
            result.append('No Data Spike available for attack.\n')

    def extract_assets(self, source, target):
        target_inv = target.get_inventory()
        target_item_count = sum(target_inv.values())
        source_avail_inv = source.get_capacity - sum(source.get_inventory().values())
        extractable_assets = {}

        ## Populating the items with a count to a temporary dictionary created for this method
        for item, quantity in target_inv.items():
            if quantity > 0:
                extractable_assets[item] = quantity

        if source_avail_inv < target_item_count:
            counter = 0
            print(f'There are {target_item_count} items, and you only have {source_avail_inv} slots available.\n')
            print(f'Asset extraction will be randomised\n')

            ## Experimenting with random.choice here to see how it works. Core logic should be easy otherwise
            while counter < target_item_count:
                selected_item = random.choice(list(extractable_assets.keys()))

                target.set_storage(selected_item, 1, 'spend')
                source.set_storage(selected_item, 1, 'create')
                extractable_assets[selected_item] -= 1

                if extractable_assets[selected_item] == 0:
                    del extractable_assets[selected_item]

                counter += 1

    def encrypt_assets(self, asset):
        quantity = 0

        if asset not in self.__inventory or asset not in self.__encrypted_assets:
            print(f"There's no {asset} to encrypt.")

        self.__inventory[asset] -= quantity
        self.__encrypted_assets[asset] += quantity

    # def inv_scan(self):

    def get_name(self):
        return self.__name
    def get_inventory(self):
        return self.__inventory
    def get_trace_level(self):
        return self.__trace_level
    def get_exposed(self):
        return self.__exposed
    def get_rig(self):
        return self.__rig

    def set_inventory(self, item, change, spend_or_create):
        if change == True or change == False:   # Done to manage the has_rig entry in the inventory dict
            self.__inventory[item] = change

        elif spend_or_create == 'spend':
            self.__inventory[item] -= change

        elif spend_or_create == 'create':
            self.__inventory[item] += change
    def set_trace_level(self, amount):
        self.__trace_level += amount
        if self.__trace_level >= 5:
            self.__exposed = True
