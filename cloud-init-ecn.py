#!/usr/bin/python

import os
import sys
import yaml
import argparse

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--cloud-config', '-f',
            default='/var/lib/cloud/instance/cloud-config.txt')
    p.add_argument('hostname', nargs='?')
    return p.parse_args()

def main():
    opts = parse_args()
    cfg = yaml.load(open(opts.cloud_config))

    if 'puppet_ecn' in cfg:
        print yaml.dump(cfg['puppet_ecn'],
                default_flow_style=False)

if __name__ == '__main__':
    main()


