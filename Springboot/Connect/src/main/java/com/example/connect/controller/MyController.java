package com.example.connect.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin(origins = "http://localhost:3000")
public class MyController {
    @GetMapping("/api/data")
    public String Home() {
        return "스프링부트로부터 온 데이터입니다.";
    }
}
