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
class MängijaT:
    def __init_(self):
        self._x = 320
        self._y = 240
        self.vx = 0
        self.vy = 0
        self.img = pygame.image.load(t_auto)
        self.rect = self.image.get_rect()
    def update(self, dt):
        self._x += self.vx * dt
        self._y += self.vy * dt
    def draw(self, s):
        pygame.draw.rect(s,[205,50,0],[self.x - self.size, self.y - self.size, self.size * 2, self.size * 2],0)
    def kokkupõrge(self, b):
        if self.x + self.img.get_width() > b.x > self.x - self.img.get_width():
            if self.y + self.img.get_height() > b.y > self.y - self.img.get_height():
                tükid.extend([tükk(self.x, self.y) for _ in range(10)])
                self.die()
    def die(self):
        self.y = 0
        self.x = random.uniform(0, 640)
        self.vy = random.uniform(1, 2)
class MängijaA:
    def __init_(self):
        self.x = 320
        self.y = 240
        self.vx = 0
        self.vy = 0
        self.img = pygame.image.load(a_auto)
    def uuenda(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
    def draw(self, s):
        pygame.draw.rect(s,[205,50,0],[self.x - self.size, self.y - self.size, self.size * 2, self.size * 2],0)
    def kokkupõrge(self, b, tükid):
        if self.x + self.img.get_width() > b.x > self.x - self.img.get_width():
            if self.y + self.img.get_height() > b.y > self.y - self.img.get_height():
                tükid.extend([tükk(self.x, self.y) for _ in range(10)])
                self.die()
class MängijaK:
    def __init_(self):
        self.x = 320
        self.y = 240
        self.vx = 0
        self.vy = 0
        self.img = pygame.image.load(k_auto)
    def uuenda(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
    def draw(self, s):
        pygame.draw.rect(s,[205,50,0],[self.x - self.size, self.y - self.size, self.size * 2, self.size * 2],0)
    def kokkupõrge(self, b, tükid):
        if self.x + self.img.get_width() > b.x > self.x - self.img.get_width():
            if self.y + self.img.get_height() > b.y > self.y - self.img.get_height():
                tükid.extend([tükk(self.x, self.y) for _ in range(10)])
                self.die()
                    
class VaenlaneT:
    def __init__(self):
        self.x = random.uniform(0, 640)
        self.y = 0
        self.vx = 0
        self.vy = random.uniform(1, 2)
        self.img = pygame.image.load("hein.png")
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if(self.y > 480):
            self.die()
class VaenlaneA:
    def __init__(self):
        self.x = random.uniform(0, 640)
        self.y = 0
        self.vx = 0
        self.vy = random.uniform(1, 2)
        self.img = pygame.image.load("vaenA.png")
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if(self.y > 480):
            self.die()
class VaenlaneK:
    def __init__(self):
        self.x = random.uniform(0, 640)
        self.y = 0
        self.vx = 0
        self.vy = random.uniform(1, 2)
        self.img = pygame.image.load("VaenK.jpg")
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if(self.y > 480):
            self.die()
    
start = pygame_gui.elements.UIButton(pygame.Rect((350, 275), (125, 50)),
                                         'Alusta mängu', 
                                         manager) 
autorid = pygame_gui.elements.UIButton(pygame.Rect((10, 10), (75, 50)),
                                         'Autorid', 
                                         manager)
autorids = pygame_gui.elements.UIButton(pygame.Rect((310, 140), (100, 50)),
                                         'Sulge', 
                                         manager)
level2 = pygame_gui.elements.UIButton(pygame.Rect((350, 275), (125, 50)),
                                         'Järgmine Tase:Kiirtee', 
                                         manager)
level3 = pygame_gui.elements.UIButton(pygame.Rect((350, 275), (125, 50)),
                                         'Järgmine Tase:Võidusõidu rada', 
                                         manager) 
kast = pygame_gui.elements.UITextBox("Graafikaga seonduvad ülesanded(mängija ikoon, takistused jms)- Andris, Harald <br> Helidega seonduvad ülesanded(mängu alguse intro, taustamuusika jms)- Mikk <br> Koodiga seonduvad ülesanded(base code, klassid jms)- Kevin, Joosep", pygame.Rect((120,140), (200, 180)), manager)
trakt = MängijaT()
auto = MängijaA()
speed = MängijaK()
vaenlasedT = [VaenlaneT() for _ in range(10)]
vaenlasedA = [VaenlaneA() for _ in range(10)]
vaenlasedK = [VaenlaneK() for _ in range(10)]
Tükid = []
kast.hide()
autorids.hide()

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
                    autorid.hide()
                    MängijaT.draw(aken)
                    pygame.image_load("rohi.png")
                    naita = True
                    if naita:
                        screen.blit(VastaneT(), VastaneT().Rect)
                    if level2:
                        naita = False
                if e.ui_element == level2: 
                    level2.hide()
                    MängijaA.draw(aken)
                    pygame.image_load("maantee.png")
                    level2 = True
                    if level2:
                        screen.blit(VastaneA(), VastaneA().Rect)
                    if level3:
                        level2 = False
                
                if e.ui_element == level3: 
                    level3.hide()
                    MängijaK.draw(aken)
                    pygame.image_load("rada.png")
                    level3 = True
                    if level3 == True:
                        screen.blit(VastanK(), VastaneK().Rect)
                if e.ui_element == autorid: 
                    kast.show()
                    autorids.show()
                if e.ui_element == autorids:
                    kast.hide()
                    autorids.hide()
    

        manager.process_events(e) #manager töötleb sündmusi
    trakt.update(dt)
    auto.update(dt)
    speed.update(dt)
    for VaenlaneT in vaenlased:
        VaenlaneT.update(dt)
    for VaenlaneA in vaenlased:
        VaenlaneA.update(dt)
    for VaenlaneK in vaenlased:
        VaenlaneK.update(dt)
    for Tükk in tükid:
        Tükk.update(aken)
    for VaenlaneT in vaenlased:
        VaenlaneT.draw(aken)
    for VaenlaneA in vaenlased:
        VaenlaneA.draw(aken)
    for VaenlaneK in vaenlased:
        VaenlaneK.draw(aken)
    aken.fill([255, 255, 255])
    aken.blit(taust, [taustx, tausty])
    manager.update(dt) # manager uuendab sündmusi
    manager.draw_ui(aken) # manager joonistab UI elemendid aknasse
    pygame.display.flip()

pygame.quit()