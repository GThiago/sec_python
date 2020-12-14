import pyglet
import time

window = pyglet.window.Window(400,100)

label = pyglet.text.Label('Error', 
                        font_name='Arial',
                        font_size=40,
                        x=window.width//2, y=window.height//2,
                        anchor_x='center', anchor_y='center')

image = pyglet.image.load('error.png')

@window.event
def on_draw():
    window.clear()
    
    label.draw()
    
    
def main(): 
    pyglet.app.run()
    
if __name__ == "__main__":
    main()