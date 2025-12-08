from manim import *


class AreaBajoCurva(Scene):
    def construct(self):
        # Título (menos grande y bien alineado)
        title = Title("El área bajo la curva (Integración)").scale(0.85).to_edge(UP)
        subtitle = Text("Aproximación por sumas de Riemann y límite → integral", font_size=22)
        subtitle.next_to(title, DOWN, buff=0.12)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=DOWN))
        # Ahora usamos audios segmentados y sincronizamos cada bloque con su narración
        # Los archivos se generaron con generate_audio_segments.py y están en el proyecto
        self.wait(0.6)

        # Ejes
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 9, 1],
            x_length=9,
            y_length=4.5,
            tips=True,
        ).to_edge(DOWN)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Función a mostrar: f(x) = 0.5 x^2
        func = lambda x: 0.5 * x ** 2
        graph = axes.plot(func, x_range=[0, 4], color=BLUE)
        graph_label = MathTex(r"f(x)=\tfrac{1}{2}x^2").next_to(graph, UR)

        # Mostrar ejes y curva
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), Write(graph_label))
        self.wait(0.6)

        # Mostrar suma de Riemann con pocas particiones
        riemann_4 = axes.get_riemann_rectangles(graph, x_range=[0, 4], dx=1.0, stroke_width=0.5, fill_opacity=0.6)
        # colocar el texto informativo justo encima del eje (evitar la franja superior)
        texto1 = Text("Suma de Riemann: 4 rectángulos (aprox.)", font_size=22)
        texto1.next_to(axes, UP, aligned_edge=LEFT, buff=0.2)
        # reproducir el audio del título/intro antes de texto1
        self.add_sound("audio_title.mp3")
        self.wait(0.2)
        self.play(FadeIn(texto1), Create(riemann_4))
        # esperar la duración aproximada del audio de la sección introductoria
        self.wait(6.3)

        # Más particiones
        riemann_8 = axes.get_riemann_rectangles(graph, x_range=[0, 4], dx=0.5, stroke_width=0.2, fill_opacity=0.6)
        texto2 = Text("Aumentamos las particiones → mejor aproximación", font_size=20).next_to(texto1, DOWN, buff=0.12)
        # reproducir el audio de riemann_4 justo antes de transformar
        self.add_sound("audio_riemann_4.mp3")
        self.play(FadeOut(texto1), Transform(riemann_4, riemann_8), Write(texto2))
        self.wait(7.95)

        # Muchísimas particiones (transición a área)
        riemann_many = axes.get_riemann_rectangles(graph, x_range=[0, 4], dx=0.1, stroke_width=0.1, fill_opacity=0.6)
        area = axes.get_area(graph, x_range=[0, 4], color=GREEN, opacity=0.5)
        texto3 = Text("En el límite, la suma → integral", font_size=20).next_to(texto2, DOWN, buff=0.12)
        # reproducir audio de riemann_8 cuando mostremos la siguiente transición
        self.add_sound("audio_riemann_8.mp3")
        self.play(FadeOut(texto2), ReplacementTransform(riemann_4, riemann_many), Write(texto3))
        self.wait(4.9)

        # Transformar a área sombreada y mostrar la expresión integral
        integral = MathTex(r"\displaystyle \int_{0}^{4} \tfrac{1}{2}x^2\,dx = \left[\tfrac{1}{6}x^3\right]_0^4 = \tfrac{32}{3} \approx 10.67")
        integral.scale(0.9).to_corner(UR)
        # reproducir audio de 'limit' antes de mostrar la integral
        self.add_sound("audio_limit.mp3")
        self.play(FadeOut(texto3))
        self.wait(6.65)
        # quitar elementos superiores y mostrar integral con su narración
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(graph_label))
        self.add_sound("audio_integral.mp3")
        self.play(Transform(riemann_many, area), FadeIn(integral))
        self.wait(10.55)

        # Explicación corta en español (lista simple compatible)
        items = [
            "La integral mide el área bajo la curva entre a y b.",
            "Las sumas de Riemann usan rectángulos para aproximar esa área.",
            "Al aumentar el número de rectángulos, la aproximación converge a la integral.",
        ]
        explanation_lines = VGroup(*[Text("• "+it, font_size=20) for it in items]).arrange(DOWN, aligned_edge=LEFT)
        explanation = explanation_lines.scale(0.85).to_corner(DL)

        # reproducir explicación más detallada
        self.add_sound("audio_explanation.mp3")
        self.play(FadeIn(explanation, shift=LEFT))
        self.wait(9.3)

        # Despedida / llamado a la acción
        bye = Text("Fin — ¡Prueba con otras funciones y límites!", font_size=26)
        bye.to_edge(UP)
        # eliminar textos que podrían permanecer
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(integral), FadeOut(area), FadeOut(graph_label))
        # despedida con audio
        self.add_sound("audio_bye.mp3")
        self.play(FadeOut(explanation), FadeIn(bye))
        self.wait(4.8)
