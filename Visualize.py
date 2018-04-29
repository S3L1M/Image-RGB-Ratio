
from scene import Scene
from topics.geometry import Vector
from mobject.tex_mobject import *
from mobject.vectorized_mobject import *
from animation.simple_animations import *

class showRatio(Scene):
    def construct(self):
        red = Vector((RIGHT*4.2)*0.120682540594, color = RED)
        blue = Vector((UP*4)*0.372455911075, color = BLUE)
        green = Vector((UP*4-1.4)*0.223491833257, color = GREEN)
        self.play(ShowCreation(red, run_time = 2))
        self.play(ShowCreation(blue, run_time = 2))
        self.play(ShowCreation(green, run_time = 2))
        