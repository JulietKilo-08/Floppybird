import pygame
import pygame_gui
import random
import sys

pygame.init()

pygame.display.set_caption('RACER')
aken = pygame.display.set_mode([800, 600])
manager = pygame_gui.UIManager([800, 600])
läbipaist = (0, 0, 0, 0)
t_auto = pygame.image.load("traktor.png")
a_auto = pygame.image.load("auto.png")
k_auto = pygame.image.load("traktor.png")
taust = pygame.image.load("taust.png")
vaenT = pygame.image.load("hein.png")
vaenA = pygame.image.load("vaenA.png")
vaenK = pygame.image.load("VaenK.jpg")
taustx= 0
tausty= 0
class MängijaT(object):
    def __init__(self):
        self.x = 80
        self.y = 60
        self.vx = 0
        self.vy = 0
        self.img = pygame.image.load("traktor.png")
    def uuenda(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
class MängijaA:
    def __init__(self):
        self.x = 80
        self.y = 60
        self.vx = 0
        self.vy = 0
        self.img = pygame.image.load("auto.png")
    def uuenda(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
class MängijaK:
    def __init__(self):
        self.x = 80
        self.y = 60
        self.vx = 0
        self.vy = 0
        self.img = pygame.image.load("traktor.png")
    def uuenda(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
class VaenlaneT:
    def __init__(self):
        self.x = 0
        self.y = random.uniform(0, 640)
        self.vx = random.uniform(1, 2)
        self.vy = 0
        self.img = pygame.image.load("hein.png")
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if(self.x > 640):
            self.die()
    def die(self):
        self.y = random.uniform(0, 480)
        self.x = 0
        self.vy = random.uniform(1, 2)
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])            
class VaenlaneA:
    def __init__(self):
        self.x = 0
        self.y = random.uniform(0, 640)
        self.vx = random.uniform(1, 2)
        self.vy = 0
        self.img = pygame.image.load("vaenA.png")
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if(self.y > 640):
            self.die()
    def die(self):
        self.y = random.uniform(0, 480)
        self.x = 0
        self.vy = random.uniform(1, 2)
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])        
class VaenlaneK:
    def __init__(self):
        self.x = 0
        self.y = random.uniform(0, 640)
        self.vx = random.uniform(1, 2)
        self.vy = 0
        self.img = pygame.image.load("VaenK.jpg")
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if(self.y > 640):
            self.die()
    def die(self):
        self.y = random.uniform(0, 480)
        self.x = 0
        self.vy = random.uniform(1, 2)
    def draw(self, s):
        s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])    
start = pygame_gui.elements.UIButton(pygame.Rect((350, 275), (125, 50)),
                                         'Alusta mängu', 
                                         manager) 
autorid = pygame_gui.elements.UIButton(pygame.Rect((10, 10), (75, 50)),
                                         'Autorid', 
                                         manager)
autorids = pygame_gui.elements.UIButton(pygame.Rect((270, 180), (100, 50)),
                                         'Sulge', 
                                         manager)
level2 = pygame_gui.elements.UIButton(pygame.Rect((350, 275), (125, 50)),
                                         'Järgmine Tase:Kiirtee', 
                                         manager)
level3 = pygame_gui.elements.UIButton(pygame.Rect((350, 275), (125, 50)),
                                         'Järgmine Tase:Võidusõidu rada', 
                                         manager) 
kast = pygame_gui.elements.UITextBox("Graafikaga seonduvad ülesanded(mängija ikoon, takistused jms)- Andris, Harald <br> Helidega seonduvad ülesanded(mängu alguse intro, taustamuusika jms)- Mikk <br> Koodiga seonduvad ülesanded(base code, klassid jms)- Kevin, Joosep", pygame.Rect((75,50), (200, 180)), manager)
version = pygame_gui.elements.UITextBox("VER 0.1<br>Muudetud:<br>-Vastased nüüd lendavad horizontaalselt... loodetavasti <br>ma ei saa proovida <br>seda veel, nupp ei tööta", pygame.Rect((600,10), (200, 180)), manager)
trakt = MängijaT()
auto = MängijaA()
speed = MängijaK()
vaenlasedT = [VaenlaneT() for _ in range(10)]
vaenlasedA = [VaenlaneA() for _ in range(10)]
vaenlasedK = [VaenlaneK() for _ in range(10)]
Tükid = []
kast.hide()
autorids.hide()
level2.hide()
level3.hide()
kell = pygame.time.Clock()
kiirus = 5
mäng_töötab = True
naita = True

while mäng_töötab: 
    dt = kell.tick() / 1000
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            mäng_töötab = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.LEFT:
                trakt.vy += -kiirus
                auto.vy += -kiirus
                speed.vy += -kiirus
            if e.key == pygame.RIGHT:
                trakt.vy += kiirus
                auto.vy += -kiirus
                speed.vy += -kiirus
        elif e.type == pygame.USEREVENT: 
            if e.user_type == pygame_gui.UI_BUTTON_PRESSED: 
                if e.ui_element == start: 
                    start.hide()
                    version.hide()
                    autorid.hide()
                    trakt.draw(aken)
                    pygame.image.load("rohi.png")
                    naita = True
                    if naita:
                        aken.blit(VaenlaneT(), VaenlaneT().Rect)
                    if level2:
                        naita = False
                if e.ui_element == level2: 
                    level2.hide()
                    MängijaA.draw(aken)
                    pygame.image.load("maantee.png")
                    level2 = True
                    if level2:
                        screen.blit(VaenlaneA(), VaenlaneA().Rect)
                    if level3:
                        level2 = False
                if e.ui_element == level3: 
                    level3.hide()
                    MängijaK.draw(aken)
                    pygame.image.load("rada.png")
                    level3 = True
                    if level3 == True:
                        aken.blit(VastanK(), VaenlaneK().Rect)
                if e.ui_element == autorid: 
                    kast.show()
                    autorids.show()
                if e.ui_element == autorids:
                    kast.hide()
                    autorids.hide()
    
        manager.process_events(e) 
    trakt.uuenda(dt)
    auto.uuenda(dt)
    speed.uuenda(dt)
    for VaenlaneT in vaenlasedT:
        VaenlaneT.update(dt)
    for VaenlaneA in vaenlasedA:
        VaenlaneA.update(dt)
    for VaenlaneK in vaenlasedK:
        VaenlaneK.update(dt)
    for VaenlaneT in vaenlasedT:
        VaenlaneT.draw(aken)
    for VaenlaneA in vaenlasedA:
        VaenlaneA.draw(aken)
    for VaenlaneK in vaenlasedK:
        VaenlaneK.draw(aken)
    aken.fill([255, 255, 255])
    aken.blit(taust, [taustx, tausty])
    manager.update(dt) 
    manager.draw_ui(aken) 
    pygame.display.flip()

pygame.quit()