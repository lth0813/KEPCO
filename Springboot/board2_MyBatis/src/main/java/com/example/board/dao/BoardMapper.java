package com.example.board.dao;

import org.apache.ibatis.annotations.Mapper;
import java.util.*;

@Mapper
public interface BoardMapper {
    public List<Map<String, Object>> listSelect();
    public List<Map<String, Object>> insert(String title, String content, String writer, String currentDate);
    public List<Map<String, Object>> detailSelect(String seq);
    public void delete(String seq);
    public void deletewithanswer(String seq);
    public void update(String seq, String title, String content);
    public void addsearchcount(String seq, int searchcount);
    public void insertAnswer(String seq, String answer, String writer);
    public List<Map<String, Object>> countAnswer(String seq);
    public List<Map<String,Object>> getCountAnswer(String seq);
    public List<Map<String,Object>> getCountAnswer2(int id);
    public void answerdelete(int id);
    public void updateAnswer(int id, String answer);
}
