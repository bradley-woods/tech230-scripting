# YAML --> JSON

import json
import os
import sys
import yaml

# initialise source_content variable
source_content = ""

# checking there is a file name passed
if len(sys.argv) > 1:
    # opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
    # failing if no file found
    else:
        print("Error: " + sys.argv[1] + " not found")
        exit(1)
# no file usage
else:
    print("Usage: python yaml_to_json.py <source_file.yaml> <target_json_file.json>")

# processing the conversion
output = json.dumps(source_content)

# if there's no target file
if len(sys.argv) < 3:
    print(output)

elif os.path.exists(sys.argv[2]):
    print("Error: " + sys.argv[2] + " already exists")
    exit(1)

# write to the new yaml file
else:
    target_file = open(sys.argv[2], "w")
    target_file.write(output)
    target_file.close()
