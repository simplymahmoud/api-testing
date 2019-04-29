# -*- coding: utf-8 -*-
from testframework.base import *
import types
from parameterized import parameterized


response_headers = {'Content-Type': 'application/json; charset=utf-8',
                    'Connection': 'keep-alive'}


class TestGet(BaseTest):
    
   
    @parameterized.expand([
    ('acquirer'),
    ('acquirer?acquirer_id=2'),    
    ('acquirer?offset=1'),
    ('acquirer?limit=1'),    
    ('bank'),
    ('bank?bank_id=501'),
    ('bank?offset=1'),
    ('bank?limit=1')
    
    
    ])
    def test_gets(self, test_string):
        """ TestCase-A: Test case for test view acquirer without parameters using GET.*
        **Test Scenario:**
        #. Test GET /path, should succeed
        #. Check response headers, should succeed
        """    	
        self.lg('%s STARTED' % self._testID)
     
        self.lg('#. Test using GET path /%s, should succeed' %test_string)
        response = self.get_request_response(uri=test_string)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
                
        self.lg('%s ENDED' % self._testID)    