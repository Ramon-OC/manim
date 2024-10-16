import numpy as np
from manim import *

class MaxCut(Scene):
    def construct(self):

        formula02 = MathTex(r"\mathbb{E}[\mathrm{Corte}] = \sum_{\text{arista }(i, j)} \frac{\theta_{ij}}{\pi} \ \ge 0.87857 \ \sum_{\text{aristas}} \frac{1 - x_i^T x_j}{2}")
        formula02.to_edge(UP, buff=2)
        self.play(FadeIn(formula02))
        self.wait(3)
        
        formula03 = MathTex(r"\mathbb{E}[\mathrm{Corte}] = \sum_{\text{arista }(i, j)} \frac{\theta_{ij}}{\pi} \ \ge 0.88 \ \sum_{\text{aristas}} \frac{1 - x_i^T x_j}{2}")
        formula03.to_edge(UP, buff=2)

        self.play(FadeOut(formula02),FadeIn(formula03))
        self.wait(3)

        formula04 = MathTex(r"\:\ge \:0.88\:MaxCut")
        self.play(Transform(formula03, formula04))

        self.wait(3)
 