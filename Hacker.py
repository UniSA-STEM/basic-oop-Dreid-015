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
                          'Data Spike': 2,
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

    def __str__(self):
        name = str(self.__name)
        rig_name = str(self.__rig.get_name()) if self.__rig is not None else "No rig in use"
        trace = int(self.__trace_level)
        inventory = self.__inventory
        counter = 0
        output = f'NAME:{name}\nRIG NAME:{rig_name}\nTRACE:{trace}\nINVENTORY:\n'

        for item in inventory:

            if inventory[item] > 0:
                counter += 1
        if counter == 0:
            output += f'{name} has no assets.\n'
        for item in inventory:
            if inventory[item] > 0:
                output += f'{item}: {inventory[item]}\n'

        output += '*********************************'

        return output

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
        exposed = self.__exposed

        if rig_inventory['Data Spike'] > 0 and exposed == False:
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
        elif exposed == True:
            print("You're exposed, you cant do that right now.")

    def extract_assets(self, source, target):
        target_inv = target.get_inventory()
        target_item_count = sum(target_inv.values())
        source_avail_inv = source.get_capacity - sum(source.get_inventory().values())
        extractable_assets = {}
        self.set_trace_level(1)

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
        rig = self.get_rig()
        has_chip = rig.get_storage()['Hardware Patch'] > 0 or self.get_inventory()['Hardware Patch'] > 0

        if asset not in self.get_inventory() or asset not in rig.get_storage():
            print(f"There's no {asset} to encrypt.")

        elif has_chip == False:
            print('No Security Chip, no encrypt')

        elif asset in rig.get_storage() and has_chip == True:
                rig.set_storage('Hardware Patch', 1, 'spend')
                rig.__inventory[asset] -= 1
                rig.__encrypted_assets[asset] += 1

        elif asset in self.__inventory and has_chip == True:
            self.set_inventory('Hardware Patch', 1, 'spend')
            self.__inventory[asset] -= 1
            self.__encrypted_assets[asset] += 1

    def inv_scan(self, item):
        inventory = self.get_inventory()
        count = self.__inventory[item]

        if item in inventory:
            print(f"You have {count} {item}'s. They have been removed")
            self.set_inventory(item, count, 'spend')

    def store_retrieve(self, item, quantity, direction):

        rig = self.get_rig()

        # Check if hacker has a rig
        if rig is None:
            print("No rig available. Acquire a rig first.")
            return

        # Check if item exists in both inventories
        if item not in self.__inventory or item not in rig.get_storage():
            print(f"{item} not available")

        # Check if item is 'Rig' (can't store/retrieve the rig itself)
        if item == 'Rig':
            print("Cannot store or retrieve the Rig item.")

        if direction == 'store':
            # Moving from Hacker inventory to Rig storage

            # Check if hacker has enough of the item
            if self.__inventory[item] < quantity:
                print(f"Not enough {item} in inventory. Available: {self.__inventory[item]}")

            # Check if rig has enough capacity
            current_rig_items = sum(rig.get_storage().values())
            if current_rig_items + quantity > rig.get_capacity():
                print(f"Not enough capacity in rig. Available slots: {rig.get_capacity() - current_rig_items}")

            # Transfer the item
            self.set_inventory(item, quantity, 'spend')
            rig.set_storage(item, quantity, 'create')
            print(f"Stored {quantity} {item}(s) in {rig.get_name()}")

        elif direction == 'retrieve':
            # Moving from Rig storage to Hacker inventory

            # Check if rig has enough of the item
            if rig.get_storage()[item] < quantity:
                print(f"Not enough {item} in rig storage. Available: {rig.get_storage()[item]}")

            # Transfer the item
            rig.set_storage(item, quantity, 'spend')
            self.set_inventory(item, quantity, 'create')
            print(f"Retrieved {quantity} {item}(s) from {rig.get_name()}")

        else:
            print("Invalid direction. Use 'store' or 'retrieve'.")

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
