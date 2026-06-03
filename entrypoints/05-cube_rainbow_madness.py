
import numpy as np
import urenderer
from OpenGL import GL
from urenderer.node import Node


def update_cube(node: Node, deltaTime: float, time_since_start: float) -> None:
    material: urenderer.renderer.opengl.Material = node.render_data["material"]

    ## SEU CÓDIGO AQUI ######################################################
    # Defina a uniform "time" do material como time_since_start
    material.set_uniform("time", time_since_start)
    #########################################################################

    time_since_start /= 10
    t = time_since_start - int(time_since_start)

    node.rotation[0] = 45
    node.rotation[1] = 360*t
    node.rotation[2] = 0


if __name__ == "__main__":
    urenderer.utils.clear_workdir("05-cube_raindow_madness")
    renderer = urenderer.renderer.OpenGLRenderer(1920, 1080)
    renderer.background_color = np.array([0, 0, 0, 1.0])
    runtime = urenderer.application.Runtime(
        renderer, name="05-cube_raindow_madness")

    shader = urenderer.renderer.Shader(
        "05-vertex.vs", "05-fragment.fs")
    material = urenderer.renderer.opengl.Material(shader)

    ## SEU CÓDIGO AQUI ######################################################
    # Crie vários cubos em posições e escalas aleatórias
    for i in range(10):
        cube = Node()
        cube.translation = np.random.uniform(-5, 5, size=3)
        cube.scale = np.random.uniform(0.1, 0.5, size=3)
        cube.render_data["mesh"] = urenderer.geometry.mesh.get_mesh_cube()
        cube.render_data["material"] = material
        cube.callbacks.append(update_cube)
        runtime.scene.add_child(cube)
    #########################################################################

    runtime.loop(n=4000, capture=np.arange(0, 4000, 40, dtype=np.int32))
    urenderer.utils.image_to_video("05-cube_raindow_madness", fps=30)
    urenderer.utils.clear_workdir("05-cube_raindow_madness", image_only=True)
