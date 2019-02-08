import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_integration_package(host):
    nginx = host.package("nri-kafka")
    assert nginx.is_installed
    assert nginx.version.startswith("1.1")
