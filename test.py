# astro game

import pygame

pygame.init()
f1 = pygame.font.Font(None, 30)

mob_run = False
term_exam1 = 0
txt_danger = f1.render('Danger! Reactor critical damage!', True, (255, 0, 0))
txt_goal1 = f1.render('find out what happened    ->    use the console.   [e]', True, (0, 255, 0))
txt_goal2 = f1.render('find out what is the breakdown    ->    go to the reactor.   [e]', True, (0, 255, 0))
txt_goal3 = f1.render('find a replacement part    ->    go to the engineering compartment.   [e]', True, (0, 255, 0))
txt_goal4 = f1.render('honor the rector    ->    go to the reactor.   [e]', True, (0, 255, 0))
txt_goal5 = f1.render('resume flight    ->    use the console.   [e]', True, (0, 255, 0))
goal_prev = 1
loca = 1
game_off = False
timdang = 0

most = 2
engener = 1
reactor = 1

ship_most_loca = True
ship_ingener_loca = False
ship_reactor_loca = False
n = 0
d = 0
n_ship = 0
up = 0
down = 0
left = 0
right = 0
state = 1
animCount = 0
video_1 = True
video_2 = False
x_ship = 100
y_ship = 270

wight = 768
height = 512

win = pygame.display.set_mode((wight, height))
clock = pygame.time.Clock()
fps = 45
x = 154
y = 240
speed = 2
txt_map = [
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',
    '11111111111111111111111111111111',

]
astro_list = pygame.image.load('astro_list.png')
astro_state = [astro_list.subsurface(0, 0, 32, 32),
               astro_list.subsurface(32, 0, 32, 32),
               astro_list.subsurface(64, 0, 32, 32),
               astro_list.subsurface(96, 0, 32, 32),
               astro_list.subsurface(128, 0, 32, 32),
               astro_list.subsurface(160, 0, 32, 32),
               astro_list.subsurface(192, 0, 32, 32),
               astro_list.subsurface(224, 0, 32, 32),
               astro_list.subsurface(256, 0, 32, 32)]
astro_dawn = [astro_list.subsurface(0, 32, 32, 32),
              astro_list.subsurface(32, 32, 32, 32),
              astro_list.subsurface(64, 32, 32, 32),
              astro_list.subsurface(96, 32, 32, 32),
              astro_list.subsurface(128, 32, 32, 32),
              astro_list.subsurface(160, 32, 32, 32),
              astro_list.subsurface(192, 32, 32, 32),
              astro_list.subsurface(224, 32, 32, 32),
              astro_list.subsurface(256, 32, 32, 32)]
astro_up = [astro_list.subsurface(0, 64, 32, 32),
            astro_list.subsurface(32, 64, 32, 32),
            astro_list.subsurface(64, 64, 32, 32),
            astro_list.subsurface(96, 64, 32, 32),
            astro_list.subsurface(128, 64, 32, 32),
            astro_list.subsurface(160, 64, 32, 32),
            astro_list.subsurface(192, 64, 32, 32),
            astro_list.subsurface(224, 64, 32, 32),
            astro_list.subsurface(256, 64, 32, 32)]
astro_left = [astro_list.subsurface(0, 96, 32, 32),
              astro_list.subsurface(32, 96, 32, 32),
              astro_list.subsurface(64, 96, 32, 32),
              astro_list.subsurface(96, 96, 32, 32),
              astro_list.subsurface(128, 96, 32, 32),
              astro_list.subsurface(160, 96, 32, 32),
              astro_list.subsurface(192, 96, 32, 32),
              astro_list.subsurface(224, 96, 32, 32),
              astro_list.subsurface(256, 96, 32, 32)]
astro_right = [astro_list.subsurface(0, 128, 32, 32),
               astro_list.subsurface(32, 128, 32, 32),
               astro_list.subsurface(64, 128, 32, 32),
               astro_list.subsurface(96, 128, 32, 32),
               astro_list.subsurface(128, 128, 32, 32),
               astro_list.subsurface(160, 128, 32, 32),
               astro_list.subsurface(192, 128, 32, 32),
               astro_list.subsurface(224, 128, 32, 32),
               astro_list.subsurface(256, 128, 32, 32)]
wall1 = astro_list.subsurface(288, 0, 32, 32)
wall2 = astro_list.subsurface(320, 0, 32, 32)
wall3 = astro_list.subsurface(352, 0, 32, 32)
mob_eye = [astro_list.subsurface(288, 32, 32, 32),
           astro_list.subsurface(288, 32, 32, 32),
           astro_list.subsurface(320, 32, 32, 32),
           astro_list.subsurface(320, 32, 32, 32),
           astro_list.subsurface(352, 32, 32, 32),
           astro_list.subsurface(384, 32, 32, 32),
           astro_list.subsurface(416, 32, 32, 32),
           astro_list.subsurface(448, 32, 32, 32),
           astro_list.subsurface(480, 32, 32, 32),
           astro_list.subsurface(288, 32, 32, 32)]
astro_ship = [pygame.image.load('astro_ship_1.png'),
              pygame.image.load('astro_ship_2.png'),
              pygame.image.load('astro_ship_3.png'),
              pygame.image.load('astro_ship_4.png'),
              pygame.image.load('astro_ship_5.png'),
              pygame.image.load('astro_ship_6.png'),
              pygame.image.load('astro_ship_7.png'),
              pygame.image.load('astro_ship_8.png'),
              pygame.image.load('astro_ship_9.png')]
astro_bg_1 = [pygame.image.load('astro_bg_1_1.png'),
              pygame.image.load('astro_bg_1_2.png'),
              pygame.image.load('astro_bg_1_3.png'),
              pygame.image.load('astro_bg_1_4.png'),
              pygame.image.load('astro_bg_1_5.png')]
astro_bg_2 = [pygame.image.load('astro_bg_2_1.png'),
              pygame.image.load('astro_bg_2_2.png'),
              pygame.image.load('astro_bg_2_3.png'),
              pygame.image.load('astro_bg_2_4.png'),
              pygame.image.load('astro_bg_2_5.png')]
astro_ship_most = pygame.image.load('astro_ship_most.png')
astro_ship_most_sms = pygame.image.load('astro_ship_most_sms.png')
astro_ship_engener = pygame.image.load('astro_ship_engener.png')
astro_ship_engener_none_det = pygame.image.load('astro_ship_engener_none_det.png')
astro_ship_reactor = pygame.image.load('astro_ship_reactor.png')
astro_ship_reactor_damage = pygame.image.load('astro_ship_reactor_damage.png')
you_win = pygame.image.load('you_win.png')
world_map = set()
for i, row in enumerate(txt_map):
    for j, char in enumerate(row):
        if char == '0':
            world_map.add((j * 32, i * 32))


def draw_video():
    global n, video_1, d, video_2, game_off
    if video_1 is True:

        win.blit(pygame.transform.scale(astro_bg_1[n // 55], (768, 512)), (0, 0))
        n += 1

        if n == 275:
            n = 0

            video_1 = False
    elif video_2 is True:

        win.blit(pygame.transform.scale(astro_bg_2[n // 55], (768, 512)), (0, 0))
        n += 1

        if n == 275:
            n = 0
            game_off = True
            video_2 = False


def draw_window():
    global animCount
    for pos1, pos2 in world_map:
        win.blit(wall3, (pos1, pos2))

    if animCount + 1 >= 45:
        animCount = 0
    if down == 1:
        win.blit(pygame.transform.scale(astro_dawn[animCount // 5], (128, 128)), (x, y))
        animCount += 1
    elif up == 1:
        win.blit(pygame.transform.scale(astro_up[animCount // 5], (128, 128)), (x, y))
        animCount += 1
    elif left == 1:
        win.blit(pygame.transform.scale(astro_left[animCount // 5], (128, 128)), (x, y))
        animCount += 1
    elif right == 1:
        win.blit(pygame.transform.scale(astro_right[animCount // 5], (128, 128)), (x, y))
        animCount += 1
    else:
        win.blit(pygame.transform.scale(astro_state[animCount // 5], (128, 128)), (x, y))

    # pygame.display.update()


# def draw_mob(ru):
# global n
# if ru is True:
# win.blit(mob_eye[n // 7], (272, 256))
# n += 1
# pygame.display.update()
# if n == 70:
# n = 0


# def draw_bg_1():
#     win.fill((0, 0, 0))
#     win.blit(astro_bg_1, (0, 0))


def draw_ship_in_space():
    global x_ship, y_ship, n_ship
    x_ship += 0.6
    y_ship -= 0.4
    if video_1 is True or video_2 is True:

        win.blit(pygame.transform.scale(astro_ship[n_ship // 9], (128, 64)), (x_ship, y_ship))
        n_ship += 1
        if n_ship == 81:
            n_ship = 0


def draw_ship_most():
    global ship_most_loca
    if ship_most_loca is True:
        if most == 1:
            win.blit(pygame.transform.scale(astro_ship_most, (768, 512)), (0, 0))
        elif most == 2:
            win.blit(pygame.transform.scale(astro_ship_most_sms, (768, 512)), (0, 0))


def draw_ship_engener():
    global ship_ingener_loca
    if ship_ingener_loca is True:
        if engener == 1:
            win.blit(pygame.transform.scale(astro_ship_engener, (768, 512)), (0, 0))
        elif engener == 2:
            win.blit(pygame.transform.scale(astro_ship_engener_none_det, (768, 512)), (0, 0))


def draw_ship_reactor():
    global ship_reactor_loca, reactor
    if ship_reactor_loca is True:
        if reactor == 1:
            win.blit(pygame.transform.scale(astro_ship_reactor_damage, (768, 512)), (0, 0))
        elif reactor == 2:
            win.blit(pygame.transform.scale(astro_ship_reactor, (768, 512)), (0, 0))


def term_exam():
    global term_exam1
    if term_exam1 == 1:
        win.blit(txt_danger, (5, 360))
    if term_exam1 == 2:
        pass


def goal(a1, b2, c3, d4, e5, f):
    if f == 1:
        win.blit(a1, (5, 390))
    elif f == 2:
        win.blit(b2, (5, 390))
    elif f == 3:
        win.blit(c3, (5, 390))
    elif f == 4:
        win.blit(d4, (5, 390))
    elif f == 5:
        win.blit(e5, (5, 390))


run = True

while run:
    clock.tick(fps)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.K_q:
            run = False

    if x <= -100 and left == 1:
        if loca != 3:
            x = wight - 20
            loca += 1
    if x >= wight and right == 1:
        if loca != 1:
            x = -30
            loca -= 1

    if loca == 1:
        ship_most_loca = True
        ship_ingener_loca = False
        ship_reactor_loca = False
    elif loca == 2:
        ship_most_loca = False
        ship_ingener_loca = True
        ship_reactor_loca = False
    elif loca == 3:
        ship_most_loca = False
        ship_ingener_loca = False
        ship_reactor_loca = True

    if goal_prev == 1:
        if keys[pygame.K_e] and x >= 540 and loca == 1 and most == 2:
            term_exam1 = 1
            goal_prev = 2
    elif goal_prev == 2:
        if keys[pygame.K_e] and x <= 380 and loca == 3:
            goal_prev = 3
    elif goal_prev == 3:
        if keys[pygame.K_e] and 110 <= x <= 170 and loca == 2:
            goal_prev = 4
            engener = 2
    elif goal_prev == 4:
        if keys[pygame.K_e] and x <= 380 and loca == 3:
            goal_prev = 5
            reactor = 2
            most = 1
            term_exam1 = 0
    elif goal_prev == 5:
        if keys[pygame.K_e] and x >= 400 and loca == 1:
            video_2 = True

    # if keys[pygame.K_e]:
    # mob_run = True

#    if keys[pygame.K_s]:
#        down = 1
#        up = 0
#        left = 0
#        right = 0
#        y += speed

#    elif keys[pygame.K_w]:
#        down = 0
#        up = 1
#        left = 0
#        right = 0
#        y -= speed
    if keys[pygame.K_a]:
        down = 0
        up = 0
        left = 1
        right = 0
        x -= speed
    elif keys[pygame.K_d]:
        down = 0
        up = 0
        left = 0
        right = 1
        x += speed

    else:
        down = 0
        up = 0
        left = 0
        right = 0
        animCount = 0
    win.fill((0, 0, 0))
    if video_1 or video_2:
        draw_video()
        draw_ship_in_space()
    # draw_mob(mob_run)
    elif video_1 is False and video_2 is False and game_off is False:
        if loca == 1:
            draw_ship_most()
        elif loca == 2:
            draw_ship_engener()
        elif loca == 3:
            draw_ship_reactor()
        draw_window()
        goal(txt_goal1, txt_goal2, txt_goal3, txt_goal4, txt_goal5, goal_prev)
        term_exam()
    elif game_off is True:
        win.blit(pygame.transform.scale(you_win, (768, 512)), (0, 0))
        if timdang <= 150:
            timdang += 1
        else:
            run = False
    pygame.display.update()
pygame.quit()
