"""
File: main.py
Description: This contains all of the created test modules
Author: Dyllan Reid
ID: reidy015@mymail.unisa.edu.au
Username: reidy015
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import Hacker
## Handled rig creation via the Hacker class so only need to import Hacker for the test methods
## Honestly was kind of lost as to what to do with Asset as I could handle it all in the other classes
## Certainly could do things cleaner and nicer by using it, but was too deep for restructuring by that point
## NOTE: the term inventory is used to denote items on the hacker. Storage for the rig

def hacker():
    hacker_1 = Hacker.Hacker('Neo')
    print(hacker_1)
    print(f'Trace Level: {hacker_1.get_trace_level()}')
    print(f'Exposed: {hacker_1.get_exposed()}')
    print()

def multiple_hackers():
    hacker_1 = Hacker.Hacker('Trinity')
    hacker_2 = Hacker.Hacker('Morpheus')
    print(hacker_1)
    print(hacker_2)
    print()

def acquire_rig_success():
    hacker_1 = Hacker.Hacker('Neo')
    hacker_1.acquire_rig('Nebuchadnezzar')
    print(hacker_1)
    print(f'Has Rig: {hacker_1.get_inventory()['Rig']}')
    print()

def acquire_rig_no_token():
    hacker_1 = Hacker.Hacker('Cypher')
    hacker_1.set_inventory('CryptoToken', 1, 'spend')
    hacker_1.acquire_rig('BetrayalRig')
    print(hacker_1)
    print()

def acquire_multiple_rigs():
    hacker_1 = Hacker.Hacker('Agent Smith')
    hacker_1.acquire_rig('FirstRig')
    hacker_1.set_inventory('CryptoToken', 1, 'create')
    hacker_1.acquire_rig('SecondRig')
    print(hacker_1)
    print()

def rig_condition():
    hacker_1 = Hacker.Hacker('Neo')
    hacker_1.acquire_rig('TestRig')
    rig = hacker_1.get_rig()
    print(rig)
    print()

def rig_damage():
    hacker_1 = Hacker.Hacker('Trinity')
    hacker_1.acquire_rig('CombatRig')
    rig = hacker_1.get_rig()
    print("Before damage:")
    print(rig)
    rig.set_damage(1)
    print("After 1 damage:")
    print(rig)
    print(f"Damage: {rig.get_damage()}")
    print()

def rig_broken():
    hacker_1 = Hacker.Hacker('Morpheus')
    hacker_1.acquire_rig('FragileRig')
    rig = hacker_1.get_rig()
    rig.set_damage(10)
    print(rig)
    print(f"Is Broken: {rig.get_is_broken()}")
    print()

def set_inventory_spend():
    hacker_1 = Hacker.Hacker('Neo')
    print("Before spending:")
    print(hacker_1)
    hacker_1.set_inventory('Data Spike', 1, 'spend')
    print("After spending 1 Data Spike:")
    print(hacker_1)
    print()

def set_inventory_create():
    hacker_1 = Hacker.Hacker('Trinity')
    print("Before creation:")
    print(hacker_1)
    hacker_1.set_inventory('Security Chip', 3, 'create')
    print("After creating 3 Security Chips:")
    print(hacker_1)
    print()

def inv_scan():
    hacker_1 = Hacker.Hacker('Cypher')
    print("Before scan:")
    print(hacker_1)
    hacker_1.inv_scan('Data Spike')
    print("After scanning Data Spike:")
    print(hacker_1)
    print()

def store_item():
    hacker_1 = Hacker.Hacker('Neo')
    hacker_1.acquire_rig('StorageRig')
    print("Before storing:")
    print(hacker_1)
    print(hacker_1.get_rig())
    hacker_1.store_retrieve('Data Spike', 1, 'store')
    print("After storing 1 Data Spike:")
    print(hacker_1)
    print(hacker_1.get_rig())
    print()

def retrieve_item():
    hacker_1 = Hacker.Hacker('Trinity')
    hacker_1.acquire_rig('RetrievalRig')
    print("Before retrieving:")
    print(hacker_1)
    print(hacker_1.get_rig())
    hacker_1.store_retrieve('Data Spike', 1, 'retrieve')
    print("After retrieving 1 Data Spike:")
    print(hacker_1)
    print(hacker_1.get_rig())
    print()

def store_no_rig():
    hacker_1 = Hacker.Hacker('Newbie')
    hacker_1.store_retrieve('Data Spike', 1, 'store')
    print()

def store_insufficient_quantity():
    hacker_1 = Hacker.Hacker('Poor')
    hacker_1.acquire_rig('EmptyRig')
    hacker_1.store_retrieve('Removable Drive', 5, 'store')
    print()

def encrypt():
    hacker_1 = Hacker.Hacker('Mario')
    hacker_1.acquire_rig('Peach')
    hacker_1.encrypt_assets('fake_item')
    print(hacker_1)
    print()

def encrypt_no_chip():
    hacker_1 = Hacker.Hacker('Neo')
    hacker_1.acquire_rig('SecureRig')
    hacker_1.encrypt_assets('Data Spike')
    print()

def encrypt_with_chip():
    hacker_1 = Hacker.Hacker('Trinity')
    hacker_1.acquire_rig('EncryptRig')
    hacker_1.set_inventory('Hardware Patch', 1, 'create')
    print("Before encryption:")
    print(hacker_1)
    hacker_1.encrypt_assets('Data Spike')
    print("After encryption:")
    print(hacker_1)
    print()

def trace_level_increment():
    hacker_1 = Hacker.Hacker('Sneaky')
    print(f"Initial Trace: {hacker_1.get_trace_level()}")
    hacker_1.set_trace_level(1)
    print(f"After +1: {hacker_1.get_trace_level()}")
    hacker_1.set_trace_level(2)
    print(f"After +2: {hacker_1.get_trace_level()}")
    print(f"Exposed: {hacker_1.get_exposed()}")
    print()

def trace_level_exposed():
    hacker_1 = Hacker.Hacker('Careless')
    print(f"Initial - Trace: {hacker_1.get_trace_level()}, Exposed: {hacker_1.get_exposed()}")
    hacker_1.set_trace_level(5)
    print(f"After +5 - Trace: {hacker_1.get_trace_level()}, Exposed: {hacker_1.get_exposed()}")
    print()

def rig_upgrade():
    hacker_1 = Hacker.Hacker('Upgrader')
    hacker_1.acquire_rig('BasicRig')
    rig = hacker_1.get_rig()
    print("Before upgrade:")
    print(rig)
    print(f"Max HP: {rig.get_max_hp()}, Capacity: {rig.get_capacity()}")
    hacker_1.set_inventory('Hardware Patch', 1, 'create')
    rig.upgrade(hacker_1)
    print("After upgrade:")
    print(rig)
    print(f"Max HP: {rig.get_max_hp()}, Capacity: {rig.get_capacity()}")
    print()

def rig_upgrade_no_patch():
    hacker_1 = Hacker.Hacker('Broke')
    hacker_1.acquire_rig('PoorRig')
    rig = hacker_1.get_rig()
    print("Before upgrade attempt")
    print(rig)
    rig.upgrade(hacker_1)
    print("After upgrade attempt")
    print(rig)
    print()

def rig_repair():
    hacker_1 = Hacker.Hacker('Kaylee')
    hacker_1.acquire_rig('Serenity')
    rig = hacker_1.get_rig()
    rig.set_damage(1)
    print("Damaged rig:")
    print(rig)
    hacker_1.set_inventory('CryptoToken', 1, 'create')
    rig.repair(hacker_1)
    print("After repair:")
    print(rig)
    print()

def rig_repair_no_damage():
    hacker_1 = Hacker.Hacker('Xerxes')
    hacker_1.acquire_rig('Untouchable')
    rig = hacker_1.get_rig()
    rig.repair(hacker_1)
    print()

def rig_generate_asset():
    hacker_1 = Hacker.Hacker('Big dog')
    hacker_1.acquire_rig('Kennel')
    rig = hacker_1.get_rig()
    print("Initial inventory:")
    print(rig)
    rig.generate_asset()
    print("Computer has decided your fate:")
    print(rig)
    print()

def rig_generate_multiple_assets():
    hacker_1 = Hacker.Hacker('Ol Macdonald')
    hacker_1.acquire_rig('FarmRig')
    rig = hacker_1.get_rig()
    print("Initial inventory:")
    print(rig)
    for iteration in range(3):
        rig.generate_asset()
    print("Computer has decided your fate:")
    print(rig)
    print()

def data_spike():
    hacker_1 = Hacker.Hacker('Attacker')
    hacker_2 = Hacker.Hacker('Target')
    hacker_1.acquire_rig('AttackRig')
    hacker_2.acquire_rig('TargetRig')

    target_rig = hacker_2.get_rig()
    print("Before attack")
    print(f"Attacker: {hacker_1.get_name()}, Trace: {hacker_1.get_trace_level()}")
    print(target_rig)

    hacker_1.data_spike(target_rig)

    print("After attack")
    print(f"Attacker: {hacker_1.get_name()}, Trace: {hacker_1.get_trace_level()}")
    print(target_rig)
    print()

def data_spike_no_spike():
    hacker_1 = Hacker.Hacker('Completely Unarmed')
    hacker_2 = Hacker.Hacker('Naive')
    hacker_1.acquire_rig('Ner gun')
    hacker_2.acquire_rig('Shield wall')

    attacker_rig = hacker_1.get_rig()
    attacker_rig.set_storage('Data Spike', 2, 'spend')

    hacker_1.data_spike(hacker_2.get_rig())
    print()

def data_spike_exposed():
    hacker_1 = Hacker.Hacker('Exposed')
    hacker_2 = Hacker.Hacker('Target')
    hacker_1.acquire_rig('AttackRig')
    hacker_2.acquire_rig('DefenseRig')

    hacker_1.set_trace_level(5)
    hacker_1.data_spike(hacker_2.get_rig())
    print()

def full():
    hacker_1 = Hacker.Hacker('Master')

    print("1. Acquiring rig")
    hacker_1.acquire_rig('EliteRig')

    print("2. Generating assets")
    rig = hacker_1.get_rig()
    rig.generate_asset()

    print("3. Storing items")
    hacker_1.store_retrieve('Data Spike', 1, 'store')

    print("4. Attempting upgrade")
    hacker_1.set_inventory('Hardware Patch', 1, 'create')
    rig.upgrade(hacker_1)

    print("5. Final state:")
    print(hacker_1)
    print(rig)
    print()

def hacker_vs_hacker():
    attacker = Hacker.Hacker('Sonic')
    defender = Hacker.Hacker('Eggman')
    
    attacker.acquire_rig('Tails')
    defender.acquire_rig('Metal Sonic')
    
    print("The tale of the tape:")
    print(attacker)
    print(defender)
    
    print("\nLets get ready to rumble:")
    attacker.data_spike(defender.get_rig())
    attacker.data_spike(defender.get_rig())
    
    print("\nAnd the winner is...")
    print(attacker)
    print(defender)
    print(defender.get_rig())
    print()

def run_all_tests():
    hacker()
    multiple_hackers()
    
    acquire_rig_success()
    acquire_rig_no_token()
    acquire_multiple_rigs()
    
    rig_condition()
    rig_damage()
    rig_broken()
    
    set_inventory_spend()
    set_inventory_create()
    inv_scan()
    
    store_item()
    retrieve_item()
    store_no_rig()
    store_insufficient_quantity()
    
    encrypt()
    encrypt_no_chip()
    encrypt_with_chip()
    
    trace_level_increment()
    trace_level_exposed()
    
    rig_upgrade()
    rig_upgrade_no_patch()
    
    rig_repair()
    rig_repair_no_damage()
    
    rig_generate_asset()
    rig_generate_multiple_assets()
    
    data_spike()
    data_spike_no_spike()
    data_spike_exposed()
    
    full()
    hacker_vs_hacker()

run_all_tests()