import turtle as t
t.shape("turtle")
angle=90
t.bgcolor("black")
t.speed(0)
for x in range(300):
if x%3==0:      
color="red"  
if x%3==1:     
color="blue"  
if x%3==2:    
color="white"  
t.color(color)  
t.forward(x)   
t.left(angle)  
t.circle(15)
