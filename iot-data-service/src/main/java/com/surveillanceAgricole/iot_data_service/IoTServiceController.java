package com.surveillanceAgricole.iot_data_service;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/iot")
public class IoTServiceController {

    @PostMapping("/data")
    public String receiveData(@RequestBody String sensorData) {
        System.out.println("Received IoT Data:" + sensorData);
        return "Data received";
    }
}
