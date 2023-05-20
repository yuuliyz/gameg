from pygame import *
init()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

game = True
update = True
win_height = 500
win_width = 700
FPS = 60
clock = time.Clock()

background = transform.scale(image.load('image.jpg'), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_width, sprite_height, sprite_speed):
        super().__init__()
        self.width = sprite_width
        self.height = sprite_height
        self.image = transform.scale(image.load(sprite_image), (sprite_width, sprite_height))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = sprite_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y += self.speed
        if keys[K_DOWN]:
            self.rect.y -= self.speed
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed

app = QApplication([])
scene = QWidget()
scene.resize(900, 700)
scene.setWindowTitle('игра')

button1 = QPushButton('начать игру')
button2 = QPushButton('настройки')
button3 = QPushButton('ааааа')

main_line = QVBoxLayout()
main_line.addWidget(button1, alignment = Qt.AlignCenter)
main_line.addWidget(button2, alignment = Qt.AlignCenter)
main_line.addWidget(button3, alignment = Qt.AlignCenter)

scene.setLayout(main_line)

def start_game():
    window = display.set_mode((win_width, win_height))
    display.set_caption('buhf')
    while game:
        for e in event.get():
            if e.type == QUIT:
                game == False
        if update:
            window.blit(background, (0, 0))


        display.update()
        clock.tick(FPS)

button1.clicked.connect(start_game)


scene.show()
app.exec_()
