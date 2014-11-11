#!/usr/bin/env python
example = """{
    "KeyPairs": [
        {
            "KeyName": "imageprocessor1",
            "KeyFingerprint": "85:73:9f:9d:09:88:f0:8a:54:cf:94:ce:62:30:93:9d:3c:8d:d8:78"
        },
        {
            "KeyName": "imageprocessor1-batchprocessing",
            "KeyFingerprint": "ce:82:7b:63:cb:cc:bd:7a:c2:16:38:bd:45:6e:0c:91:5f:ba:79:cb"
        },
        {
            "KeyName": "Key Pair 1",
            "KeyFingerprint": "c4:73:16:13:aa:d3:87:02:fe:17:65:25:11:a8:2a:2a:df:c1:4c:b8"
        }
    ]
}"""

import sys
import json

data = json.load(sys.stdin)

if 'KeyPairs' not in data:
    print "false"
    sys.exit(0)

for k in data['KeyPairs']:
    if k['KeyName'] == sys.argv[1]:
        print "true"
        sys.exit(0)

print "false"
sys.exit(0)

