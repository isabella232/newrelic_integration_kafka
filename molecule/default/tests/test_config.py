

def test_config(host):
    newrelic_integration_config = host.file(
        '/etc/newrelic-infra/integrations.d/kafka-config.yml'
    )

    assert 'integration_name: com.newrelic.kafka' \
        in newrelic_integration_config.content_string
