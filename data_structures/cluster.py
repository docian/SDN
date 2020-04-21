from data_structures.network_collection import NetworkCollection
class Cluster:
    def __init__(self, name:str, network_dict:dict, security_level:int):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """
        self.name = name
        self.security_level = security_level
        self.network_dict = [NetworkCollection(x,network_dict[x]) for x in network_dict.keys()]
        
    def __str__(self):
        return {'name':self.name,'security_level':self.security_level,'networks':[print(f'{x.__str__()}'+'\n') for x in self.network_dict]}
        
