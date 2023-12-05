package com.example.board.controlloer;

import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.LocalDate;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.example.board.dao.BoardMapper;

import jakarta.servlet.http.HttpServletRequest;

@RestController
public class DBController {
    @Autowired
    BoardMapper boardMapper;

    @GetMapping("board/list")
    public String BoardList() {
        List<Map<String, Object>> qrySet = boardMapper.listSelect();
        String title = null;
        String seq = null;
        String writer = null;
        String searchcount = null;
        String countanswer = null;
        String currentDate = null;
        String html = """ 
            <!DOCTYPE html>
            <html>
                <head>
                    <link rel="stylesheet" href="/boardmain.css">
                    <title>게시판</title>
                </head>
                <body>
                    <h1>스프링부트(Mybatis) 게시판</h1>
                    <div class="wrapper">
                        <div class="container">
                            <div class="boardlist">
                                <div class="seq"><strong>게시글 번호</strong></div>
                                <div class="title"><strong>&nbsp제목</strong></div>
                                <div class="writer"><strong>게시자</strong></div>
                                <div class="date"><strong>작성일</strong></div>
                                <div class="searchcount"><strong>조회수</strong></div>
                            </div>
        """;    
        for (int i = 0; i < qrySet.size(); i++) {
            title = qrySet.get(i).get("title").toString();
            seq = qrySet.get(i).get("seq").toString();
            writer = qrySet.get(i).get("writer").toString();
            searchcount = qrySet.get(i).get("search_count").toString();
            currentDate = qrySet.get(i).get("write_date").toString();
            countanswer = boardMapper.countAnswer(seq).get(0).get("cnt").toString();
            html += String.format("""
<div class="boardcontent">
    <div class="seq">%s</div>
    <div class="title">
        <div class=titlecon>
            <a href="/board/detail?seq=%s">%s (%s)</a>
        </div>
        <div class=update>
            <a href="/board/update?seq=%s">수정</a>
        </div>
        <div class=delete>
            <a href="/board/delete?seq=%s">삭제</a>
        </div>
    </div>
    <div class="writer">%s</div>
    <div class="date">%s</div>
    <div class="searchcount">%s</div>
</div>      
""",i+1,seq,title,countanswer,seq,seq,writer,currentDate,searchcount);
        }
        html += """
                        </div>
                        <div class="insertbutton">
                            <a href="/"><button type="button">새 글 작성</button></a>
                        </div>
                </body>
            </html>       
        """;
        return html;
    }

    @GetMapping("board/list1")
    public String boardlist1() {
        String result = boardMapper.listSelect().toString();
        String html = "<h1>"+result+"</h1>";
        return html;
    }

    @GetMapping("board/insert")
    public String boardInsert(
        @RequestParam("title") String title,
        @RequestParam("content") String content,
        @RequestParam("writer") String writer) {
            // LocalDate currentDate = LocalDate.now();
            String date = LocalDate.now().toString();
            String time = LocalTime.now().toString().substring(0, 8);
            String writeDate = date + " " + time;
            if (title == "") {
                title = "(제목 없음)";
            }
            if (content == "") {
                content = "(내용 없음)";
            }
            if (writer == "") {
                writer = "익명";
            }
            boardMapper.insert(title, content, writer, writeDate);
            return String.format("""
<html>
    <head>
        <link rel="stylesheet" href="/boardmsg.css">
        <title>등록 완료!</title>
    </head>
    <body>
        <div class=container>
            <div class=showmsg>
                %s님의 글이 정상적으로 등록되었습니다.
            </div>
            <div class=btn>
                <a href="/board/list">
                <button type=button>확인</button>
                </a>
            </div>
        </div>
    </body>
</html>  
""",writer);
    }

    @GetMapping("board/detail")
    public String boardDetail(HttpServletRequest request) {
        String seq = request.getParameter("seq");
        String qrySet = boardMapper.detailSelect(seq).get(0).get("content").toString();
        String writer = boardMapper.detailSelect(seq).get(0).get("writer").toString();
        String title = boardMapper.detailSelect(seq).get(0).get("title").toString();
        int searchcount = Integer.parseInt(boardMapper.detailSelect(seq).get(0).get("search_count").toString());
        searchcount += 1;
        boardMapper.addsearchcount(seq, searchcount);
        List<Map<String,Object>> answerQrySet = boardMapper.getCountAnswer(seq);
        int count = boardMapper.getCountAnswer(seq).size();
        String html = String.format("""
<html>
    <head>
        <link rel="stylesheet" href="/boardmsg.css">
        <title>게시물</title>
    </head>
    <body>
        <div class=container>
            <div class=msgtitle>%s</div>
            <div class=msgwriter>%s</div>
            <div class=showmsg>
                %s
            </div>
            <div class=btn>
                <a href="/board/answer?seq=%s">
                <button type=button>답글 달기</button>
                <a href="/board/list">
                <button type=button>목록으로</button>
                </a>
            </div>
        </div>
        <div class=answercontainer>
""",title,writer,qrySet,seq);
        if (count > 0) {
            for (int i = 0; i < count; i++) {
                String answer = answerQrySet.get(i).get("answer").toString();
                String writer2 = answerQrySet.get(i).get("writer").toString();
                String id = answerQrySet.get(i).get("id").toString();
                html += String.format("""
<div class="replycontainer">
    <div class="reply">
        <div class="replyname"><strong>%s</strong></div>
        <div class="replycontent">%s</div>
    </div>
    <div class="replybutton">
        <div class="replyupdate">
            <button><a href="/answer/update?id=%s">수정</a></button>
        </div>
        <div class="replydelete">
            <button><a href="/answer/delete?id=%s">삭제</a></button>
        </div>
    </div> 
</div>                   
""",writer2,answer,id,id);
            }
        } else {
            html += "<div class='noreply'>아직 댓글이 없습니다. 새로운 댓글을 입력해보세요!</div>";              
        }
        return html+"</div></body></html>";
    }

    @GetMapping("board/delete")
    public String boardDelete(@RequestParam("seq") String seq) {
        String title = boardMapper.detailSelect(seq).get(0).get("title").toString();
        boardMapper.delete(seq);
        boardMapper.deletewithanswer(seq);
        return String.format("""
<html>
    <head>
        <link rel="stylesheet" href="/boardmsg.css">
        <title>삭제 완료!</title>
    </head>
    <body>
        <div class=container>
            <div class=showmsg>
                %s 글이 삭제되었습니다.
            </div>
            <div class=btn>
                <a href="/board/list">
                <button type=button>확인</button>
                </a>
            </div>
        </div>
    </body>
</html>  
""",title); 
}

    @GetMapping("board/update")
    public String boardUpdate(String seq) {
        String title = boardMapper.detailSelect(seq).get(0).get("title").toString();
        String content = boardMapper.detailSelect(seq).get(0).get("content").toString();
        return String.format(
"""
<html>
    <head>
        <link rel="stylesheet" href="/boardinsert.css">
        <title>게시물 수정</title>
    </head>
    <body>
        <div class="wrapper">
            <div class="inserttitle">게시물 수정</div>
            <form action="/board/update/content" method="get">
                <input class="seq" type="hidden" value="%s" name="seq">
                <div class="col">
                    <div class="row" >제목</div>
                    <input class="title" type="text" name="title" value="%s" maxlength="22">
                </div>
                <div class="col" id="content">
                    <div class="row">내용</div>
                    <textarea class="content" name="content">%s</textarea>
                </div>
                <div class="savebutton">
                    <div><button type="submit">수정</button></div>
                    <div><a href="/board/list"><button type="button">취소</button></a></div>
                </div>
            </form>
        </div>
    </body>
</html>
""",seq,title,content);
    }

    @GetMapping("board/update/content")
    public String updateContent(
        @RequestParam("seq") String seq,
        @RequestParam("title") String title,
        @RequestParam("content") String content) {
        String writer = boardMapper.detailSelect(seq).get(0).get("writer").toString();
        boardMapper.update(seq, title, content);
        return String.format("""
<html>
    <head>
        <link rel="stylesheet" href="/boardmsg.css">
        <title>수정 완료!</title>
    </head>
    <body>
        <div class=container>
            <div class=showmsg>
                %s님의 글이 수정되었습니다.
            </div>
            <div class=btn>
                <a href="/board/list">
                <button type=button>확인</button>
                </a>
            </div>
        </div>
    </body>
</html> 
""",writer);
        }
    @GetMapping("board/answer")
    public String answerInsert(
        @RequestParam("seq") String seq) {
            return String.format(
"""
<html>
    <head>
        <link rel="stylesheet" href="/boardinsert.css">
        <title>답글 작성</title>
    </head>
    <body>
        <div class="wrapper">
            <div class="inserttitle">답글 달기</div>
            <form action="/board/answer/execute" method="get">
                <input class="seq" type="hidden" value="%s" name="seq">
                <div class="col">
                    <div class="row" >작성자</div>
                    <input class="title" type="text" name="writer" maxlength="5">
                </div>
                <div class="col" id="content">
                    <div class="row">내용</div>
                    <textarea class="content" name="answer" maxlength="255"></textarea>
                </div>
                <div class="savebutton">
                    <div><button type="submit">등록</button></div>
                    <div><a href="/board/detail?seq=%s"><button type="button">취소</button></a></div>
                </div>
            </form>
        </div>
    </body>
</html>             
""",seq,seq);
    }

    @GetMapping("board/answer/execute")
    public String boardAnswerInsert(
        @RequestParam("seq") String seq,
        @RequestParam("answer") String answer,
        @RequestParam("writer") String writer
    ) {
        if (writer == "") {
            writer = "익명";
        }
        if (answer == "") {
            answer = "(내용없음)";
        }
        boardMapper.insertAnswer(seq, answer, writer);
        return String.format("""
<html>
    <head>
        <link rel="stylesheet" href="/boardmsg.css">
        <title>답글 작성 완료!</title>
    </head>
    <body>
        <div class=container>
            <div class=showmsg>
                %s님의 답글이 등록되었습니다.
            </div>
            <div class=btn>
                <a href="/board/detail?seq=%s">
                <button type=button>확인</button>
                </a>
            </div>
        </div>
    </body>
</html> 
""",writer,seq);
    }

    @GetMapping("answer/delete")
    public String answerDelete(@RequestParam("id") int id) {
        String writer = boardMapper.getCountAnswer2(id).get(0).get("writer").toString();
        String seq = boardMapper.getCountAnswer2(id).get(0).get("seq").toString();
        boardMapper.answerdelete(id);
        return String.format("""
<html>
    <head>
        <link rel="stylesheet" href="/boardmsg.css">
        <title>답글 삭제 완료!</title>
    </head>
    <body>
        <div class=container>
            <div class=showmsg>
                %s님의 답글이 삭제되었습니다.
            </div>
            <div class=btn>
                <a href="/board/detail?seq=%s">
                <button type=button>확인</button>
                </a>
            </div>
        </div>
    </body>
</html>  
""",writer,seq); 
}

    @GetMapping("answer/update")
        public String answerUpdate(@RequestParam("id") int id) {
            String answer = boardMapper.getCountAnswer2(id).get(0).get("answer").toString();
            String seq = boardMapper.getCountAnswer2(id).get(0).get("seq").toString();
            return String.format(
"""
<html>
    <head>
        <link rel="stylesheet" href="/boardinsert.css">
        <title>답글 수정</title>
    </head>
    <body>
        <div class="wrapper">
            <div class="inserttitle">답글 수정</div>
            <form action="/answer/update/content" method="get">
                <input class="id" type="hidden" value="%s" name="id">
                <div class="col" id="content">
                    <div class="row">내용</div>
                    <textarea class="content" name="answer" maxlength="255">%s</textarea>
                </div>
                <div class="savebutton">
                    <div><button type="submit">수정</button></div>
                    <div><a href="/board/detail?seq=%s"><button type="button">취소</button></a></div>
                </div>
            </form>
        </div>
    </body>
</html>
""",id,answer,seq);
    }

    @GetMapping("answer/update/content")
    public String updateAnswer(
        @RequestParam("answer") String answer,
        @RequestParam("id") int id) {
        String seq = boardMapper.getCountAnswer2(id).get(0).get("seq").toString();
        String writer = boardMapper.getCountAnswer2(id).get(0).get("writer").toString();
        boardMapper.updateAnswer(id, answer);
        return String.format("""
<html>
    <head>
        <link rel="stylesheet" href="/boardmsg.css">
        <title>수정 완료!</title>
    </head>
    <body>
        <div class=container>
            <div class=showmsg>
                %s님의 답글이 수정되었습니다.
            </div>
            <div class=btn>
                <a href="/board/detail?seq=%s">
                <button type=button>확인</button>
                </a>
            </div>
        </div>
    </body>
</html> 
""",writer,seq);
        }
}