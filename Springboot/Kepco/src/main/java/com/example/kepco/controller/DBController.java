package com.example.kepco.controller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.kepco.dao.DemoDao;

import jakarta.servlet.http.HttpServletRequest;

@RestController
public class DBController {
    @Autowired
    DemoDao demoDao;

    @GetMapping("/jdbc/demo")
    public List<Map<String, Object>> jdbcDemo() {
        return demoDao.select();
    }

    // @GetMapping("/jdbc/demo/insert")
    // public String jdbcDemoInsert() {
    //     demoDao.insert();
    //     return "잘 저장되었습니다."
    // }
    @GetMapping("jdbc/demo/insert")
    public String jdbcTest(HttpServletRequest request) {
        List<Map<String, Object>> value = demoDao.maxSeqSelect();
        Map<String,Object> result = value.get(0);
        int maxSeq = Integer.parseInt(result.get("seq").toString()); 
        int seq = maxSeq + 1;
        String seq1 = Integer.toString(seq);
        String user = request.getParameter("user");
        demoDao.insert(seq1,user);
        String message = String.format("%s 님이 저장되었습니다. 총 %d명의 회원이 있습니다.",user,seq);
        return message;
    }
}
