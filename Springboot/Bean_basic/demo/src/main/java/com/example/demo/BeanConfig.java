package com.example.demo;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.ImportResource;

import com.example.demo.config.Game;

@Configuration
@ImportResource("classpath:application.xml")
@ComponentScan(basePackageClasses = BeanConfig.class)

public class BeanConfig {
    @Bean
    public Game game() {
        return new Game();
    }
}
