from manim import *

class MaxCut(Scene):
    def construct(self):
        # Crear el texto "Unit Vectors"
        unit_vectors_text = Text("Vectores Unitarios", font_size=30).shift(LEFT*3)
        unit_vector_math = MathTex(r"x_i \in \mathbb{R}^n", font_size=30, color=WHITE).next_to(unit_vectors_text, DOWN)

        scalars_text = Text("Escalares", font_size=30).shift(RIGHT*3)
        scalars_math = MathTex(r"x_i \in \{-1, 1\}", font_size=30, color=WHITE).next_to(scalars_text, DOWN)

        # Crear una flecha entre los dos grupos de texto
        arrow = Arrow(start=unit_vectors_text.get_right(), end=scalars_text.get_left(), buff=0.4, color=RED, stroke_width=6)

        self.play(Write(unit_vectors_text), 
            Write(unit_vector_math),
            Write(scalars_text), 
            Write(scalars_math),
            Create(arrow))

        self.wait(2)

        redondeo = Text("redondeo", font_size=20).next_to(arrow, DOWN)
        self.play(FadeIn(redondeo))
        self.wait(2)
        