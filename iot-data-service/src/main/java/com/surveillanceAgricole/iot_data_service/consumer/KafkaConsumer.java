package com.surveillanceAgricole.iot_data_service.consumer;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.EnableKafka;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
@EnableKafka
public class KafkaConsumer {

    @KafkaListener(topics="topic-exemple-1", groupId = "grp1")
    public void listen(ConsumerRecord<String, String> record) {
        System.out.println("Received data from Kafka:"+record.value());
    }
}
