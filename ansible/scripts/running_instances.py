#!/usr/bin/env python
import sys
import json

data = json.load(sys.stdin)

out = []
for res in data['Reservations']:
    for ins in res['Instances']:
        if ins['State']['Name'] == "running":
            out.append(ins['InstanceId'])

print json.dumps(out)
sys.exit(0)
