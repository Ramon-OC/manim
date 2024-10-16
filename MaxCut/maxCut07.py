import numpy as np
from manim import *

class MaxCut(Scene):
    def construct(self):

        # añadir informacion
        titulo = MathTex(r"\mathbb{P}\left(etiqueta\:x_i\:\ne \:etiqueta\:x_j\right)", color=WHITE).to_edge(UL).shift(LEFT)
        titulo.scale(0.7)  # Scaled down slightly

        nodo_i = Circle(color=WHITE, radius=0.5).next_to(titulo, DOWN, buff=0.5).scale(0.6)
        etiqueta_i = Text("j", color=WHITE).move_to(nodo_i.get_center()).scale(0.6)

        nodo_j = Circle(color=WHITE, radius=0.5).next_to(nodo_i, LEFT, buff=0.5).scale(0.6)
        etiqueta_j = Text("i", color=WHITE).move_to(nodo_j.get_center()).scale(0.6)

        arista = Line(nodo_j.get_right(), nodo_i.get_left(), color=WHITE)


        self.play(Create(titulo),
            Create(nodo_i),
            Create(etiqueta_i),
            Create(nodo_j),
            Create(etiqueta_j),
            Create(arista))
        self.wait(2)


        # circulo con la etiquetas, vectores y 
        circle = Circle(radius=3).move_to(ORIGIN)
        dashed_line = DashedLine(start=3.5*LEFT, end=3.5*RIGHT,color=GREEN)
        dashed_line.rotate(45 * DEGREES) 

        vec_1 = Vector([0, -3])
        vec_2 = Vector([-3, 0])

        labelArrow01 = MathTex(r"x_{i}", color=WHITE).scale(1.2).next_to(vec_1, DOWN, buff=0.5)
        labelArrow02 = MathTex(r"x_{j}", color=WHITE).scale(1.2).next_to(vec_2, LEFT, buff=0.5)

        self.play(Create(circle),
            Create(dashed_line),
            Create(vec_1),
            Create(vec_2),
            Create(labelArrow01),
            Create(labelArrow02))

        self.wait(2)

        # se añade el angulo entre las dos flechas
        angle = Arc(
            radius=1.2,  # Radio del arco que representa el ángulo
            start_angle=vec_2.get_angle(),  # Ángulo inicial basado en vec_1
            angle=PI/2,  # El ángulo entre los dos vectores es de 90 grados (PI/2 radianes)
            color=BLUE
        )
        # Etiqueta del ángulo
        angle_label = MathTex(r"\theta _{i,\:j}", color=WHITE).scale(1.2).move_to(1.8*LEFT + 0.5*DOWN)
        angle_label.scale(0.7)  # Scaled down slightly


        self.play(Create(angle),
            Create(angle_label))

        self.wait(2)


        # Añadir un sombreado rojo a los extremos
        shaded_area01 = Sector(
            outer_radius=3,
            angle=PI/2,
            start_angle=2*PI/2,
            color=RED,
            fill_opacity=0.3
        )

        shaded_area02 = Sector(
            outer_radius=3,
            angle=PI/2,
            start_angle=4*PI/2,
            color=RED,
            fill_opacity=0.3
        )

        self.play(Create(shaded_area01),Create(shaded_area02))
        self.wait(1)


        shaded_area03 = Sector(
            outer_radius=3,
            angle=PI/2,
            start_angle=3*PI/2,
            color=BLUE,
            fill_opacity=0.3
        )

        shaded_area04 = Sector(
            outer_radius=3,
            angle=PI/2,
            start_angle=PI/2,
            color=BLUE,
            fill_opacity=0.3
        )


        self.play(Create(shaded_area03),Create(shaded_area04))
        self.play(Rotate(dashed_line, angle=90 * DEGREES, run_time=1))
        self.wait(2)

        self.play(FadeOut(shaded_area03),
            FadeOut(shaded_area01),
            FadeOut(shaded_area02),
            FadeOut(shaded_area04),
            FadeOut(dashed_line),
            FadeOut(angle),
            FadeOut(angle_label),
            FadeOut(circle),
            FadeOut(dashed_line),
            FadeOut(vec_1),
            FadeOut(vec_2),
            FadeOut(labelArrow01),
            FadeOut(labelArrow02),
            FadeOut(nodo_i),
            FadeOut(etiqueta_i),
            FadeOut(nodo_j),
            FadeOut(etiqueta_j),
            FadeOut(arista))



        titulo02 = MathTex(r"\mathbb{P}\left(etiqueta\:x_i\:\ne \:\:etiqueta\:x_j\right)=\frac{\theta _{i,\:j}}{\pi}", color=WHITE)
        titulo02.to_edge(UP, buff=1)
        self.play(Transform(titulo, titulo02))
        self.wait(1)


        formula02 = MathTex(r"\mathbb{E}[\mathrm{Corte}] = \sum_{\text{arista }(i, j)} \frac{\theta_{ij}}{\pi} \ \text{vs} \ \sum_{\text{aristas}} \frac{1 - x_i^T x_j}{2}")
        formula02.next_to(titulo02, DOWN)
        self.play(FadeIn(formula02))
        self.wait(2)
 
        formula03 = MathTex(r"\frac{\theta_{i j}}{\pi} \quad \frac{1-{x_i}^T x_j}{2}")
        formula03.next_to(formula02, DOWN,buff=1.5)
        self.play(FadeIn(formula03))
        self.wait(2)

        formula041 = MathTex(r"\frac{\theta_{i j}}{\pi} ")
        formula042 = MathTex(r"\frac{1-cos({\theta _{i,\:j}})}{2}")
        formula042.next_to(formula02, DOWN,buff=1.5)
        formula042.shift(LEFT * 2)
        formula041.next_to(formula042, LEFT)

        self.play(FadeOut(formula03))
        self.play(FadeIn(formula041),FadeIn(formula042))

        self.wait(2)

        # Colocar formula042 debajo de formula041
        formula042.next_to(formula041, DOWN)

        # Crear una línea horizontal entre los extremos inferiores de formula041 y formula042
        divider_line = Line(
            start=formula041.get_left(),  # Inicio en el extremo izquierdo de formula041
            end=formula041.get_right()    # Fin en el extremo derecho de formula041
        )

        # Ajustar el ancho de la línea al ancho de formula041 (o formula042 si es mayor)
        divider_line.scale_to_fit_width(max(formula041.width, formula042.width))
        self.play(
            formula041.animate.shift(UP),
            formula042.animate.next_to(formula041, DOWN),
            Create(divider_line)
        )

        self.wait(2)


        # Crear los ejes y la gráfica
        axes = Axes(
            x_range=[0, 4, 1],  # Rango ajustado del eje x
            y_range=[0, 1.5, 0.5],  # Rango ajustado del eje y
            axis_config={"color": WHITE},
            tips=False  # Ocultar las flechas en los extremos de los ejes
        ).add_coordinates()

        labels = axes.get_axis_labels(x_label=MathTex(r"\theta"), y_label=MathTex(r"y"))

        def limited_function(theta):
            value = (theta / np.pi) / ((1 - np.cos(theta)) / 2)
            return min(max(value, 0), 1.5)  # Limitar entre 0 y 1.5



        # Definir la función
        graph = axes.plot(
            limited_function,

            x_range=[0.9, 3.8],  # Limitar el rango x para evitar que se salga del área visible

            color=WHITE
        )

        # Añadir etiquetas de puntos de interés
        point_theta = 2.34
        point_y = (point_theta / np.pi) / ((1 - np.cos(point_theta)) / 2)
        dot = Dot(axes.coords_to_point(point_theta, point_y), color=YELLOW)
        

        # Añadir las líneas punteadas
        h_line = DashedLine(start=axes.c2p(0, point_y), end=axes.c2p(point_theta, point_y), color=YELLOW)
        v_line = DashedLine(start=axes.c2p(point_theta, 0), end=axes.c2p(point_theta, point_y), color=YELLOW)

        theta_label = MathTex(r"2.34\dots").next_to(v_line, DOWN)
        y_label = MathTex(r"0.87\dots").next_to(h_line, LEFT)

        # Agrupar todos los elementos de la gráfica
        axes_group = VGroup(axes, graph, labels, dot, theta_label, y_label, h_line, v_line)

        # Ajustar el tamaño de la gráfica y colocarla en la esquina inferior derecha
        axes_group.scale(0.5)  # Reducir el tamaño de la gráfica
        axes_group.to_corner(DR)  # Posicionarla en la esquina inferior derecha

        # Colocar todo en la escena
        self.play(Create(axes), Write(labels),Create(graph),Create(dot), Write(theta_label), Write(y_label),Create(h_line), Create(v_line))
        self.wait(2)

        finala = MathTex(r"\ge 0.87857",color=BLUE).next_to(divider_line, RIGHT)
        finala.scale(0.5)
        self.play(Write(finala))
        self.wait(2)
