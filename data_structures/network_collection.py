from .entry import Entry
import re
import socket, struct


class NetworkCollection():
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.
        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """     
        self.ipv4_network = ipv4_network
        if type(raw_entry_list) != list:
            raise TypeError
        self.entries = []
        for x in raw_entry_list:
            self.entries.append(Entry(x['address'], x['available'],x['last_used']))
        self.remove_invalid_records()

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """        
        remover = lambda x : re.search("(^[01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$", x.address) != None
        temp_entries = list(filter(remover,self.entries))
        self.entries = [x for x in temp_entries]        
             
    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """
        self.entries = sorted(self.entries, key = lambda x : x.compare_key())
        

        
    def __str__(self):
        return {self.ipv4_network.__str__():[print(f'\t{x.__str__()}') for x in self.entries].__str__()}
