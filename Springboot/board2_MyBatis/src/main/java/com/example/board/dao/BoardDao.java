package com.example.board.dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class BoardDao {
    @Autowired
    JdbcTemplate jt;

    // public List<Map<String, Object>> listSelect() {
    //     String sqlStmt = "SELECT * FROM BOARD";
    //     return jt.queryForList(sqlStmt);
    // }

    // public void insert(String title, String content, String writer) {
    //     String sqlStmt = String.format("INSERT INTO BOARD (title, content, writer) VALUES ('%s', '%s', '%s')",title, content, writer);
    //     jt.execute(sqlStmt);
    // }

    // public List<Map<String, Object>> detailSelect(String seq) {
    //     String sqlStmt = String.format("SELECT * FROM BOARD WHERE seq = %s",seq);
    //     return jt.queryForList(sqlStmt);
    // }

    // public void delete(String seq) {
    //     String sqlStmt = String.format("DELETE FROM board WHERE seq = '%s'",seq);
    //     String sqlStmt2 = String.format("DELETE FROM board_answer WHERE seq = '%s'",seq);
    //     jt.execute(sqlStmt);
    //     jt.execute(sqlStmt2);
    // }

    // public void update(String seq, String title, String content) {
    //     String sqlStmt = String.format("UPDATE board SET title='%s', content='%s' WHERE seq = %s",title,content,seq);
    //     jt.execute(sqlStmt);
    // }

    // public void addsearchcount(String seq, int searchcount) {
    //     String sqlStmt = String.format("UPDATE board SET search_count = %d WHERE seq = %s",searchcount,seq);
    //     jt.execute(sqlStmt);
    // }

    // public void insertAnswer(String seq, String answer, String writer) {
    //     String sqlStmt = String.format("INSERT INTO board_answer(seq, answer, writer) VALUES ('%s','%s','%s')",seq,answer,writer);
    //     jt.execute(sqlStmt);
    // }

    // public List<Map<String,Object>> getCountAnswer(String seq) {
    //     String sqlStmt = String.format("SELECT * FROM board_answer WHERE seq = %s",seq);
    //     return jt.queryForList(sqlStmt);
    // }

    // public List<Map<String,Object>> getCountAnswer2(int id) {
    //     String sqlStmt = String.format("SELECT * FROM board_answer WHERE id = %s",id);
    //     return jt.queryForList(sqlStmt);
    // }

    // public void answerdelete(int id) {
    // String sqlStmt = String.format("DELETE FROM board_answer WHERE id = %d",id);
    // jt.execute(sqlStmt);
    // }

    // public void updateAnswer(int id, String answer) {
    //     String sqlStmt = String.format("UPDATE board_answer SET answer='%s' WHERE id = %s",answer,id);
    //     jt.execute(sqlStmt);
    // }
}
