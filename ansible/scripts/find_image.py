#!/usr/bin/env python
example = """
"master_instance.instances": [
        {
            "ami_launch_index": "0",
            "architecture": "x86_64",
            "dns_name": "ec2-54-65-72-82.ap-northeast-1.compute.amazonaws.com",
            "ebs_optimized": false,
            "hypervisor": "xen",
            "id": "i-bd69274f",
            "image_id": "ami-4985b048",
            "instance_type": "t2.micro",
            "kernel": null,
            "key_name": "imageprocessor1-batchprocessing",
            "launch_time": "2014-11-11T22:10:34.000Z",
            "placement": "ap-northeast-1c",
            "private_dns_name": "ip-172-31-26-227.ap-northeast-1.compute.internal",
            "private_ip": "172.31.26.227",
            "public_dns_name": "ec2-54-65-72-82.ap-northeast-1.compute.amazonaws.com",
            "public_ip": "54.65.72.82",
            "ramdisk": null,
            "region": "ap-northeast-1",
            "root_device_name": "/dev/xvda",
            "root_device_type": "ebs",
            "state": "running",
            "state_code": 16,
            "virtualization_type": "hvm"
        }
    ]
"""

import sys
import json

data = json.load(sys.stdin)

for k in data['Images']:
    if k['Name'] == sys.argv[1]:
        print k['ImageId']
        sys.exit(0)

sys.exit(0)

