import yaml


def test_global_config(host):
    newrelic_integration_config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )

    assert 'integration_name: com.newrelic.kafka' \
        in newrelic_integration_config.content_string


def test_kafka_metrics_zookeeper(host):
    config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )
    config_object = yaml.load(config.content_string)
    kafka_metrics_config = [
        el for el in config_object['instances']
        if el['name'] == "metric-zookeeper-bootstrap"
    ]

    assert len(kafka_metrics_config) == 1

    # command = metrics
    assert 'command' in kafka_metrics_config[0]
    assert kafka_metrics_config[0]['command'] == "metrics"

    # zookeeper connection config
    arguments = kafka_metrics_config[0]['arguments']
    # arguments:
    #   cluster_name: test_zookeeper
    # zookeeper_hosts parse json
    assert arguments['autodiscover_strategy'] == "zookeeper"
    assert arguments['zookeeper_auth_scheme'] == ""
    assert arguments['zookeeper_auth_secret'] == ""
    assert arguments['zookeeper_path'] == "/test/path"


def test_kafka_metrics_zookeeper_override(host):
    config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )
    config_object = yaml.load(config.content_string)
    kafka_metrics_config = [
        el for el in config_object['instances']
        if el['name'] == "metric-zookeeper-bootstrap-override"
    ]

    assert len(kafka_metrics_config) == 1

    # command = metrics
    assert 'command' in kafka_metrics_config[0]
    assert kafka_metrics_config[0]['command'] == "metrics"

    # zookeeper connection config
    arguments = kafka_metrics_config[0]['arguments']
    assert arguments['autodiscover_strategy'] == "zookeeper"
    assert arguments['zookeeper_auth_scheme'] == ""
    assert arguments['zookeeper_auth_secret'] == ""
    # this was overriden
    assert arguments['zookeeper_path'] == "/test/path/override"


def test_kafka_metrics_bootstrap(host):
    config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )
    config_object = yaml.load(config.content_string)
    kafka_metrics_config = [
        el for el in config_object['instances']
        if el['name'] == "metric-broker-bootstrap"
    ]

    assert len(kafka_metrics_config) == 1
    assert 'command' in kafka_metrics_config[0]
    assert kafka_metrics_config[0]['command'] == "metrics"

    arguments = kafka_metrics_config[0]['arguments']
    assert arguments['autodiscover_strategy'] == "bootstrap"
    assert arguments['bootstrap_broker_host'] == "bootstrap.localhost"
    assert arguments['bootstrap_broker_kafka_port'] == 9092
    assert arguments['bootstrap_broker_kafka_protocol'] == "PLAINTEXT"


def test_labels(host):
    config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )
    config_object = yaml.load(config.content_string)

    for el in config_object['instances']:
        labels = el['labels']
        assert labels['lorem'] == "ipsum"
        assert labels['dolor'] == "sit ament"
