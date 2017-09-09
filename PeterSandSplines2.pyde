'''Trying to clone Generative Bot's Sand Splines
Peter Farrell with Curtis
Sept. 8, 2017'''

start = 50
end = 550
distbetween = 70

class Spline:
    def __init__(self,y,ran):
        self.xvals = [x for x in range(start,end,distbetween)]
        self.yval = y
        self.controlpts = [] #empty for now
        for i in self.xvals:
            self.controlpts.append([i + 50*0.3,self.yval])
            self.controlpts.append([i + 50*0.6,self.yval])
        self.randomvalue = ran
            
    def update(self):
        for j,xval in enumerate(self.xvals):
            if j < len(self.xvals)-1:
                bezier(xval,self.yval,
                    self.controlpts[int(2*j)][0],
                    self.controlpts[int(2*j)][1],
                    self.controlpts[int(2*j+1)][0],
                    self.controlpts[int(2*j+1)][1],
                    self.xvals[j+1],
                    self.yval)
        for n,pt in enumerate(self.controlpts):
            #println(pt)
            #pt[0] += ((-1)**n)*self.randomvalue**n
            pt[1] += random(-self.randomvalue,
                            self.randomvalue)

splineList = []
for i in range(20):
    splineList.append(Spline(20+20*i,i+1)) #create a spline

def setup():
    size(600,600)
    
def draw():
    global splineList
    fill(255,5)
    rect(0,0,width,height)
    #background(255)
    for sp in splineList:
        sp.update()

    