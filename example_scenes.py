#!/usr/bin/env python

from helpers import *

from mobject.tex_mobject import TexMobject
from mobject import Mobject
from mobject.image_mobject import ImageMobject
from mobject.vectorized_mobject import *

from animation.animation import Animation
from animation.transform import *
from animation.simple_animations import *
from animation.playground import *
from topics.geometry import *
from topics.characters import *
from topics.functions import *
from topics.number_line import *
from topics.combinatorics import *
from scene import Scene
from camera import Camera
from mobject.svg_mobject import *
from mobject.tex_mobject import *

from mobject.vectorized_mobject import *

from old_projects import three_dimensions
from old_projects.eola import *

import sys

## To watch one of these scenes, run the following:
## python extract_scenes.py -p file_name <SceneName>


class showRatio(Scene):
    def construct(self):
        ratioR = float(sys.argv[4])
        ratioG = float(sys.argv[5])
        ratioB = float(sys.argv[6])
        ratioRv = float(sys.argv[7])

        red = Vector((RIGHT*4.2)*ratioR, color=RED)
        blue = Vector((UP*4)*ratioB, color=BLUE)
        green = Vector((UP*4-1.4)*ratioG, color=GREEN)
        redv = Vector((RIGHT*4.2)*ratioRv, color=RED)

        help = TextMobject("with the help of 3blue1brown's Lib")
        for mob in help.submobjects[13:13+5]:
            mob.highlight(BLUE)
        for mob in help.submobjects[18:18+6]:
            mob.highlight('#B1695F')
        Title = TexMobject("Colors Ratio", color=TEAL)
        Ratio = TextMobject([str(round(ratioR*100, 2)), str(round(ratioG*100, 2)),str(round(ratioB*100, 2))])
        Ratio2 = TextMobject([str(round(ratioRv*100, 2)), str(round(ratioG*100, 2)),str(round(ratioB*100, 2))])
        Ratio.split()[0].highlight(RED)
        Ratio.split()[1].highlight(GREEN)
        Ratio.split()[2].highlight(BLUE)
        Ratio.next_to(Title, DOWN, buff=0.5)
        Ratio2.split()[0].highlight(RED)
        Ratio2.split()[1].highlight(GREEN)
        Ratio2.split()[2].highlight(BLUE)
        Ratio2.next_to(Title, DOWN, buff=0.5)

        self.play(Write(Title.highlight(YELLOW).to_edge(DOWN), run_time=1))
        self.play(ShowCreation(red, run_time=2))
        self.play(ShowCreation(blue, run_time=2))
        self.play(ShowCreation(green, run_time=2))
        self.play(Write(Ratio))
        self.dither(4)
        self.remove(Ratio)
        self.play(Transform(red, redv))
        self.play(Write(Ratio2))
        self.dither(3)
        self.clear()
        self.play(Write(TextMobject("Made by : M.Selim :]", color=YELLOW).scale(2), run_time = 2))
        self.play(Write(help.to_edge(DOWN)), run_time=4)
        self.dither(7)

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.rotate(np.pi/8)
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.dither()

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda (x, y, z) : complex_to_R3(np.exp(complex(x, y))),
            square
        ))
        self.dither()


class WriteStuff(Scene):
    def construct(self):
        self.play(Write(TextMobject("Stuff").scale(3)))

class Det(Scene):
    def construct(self):
        red = Vector((RIGHT*4.2)*0.137, color = RED)
        blue = Vector((UP*4), color = BLUE)
        green = Vector((UP*4-1.4)*0.054, color = GREEN)
        self.play(ShowCreation(red, run_time = 2))
        self.play(ShowCreation(blue, run_time = 2))
        self.play(ShowCreation(green, run_time = 2))


class DefineColumnSpace(Scene):
    def construct(self):
        left_words = TextMobject(
            "Set of all possible\\\\",
            "outputs",
            "$A\\vec{\\textbf{v}}$",
        )
        left_words[1].highlight(TEAL)
        VMobject(*left_words[-1][1:]).highlight(YELLOW)
        arrow = DoubleArrow(LEFT, RIGHT).to_edge(UP)
        right_words = TextMobject("``Column space''", "of $A$")
        right_words[0].highlight(left_words[1].get_color())

        everyone = VMobject(left_words, arrow, right_words)
        everyone.arrange_submobjects(RIGHT)
        everyone.to_edge(UP)

        self.play(Write(left_words))
        self.dither()
        self.play(
            ShowCreation(arrow),
            Write(right_words)
        )
        self.dither()
