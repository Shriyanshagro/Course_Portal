#!/usr/bin/python

import unittest
from gluon.globals import Request, Session, Storage, Response
from gluon.contrib.test_helpers import form_postvars

class DefaultController(unittest.TestCase):
    def setUp(self):
        # print self
        request = Request()  # Use a clean request
        session = Session()  # Use a clean session

    def testIndex(self):
        form_postvars("bla", {"body": "yes"}, request, action="create", record_id=None)
        resp = index()

        self.assertFalse(resp['form'].errors) # do we have errors?
        self.assertFalse(resp['form'].errors.has_key('name')) # is something missing?

        self.assertEquals(2, len(resp["results"]))

        db(db.bla.id>0).delete()
        db.commit()
