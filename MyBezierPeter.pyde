'''Our own Bezier curves!
Peter F. and Curtis
Sept. 8, 2017'''

midpoints = []

class MyBezier:
    
    def __init__(self,pt1,pt2,pt3):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3
        
    def update(self,p):
        global midpoints
        #p = 0.0 #proportion
        stroke(0)
        #draw the three points
        ellipse(self.pt1[0],self.pt1[1],10,10)
        ellipse(self.pt2[0],self.pt2[1],10,10)
        ellipse(self.pt3[0],self.pt3[1],10,10)
        line(self.pt1[0],self.pt1[1],
             self.pt2[0],self.pt2[1])
        line(self.pt2[0],self.pt2[1],
             self.pt3[0],self.pt3[1])
        self.pt4 = PVector(lerp(self.pt1[0],self.pt2[0],p),
                       lerp(self.pt1[1],self.pt2[1],p))
        self.pt5 = PVector(lerp(self.pt2[0],self.pt3[0],p),
                       lerp(self.pt2[1],self.pt3[1],p))
        ellipse(self.pt4.x,
                self.pt4.y,
                10,10)
        ellipse(self.pt5.x,
                self.pt5.y,
                10,10)
        line(self.pt4.x,self.pt4.y,
             self.pt5.x,self.pt5.y)
        midpoints.append([lerp(self.pt4.x,self.pt5.x,p),
                        lerp(self.pt4.y,self.pt5.y,p)])

        fill(255,0,0)#red
        noStroke()
        for pt in midpoints:
            ellipse(pt[0],pt[1],5,5)
        
def midpoint(pt1,pt2):
    x = (pt1[0] + pt2[0])/2.0
    y = (pt1[1] + pt2[1])/2.0
    return [x,y]
        
b = MyBezier([100,100],[200,500],[400,300])
p = 0.0 #proportion
dp = 0.01


def setup():
    size(600,600)
    
def draw():
    global b,p,dp,midpoints
    background(255)
    b.update(p)
    p += dp
    if p >= 1.0 or p <= 0.0:
        dp = -dp
    