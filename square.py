class Square():

    def __init__(self,x1,y1,x2,y2,canvas,outer,var,line):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.canvas = canvas
        self.line = line
        self.u = 0
        self.u_prim = 0
        self.v = 0

        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="white", outline = 'black')
        #left
        canvas.create_line(x1-70,y1+60,x1,y1+60)
        #right
        canvas.create_line(x2,y1+60,x2+70,y1+60)

        canvas.create_text((x1+40,y1+30), text="P"+str(var))


        if outer == False:
            canvas.create_rectangle(x1-70,y1+35,x1-50,y1+85, fill="black", outline = 'black')
            canvas.create_rectangle(x1-70,y2-35,x1-50,y2-85, fill="black", outline = 'black')

        canvas.create_text((x1+40,y1+30), text="P"+str(var))
        self.draw_tags()
       


    def draw_tags(self):
        #self.canvas.create_text((self.x1+40, self.y2+10),text="1")
        aux = 10
        for i in self.line:
            if (i != 0):
                self.canvas.create_text((self.x1+40, self.y2+aux), tag="tag",text=str(i))
            else:
                self.canvas.create_text((self.x1+40, self.y2+aux), tag="tag",text="delay")
            
            aux = aux+15
        
        #u
        if(self.u != 0):
            self.canvas.create_text((self.x1-15,self.y1+50), tag="tag", text=str(self.u))
        else:
            self.canvas.create_text((self.x1-15,self.y1+50), tag="tag", text="")

        #uprim
        if(self.u_prim != 0):
            self.canvas.create_text((self.x2+15,self.y1+50), tag="tag", text=str(self.u_prim))
        else:
            self.canvas.create_text((self.x2+15,self.y1+50), tag="tag", text="")
        
        if(self.v == None):
            self.canvas.create_text((self.x1+40,self.y1+90),tag="tag", text="")
        else:
            self.canvas.create_text((self.x1+40,self.y1+90),tag="tag", text=str(self.v))


        




    def __str__(self):
        return str(self.x1) + " " + str(self.y1) + " " + str(self.x2) + " " + str(self.y2)