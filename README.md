# NewRelic Kafka Integration

Master: [![Build Status](https://travis-ci.org/sansible/newrelic_integration_kafka.svg?branch=master)](https://travis-ci.org/sansible/newrelic_integration_kafka)
Develop: [![Build Status](https://travis-ci.org/sansible/newrelic_integration_kafka.svg?branch=develop)](https://travis-ci.org/sansible/newrelic_integration_kafka)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This role install Kafka integration with NewRelic.


## Installation and Dependencies

To install run `ansible-galaxy install sansible.newrelic_integration_kafka` or add this to your
`roles.yml`.

```YAML
- name: sansible.newrelic_integration_kafka
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`

You can configure agent by passing in yaml object to
`sansible_newrelic_integration_kafka_instances`. For latest configuration options
please check [kafka-config.yml.sample].


## Tags

This role uses tags: **build** and **configure**

* `build` - Installs nri-kafka
* `configure` - Configures kafks integration


## Examples

Simply include role in your playbook

To include zookeeper or bootstrap argument simply include `autodiscover_strategy: zookeeper`
or `autodiscover_strategy: bootstrap`.

```YAML
- name: Install and Configure newrelic_integration_kafka
  hosts: somehost

  roles:
    - role: sansible.newrelic_integration_kafka
      sansible_newrelic_integration_kafka_zookeeper:
        hosts:
          - host: zookeeper.app.internal
            port: 2181
      sansible_newrelic_integration_kafka_instances:
        - name: metric
          command: metrics
          arguments:
            cluster_name: kafka
            autodiscover_strategy: zookeeper
```


[kafka-config.yml.sample]: https://github.com/newrelic/nri-kafka/blob/master/kafka-config.yml.sample
