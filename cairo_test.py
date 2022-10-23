import cairo

inches = 25.4 #used to convert from mm

def make_side(ctx, w, h, tab_width, tab_depth):
    (org_x, org_y) = ctx.get_current_point()

    #top side
    num_tabs_horz = int(w/(tab_width*2))
    for _ in range(num_tabs_horz):
        ctx.rel_line_to(tab_width,0)
        ctx.rel_line_to(0,-tab_depth)
        ctx.rel_line_to(tab_width,0)
        ctx.rel_line_to(0,tab_depth)
    #finish incase tab width is not divisible
    #this could cause trouble in the case of ending on a tab?
    ctx.line_to(org_x+w, org_y)

    #right side
    num_tabs_vert = int(h/(tab_width*2))
    for _ in range(num_tabs_vert):
        ctx.rel_line_to(0,tab_width)
        ctx.rel_line_to(tab_depth,0)
        ctx.rel_line_to(0,tab_width)
        ctx.rel_line_to(-tab_depth,0)
    ctx.line_to(org_x+w, org_y+h)

    #bottom side
    num_tabs_horz = int(w/(tab_width*2))
    for _ in range(num_tabs_horz):
        ctx.rel_line_to(-tab_width,0)
        ctx.rel_line_to(0,tab_depth)
        ctx.rel_line_to(-tab_width,0)
        ctx.rel_line_to(0,-tab_depth)
    #finish incase tab width is not divisible
    #this could cause trouble in the case of ending on a tab?
    ctx.line_to(org_x, org_y+h)

    #left side
    num_tabs_vert = int(h/(tab_width*2))
    for _ in range(num_tabs_vert):
        ctx.rel_line_to(0,-tab_width)
        ctx.rel_line_to(-tab_depth,0)
        ctx.rel_line_to(0,-tab_width)
        ctx.rel_line_to(tab_depth,0)
    ctx.line_to(org_x, org_y)

    ctx.close_path()
    ctx.fill()

if __name__ == "__main__":
    with cairo.SVGSurface("test.svg", 800, 800) as surface:
        context = cairo.Context(surface)
        context.set_source_rgb(1,0,1)
        context.move_to(50,50)
        make_side(context, 250, 250, 50, 10)

