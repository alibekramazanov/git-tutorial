# json_operations.py - Exercise 1

import json

print("=" * 80)
print("EXERCISE 1: Parse JSON and display interface status")
print("=" * 80 + "\n")

# Read JSON file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Print header
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print(f"{'-'*50} {'-'*20} {'-'*8} {'-'*6}")

# Parse and display data
# Assuming the JSON structure has an 'imdata' key with interface information
if 'imdata' in data:
    for item in data['imdata']:
        # Extract interface data (structure depends on actual JSON)
        if 'l1PhysIf' in item:
            interface = item['l1PhysIf']['attributes']
            
            dn = interface.get('dn', '')
            description = interface.get('descr', '')
            speed = interface.get('speed', 'inherit')
            mtu = interface.get('mtu', '9150')
            
            print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")

print("\n" + "=" * 80 + "\n")