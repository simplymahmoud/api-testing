# -*- coding: utf-8 -*-
from testframework.base import *
import types


response_headers = {'Content-Type': 'application/json; charset=utf-8',
                    'Connection': 'keep-alive'}

post = {"id": 1,
        "userId": 1, 
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", 
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}  
                
class TestPosts(BaseTest):

   
    def test001_create(self):
        """ TestCase-1: Test case for test create post using POST /posts/.*
        **Test Scenario:**
        #. Create post using POST /posts/, should succeed
        #. Check response headers, should succeed
        #. Check response body, should succeed
        """    	
        self.lg('%s STARTED' % self._testID)
        
        self.lg('#. Create post using POST /posts/, should succeed')
        response = self.post_request_response(uri='/posts', data=post)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.ok)
        
        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]    
        
        self.lg('#. Check response body, should succeed')
        self.assertEqual(type(response.json()), types.DictType)
        self.assertEqual(response.json(), post)        
        
        self.lg('%s ENDED' % self._testID)

    def test002_view(self):
        """ TestCase-2: Test case for test view post using GET /posts/{id}.*
        **Test Scenario:**
        #. View post using GET /posts/{id}, should succeed
        #. Check response headers, should succeed
        #. Check response body, should succeed
        """    	
        self.lg('%s STARTED' % self._testID)
     
        self.lg('#. View post using GET /posts/{id}, should succeed')
        response = self.get_request_response(uri='/posts/%d' % post["id"])
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        
        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]    
        
        self.lg('#. Check response body, should succeed')
        self.assertEqual(type(response.json()), types.DictType)
        [self.assertEqual(response.json()[key], post[key]) for key in response.json().keys()]
                
        self.lg('%s ENDED' % self._testID)

    def test003_list(self):
        """ TestCase-3: Test case for test list posts using GET /posts.*
        **Test Scenario:**
        #. List posts using GET /posts, should succeed
        #. Check response headers, should succeed
        #. Check response body, should succeed
        """    	
        self.lg('%s STARTED' % self._testID)
          
        self.lg('#. View post using GET /posts, should succeed')
        response = self.get_request_response(uri='/posts')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        
        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]    
        
        self.lg('#. Check response body, should succeed')
        self.assertEqual(type(response.json()), types.ListType)
        for post_dict in response.json():
            self.assertEqual(type(post_dict), types.DictType)
            for key in post.keys():                
                self.assertIn(key, post_dict.keys())
            if post_dict['id'] == post['id']:        
                [self.assertEqual(post_dict[key], post[key]) for key in post.keys()]
 
        
        self.lg('%s ENDED' % self._testID)

    def test004_update(self):
        """ TestCase-4: Test case for test update post using PUT /posts/{id}.*
        **Test Scenario:**
        #. Update post using PUT /posts/{id}, should succeed
        #. Check response headers, should succeed
        #. Check response body, should succeed
        """    	
        self.lg('%s STARTED' % self._testID)
        post = {"id": 1,
                "userId": 1, 
                "title": "new title", 
                "body": "new body"}   
                
        self.lg('#. Update post using PUT /posts/{id}, should succeed')
        response = self.put_request_response(uri='/posts/%d' % post["id"], data=post)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        
        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]    
        
        self.lg('#. Check response body, should succeed')
        self.assertEqual(type(response.json()), types.DictType)
        [self.assertEqual(response.json()[key], post[key]) for key in post.keys()]
        
        self.lg('%s ENDED' % self._testID)

    def test005_delete(self):
        """ TestCase-5: Test case for test delete post using DELETE /posts/{id}.*
        **Test Scenario:**
        #. Delete post using DELETE /posts/{id}, should succeed
        #. Check response headers, should succeed
        #. Check response body, should succeed
        """    	
        self.lg('%s STARTED' % self._testID)
        
        self.lg('#. Delete post using DELETE /posts/{id}, should succeed')
        response = self.delete_request_response(uri='/posts/%d' % post["id"])
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        
        self.lg('#. Check response headers, should succeed')
        [self.assertIn(header, response.headers.keys()) for header in response_headers.keys()]
        [self.assertEqual(response_headers[header], response.headers[header]) for header in response_headers.keys()]    
        
        self.lg('#. Check response body, should succeed')
        self.assertEqual(type(response.json()), types.DictType)
        self.assertEqual(response.json(), {})
        
        self.lg('%s ENDED' % self._testID)