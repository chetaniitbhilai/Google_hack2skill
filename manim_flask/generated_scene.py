
from manim import *

class GeneratedScene(MovingCameraScene):
    def get_final_camera_setup(self):
        # Create all mobjects first
        title = Tex(r"Set Theory and Limit Superior/Inferior", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title

        element0 = Tex(r"$(\bigcup_{i \in I} E_i)^c \subset \bigcap_{i \in I} E_i^c$", font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r"Let $I = \phi$. Then the LHS $= \phi^c = X$", font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r"For every $0 < \alpha < 1$, we can find $N \ni \alpha < 1 - \frac{1}{n}$ for all $n \ge N$. This shows that $\alpha \in E_* \implies \alpha \in E^*$", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r"In general $E_* \subset E^*$", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r"Examples: 1. $E_n = (0, 1 + \frac{1}{n}), \quad n = 1, 2, \dots$ Then $E_* = E^* = (0, 1)$. ", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r"2. $E_n = [\frac{1}{n}, 1-\frac{1}{n}], \quad n = 2, 3, \dots$ Then $E_* = E^* = (0, 1)$. ", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r"3. $E_n = \{0, \frac{1}{n}, \frac{2}{n}, \dots, \frac{n-1}{n}, 1\}, \quad n = 1, 2, \dots$ Then $E_* = \{0, 1\}$. Further, any rational number $\frac{p}{q}$ in the interval $(0, 1)$ can be represented as $\frac{pK}{qK}$ for $n = qK, m = pK, K = 1, 2, \dots$. Thus each $\frac{p}{q} \in (0, 1)$ will belong to infinitely many $E_n$'s. So, $E^* = \{\frac{p}{q}: \frac{p}{q} \text{ is a rational in } [0, 1]\}$.", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        element7 = Tex(r"4. Let $E_n = A$ for $n$ even $= B$ for $n$ odd Then $E_* = A \cap B, E^* = A \cup B$.", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element7)
        prev_mobject = element7

        # Group all content elements
        content = VGroup(*content_elements)
        self.add(title)
        title.set_opacity(0)
        self.camera.auto_zoom([title], margin=1)
        current_content = [title]
        for element in content_elements[1:]:
            self.add(element)
            element.set_opacity(0)
            current_content.append(element)
        self.play(
            self.camera.auto_zoom(
                content,
                margin=0.5,
                animate=True
            ).build(),
            run_time=2
        )
        self.camera.frame.save_state()
        self.camera.auto_zoom(content, margin=0.5)
        final_frame_center = self.camera.frame.get_center()
        final_focal_width = self.camera.frame.get_width()
        self.camera.frame.restore()
        return final_frame_center, final_focal_width

    def construct(self):
        # Get the final camera settings from a silent run
        final_center, final_width = self.get_final_camera_setup()
        title = Tex(r"{title}", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title

        element0 = Tex(r"$(\bigcup_{i \in I} E_i)^c \subset \bigcap_{i \in I} E_i^c$", font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r"Let $I = \phi$. Then the LHS $= \phi^c = X$", font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r"For every $0 < \alpha < 1$, we can find $N \ni \alpha < 1 - \frac{1}{n}$ for all $n \ge N$. This shows that $\alpha \in E_* \implies \alpha \in E^*$", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r"In general $E_* \subset E^*$", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r"Examples: 1. $E_n = (0, 1 + \frac{1}{n}), \quad n = 1, 2, \dots$ Then $E_* = E^* = (0, 1)$. ", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r"2. $E_n = [\frac{1}{n}, 1-\frac{1}{n}], \quad n = 2, 3, \dots$ Then $E_* = E^* = (0, 1)$. ", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r"3. $E_n = \{0, \frac{1}{n}, \frac{2}{n}, \dots, \frac{n-1}{n}, 1\}, \quad n = 1, 2, \dots$ Then $E_* = \{0, 1\}$. Further, any rational number $\frac{p}{q}$ in the interval $(0, 1)$ can be represented as $\frac{pK}{qK}$ for $n = qK, m = pK, K = 1, 2, \dots$. Thus each $\frac{p}{q} \in (0, 1)$ will belong to infinitely many $E_n$'s. So, $E^* = \{\frac{p}{q}: \frac{p}{q} \text{ is a rational in } [0, 1]\}$.", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        element7 = Tex(r"4. Let $E_n = A$ for $n$ even $= B$ for $n$ odd Then $E_* = A \cap B, E^* = A \cup B$.", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element7)
        prev_mobject = element7

        content = VGroup(*content_elements)
        self.camera.frame.move_to(final_center)
        self.camera.frame.set_width(final_width)
        self.play(Write(title))
        self.wait(1)

        self.play(Write(element0))
        self.wait(1)

        self.play(Write(element1))
        self.wait(1)

        self.play(Write(element2))
        self.wait(1)

        self.play(Write(element3))
        self.wait(1)

        self.play(Write(element4))
        self.wait(1)

        self.play(Write(element5))
        self.wait(1)

        self.play(Write(element6))
        self.wait(1)

        self.play(Write(element7))
        self.wait(1)

        self.wait(2)
