 ## Assignment: Vertex Drawing
 ## Student: Daniel Wooden
 ## Pasadena City College, Spring 2026
 ## Course Name: DMA60 Creative Coding
 ## Prof. George McKinney
 ## Project Description: Vertex Drawing (Shapes or characters)
 ## Last Modified: 3/9/26
 
 ## My challenges while making this was where the points, and shapes would really
 ## end up at as i'm still trying to get use to the x, y, width, height and the
 ## starting and end point of things especially with the curves of shapes. I'd 
 ## like to keep playing with it more, and experiment with it. My thought process
 ## of this was honestly just going with the flow, and see what could be done by
 ## practicing the code, and placement of things. 

def setup():
    size(450, 400)

def draw():
    background(255)
    
    ## top line red rect + black cir
    line(20,50,415,110)
    rect(50, 25, 25, 50)
    rect(90, 35, 25, 50)
    rect(130, 45, 25, 50)
    fill(5)
    circle(195,75,50)
    circle(260,85,50)
    circle(326,96,50)
    circle(390,108,50)
    
    ## red circles
    fill(255,0,0)
    circle(195,130,50)
    circle(260,145,50)
    circle(326,165,50)
    circle(390,185,50)

    ## bottom line 
    line(20,51,414,353)
    line(400,90,414,353)
    
    ## bottom left vertex, red eyes
    fill(255,0,0)
    beginShape()
    vertex(150, 350)
    bezierVertex(380, 210, 280, 475, 150, 350)
    bezierVertex(20, 20, 20, 375, 150, 350)
    endShape()

def mousePressed():
    print(mouseX, mouseY)
