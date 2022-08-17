from gl import Renderer, V3, color
from obj import Texture
from shaders import *

width = 960
height = 540


rend = Renderer(width, height)

modelo = 'model.obj'
escala = V3(4,4,4)
traslacion = V3(2,0,-9)
rotacion = V3(0,0,0)

rend.active_texture = Texture('model.bmp')
rend.active_shader = toon
rend.glLoadModelShade(modelo, escala, traslacion, rotacion)
rend.glFinish("lab2_muestras/toon.bmp")

#rend.active_texture = Texture('model.bmp')
#rend.active_shader = NightVision
#rend.glLoadModelShade(modelo, escala, traslacion, rotacion)
#rend.glFinish("lab2_muestras/NightVision.bmp")

#rend.active_texture = Texture('model.bmp')
#rend.active_shader = MotherRussia
#rend.glLoadModelShade(modelo, escala, traslacion, rotacion)
#rend.glFinish('lab2_muestras/MotherRussia.bmp')

#rend.active_texture = Texture('model.bmp')
#rend.active_shader = ShuffleColor
#rend.glLoadModelShade(modelo, escala, traslacion, rotacion)
#rend.glFinish('lab2_muestras/ShuffleColor.bmp')

