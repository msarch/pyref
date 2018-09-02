
# {{{ EMPTY -------------------------------------------------------------------
'''

                                     . . .

'''
# simple example --------------------------------------------------------------

# }}} ------------------------------ END OF SECTION ---------------------------

# {{{ DICTIONARY --------------------------------------------------------------
'''

                                     DICTS

'''
# simple dict example ---------------------------------------------------------


# }}} ----------------------- END OF DICTIONARY SECTION -----------------------

# {{{ FOR LOOP ----------------------------------------------------------------

'''

                                      FOR

'''
# custom range generator using yield ------------------------------------------

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

for x in my_range(1, 10, 0.5):
    print x

# }}} ------------------------------ END OF SECTION ---------------------------

# {{{ GENERATORS --------------------------------------------------------------

'''

                                    GENERATORS

'''

# simple generator example ----------------------------------------------------

def gen():
        for i in range(1, 6):
            yield i

g = gen()  # g is a generator here.
g.next() # --> 1
g.next()  # --> 2
g.next()  # --> 3 etc...
for i in g:
    print i


# pair generator example ------------------------------------------------------

a=[x for x in range (10)]
print a

def iterate_pairs(l):
    for i in xrange(len(l)/2):
        yield (l[2*i], l[2*i + 1])

for x, y in iterate_pairs(a):
    print  x
    print  y
    print


# groups of 4 points generator example ----------------------------------------

def quad_generator(pts):
    for i in range(0,len(pts)-1, 3):
        j=(i+3)/4
        yield j,  pts[i], pts[i+1], pts[i+2], pts[i+3], rec_color[j]

list_of_pts = ('a','b','c','d','e','f','g','h','i','j','k','l','a')
quads = quad_generator(list_of_pts)
for i, a, b, c, d in quads:
    print i, a, b, c, d

    # }}} ----------------------- END OF GENERATORS SECTION -----------------------

# {{{ GEOMETRY ----------------------------------------------------------------
'''

                                    GEOMETRY

'''
# normal of an edge -----------------------------------------------------------
    '''
    ---------------------------------------------------------------------------
    NORMAL VECTOR
    To get a normal between points p1 and p2 rotate the vector p1->p2 clockwise
    through 90 degrees. That is for a segment going from (x1,y1) to (x2,y2):

        n = (dy, -dx) with: dx=x2-x1 and dy=y2-y1,

    The opposite normal vector is: n’=(-dy, dx)
    ---------------------------------------------------------------------------
    '''

    Point = namedtuple('Point', 'x y')
vtx= [(1, 2), (3, 4), (5, 6)]
for i,v in enumerate(vtx[0: -1]):
    norm = Point(v[i+1].x - v[i].x, v[i+1].y - v[i].y)
    print 'edge', i, norm


# transformation matrix 2D example --------------------------------------------
    '''
    A trois coordonnées, avec des matrices qui sont toujours carrées,
    on peut composer plusieur transformations en multipliant les matrices
    correspondant à chaque opération DANS UN ORDRE PRECIS.
    Si le point 2D devient artificielement un vecteur à 3 coordonnées (x,y,z)
    (par défaut on fixe z=1), la matrice générale des transformations 2d devient :
                    [x']   [a b m]   [x]   [ax + by + mz]   [ax + by + mz]
                    [y'] = [c d n] * [y] = [cx + dy + nz] = [cx + dy + nz]
                    [z']   [0 0 1]   [z]   [0x + 0y + 1z]	[     1      ]


    Transformation matrix for a (dx,dy) translation
    -----------------------------------------------

                        [ 1  0  dx]
                        [ 0  1  dy]
                        [ 0  0   1]

    Matrice type de mise à l'échelle
    --------------------------------

                        [Sx  0  0]
                        [ 0 Sy  0]
                        [ 0  0  1]

    Matrice de rotation
    -------------------

                    [ cosθ −sinθ    0]
                    [ sinθ  cosθ    0]
                    [   0     0     1]

    '''


import math
from collections import namedtuple

Point  = namedtuple('Point', 'x y')
ORIGIN = Point(0.0, 0.0)
MAT_ID = [1, 0, 0, 0, 1, 0, 0, 0, 1]  # Identity matrix
MAT_X_flip = [1, 0, 0, 0, -1, 0, 0, 0, 1]  # X axi symetry matrix
MAT_Y_flip = [-1, 0, 0, 0, 1, 0, 0, 0, 1]  # Y axi symetry matrix


def cos_sin_deg(deg):
    '''
    Return the cosine and sin for the given angle
    in degrees, with special-case handling of multiples
    of 90 for perfect right angles
    (by Casey Duncan and contributors)
    '''
    deg = deg % 360.0
    if deg == 90.0:
        return 0.0, 1.0
    elif deg == 180.0:
        return -1.0, 0
    elif deg == 270.0:
        return 0, -1.0
    rad = math.radians(deg)
    return math.cos(rad), math.sin(rad)

def transform(verts, M=MAT_ID):
    '''
    applies matrix M transformation to all self vertexes
    '''
    newverts = [ (M[0]*v[0]+M[1]*v[1]+M[2],
            M[3]*v[0]+M[4]*v[1]+M[5]) for v in verts]
    return(newverts)

def offset(verts,dx,dy):
    newverts = [(v[0] + dx, v[1] + dy) for v in verts]
    return(newverts)








# transformation matrix 3D example --------------------------------------------
from math import cos, sin, radians

def trig(angle):
  r = radians(angle)
  return cos(r), sin(r)

def matrix(rotation=(0,0,0), translation=(0,0,0)):
  xC, xS = trig(rotation[0])
  yC, yS = trig(rotation[1])
  zC, zS = trig(rotation[2])
  dX = translation[0]
  dY = translation[1]
  dZ = translation[2]
  return [[yC*xC, -zC*xS+zS*yS*xC, zS*xS+zC*yS*xC, dX],
    [yC*xS, zC*xC+zS*yS*xS, -zS*xC+zC*yS*xS, dY],
    [-yS, zS*yC, zC*yC, dZ],
    [0, 0, 0, 1]]

def transform(point=(0,0,0), vector=(0,0,0)):
  p = [0,0,0]
  for r in range(3):
    p[r] += vector[r][3]
    for c in range(3):
      p[r] += point[c] * vector[r][c]
  return p

if __name__ == '__main__':
  point = (7, 12, 8)
  rotation = (0, -45, 0)
  translation = (0, 0, 5)
  matrix = matrix(rotation, translation)
  print (transform(point, matrix))

# }}} ------------------------------ END OF SECTION ---------------------------

# {{{ LISTS -------------------------------------------------------------------
'''

                                     LISTS

                            ┌─────────────────┐
                            │() : tuples      │
                            │[] : lists       │
                            │{} : dictionaries│
                            └─────────────────┘
'''
# Looping Over Lists ----------------------------------------------------------
# The for-in statement makes it easy to loop over the items -------------------
for item in L:
    print item


# Looping Over Lists ----------------------------------------------------------
# If you need both index / item, use enumerate --------------------------------
for index, item in enumerate(L):
    print index, item


# Looping Over Lists ----------------------------------------------------------
# enumerate until 1 before end of list (slice) --------------------------------
    vtx= [(1, 2), (3, 4), (5, 6)]
    for i,v in enumerate(vtx[0: -1]):
        normal = ((vtx[i+1].x - vtx[i].x, vtx[i+1].y - vtx[i].y))
        print i, normal


# Looping Over Lists ----------------------------------------------------------
# If you need only the index, use range and len -------------------------------
for index in range(len(L)):
    print index


# Looping Over Lists ----------------------------------------------------------
# list supports the iterator protocol. To explicitly create an iterator, use the built-in iter function:
i = iter(L)
item = i.next() # fetch first value
item = i.next() # fetch second value


# Looping Over Lists ----------------------------------------------------------
# iter through pair of coordinates in a flat list of coords--------------------
flat_verts = [1, 2, 3, 4, 5, 6]
v = iter(flat_verts)
for i in xrange(len(flat_verts)/2):
    x = v.next()
    y = v.next()
    print x,y
    print


# flatten a list of list ------------------------------------------------------
flatten = lambda l: [item for sublist in l for item in sublist]
vtx= [(1, 2), (3, 4), (5, 6)]
flat_verts = flatten(vtx)
print flat_verts


# }}} ----------------------- END OF LIST SECTION -----------------------------

# {{{ LISTS 2 -----------------------------------------------------------------

# sorting ---------------------------------------------------------------------
student_tuples = [('john', 'A', 15),
                  ('jane', 'B', 12),
                  ('dave', 'B', 10) ]
sorted(student_tuples, key=lambda student: student[2])   # sort by age


# zip -------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
for num, let in zip(numbers, letters):
    print "Letter %d is '%s'" % (num, let)
'''
    Letter 1 is 'a'
    Letter 2 is 'b'
    Letter 3 is 'c'
    Letter 4 is 'd'
    Letter 5 is 'e'
'''

# min / max / sort a list of lists / “key" function ---------------------------
nested_list = [['cherry', 7], ['apple', 100], ['anaconda', 1360]]
max(nested_list, key=lambda x: x[1])
'''
['anaconda', 1360]
'''
# The same also works for built-in min function:
min(nested_list, key=lambda x: x[1])
'''
['cherry', 7]
'''
# works for sorted function:
sorted(nested_list, key=lambda x: x[1])
[['cherry', 7], ['apple', 100], ['anaconda', 1360]]


# }}} ----------------------- END OF LISTS 2 SECTION --------------------------

# {{{ OPEN GL -----------------------------------------------------------------

'''

                                      OPEN GL

'''

# circle (function) -----------------------------------------------------------
def circle(center=(0,0), radius=100, color=(255,255,255,255), sk=still):
    '''
    Circle, outline only
    '''
    # number of divisions per ∏ rads (half the circle)
    stepangle = math.pi / (int(radius / 5) + 12)
    # with vertices numbered like a clock,  GL_TRIANGLE_STRIP order is:
    # 11, 12, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5
    vtx = [0, radius]  # create list and first element
    phi = 0
    while phi < 2.0 * math.pi:
        vtx.append(radius * math.sin(phi))
        vtx.append(radius * math.cos(phi))
        phi += stepangle
    vtx.extend([0, radius])  # add right side vertex
    n = int(len(vtx) / 2)
    circle=batch.add(n, GL_LINE_STRIP, sk, 'v2f/static', 'c4B/static')
    circle.colors = color*n
    circle.vertices = translate(vtx, center)
    return(circle) # is a vertex_list since batch.add() returns a vertex_list


# colors ----------------------------------------------------------------------
orange  =(255, 127,   0, 255)
white   =(255, 255, 255, 255)
black   =(  0,   0,   0, 255)
yellow  =(255, 255,   0, 255)
red     =(255,   0,   0, 255)
blue    =(127, 127, 255, 255)
blue50  =(127, 127, 255, 127)
pink    =(255, 187, 187, 255)
very_light_grey =(242, 242, 242, 255)
# kapla_colors
r_k =(255, 69,   0,   255)  # red kapla
b_k =(  0,  0, 140,   255)  # blue kapla
g_k =(  0, 99,   0,   255)  # green kapla
y_k =(255, 214,  0,   255)  # yellow kapla


# dot -------------------------------------------------------------------------
pt=batch.add(5, pyglet.gl.GL_LINE_STRIP, wheel,'v2i/static', 'c4B/static')
pt.colors = (255,0,0,255)*5  # inaccessible color data
pt.vertices = translate([-3, 0, 3, 0, 0, 0, 0, 3, 0, -3], RADIUS,0)


# rectangle (plain) -----------------------------------------------------------
red_rec=batch.add(6, pyglet.gl.GL_TRIANGLES, still, 'v2f/static', 'c4B/static')
red_rec.colors = (255,0,0,230)*6
red_rec.vertices = (0,0,0,100,100,100,100,100,100,0,0,0)


# rectangle (outline) ---------------------------------------------------------
red_rec=batch.add(5, pyglet.gl.GL_LINE_STRIP, still, 'v2f/static', 'c4B/static')
red_rec.colors = (255,0,0,230)*5
red_rec.vertices = (0,0,0,w,w,h,0,h,0,0)


# rectangle (function) --------------------------------------------------------
def rec(w=100, h=100, color=(255,255,255,255), pos=ORIGIN, sk=still):
    rec=batch.add(6, pyglet.gl.GL_TRIANGLES, sk, 'v2f/static', 'c4B/static')
    rec.colors = color*6
    rec.vertices = translate((0,0,0,h,w,h,w,h,w,0,0,0), pos)
    return(rec) # batch.add() returns a vertex_list

rec_1 = rec(w=width, h=height, color=white, pos=(pox_x, pos_y))




##--- SQUIRTLE SVG SHAPE ------------------------------------------------------
import squirtle
class SVGshape(Shape):
    def setup(self,svg=None):
        self.svg = svg

    def draw(self):
        """
        svg shapes are drawn by squirtle which overides our draw method
        """
        self.svg.draw(self.pos[0], self.pos[1], scale=1, angle=0)


##--- POINT -------------------------------------------------------------------
class Point(Shape):
    """
    Simple Point, Autocad style cross
    """

    def setup(self):
        self.vtx = [-3, 0, 3, 0, 0, 0, 0, 3, 0, -3]
        self.glstring = (5, pyglet.gl.GL_LINE_STRIP, None, ('v2i/static',
            self.vtx),('c4B/static', self.color * 5))


##--- LINE FROM TWO POINTS ----------------------------------------------------
class Line(Shape):
    """
    Simple line defined by 2 points, requires: Point()
    """

    def setup(self, p1=Point(), p2=Point()):
        self.p1, self.p2 = p1, p2
        self.glstring = (2, pyglet.gl.GL_LINES, None,('v2f/static',
            (self.p1.pos[0], self.p1.pos[1], self.p2.pos[0], self.p2.pos[1])),
            ('c4B/static', self.color * 2))


##--- FILLED RECTANGLE --------------------------------------------------------
class Rect(Shape):
    """
    Rectangle, orthogonal, FILED, origin is bottom left
    N,S,E,W = north, south east, west coordinates
      _N_
    W|___|E
       S
    """

    def setup(self, N=0, S=0, E=0, W=0):  # kapla default size
        self.vtx = [E, S, W, S, W, N, E, N]
        self.glstring = (4,
                pyglet.gl.GL_TRIANGLE_FAN,
                None,
                ('v2f/static', self.vtx),
                ('c4B/static', self.color * 4))


##--- EMPTY RECTANGLE ---------------------------------------------------------
class Rect2(Shape):
    """
    Rectangle, orthogonal, OUTLINE ONLY, origin is bottom left
    """

    def setup(self, S=0, E=0, N=0, W=0):  # kapla default size
        self.vtx = [E, S, W, S, W, N, E, N, E, S]
        self.glstring = (5,
                pyglet.gl.GL_LINE_STRIP,
                None,
                ('v2f/static', self.vtx),
                ('c4B/static', self.color * 5))


##--- EMPTY CIRCLE ------------------------------------------------------------
class Circle(Shape):
    """
    Circle, outline only
    """

    def setup(self, radius=100, point=None):
        if point:
            self.radius = math.sqrt(point[0]**2+point[1]**2)
        else: self.radius = radius
        phi = 0
        stepangle = PI / (int(self.radius / 5) + 12)
        # number of divisions per ∏ rads (half the circle)
        # with vertices numbered like a clock,  GL_TRIANGLE_STRIP order is:
        # 11, 12, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5
        self.vtx = [0, self.radius]  # create list and first element
        while phi < TWOPI:
            self.vtx.append(self.radius * math.sin(phi))
            self.vtx.append(self.radius * math.cos(phi))
            phi += stepangle
        self.vtx.extend([0, self.radius])  # add right side vertex
        n = int(len(self.vtx) / 2)
        self.glstring = (n,
                pyglet.gl.GL_LINE_STRIP,
                None,
                ('v2f/static',self.vtx),
                ('c4B/static', self.color * n))


##--- CROSSHAIR VERTICAL ------------------------------------------------------
class Vline(Shape):
    """
    fullscreen vertical line
    """

    def setup(self):
        self.vtx = [0, 0]  # x only
        self.glstring = (2,
                pyglet.gl.GL_LINES,
                None,
                ('v2f/static',
                (self.vtx[0], -SCREEN_HEIGHT, self.vtx[0], SCREEN_HEIGHT)),
                ('c4B/static', self.color * 2))


##--- CROSSHAIR HORIZONTAL ----------------------------------------------------
class Hline(Shape):
    """
    fullscreen horizontal line
    """

    def setup(self):
        self.vtx = [0, 0]
        self.glstring = (2,
                pyglet.gl.GL_LINES,
                None, ('v2f/static',
                (-SCREEN_WIDTH, self.vtx[1], SCREEN_WIDTH, self.vtx[1])),
                ('c4B/static', self.color * 2))

# }}} ------------------------ END OF OPEN GL SECTION -------------------------

# {{{ PYGLET ------------------------------------------------------------------

'''

                                 PYGLET

'''


# pyglet clock ----------------------------------------------------------------

from pyglet.clock import schedule
# Schedule a function to be called every frame.
schedule(self, func, *args, **kwargs)
# Schedule a function to be called every interval seconds.
schedule_interval(self, func, interval, *args, **kwargs)
# Schedule a function to be called every interval seconds, beginning at a time that does not coincide with other scheduled events.
schedule_interval_soft(self, func, interval, *args, **kwargs)
# Schedule a function to be called once after delay seconds.
schedule_once(self, func, delay, *args, **kwargs)
# Remove a function from the schedule.
unschedule(self, func)

# }}} ------------------------- END OF PYGLET SECTION -------------------------

'''   VIM memo

     zM  : fold all
     zR  : unfold all

     42G : go to line 42
     42gg

     H         cursor to higher
     M         cursor to middle
     L         cursor to lower part of screen

     Ctrl-u    screen up ½ page
     Ctrl-d    screen down ½ page

'''

# vim: set foldenable foldmarker={{{,}}} foldlevel=0 foldmethod=marker foldcolumn=2 :
# vim: set syntax=python
# vim: set nonu!
