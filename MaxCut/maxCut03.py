from manim import *

class MaxCut(Scene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)  

        plane = Surface(lambda u, v: np.array([u, v, 0]),
                        u_range=[-2, 2], v_range=[-2, 2],
                        fill_opacity=0.5, color=GREEN)
        plane.rotate(PI / 3, axis=Y_AXIS).rotate(PI / 3, axis=X_AXIS)

        center = ORIGIN
        vectors = [
            Arrow3D(center, [-1, -1, -1], color=BLUE),
            Arrow3D(center, [-1.5, -0.5, 1], color=BLUE),
            Arrow3D(center, [1.5, -0.5, -1], color=RED),
            Arrow3D(center, [-1, 1.5, -1], color=BLUE),
            Arrow3D(center, [2, 1., 0], color=RED),
        ]

        # ortientación de la camara
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # anima los vectores
        for vec in vectors:
            self.add(vec)
        self.play(*[Create(vec) for vec in vectors])
        self.wait(2) 

        self.add(plane)
        self.play(Create(plane))
        self.wait(2)  

        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=2)
        self.wait(1)  

        nodo_rojo = Circle(color=RED, radius=0.5).to_edge(DOWN, buff=1).shift(RIGHT * 3)
        etiqueta_rojo = Text("i", color=WHITE).move_to(nodo_rojo.get_center())
        etiqueta_valor01 = Text("-1", color=RED).next_to(nodo_rojo, UP, buff=0.5)
        equation01 = MathTex(r"si\:u^T\:x_i<\:0", font_size=48).next_to(nodo_rojo, RIGHT, buff=0.5)

        nodo_azul= Circle(color=BLUE, radius=0.5).to_edge(UP, buff=1).shift(LEFT * 6)
        etiqueta_azul = Text("i", color=WHITE).move_to(nodo_azul.get_center())
        etiqueta_valor02 = Text("1", color=BLUE).next_to(nodo_azul, DOWN, buff=0.5)
        equation02 = MathTex(r"si\:u^T\:x_i\ge 0", font_size=48).next_to(nodo_azul, RIGHT, buff=0.5)

        equation03 = MathTex(r"u \sim \mathcal{N}(0, I)", font_size=48).to_edge(DOWN, buff=1).shift(LEFT * 3)

        self.play(Write(nodo_azul), 
            Write(etiqueta_azul), 
            Write(equation02),
            Write(nodo_rojo),
            Write(etiqueta_rojo), 
            Write(equation01),
            Write(etiqueta_valor02),
            Write(etiqueta_valor01),
            Write(equation03))

        self.wait(2)
