"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Dyllan Reid
ID: reidy015@mymail.unisa.edu.au
Username: reidy015
This is my own work as defined by the University's Academic Misconduct Policy.
"""
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
        self.__trace_level = 0
        self.__exposed = False

    def acquire_rig(self, rig_name):
        inventory = self.get_inventory()
        rig_status = inventory['Rig']

        if rig_status == False and inventory['CryptoToken'] > 0:
            self.set_inventory('Rig', True, 'create')
            self.set_inventory('CryptoToken', 1, 'spend')
            created_rig = Rig.Rig(rig_name)
            print(f'{rig_name} ready to hack the planet.')
            return created_rig

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
                    self.extract_assets(target)

        elif rig_inventory['Data Spike'] <= 0:
            result.append('No Data Spike available for attack.\n')

    def extract_assets(self, target):
        target_inv = target.get_inventory()

        for item in target_inv:
            item_count = target_inv[item]
            # HAndle encryption with a second dictionary to count it all
            if item.endswith('_enc'):
            self.set_inventory(item, item_count, 'create')


    # def encrypt_assets(self):
    # Ensure to add any encrypted items to the Rig.assets list with the _encrypted suffix

    # def upgrade_rig(self):

    # def inv_scan(self):

    def get_name(self):
        return self.__name
    def get_inventory(self):
        return self.__inventory
    def get_trace_level(self):
        return self.__trace_level
    def get_exposed(self):
        return self

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
