package com.example.kepco.controller;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.example.kepco.dto.Member;


@Controller
public class HomeController {
    
    // 1번째 방법 - RequestMapping
    @RequestMapping("/") // 접속할 주소 설정
    public String home() {
        return "html/string"; // 접속할 주소의 페이지 정보
        // 리턴 쪽에서는 대소문자는 구분 안함, 폴더명, 파일명은 같아야함
    }

    // 2번째 방법 - GetMapping 리턴 값 없는 void로 만들기
    @GetMapping("html/void") // 접속할 주소이면 페이지 정보
    public void htmlVoid() {

    }

    // 3번째 방법 - Map 타입으로 보내기
    @GetMapping("html/map")
    public Map<String, Object> htmlMap(Map<String, Object> map){
        Map<String, Object> map2 = new HashMap<String, Object>();
        return map2;
    }

    // 4번째 방법 - Model로 보내기(Spring에서 지원)
    @GetMapping("html/model")
    public Model htmlModel(Model model) { // 객체 타입이 model임
        return model;
    }

    @GetMapping("html/model_view")
    public ModelAndView htmlModel() {
        ModelAndView mav = new ModelAndView();
        return mav;
    }

    @GetMapping("html/object")
    public Member htmlObject() { // Member가 없으므로 DTO라고 새로 만듬
        Member member = new Member("kim",null,null);
        member.setName("Lim");
        // member.setAge(33);
        return member;
    }
    
    @RequestMapping("html/exam")
    public String exam() {
        return "html/exam";
    }

    @GetMapping("req/http")
    public String httpReq() {
        return "html/request";
    }

    @GetMapping("jdbc/html")
    public String jdbcHtml() {
        return "html/demo";
    }
}
