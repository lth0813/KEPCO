package com.example.story.mapper;

import org.apache.ibatis.annotations.Mapper;
import java.util.*;

@Mapper
public interface DemoMapper {
    public List<Map<String, Object>> select();
    public List<Map<String, Object>> selectById(String seq);
}
