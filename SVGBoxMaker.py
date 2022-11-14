import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cairo

def MakeSide(ctx,w,h,tab_depth,horz_tab_count,vert_tab_count,horz_tab_first,vert_tab_first):
    (org_x, org_y) = ctx.get_current_point()
    horz_tab_size = w/(horz_tab_count*2+1)
    vert_tab_size = h/(vert_tab_count*2+1)
    
    if(horz_tab_first and vert_tab_first):
        ctx.rel_line_to(-tab_depth,0)

    #topside
    if(horz_tab_first):
        if(not vert_tab_first):
            ctx.rel_line_to(0,-tab_depth)  
        for _ in range(horz_tab_count):
            ctx.rel_line_to(horz_tab_size,0)
            ctx.rel_line_to(0,tab_depth)
            ctx.rel_line_to(horz_tab_size,0)
            ctx.rel_line_to(0,-tab_depth)
        ctx.rel_line_to(horz_tab_size,0)
        if(vert_tab_first):
            ctx.rel_line_to(tab_depth,0)
        ctx.rel_line_to(0,tab_depth)
    else:
        for _ in range(horz_tab_count):
            ctx.rel_line_to(horz_tab_size,0)
            ctx.rel_line_to(0,-tab_depth)
            ctx.rel_line_to(horz_tab_size,0)
            ctx.rel_line_to(0,tab_depth)
        ctx.rel_line_to(horz_tab_size,0)

    #TODO add this to all the tab virst movements
    # if(not(vert_tab_first and horz_tab_first)):
    #     ctx.rel_line_to(0,-tab_depth)
    
    #rightside
    if(vert_tab_first):
        if(not horz_tab_first):
            ctx.rel_line_to(tab_depth,0)
        for _ in range(vert_tab_count):
            ctx.rel_line_to(0,vert_tab_size)
            ctx.rel_line_to(-tab_depth,0)
            ctx.rel_line_to(0,vert_tab_size)
            ctx.rel_line_to(tab_depth,0)
        ctx.rel_line_to(0,vert_tab_size)
        if(horz_tab_first):
            ctx.rel_line_to(0,tab_depth)
        ctx.rel_line_to(-tab_depth,0)
    else:
        for _ in range(vert_tab_count):
            ctx.rel_line_to(0,vert_tab_size)
            ctx.rel_line_to(tab_depth,0)
            ctx.rel_line_to(0,vert_tab_size)
            ctx.rel_line_to(-tab_depth,0)
        ctx.rel_line_to(0,vert_tab_size)

    #bottomside
    if(horz_tab_first):
        if(not vert_tab_first):
            ctx.rel_line_to(0,tab_depth)
        for _ in range(horz_tab_count):
            ctx.rel_line_to(-horz_tab_size,0)
            ctx.rel_line_to(0,-tab_depth)
            ctx.rel_line_to(-horz_tab_size,0)
            ctx.rel_line_to(0,tab_depth)
        ctx.rel_line_to(-horz_tab_size,0)
        if(vert_tab_first):
            ctx.rel_line_to(-tab_depth,0)
        ctx.rel_line_to(0,-tab_depth)
    else:
        for _ in range(horz_tab_count):
            ctx.rel_line_to(-horz_tab_size,0)
            ctx.rel_line_to(0,tab_depth)
            ctx.rel_line_to(-horz_tab_size,0)
            ctx.rel_line_to(0,-tab_depth)
        ctx.rel_line_to(-horz_tab_size,0)

    #leftside
    if(vert_tab_first):
        if(not horz_tab_first):
            ctx.rel_line_to(-tab_depth,0)
        for _ in range(vert_tab_count):
            ctx.rel_line_to(0,-vert_tab_size)
            ctx.rel_line_to(tab_depth,0)
            ctx.rel_line_to(0,-vert_tab_size)
            ctx.rel_line_to(-tab_depth,0)
        ctx.rel_line_to(0,-vert_tab_size)
        if(horz_tab_first):
            ctx.rel_line_to(0,-tab_depth)
        ctx.rel_line_to(tab_depth,0)
    else:
        for _ in range(vert_tab_count):
            ctx.rel_line_to(0,-vert_tab_size)
            ctx.rel_line_to(-tab_depth,0)
            ctx.rel_line_to(0,-vert_tab_size)
            ctx.rel_line_to(tab_depth,0)
        ctx.rel_line_to(0,-vert_tab_size)
    
    ctx.close_path()
    ctx.fill()
            
def MakeBox(context,org_x,org_y,w,h,d,tab_depth):
    context.move_to(org_x,org_y)
    MakeSide(context, w, h, tab_depth, w, h, False, False)
    context.move_to(org_x+w+tab_depth*3, org_y)
    MakeSide(context, d, h, 0.1, d, h, False, True)
    context.move_to(org_x+w+d+tab_depth*7, org_y)
    MakeSide(context, w, d, 0.1, w, d, True, True)


def InitWindow():
    app = QApplication(sys.argv)
    window = QWidget()
    b = QLabel(window)
    b.setText('Hello World!')
    window.setGeometry(100,100,200,50)
    b.move(50,20)
    window.setWindowTitle("PyQt5")
    window.show()
    sys.exit(app.exec_())

class window(QWidget):
    def __init__(self, parent = None):
        super(window, self,).__init__(parent)
        self.resize(200,50)
        self.setWindowTitle("Hi")
        self.label = QLabel(self)
        self.label.setText('Hello World!')
        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50,20)

if __name__ == '__main__':
    with cairo.SVGSurface("test.svg", 800, 800) as surface:
        surface.set_document_unit(cairo.SVGUnit.IN) #5 : inches
        context = cairo.Context(surface)
        context.set_source_rgb(1,0,1)
        context.move_to(0,0)
        tab_depth = 1.5/25.4
        MakeSide(context, 4, 1.75, tab_depth, 7, 3, False, False)
        context.move_to(0,3)
        MakeSide(context, 4, 1.75, tab_depth, 7, 3, True, False)
        context.move_to(0,6)
        MakeSide(context, 1.75, 1.75, tab_depth, 3, 3, True, True)
        
