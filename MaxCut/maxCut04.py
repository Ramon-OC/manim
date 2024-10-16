
from manim import *

class MaxCut(Scene):
    def construct(self):
        # Crear el nodo azul
        nodo_i = Circle(color=WHITE, radius=0.5).shift(LEFT * 4)
        etiqueta_i = Text("i", color=WHITE).move_to(nodo_i.get_center())

        # Crear la ecuación
        piecewise_function = MathTex(
            r"x_i = "
            r"\begin{cases}"
            r"1 & \text{con probabilidad } 50\% \\"
            r"-1 & \text{con probabilidad } 50\%"
            r"\end{cases}"
        ).next_to(nodo_i, RIGHT, buff=1)

        # Animaciones
        self.play(Create(nodo_i), Write(etiqueta_i))
        self.play(FadeIn(piecewise_function))

        # Mantener la escena en pantalla
        self.wait(2)

        # Quita el texto y agrega un nuevo nodo. 
        self.play(FadeOut(piecewise_function))
        nodo_j = Circle(color=WHITE, radius=0.5).shift(RIGHT * 4)
        etiqueta_j = Text("j", color=WHITE).move_to(nodo_j.get_center())
        arista = Line(nodo_i.get_right(), nodo_j.get_left(), color=WHITE)

        self.play(Create(nodo_j), Write(etiqueta_j),Write(arista))

        # Cambia el texto de abajo
        text01 = Tex(r"El algoritmo probabilístico tiene $\frac{1}{2}$ de probabilidad de que una arista sea parte del corte, y $\frac{1}{2}$ de probabilidad que no sea así.").next_to(arista, DOWN, buff=1.5)
        text01.scale(0.7)
        self.play(FadeIn(text01))
        self.wait(2)


        # Cambia el color de los nodos y la arista 
        self.play(
            nodo_i.animate.set_color(BLUE),
            nodo_j.animate.set_color(RED),
            arista.animate.set_color(GREEN)
        )

        # segunda formula
        secondFormula = MathTex(
            r"\sum_{\text{aristas}} \frac{1}{2} = \frac{1}{2} \# \text{aristas} \geq \frac{1}{2} \text{Max-Cut}"
        ).next_to(arista, DOWN, buff=1.5)
        self.play(FadeOut(text01),FadeIn(secondFormula))
        self.wait(2)

