import unittest
from ListOfDictionaries import *

class TestList(unittest.TestCase):

    def test_list_hosts(self):
        l = ListOfDictionaries();
        l.addHost("aKey", "aHost")
        l.addHost("aKey1", "aHost1")
        l.addHost("aKey2", "aHost2")
        l.addHost("aKey3", "aHost3")
        l.addHost("aKey4", "aHost4")
                        
        self.assertEqual(l.listHost("aKey"), "aHost");
        self.assertEqual(l.listHost("aKey1"), "aHost1");
        self.assertEqual(l.listHost("aKey2"), "aHost2");
        self.assertEqual(l.listHost("aKey3"), "aHost3");
        self.assertEqual(l.listHost("aKey4"), "aHost4");
        
    def test_delete_host(self):
        l = ListOfDictionaries()
        l.addHost("HostKey", "HostValue")
        l.deleteHost("HostKey")

        self.assertEqual(l.listHost("HostKey"), None)
    
    def update_host(self):
        l = ListOfDictionaries();
        l.addHost("aKey", "aHost")
        l.updateHost("aKey", "NewHostValue")
        
        self.assertEqual(l.listHost("aKey"), "NewHostValue");
