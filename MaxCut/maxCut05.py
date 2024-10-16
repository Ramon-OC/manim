from manim import *
import numpy as np

class MaxCut(Scene):
    def construct(self):
        title = Tex(r"Goemans y Williamson")
        title.scale(1.2)  
        title.to_edge(UP,buff=1)  
        
        equation = MathTex(r"\max \sum_{\text{aristas}(i, j)} \frac{1 - x_i x_j}{2}")
        equation.scale(0.9) 
        equation.next_to(title, DOWN, buff=0.3)  
        
        condition = MathTex(r"x_i \in \{-1, 1\}")
        condition.scale(0.9)  
        condition.next_to(equation, DOWN, buff=0.2)  
        
        self.play(FadeIn(title),
                  Write(equation),
                  Write(condition))
        self.wait(2)
        
        line = Line(start=condition.get_left() + UP * 0.1, end=condition.get_right() + UP * 0.1)
        condition02 = MathTex(r"x_i \in \mathbb{R}^n, \left\| x_i \right\| = 1")
        condition02.scale(0.9)  
        condition02.next_to(condition, DOWN, buff=0.2)  
        self.play(Write(condition02),Create(line))
        self.wait(2)
        
        axes = Axes(
            x_range=[-1.1, 1.1],
            y_range=[-1.1, 1.1],
            axis_config={"color": GRAY},
        ).scale(0.5)  
        
        circle = Circle(radius=1, color=BLUE)
        circle.scale(1)  
        
        vector = Arrow(start=axes.c2p(0, 0), end=axes.c2p(0.30, 0), buff=0, color=RED)
        vector_group = VGroup(axes, circle, vector)
        vector_group.next_to(condition02, DOWN, buff=0.3) 
        vector_group.shift(DOWN * 0.2)  
        
        self.play(Create(vector_group))
        self.wait(1)
        
        def normalize_to_circle(x, y):
            norm = np.sqrt(x**2 + y**2)
            return x/norm, y/norm
        
        positions = [
            (0.5, 0),       # Eje x positivo
            (0.4, 0.3),     # Primer cuadrante
            (-0.4, 0.4),    # Segundo cuadrante
            (-0.5, 0),      # Eje x negativo
            (-0.4, -0.3),   # Tercer cuadrante
            (0.4, -0.4),    # Cuarto cuadrante
        ]
        for x, y in positions:
            end_point = axes.c2p(x,  y)  
            self.play(vector.animate.put_start_and_end_on(axes.c2p(0, 0), end_point), run_time=1.5)
            self.wait(0.5)
        
        self.wait(2)
        self.play(FadeOut(vector_group),FadeOut(VGroup(axes, circle, vector)))  
        self.wait(2)

        equationDos = MathTex(r"\max \sum_{\text{aristas}(i, j)} \frac{1 - x_i^Tx_j}{2}")
        equationDos.scale(0.9) 
        equationDos.next_to(title, DOWN, buff=0.3) 

        self.play(Transform(equation, equationDos))
        self.wait(2)


        equationTres = MathTex(r"X=\left[x_i^T\:x_j\right]_{i,\:j}")
        equationTres.next_to(condition, DOWN, buff=2)  
        self.play(FadeIn(equationTres))
        self.wait(2)

        self.play(FadeOut(equationTres),
            FadeOut(line),
            FadeOut(equation),
            FadeOut(condition),
            FadeOut(condition02))

        expressionDos = MathTex(
            r"\max \sum_{\text{aristas}} \frac{1 - X_{ij}}{2} \\",
            r"X \in \mathbb{R}^{n \times n} \\",
            r"X \succeq 0, \\",
            r"X_{ii} = 1, \; i = 1, \ldots, n \\",
            r"X = \left[x_1 \ldots x_n\right]\left[x_1 \ldots x_n\right]^T"
        )
        expressionDos.move_to(ORIGIN)

        self.play(Write(expressionDos))
        self.wait(2)
