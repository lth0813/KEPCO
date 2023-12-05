package com.example.demo;

import java.io.IOException;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import com.example.demo.config.Game;
import com.example.demo.config.ImageUtil;
import com.example.demo.config.Movie;
import com.example.demo.config.Music;
import com.example.demo.config.TV;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) throws IOException {
		ApplicationContext context = new AnnotationConfigApplicationContext(BeanConfig.class);
		
		Game game = (Game) context.getBean("game"); //BeanConfig class
		game.play();

		Movie movie = (Movie) context.getBean("movie"); //BeanConfig (xml)
		movie.play();

		TV tv = (TV) context.getBean("TV"); //BeanConfig (xml)
		tv.play();

		Music music = (Music) context.getBean("music");
		music.play();

		ImageUtil imageutil = (ImageUtil) context.getBean("imageutil");
		imageutil.save("http://ggoreb.com/images/luffy.jpg");

		((AnnotationConfigApplicationContext) context).close();


	}
}
