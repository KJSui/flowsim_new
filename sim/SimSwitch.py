#!/usr/bin/python
# -*- coding: utf-8 -*-

"""sim/SimSwitch.py: Class of switch profile the forwarding table, and other parameters, of a switch.
"""
__author__      = 'Kuan-yin Chen'
__copyright__   = 'Copyright 2014, NYU-Poly'

# Built-in modules
# Third-party modules
import netaddr as na
# User-defined modules
import SimConfig as cfg


class SimSwitch:
    """Class of a switching node in the network.

    Attributes:
        table (dict: 2-tuple netaddr.IpAddress -> float64):
            Forwarding table, key is 2-tuple (src_ip, dst_ip) and value is byte counter.
        tablesize (int): Maximum number of flow entries allowed in table
        n_hosts (int): Number of hosts connected with this edge switch.
        base_ip
        end_ip

    """

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'noname')
        self.table = {}     # key is 2-tuple (src_ip, dst_ip), value is byte counter
        self.table_size = kwargs.get('table_size', 1000) if (not cfg.OVERRIDE_TABLESIZE)    \
                          else cfg.TABLESIZE_PER_SW
        self.n_hosts = kwargs.get('n_hosts', 100) if (not cfg.OVERRIDE_N_HOSTS)     \
                       else cfg.N_HOSTS_PER_SW
        self.base_ip = na.IPAddress(0)
        self.end_ip = na.IPAddress(0)


    def __str__(self):
        ret =   'Switch name %s\n'                  %(self.name) + \
                '\ttable_size: %s\n'                %(self.table_size) + \
                '\tn_hosts: %s\n'                   %(self.n_hosts) + \
                '\tbase_ip: %s\n'                   %(self.base_ip) + \
                '\tend_ip: %s\n'                    %(self.end_ip) + \
                '\tcurrent # of entries: %s\n'      %(len(self.table))
        return ret


    def get_usage(self):
        return len(self.table)


    def get_util(self):
        return float(len(self.table)) / float(self.table_size)


    def install_flow_entry(self, src_ip, dst_ip):
        if (not (src_ip, dst_ip) in self.table):
            self.table[(src_ip, dst_ip)] = 0.0


    def remove_flow_entry(self, src_ip, dst_ip):
        del self.table[(src_ip, dst_ip)]
        # Prevent exceptions??


