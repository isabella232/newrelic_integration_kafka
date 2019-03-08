import yaml
import json


def test_global_config(host):
    newrelic_integration_config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )

    assert 'integration_name: com.newrelic.kafka' \
        in newrelic_integration_config.content_string


def test_kafka_metrics(host):
    config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )
    config_object = yaml.load(config.content_string)
    kafka_metrics_config = [
        el for el in config_object['instances']
        if el['name'] == "kafka-metrics"
    ]

    assert len(kafka_metrics_config) == 1
    assert 'command' in kafka_metrics_config[0]
    assert kafka_metrics_config[0]['command'] == "metrics"


def test_kafka_inventory(host):
    config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )
    config_object = yaml.load(config.content_string)
    kafka_inventory_config = [
        el for el in config_object['instances']
        if el['name'] == "kafka-inventory"
    ]

    assert len(kafka_inventory_config) == 1
    assert 'command' in kafka_inventory_config[0]
    assert kafka_inventory_config[0]['command'] == "inventory"


def test_kafka_consumer_offset(host):
    config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )
    config_object = yaml.load(config.content_string)
    kafka_consumer_offset_config = [
        el for el in config_object['instances']
        if el['name'] == "kafka-consumer-offsets"
    ]

    assert len(kafka_consumer_offset_config) == 1
    assert 'command' in kafka_consumer_offset_config[0]
    assert kafka_consumer_offset_config[0]['command'] == "consumer_offset"


def test_zookeeper_config(host):
    config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )
    config_object = yaml.load(config.content_string)
    zookeeper_hosts_config = [
        el['arguments']['zookeeper_hosts'] for el in config_object['instances']
        if el['arguments'] and el['arguments']['zookeeper_hosts']
    ]

    assert len(zookeeper_hosts_config) == 3,\
        "Expecting 3 zookeeper arguments, one from each module"

    for zookeeper_hosts in zookeeper_hosts_config:
        hosts = json.loads(zookeeper_hosts)

        assert len(hosts) == 1
        assert hosts[0]['host'] == "zookeeper1.localnet"
        assert hosts[0]['port'] == 2181
