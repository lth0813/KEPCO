package com.example.kepco.controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.kepco.dao.DemoDao;

import jakarta.servlet.http.HttpServletRequest;

@Controller
@RestController
public class RequestControlloer {
    @GetMapping("res/http")
    public String httpRes(HttpServletRequest request) {
        String name = request.getParameter("name");
        String pageNum = request.getParameter("pageNum");
        String age = request.getParameter("age");
        return "name : "+name+"\n"+"pageNum : "+pageNum+"\n"+"age : "+age;
    }

    @GetMapping("req/param1")
    public String param1(
        @RequestParam("key1") String key1,
        @RequestParam("key2") String key2
    ) {
        return key1+", "+key2;
    }

    @GetMapping("req/param2")
    public String param2(
        @RequestParam Map<String, Object> map
    ) {
        return map.toString();
    }

    @GetMapping("req/path/{path1}/{path2}")
    public String path(
        @PathVariable("path1") String path1,
        @PathVariable("path2") String path2
    ) {
        return path1+", "+path2;
    }

    @GetMapping("req/data")
    public Map<String,Object> exam2(
        @RequestParam Map<String, Object> map
    ) {
        return map;
    }

    @Autowired
    DemoDao demoDao;
    // @GetMapping("/jdbc/demo/insert")
    // public String jdbcDemoInsert(HttpServletRequest request) {
    //     String seq = request.getParameter("seq");
    //     String user = request.getParameter("user");
    //     demoDao.insert(seq,user);
    //     return user+"가 잘 저장되었습니다.";
    // }
    

}
