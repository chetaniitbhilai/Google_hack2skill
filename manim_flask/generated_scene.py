
from manim import *

class GeneratedScene(MovingCameraScene):
    def get_final_camera_setup(self):
        # Create all mobjects first
        title = Tex(r"Convention for Empty Index Sets", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title

        element0 = Tex(r"If the index set $I$ is empty, we make the convention that $\bigcup_{i \in I} E_i = \phi$ and $\bigcap_{i \in I} E_i = \Omega$.", font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r"The main reason for this rather surprising convention is that the unions become larger with inclusion of more sets, whereas the intersections become smaller.", font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r"For example, if $I_1$ and $I_2$ are two nonempty index sets, $I_1 \subset I_2$ then $\bigcap_{i \in I_1} E_i \supseteq \bigcap_{i \in I_2} E_i$.", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r"Hence the smallest possible index set, i.e. $\phi$ should lead to the largest intersection, i.e., $\Omega$.", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r"This convention is also consistent with De-Morgan's laws.", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

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

        element0 = Tex(r"If the index set $I$ is empty, we make the convention that $\bigcup_{i \in I} E_i = \phi$ and $\bigcap_{i \in I} E_i = \Omega$.", font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r"The main reason for this rather surprising convention is that the unions become larger with inclusion of more sets, whereas the intersections become smaller.", font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r"For example, if $I_1$ and $I_2$ are two nonempty index sets, $I_1 \subset I_2$ then $\bigcap_{i \in I_1} E_i \supseteq \bigcap_{i \in I_2} E_i$.", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r"Hence the smallest possible index set, i.e. $\phi$ should lead to the largest intersection, i.e., $\Omega$.", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r"This convention is also consistent with De-Morgan's laws.", font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

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

        self.wait(2)
