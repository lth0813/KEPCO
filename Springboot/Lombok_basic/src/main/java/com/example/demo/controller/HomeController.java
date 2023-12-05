package com.example.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import lombok.extern.slf4j.Slf4j;

@Controller
@Slf4j
public class HomeController {
    @RequestMapping("/mypage")
    public String home() {
        log.trace("trace!");
        return "home";
    }
}
