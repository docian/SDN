from _datetime import datetime
import ipaddress
import socket, struct

class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """
        self.address = address
        self.available = False
        if available == 'true':
            self.available = True
        self.last_used = datetime.strptime(last_used,"%d/%m/%y %H:%M:%S")
     
      
    def compare_key(self):
        ip = socket.inet_aton(self.address)
        return struct.unpack("!L", ip)[0]
        
    def __eq__(self, other_entry):
        """
        Compares instance with other Entry instance
        """
        if type(other_entry) != Entry:
            raise TypeError('Not an Entry type')
        if self.address == other_entry.address and self.available == other_entry.available and self.last_used == other_entry.last_used:
            return True
        return False
    
    def __str__(self):
        return {'address':self.address,'available':self.available,'last_used':self.last_used.__str__()}
            
        
