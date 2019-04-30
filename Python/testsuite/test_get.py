# -*- coding: utf-8 -*-
from testframework.base import *
import types
from parameterized import parameterized


response_headers = {'Content-Type': 'application/json; charset=utf-8'}

class TestGet(BaseTest):
      
    @parameterized.expand([
    ('acquirer'),
    ('acquirer?acquirer_id=2'),    
    ('acquirer?offset=1'),
    ('acquirer?limit=1'),    
    ('bank'),
    ('bank?bank_id=501'),
    ('bank?offset=1'),
    ('bank?limit=1'),
    ('expectedfiles'),
    ('expectedfiles?acquirer_id=1'),
    ('expectedfiles?offset=1'),
    ('nocreportline'),
    ('nocreportline?file_id=99261'),
    ('nocreportline?file_id=record_id=1'), 
    ('nocreportline?file_id=match_status=M'),  
    ('nocreportline?file_id=payment_reference=271900000940'),  
    ('nocreportline?file_id=MOEA=000000271910000001160000100001'),  
    ('nocreportline?file_id=acquirer_reference_number=74143617117000197802095'),
    ('nocreportsummary?acquirer_id=2&date_reg=20190214'),
    ('paymentreportline?file_id=94971'),
    ('paymentreportline?record_id=2'),    
    ('paymentreportline?from_date=20160301&to_date=20190301'),
    ('paymentreportline?match_status=X'),
    ('paymentreportline?offset=1'),
    ('paymentreportsummary?acquirer_id=2&date_reg=20190128'),
    ('report?acquirer_id=2&file_category=PR'),
    ('report?acquirer_id=2&file_type_id=1002'),
    ('report?acquirer_id=2&file_id=94971'),  
    ('report?file_category=NR&from_date=20180301&to_date=20190301'),
    ('reportfilesummary?acquirer_id=2&date_reg=20190128'),
    ('settlementreportline?file_id=91751'), 
    ('settlementreportline?file_id=91751&match_status=M'),
    ('settlementreportline?record_id=1&match_status=M&file_id=91751'), 
    ('settlementreportline?record_id=1&MOEA=0108646109220640001000001'),  
    ('settlementreportsummary?acquirer_id=2&date_reg=20190128'),  
    ('statement?file_id=94251&statement_id=44512'),
    ('statement/match/summary?bank_id=15&date_reg=20190306'),
    ('statementline?statement_line_id=126&statement_id=44512'),
    ('statementsummary?date_reg=20190214'),
    ('statementsummarydetails?date_reg=20190214&lba_nr=216')
     
    ])
    def test_gets(self, test_string):
        """ TestCase-A: Test case for test using GET.*
        **Test Scenario:**
        #. Test GET /path, should succeed
        #. Check response headers, should succeed
        """    	
        self.lg('%s STARTED' % self._testID)
     
        self.lg('#. Test using GET path /%s, should succeed' %test_string)
        response = self.get_request_response(uri=test_string)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        
        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]    
        
        self.lg('#. Check response body, should succeed')
        self.assertEqual(type(response.json()), types.DictType)
        #[self.assertEqual(response.json()[key], post[key]) for key in response.json().keys()]        
                
        self.lg('%s ENDED' % self._testID)    
