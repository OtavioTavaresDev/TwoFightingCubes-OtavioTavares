from ursina import *
from ursina.prefabs.health_bar import HealthBar
import sys

app = Ursina()

p1_vida = HealthBar(max_value=500, bar_color=color.red, parent=camera.ui_camera, position=(-0.5,0.4))
p2_vida = HealthBar(max_value=500, bar_color=color.red, parent=camera.ui_camera, position=(0,0.4))

p1 = Entity(model='cube', color=color.red, position=(-4,-2,0), collider="box")
Sky()
p2 = Entity(model="cube", position=(4, -2, 0), color=color.blue, collider="box")
chao = Entity(model='cube', scale=(30, 0.3, 30), collider="block", color=color.rgb(30, 120, 80), position=(0, -3, 0))

pontos_p1 = 0
ponto_p1 = Text(text=f"{pontos_p1}/5",color=color.black, parent=camera.ui_camera, position =(-0.3, 0.2))
tutorial = Text(text=r"right = A | D = left  | Q W E ", color=color.black, parent=camera.ui_camera, position=(-0.5,-0.1))
tutorial2 = Text(text=r"right = J | L = left  | O I U ", color=color.black, parent=camera.ui_camera, position=(0.2,-0.1))
pontos_p2 = 0
ponto_p2 = Text(text=f"{pontos_p2}/5",color=color.black, parent=camera.ui_camera, position =(0.3, 0.2))

def update():
    global pontos_p1, pontos_p2, ponto_p1, ponto_p2
    if p1_vida.value == 0:
        pontos_p2 += 1
        ponto_p2.text = f"{pontos_p2}/5"
        p1_vida.value += 500
        p2_vida.value += 500
        p1_vida.bar_color = color.red
        p2_vida.bar_color = color.red
        p1.position = (-4,-2,0)
        p2.position = (4, -2, 0)

    if p2_vida.value == 0:
        pontos_p1 += 1
        ponto_p1.text = f"{pontos_p1}/5"
        p1_vida.value += 500
        p2_vida.value += 500
        p2_vida.bar_color = color.red
        p1_vida.bar_color = color.red
        p1.position = (-4,-2,0)
        p2.position = (4, -2, 0)

    if p1_vida.value <= 380:
        p1_vida.bar_color = color.yellow

    if p2_vida.value <= 380:
        p2_vida.bar_color = color.yellow

    if soco1_p1.intersects(p2):
        p2_vida.value -= 10

    if soco2_p1.intersects(p2):
        p2_vida.value -= 20

    if soco3_p1.intersects(p2):
        p2_vida.value -= 30

    if soco1_p2.intersects(p1):
        p1_vida.value -= 10

    if soco2_p2.intersects(p1):
        p1_vida.value -= 20

    if soco3_p2.intersects(p1):
        p1_vida.value -= 30


    if p2.intersects(p1) or p1.intersects(p2):
        pass
    else:
        p1.x += held_keys["d"] * time.dt * 3
    p1.x -= held_keys["a"] * time.dt * 2

    if p1.intersects(p2) or p2.intersects(p1):
        pass
    else:
        p2.x -= held_keys["j"] * time.dt * 3
    p2.x += held_keys["l"] * time.dt * 2

def input(key):
    global collisor_soco_P1, collisor_soco_P2

    if key == "q":
        soco1_p1.position = (0.7,-0.1,0)
        soco1_p1.visible = True
    else:
        soco1_p1.position = (0.7,-14,0)
        soco1_p1.visible = False




    if key == "w":
        soco2_p1.position = (0.9,0.2,0)
        soco2_p1.visible = True
    else:
        soco2_p1.position = (0.9,-15,0)
        soco2_p1.visible = False

    if key == "e":
        soco3_p1.position = (0.92, 0.38,0)
        soco3_p1.visible = True
    else:
        soco3_p1.position = (0.7,-16,0)
        soco3_p1.visible = False

 #^^p1


    if key == "o":
        soco1_p2.position = (-0.5,0.2,0)
        soco1_p2.visible = True
    else:
        soco1_p2.position = (-0.7,20,0)
        soco1_p2.visible = False


    if key == "i":
        soco2_p2.position = (-0.9,0.2,0)
        soco2_p2.visible = True
    else:
        soco2_p2.position = (-0.9,22,0)
        soco2_p2.visible = False

    if key == "u":
        soco3_p2.position = (-0.92,0.38,0)
        soco3_p2.visible = True
    else:
        soco3_p2.position = (-0.7,24,0)
        soco3_p2.visible = False




soco1_p1 = Entity(model='cube', color=color.red, collider="box", parent=p1, position=(0.7,-14,0), scale=(1,0.3,0), visible = False)
soco2_p1 = Entity(model='cube', color=color.red, collider="box", parent=p1, position=(0.8,-15,0), scale=(1,0.3,0), visible = False)
soco3_p1 = Entity(model='cube', color=color.red, collider="box", parent=p1, position=(0.9,-16,0), scale=(1,0.3,0), visible = False)

soco1_p2 = Entity(model='cube', color=color.blue, collider="box", parent=p2, position=(-0.7, 20, 0), scale=(1, 0.3, 0),visible=False)
soco2_p2 = Entity(model='cube', color=color.blue, collider="box", parent=p2, position=(-0.8, 22, 0), scale=(1, 0.3, 0),visible=False)
soco3_p2 =Entity(model='cube', color=color.blue, collider="box", parent=p2, position=(-0.9,24,0), scale=(1,0.3,0), visible = False)


if app:
    app.run()
else:
    sys.exit()
