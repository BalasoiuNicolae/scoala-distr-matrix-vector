import tkinter
from square import Square

height=500
width=1600
initial_height_x = 200
whitespace_width_x = 80
initial_height_y  = 190
whitespace_width_y = 120

matrix = [[1,2,3],[1,2,2],[1,2,3],[1,4,3]]
vect = [1,2,3]
list_squares = []
top = tkinter.Tk()
canvas = tkinter.Canvas(top, bg="white", height=500, width=1600)

def systolic_trick():
    
    aux = 0
    for line in matrix:
        for i in range(aux):
            line.insert(0, 0)
        aux = aux + 1
    

def draw_vector(top):       
    global I
    I = tkinter.Label(top, height = 1, width = 50, font=("Purisa", 16), text="Input:" + string_builder(vect))
    I.pack()

def draw():

    for i in range(len(matrix)):
        outer = False
        helper = i+1
        x1 = helper*initial_height_x
        x2 = helper*initial_height_x + whitespace_width_x
        y1 = initial_height_y
        y2 = initial_height_y + whitespace_width_y
        if i==0:
            outer = True
        item = Square(x1,y1,x2,y2,canvas,outer,i,matrix[i])
        list_squares.append(item)


    draw_vector(top)
    button = tkinter.Button(top, text = "Advance", command= step)
    button.pack()
    canvas.pack()

def string_builder(array):
    string = ""
    for i in range(len(array)):
        if(i != len(array)-1):
            string = string+str(array[i])+","
        else:
            string = string+str(array[i])

    return string    

def step():
    
    i = len(list_squares)-1
    while(i > 0):
        list_squares[i].u = list_squares[i-1].u_prim
        list_squares[i].u_prim = list_squares[i].u
        if list_squares[i].line: #check if list is not empty
            aux = list_squares[i].line.pop(0)
            list_squares[i].v = list_squares[i].v + list_squares[i].u * aux
        i= i-1

    if list_squares[0].line:
        aux = list_squares[0].line.pop(0)
    if vect:
        aux = vect.pop(0)
        list_squares[0].u = aux 
        list_squares[0].u_prim = aux
        if(list_squares[0].u != None):
            list_squares[0].v = list_squares[0].v + list_squares[0].u * aux
    else:
        list_squares[0].u = 0 
        list_squares[0].u_prim = 0

    I.configure(text = "Vector: " + string_builder(vect))
    canvas.delete("tag")

    for k in list_squares:
         k.draw_tags()  

def main():
    systolic_trick()
    draw() 
    top.mainloop()

main()
