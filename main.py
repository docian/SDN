from data_structures.datacenter import Datacenter
import http.client
from time import sleep
import json

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, endpoint, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    conn = http.client.HTTPConnection(url)  # @UndefinedVariable  
    res = None
    while(max_retries > 0):
        conn.request("GET", endpoint) 
        res = conn.getresponse()
        data = res.read() 
        if res.status == 200:             
            break
        sleep(delay_between_retries)
        max_retries -= 1   
    conn.close()  
    return data.decode("utf-8")

def main():
    """
    Main entry to our program.
    """
    URL = 'www.mocky.io'
    endpoint = "/v2/5e539b332e00007c002dacbe"
    data = json.loads(get_data(URL, endpoint))
    print(data)
    
    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]
    for x in datacenters:
        print(x.__str__())



if __name__ == '__main__':
    main()