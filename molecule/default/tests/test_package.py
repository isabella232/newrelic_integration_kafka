import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_integration_package(host):
    newrelic_kafka = host.package("nri-kafka")
    assert newrelic_kafka.is_installed
    assert newrelic_kafka.version.startswith("1.1")
