package finalproject;

import processing.core.PApplet;
import processing.core.PImage;
import java.lang.Object;
import javax.swing.Timer;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
public class FinalProject extends PApplet {
	
public boolean moveRight = false;
public boolean moveLeft = false;
public boolean moveUp = false;
public boolean moveDown = false;

public float time2 = 0;
public double time = 0.0;

public float timer1 = 0;
public float speed = 5;
public float yChange = 0;
public float yx = 0;
	
public float x = 400;
public float y = 350;

public int delay = 100; //milliseconds
public ActionListener taskPerformer = new ActionListener() {
    public void actionPerformed(ActionEvent evt) {
    	
    		
    		
        	y += speed;
    	
    }
};

public Object timer = new Object();
public void setup() {
	size(800, 700);
}
	public void draw() {
		background(255, 255, 255);
			
			
		moveRect();
		translate(x, y);
		drawRect();
	}
		
	public int xs = 0;
	public int ys = 0;
		
	public void drawRect(){
		fill(0, 0, 0);
		rect(xs, ys, 75, 150);
	}
	public void keyPressed()
	{
		if(key == 'a')
		{
			moveLeft = true;
		}
		if(key == 'd')
		{
			moveRight = true;
		}
		if(key == 'w')
		{
			moveUp = true;
		}
	}
	public void keyReleased()
	{
		if(key == 'a')
		{
			moveLeft = false;
		}
		if(key == 'd')
		{
			moveRight = false;
		}
		if(key == 'w')
		{
			yx = y + yChange;
			//while(y < yx){
			moveUp = false;
				//y += speed;
			
			new Timer(delay, taskPerformer).start();
			//moveUp = false;
			yChange = 0;
			time = 0;
				//System.out.println("hi");
				
			//}
			
			//yChange = 0;
			//time = 0;
		}
	}
	public void moveRect(){
		while (moveDown){
			moveUp = false;
			if(!moveDown){
				break;
			}
		}
		if(x < 0 ){
			moveLeft = false;
			x += speed;
		}
		else if (x > 725){
			moveRight =  false;
			x -= speed;
		}
		else
		{
			if(moveRight && moveUp){
				if(time <= 2){

					x += speed;
					y -= speed;
					time += 0.1;
					yChange += speed;
				}
				else if(time > 2){
					yx = y + yChange;
					while(y > yx){
						moveUp = false;
						y += speed;
						yChange = 0;
						time = 0;
						System.out.println("hi");
						
					}
					//yChange = 0;
					//time = 0;
				}
			}
			boolean testCondition = false;
			if(moveLeft && moveUp){
				if(time <= 2){
					x -= speed;
					y -= speed;
					time = time + 0.1;
					yChange += speed;
				}
				else if(time > 2){
					moveUp = false;
					//reverses y
					yx = y+yChange;
					while(y < yx){
						System.out.println(y);
						y += (speed/10);
					}	
					yChange = 0;
					time = 0;
				}
			}
			else if(moveRight) 
			{
				x += speed;
				//y += speed;
			}
			else if(moveLeft)
			{
				x -= speed;
				//y -= speed;
			}
			else if(moveUp && time <= 2){
				
				y -= speed;
				time = time + 0.1;
				yChange += speed;
			}
				
				
				
					//y += (yChange);
					//time2 += 0.1;
					//time2 = 0;
				
					//int delay = 250; //milliseconds
					//ActionListener taskPerformer = new ActionListener() {
					    //public void actionPerformed(ActionEvent evt) {
					       // y += speed;
					    //}
					//};
					//while(y < yx){
			else if (moveUp && time > 2){
				yx = y+yChange;
				
				//while(y < yx){
					
					
					System.out.println("hi");
					//new Timer(delay, taskPerformer).start();
					if(y < yx){
						moveDown = true;
					}
					if(moveDown)
						new Timer(delay, taskPerformer).start();
				//}
				/*while(moveDown){
					new Timer(delay, taskPerformer).start();
					if(y < yx){
						System.out.println("hi");
						moveDown = false;
						break;
					}
				}*/
				
				
							
					
						//moveUp = false;
				        //try {
				            //Thread.sleep(3000);
				            
				        //} catch (InterruptedException e) {
				            // TODO Auto-generated catch block
				           // e.printStackTrace();
				        //}
						
					//}
				yChange = 0;
				time = 0;
			}
				
			
		}
	}
}

