from unittest import TestCase
from nose.tools import assert_raises
from nose.tools import assert_not_equal, assert_true
from ..helpers.integration_test_helper import IntegrationTestHelper


class TestPostalcodeFunctions(TestCase):

    def setUp(self):
        self.env_variables = IntegrationTestHelper.get_environment_variables()
        self.sql_api_url = "{0}://{1}.{2}/api/v1/sql".format(
            self.env_variables['schema'],
            self.env_variables['username'],
            self.env_variables['host'],
        )

    def test_if_select_with_ipaddress_point_is_ok(self):
        query = "SELECT cdb_geocode_ipaddress_point(ip) " \
            "as geometry FROM {0} LIMIT 1&api_key={1}".format(
                self.env_variables['table_name'],
                self.env_variables['api_key'])
        geometry = IntegrationTestHelper.execute_query(self.sql_api_url, query)
        assert_not_equal(geometry['geometry'], None)

    def test_if_select_with_ipaddress_without_api_key_raise_error(self):
        query = "SELECT cdb_geocode_ipaddress_point(ip) " \
            "as geometry FROM {0} LIMIT 1".format(
                self.env_variables['table_name'])
        try:
            IntegrationTestHelper.execute_query(self.sql_api_url, query)
        except Exception as e:
            assert_true(e.message[0] in ["Geocoding permission denied", "function cdb_geocode_ipaddress_point(text) does not exist"])
