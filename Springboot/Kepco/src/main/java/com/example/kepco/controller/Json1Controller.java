package com.example.kepco.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.example.kepco.dto.Member;

@Controller
@ResponseBody // 리턴 값이 주소대신에 html 문자열로 보냄
public class Json1Controller {
    @GetMapping("json/string") // 요청하는 주소
    public String json() {
        return """
            <head>
                <style>
                    p {
                        color:blue;
                    }
                    strong {
                        color:red;
                    }
                </style>
                <title>json 첫 번째 방법</title>
            </head>
            <body>
            <p>
                <strong>json</strong>/string
            </p>
            <br>
            <a href="/html/void">이동</a>
            </body> 
                """; // html 문자열, 태그 같은거도 적용됨
    }

    @GetMapping("json/map")
    public Map<String, Object> jsonMap(Map<String, Object> map) {
        Map<String, Object> map2 = new HashMap<String, Object>();
        map2.put("key3", true);
        map2.put("key1", "value");
        map2.put("key2", 1234);
        System.out.println(map2.toString());
        return map2;
    }

    @GetMapping("json/object")
    public Member jsonObject() {
        Member member = new Member("",null,null);
        member.setName("Lim");
        // member.setAge(33);
        return member;
    }

    @GetMapping("json/list")
    public List<String> jsonList() {
        List<String> list = new ArrayList<>();
        for (int i = 1; i <= 3; i++) {
            list.add(Integer.toString(i));
        }
        return list;

    }

    @GetMapping("json/exam")
    public Map<String, Object> jsonMap2(Map<String, Object>map) {
        Map<String, Object> map1 = new LinkedHashMap<String, Object>();
        // Map<String, Object> map2 = new LinkedHashMap<String, Object>();
        // map2.put("name","가");
        // map2.put("userId","A");
        // map2.put("userPassword","1");
        // Map<String, Object> map3 = new LinkedHashMap<String, Object>();
        // map3.put("name","나");
        // map3.put("userId","B");
        // map3.put("userPassword","2");
        List<Object> list = new ArrayList<>();
        list.add(new Member("가","A","1"));
        list.add(new Member("나","B","2"));
        map1.put("count", list.size());
        map1.put("list", list);
        return map1;
    }

}

