from data_structures.cluster import Cluster
import json

class Datacenter:
    def __init__(self, name:str, cluster_dict:dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.clusters = [Cluster(x, cluster_dict[x]["networks"], cluster_dict[x]["security_level"]) for x in cluster_dict.keys()]
        pass

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        pass
    
    def __str__(self):
        return {self.name:[print(x.__str__()) for x in self.clusters]}
