package com.example.story.controller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.story.mapper.DemoMapper;

@RestController
public class DBController {
    @Autowired
    DemoMapper demoMapper;
    
    @GetMapping("/mybatis/demo")
    public List<Map<String, Object>> mybatisDemo() {
        return demoMapper.select();
    }

    @GetMapping("/mybatis/demobyid")
    public List<Map<String, Object>> mybatisDemoById(@RequestParam String seq) {
        return demoMapper.selectById(seq);
    }
    
}
