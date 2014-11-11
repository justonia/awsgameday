#!/usr/bin/env python
example = """{
        "changed": true,
        "instance_ids": [
            "i-ca511f38"
        ],
        "instances": [
            {
                "ami_launch_index": "0",
                "architecture": "x86_64",
            }
         ]
}"""

import sys
import json

data = json.load(sys.stdin)

print data['instance_ids'][0]
