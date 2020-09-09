# coding: utf-8

"""
    KS Trade API's

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.quote_api import QuoteApi  # noqa: E501
from openapi_client.rest import ApiException


class TestQuoteApi(unittest.TestCase):
    """QuoteApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.quote_api.QuoteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_instruments_details(self):
        """Test case for get_instruments_details

        Get full details  # noqa: E501
        """
        pass

    def test_get_ltp_quote(self):
        """Test case for get_ltp_quote

        Get LTP quote  # noqa: E501
        """
        pass

    def test_get_market_details_quote(self):
        """Test case for get_market_details_quote

        Get market details quote  # noqa: E501
        """
        pass

    def test_get_ohlc_quote(self):
        """Test case for get_ohlc_quote

        Get OHLC quote  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()