'''
Created on Apr 17, 2020

@author: dan
'''

import unittest
from tests import expected_lst,input_lst,input_sorted,expected_sorted_lst
from data_structures.network_collection import NetworkCollection

class NetworkCollectionTests(unittest.TestCase):
    '''
    classdocs
    '''
    
#     def setUp(self):
#         unittest.TestCase.setUp(self)
#         self.network_collection = NetworkCollection("192.168.0.0/24", input_lst)
    
    def test_remove_invalid_records(self):
        self.network_collection = NetworkCollection("192.168.0.0/24", input_lst)
        self.network_collection.remove_invalid_records()           
        print(self.network_collection.__str__())         
        for i in range(len(self.network_collection.entries)):
            self.assertTrue(self.network_collection.entries[i] == expected_lst[i],f'expected:{expected_lst[i].__str__()} actual:{self.network_collection.entries[i].__str__()}') 


    def test_sort_records(self):
        self.network_collection = NetworkCollection("192.168.0.0/24", input_sorted)
        self.network_collection.sort_records()
        for i in range(len(self.network_collection.entries)):
            self.assertTrue(self.network_collection.entries[i] == expected_sorted_lst[i],f'expected:{expected_sorted_lst[i].__str__()} actual:{self.network_collection.entries[i].__str__()}') 
        
if __name__ == '__main__':
    unittest.main()
        