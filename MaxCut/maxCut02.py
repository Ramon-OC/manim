from manim import *
import random

class MaxCut(Scene):
    def construct(self):
        radio_nodo = 0.2
        radio = 0.2
        
        def crear_grafica():
            # Definir colores
            colores = [RED, BLUE]
            
            # Definir los nodos con color aleatorio
            nodos = [
                Circle(color=random.choice(colores), radius=radio_nodo).shift(LEFT * 1.5 + UP),
                Circle(color=random.choice(colores), radius=radio_nodo).shift(LEFT * 1.5),
                Circle(color=random.choice(colores), radius=radio_nodo).shift(LEFT * 1.5 + DOWN),
                Circle(color=random.choice(colores), radius=radio_nodo).shift(RIGHT * 1.5 + UP),
                Circle(color=random.choice(colores), radius=radio_nodo).shift(RIGHT * 1.5 + DOWN),
            ]

            # Crear etiquetas con un tamaño de texto más pequeño
            etiquetas = [Text(str(i), color=WHITE, font_size=24).move_to(nodo.get_center()) for i, nodo in enumerate(nodos)]
            
            # Función para definir el color de la arista
            def color_arista(nodo1, nodo2):
                return GREEN if nodo1.color != nodo2.color else WHITE

            # Definir aristas con colores dependientes de los nodos conectados
            aristas = [
                Line(nodos[0].get_center() + DOWN * radio, nodos[1].get_center() + UP * radio, color=color_arista(nodos[0], nodos[1])),
                Line(nodos[1].get_center() + DOWN * radio, nodos[2].get_center() + UP * radio, color=color_arista(nodos[1], nodos[2])),
                Line(nodos[2].get_center() + RIGHT * radio, nodos[4].get_center() + LEFT * radio, color=color_arista(nodos[2], nodos[4])),
                Line(nodos[0].get_center() + RIGHT * radio, nodos[3].get_center() + LEFT * radio, color=color_arista(nodos[0], nodos[3])),
                Line(nodos[0].get_center() + RIGHT * radio, nodos[4].get_center() + LEFT * radio, color=color_arista(nodos[0], nodos[4])),  # 0-4
                Line(nodos[3].get_center() + DOWN * radio, nodos[4].get_center() + UP * radio, color=color_arista(nodos[3], nodos[4])),
            ]

            # Crear los objetos de la gráfica
            grafica = VGroup(*nodos, *etiquetas, *aristas)
            return grafica
        
        texto_principal = MathTex(r"2^n", font_size=36).move_to(ORIGIN)
        descripcion = Text("donde n es el número de nodos", font_size=24).next_to(texto_principal, DOWN)

        titulo = VGroup(
            Text("Algoritmo ingenuo: ", font_size=36),
            texto_principal
        ).arrange(RIGHT)

        # Mostrar las gráficas y el texto
        self.play(Write(titulo))
        self.play(FadeIn(descripcion))

        graficas_list = []
        for _ in range(10):
            graficas = VGroup(
                crear_grafica().scale(0.6).shift(LEFT * 4 + UP * 2),  # Primer fila
                crear_grafica().scale(0.6).shift(ORIGIN + UP * 2),
                crear_grafica().scale(0.6).shift(RIGHT * 4 + UP * 2),
                crear_grafica().scale(0.6).shift(LEFT * 4 + DOWN * 2),  # Segunda fila
                crear_grafica().scale(0.6).shift(ORIGIN + DOWN * 2),
                crear_grafica().scale(0.6).shift(RIGHT * 4 + DOWN * 2)
            )
            
            graficas_list.append(graficas)

            self.play(*[Create(grafica) for grafica in graficas])
            self.wait(1)
            
        self.play(
            FadeOut(titulo),
            FadeOut(descripcion)
        )
        self.wait(1)
        
        # Crear la línea de tiempo centrada entre las dos filas de gráficas
        timeline = Line(start=LEFT * 4, end=RIGHT * 4, color=WHITE).shift(UP * 0.25)
        arrow = Arrow(start=timeline.get_end(), end=timeline.get_end() + RIGHT * 0.5, color=WHITE)
        
        # Crear marcadores
        marker1 = Line(UP * 0.2, DOWN * 0.2, color=BLUE_B).move_to(timeline.get_left() + RIGHT * 2)
        marker2 = Line(UP * 0.2, DOWN * 0.2, color=BLUE_B).move_to(timeline.get_right() - RIGHT * 0.5)
        
        # Crear etiquetas
        label1 = Text("Algoritmo de\nAproximación", font_size=24, color=BLUE_B).next_to(marker1, DOWN, buff=0.3)
        label2 = Text("Algoritmo\nExacto", font_size=24, color=BLUE_B).next_to(marker2, DOWN, buff=0.3)
        
        
        # Crear fórmula matemática centrada debajo de la línea de tiempo
        formula = MathTex(r"\text{Corte} \geq C \text{ Max-Cut}", color=WHITE).scale(1.2).next_to(timeline, DOWN, buff=0.5)
        
        # Agrupar todos los elementos de la línea de tiempo
        timeline_group = VGroup(timeline, arrow, marker1, marker2, label1, label2, formula)
        
        # Centrar todo el grupo entre las dos filas de gráficas
        timeline_group.move_to(ORIGIN)
        
        # Animar
        self.play(Create(timeline), Create(arrow))
        self.play(Create(marker1), Create(marker2))
        self.play(Write(label1), Write(label2))
        
        self.wait(3)

        
        self.play(
            FadeOut(timeline),
            FadeOut(arrow),
            FadeOut(marker1),
            FadeOut(marker2),
            FadeOut(label1),
            FadeOut(label2)
        )

        self.play(Write(formula))
        
        # Mantener la escena
        self.wait(2)
        
        for graficas in graficas_list:
        
            self.play(*[FadeOut(grafica) for grafica in graficas])
            self.wait(1)
            
        self.wait(2)
        
        longTex = Tex(r"""
        \begin{minipage}{0.7\textwidth}
        C es el factor de aproximación. Cuanto más cercano a 1 sea su valor, 
        mejor será el rendimiento del algoritmo de aproximación. Por el 
        contrario, si su valor se aproxima a 0, tiene una peor aproximación.
        \end{minipage}
        """).next_to(formula, DOWN, buff=0.2)
        
        longTex.scale(0.7)

        self.play(FadeIn(longTex))
        
        self.wait(3)

        self.play(
            FadeOut(longTex),
            FadeOut(formula)
        )

        self.wait(3)
