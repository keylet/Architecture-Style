package com.example;

import javax.jws.WebService;

@WebService(endpointInterface = "com.example.HelloService")
public class HelloServiceImpl implements HelloService {
    public String sayHello(String name) {
        return "Hello, " + name;
    }
}
