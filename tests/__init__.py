from data_structures.entry import Entry
input_lst = [
            {
            "address": "255.255.255.0",
            "available": True,
            "last_used": "30/01/20 17:00:00"
          },
          {
            "address": "192.168..0.3",
            "available": True,
            "last_used": "30/01/20 17:00:00"
          },
          {
            "address": "192.168.0",
            "available": False,
            "last_used": "30/01/20 17:00:00"
          },
          {
            "address": "192.168.0.288",
            "available": False,
            "last_used": "30/01/20 17:00:00"
          },
          {
            "address": "invalid",
            "available": True,
            "last_used": "30/01/20 17:00:00"
          },
          {
            "address": "192.168.0.1",
            "available": False,
            "last_used": "30/01/20 16:00:00"
          },
          {
            "address": "192.168.0.4",
            "available": True,
            "last_used": "30/01/20 17:00:00"
          }
    ]
expected_lst=[
        Entry("255.255.255.0", True,"30/01/20 17:00:00"),
        Entry("192.168.0.1",False,"30/01/20 16:00:00"),
        Entry("192.168.0.4",True,"30/01/20 17:00:00"),
    ]

input_sorted =[
              {
            "address": "192.168.0.218",
            "available": False,
            "last_used": "30/01/20 17:00:00"
          },
          {
            "address": "255.255.255.0",
            "available": True,
            "last_used": "30/01/20 17:00:00"
          },
          {
            "address": "192.168.0.1",
            "available": False,
            "last_used": "30/01/20 16:00:00"
          },
          {
            "address": "192.168.0.4",
            "available": True,
            "last_used": "30/01/20 17:00:00"
          }
    ]

expected_sorted_lst=[        
        Entry("192.168.0.1", True,"30/01/20 16:00:00"),
        Entry("192.168.0.4",True,"30/01/20 17:00:00"),
        Entry("192.168.0.218",False,"30/01/20 17:00:00"),
        Entry("255.255.255.0",True,"30/01/20 17:00:00")
    ]