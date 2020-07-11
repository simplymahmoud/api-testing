# -*- coding: utf-8 -*-
import logging
import time

from testconfig import config
from unittest import TestCase
import requests
import json

default_headers = {'Content-Type': 'application/json; charset=utf-8', 'Connection': 'keep-alive'}
TIMEOUT = 30


class BaseTest(TestCase):
    logger = logging.getLogger('api_testsuite')
    handler = logging.FileHandler(config['logs']['filename'])
    formatter = logging.Formatter('%(asctime)s [%(testid)s] [%(levelname)s] %(message)s',
                                  '%d/%m/%Y %I:%M:%S %p')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, config['logs']['level']))

    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)
        self.url = config['main']['url']

    def setUp(self):
        self._testID = self._testMethodName
        self._startTime = time.time()
        self._logger = logging.LoggerAdapter(logging.getLogger('api_testsuite'),
                                             {'testid': self.shortDescription().split(':')[0] or self._testID})
        self.lg('Testcase %s Started at %s' % (self._testID, self._startTime))
        self.session = requests.Session()

    def tearDown(self):
        """
        Environment cleanup and logs collection.
        """
        self.session.close()
        if hasattr(self, '_startTime'):
            executionTime = time.time() - self._startTime
        self.lg('Testcase %s Execution Time is %s sec.' % (self._testID, executionTime))

    def lg(self, msg):
        self._logger.info(msg)

    def get_request_response(self, uri, headers=None, payload=None):
        if not headers: headers = default_headers
        self.lg('GET %s' % self.url + uri)
        return self.session.get(self.url + uri, params=payload, headers=headers, timeout=TIMEOUT, allow_redirects=False)

    def post_request_response(self, uri, data, headers=None):
        if not headers: headers = default_headers
        self.lg('POST %s' % self.url + uri)
        return self.session.post(self.url + uri, data=json.dumps(data), headers=headers, timeout=TIMEOUT,
                                 allow_redirects=False)

    def put_request_response(self, uri, data, headers=None):
        if not headers: headers = default_headers
        self.lg('PUT %s' % self.url + uri)
        return self.session.put(self.url + uri, data=json.dumps(data), headers=headers, timeout=TIMEOUT,
                                allow_redirects=False)

    def delete_request_response(self, uri, headers=None):
        if not headers: headers = default_headers
        self.lg('DELETE %s' % self.url + uri)
        return self.session.delete(self.url + uri, headers=headers, timeout=TIMEOUT, allow_redirects=False)

    def pretty_print_request(self, request):
        self._logger.debug('\n{}\n{}\n\n{}\n\n{}\n'.format(
            '-----------Request----------->',
            request.method + ' ' + request.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
            request.body)
        )

    def pretty_print_response(self, response):
        self._logger.debug('\n{}\n{}\n\n{}\n\n{}\n'.format(
            '<-----------Response-----------',
            'Status code:' + str(response.status_code),
            '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
            response.text)
        )
