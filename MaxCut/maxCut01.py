from manim import *
import random


class MaxCut(Scene):
    def construct(self):
        nodo_i = Circle(color=BLUE, radius=0.5).shift(LEFT)
        nodo_j = Circle(color=RED, radius=0.5).shift(RIGHT)

        etiqueta_i = Text("i", color=WHITE).move_to(nodo_i.get_center())
        etiqueta_j = Text("j", color=WHITE).move_to(nodo_j.get_center())

        arista = Line(nodo_i.get_right(), nodo_j.get_left(), color=WHITE)
        texto_1 = Tex(r"$x_ix_j = 1$").shift(DOWN)

        self.play(Create(nodo_i), Create(etiqueta_i), Create(nodo_j), Create(etiqueta_j), Create(arista), Write(texto_1))
        self.wait(2)

        # Slide 02
        self.play(nodo_i.animate.set_color(RED), nodo_j.animate.set_color(BLUE))
        texto_2 = Tex(r"$x_ix_j = -1$").shift(DOWN)
        self.play(Transform(texto_1, texto_2))
        self.wait(2)
        
        # Slide 03
        texto_3 = Tex(r"$\frac{1-x_ix_j}{2} = \begin{cases} 1 & \text{si } x_i \neq x_j \\ 0 & \text{si } x_i = x_j \end{cases}$").shift(DOWN * 1.5)
        self.play(Transform(texto_1, texto_3))
        self.wait(2)
        
        # Slide 04: Graficar cinco nodos en cuadrícula
        self.play(FadeOut(nodo_i), FadeOut(etiqueta_i), FadeOut(nodo_j), FadeOut(etiqueta_j), FadeOut(arista))

         # Desplazamiento hacia arriba
        desplazamiento_vertical = UP * 1  # Ajusta el valor según sea necesario

        # Definir nodos con el desplazamiento
        nodos = [
            Circle(color=RED, radius=0.3).shift(LEFT * 2 + UP + desplazamiento_vertical),  # Nodo 1
            Circle(color=RED, radius=0.3).shift(LEFT * 2 + 0 + desplazamiento_vertical),   # Nodo 0
            Circle(color=RED, radius=0.3).shift(LEFT * 2 + DOWN + desplazamiento_vertical),  # Nodo 2
            Circle(color=BLUE, radius=0.3).shift(RIGHT * 2 + UP + desplazamiento_vertical),  # Nodo 3
            Circle(color=BLUE, radius=0.3).shift(RIGHT * 2 + DOWN + desplazamiento_vertical),# Nodo 4
        ]

        # Crear etiquetas en la nueva posición
        etiquetas = [Text(str(i), color=WHITE).move_to(nodo.get_center()) for i, nodo in enumerate(nodos)]

        # Definición del radio
        radio = 0.3

        # Definir aristas con los nodos desplazados
        aristas = [
            Line(nodos[0].get_center() + DOWN * radio, nodos[1].get_center() + UP * radio, color=WHITE),
            Line(nodos[1].get_center() + DOWN * radio, nodos[2].get_center() + UP * radio, color=WHITE),
            Line(nodos[2].get_center() + RIGHT * radio, nodos[4].get_center() + LEFT * radio, color=GREEN),
            Line(nodos[0].get_center() + RIGHT * radio, nodos[3].get_center() + LEFT * radio, color=GREEN),
            Line(nodos[0].get_center() + RIGHT * radio, nodos[4].get_center() + LEFT * radio, color=GREEN),  # 0-4
            Line(nodos[3].get_center() + DOWN * radio, nodos[4].get_center() + UP * radio, color=WHITE),      # 3-4
        ]

        # Mostrar nodos y etiquetas
        self.play(*[Create(nodo) for nodo in nodos])
        self.play(*[Write(etiqueta) for etiqueta in etiquetas])
        self.wait(1)

        # Mostrar aristas
        self.play(*[Create(arista) for arista in aristas])
        self.wait(2)

        # Slide 05: Función de corte
        self.play(FadeOut(texto_1))

        texto_4 = MathTex(
            r"\text{Corte}", r"&=", r"\sum_{\text{aristas}(i, j)}", r"\frac{1 - x_i x_j}{2}",
        ).shift(DOWN * 1.5)
        
        self.play(Write(texto_4))
        self.wait(2)

        # Slide 06: Expresión Max-Cut
        texto_6 = MathTex(
            r"\text{Max-Cut}", r"&=", r"\max", r"\sum_{\text{aristas}(i, j)}", r"\frac{1 - x_i x_j}{2}"
        ).shift(DOWN * 1.5)
        
        # Transición a Slide 06
        self.play(
            TransformMatchingTex(
                texto_4, texto_6,
                key_map={
                    r"\text{Cut}": r"\text{Max-Cut}",
                }
            )
        )
        self.wait(2)
        
        # Dejar todo en negro
        # Quitar todos los elementos (hacer FadeOut)
        self.play(
            *[FadeOut(nodo) for nodo in nodos],
            *[FadeOut(etiqueta) for etiqueta in etiquetas],
            *[FadeOut(arista) for arista in aristas],
            FadeOut(texto_6)
        )
        self.wait(1)
        
