# -*- coding: utf-8 -*-

import unittest
import logging
import dyndnsc


class DynDnscTestCases(unittest.TestCase):
    def setUp(self):
        logging.info("TestCases are being initialized")
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

#     def test_version(self):
#         import pkg_resources
#         print(pkg_resources.get_distribution("dyndnsc").version)  # pylint: disable=E1103

    def test_commanddetector(self):
        det = dyndnsc.detector.IPDetector_Command(options={'command': 'echo "127.0.0.1"'})
        self.assertEqual("127.0.0.1", det.detect())
        det = dyndnsc.detector.IPDetector_Command(options={'command': 'echo "127.0.0.2"'})
        self.assertEqual("127.0.0.2", det.detect())

    def test_teredo(self):
        # constructor: test invalid options
        det = dyndnsc.detector.IPDetector_Teredo(options={'iface': 'tun0'})
        logging.info(det.detect())
        # self.assertEquals(type(d.detect()), type(''))

    def test_update_noip(self):
        logging.basicConfig()
        config = {}
        config['hostname'] = "dyndnsc.no-ip.biz"
        config['userid'] = "example"
        config['password'] = "foobar"
        config['protocol'] = "noip"
        config['method'] = "random"
        config['sleeptime'] = 60
        dyndnsclient = dyndnsc.getDynDnsClientForConfig(config)
        self.assertTrue(dyndnsclient.needsCheck())
