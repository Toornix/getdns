from dnsdb.api import APIClient
from getdns import getdns
from nose.tools import assert_equal
import sys
import os

default_username = 'test'
default_password = '123456'
default_proxy = 'http://localhost:8081'
default_api_url = 'http://localhost:8080/api/v1'


def test_validate_ip():
    assert getdns.validate_ip("1.1.1") == False
    assert getdns.validate_ip("255.255.255.255") == True
    assert getdns.validate_ip("1.1.1.256") == False
    assert getdns.validate_ip("1.1.1.-1") == False


def test_config():
    if os.path.exists(getdns.CONFIG_PATH):
        os.remove(getdns.CONFIG_PATH)
    temp = sys.argv
    sys.argv = [temp[0]]
    sys.argv += ['config', '-u', default_username, '-p', default_password, '--proxy', default_proxy, '--api-url',
                 default_api_url]
    getdns.main()
    defaults = getdns.get_defaults()
    assert_equal(defaults['username'], default_username)
    assert_equal(defaults['password'], default_password)
    assert_equal(defaults['proxy'], default_proxy)
    assert_equal(defaults['api_url'], default_api_url)
    sys.argv = temp
