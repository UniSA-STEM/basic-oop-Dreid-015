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
            print('Rig acquired.')

        elif rig_status == True:
            print("Hackers can only have 1 rig")

        elif inventory['CryptoToken'] > 0:
            print('No CryptoToken, No rig.')

        return created_rig

    # def data_spike(self, target):
    #     rig_inventory =
    #
    #     if self.__

    # def extract_assets(self):

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
