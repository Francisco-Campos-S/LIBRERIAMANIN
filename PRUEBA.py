from manim import *

class HelloWorld(Scene):
    def construct(self):
        helloWorld = Text("Hello world!")
        self.play(Write(helloWorld))
        self.wait()