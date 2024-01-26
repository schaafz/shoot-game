def wait():
    while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        basic.pause(0)

def on_button_pressed_ab():
    global stv2, stv, stv3, score, gameov, currscore, menusel__1
    if gameov == 1:
        basic.clear_screen()
        stv2 = 0
        stv = 0
        stv3 = 0
        score = 0
        gameov = 0
        currscore = -1
        menusel__1 = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

highscore2 = 0
highscore = 0
img3: Image = None
img2: Image = None
pause3 = 0
pause2 = 0
pause1 = 0
pausev = 0
hitv = 0
dropposx3 = 0
dropposx2 = 0
dropposx = 0
droposy3 = 0
droposy2 = 0
droposy = 0
shooty = 0
randomov = 0
sv = 0
shootx = 0
enemy_posy = 0
enemy_posx = 0
pos = 0
next_speed = 0
speed = 0
gov = 0
img: Image = None
shootv = 0
menusel__1 = 0
currscore = 0
score = 0
stv3 = 0
stv = 0
stv2 = 0
gameov = 0
showv = 0

def on_forever():
    global shootv, img, gov, gameov, currscore, speed, next_speed, pos, enemy_posx, enemy_posy, stv, score
    music.set_volume(83)
    if menusel__1 == 1:
        if stv != 1 and gameov == 0:
            shootv = 0
            radio.set_group(37)
            img = images.create_big_image("""
                . . . . . . # # # .
                . . . . . # . # . #
                . . . . . # # # # #
                . . . . . . # . # .
                . . . . . # . . . #
                """)
            led.plot_brightness(2, 2, 0)
            gov = 0
            gameov = 0
            currscore = 0
            speed = 700
            next_speed = 3
            pos = 7
            enemy_posx = 0
            enemy_posy = 0
            img.scroll_image(1, 150)
            music.play(music.tone_playable(233, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(523, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(659, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(784, music.beat(BeatFraction.BREVE)),
                music.PlaybackMode.IN_BACKGROUND)
            while not (input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B)):
                basic.pause(0)
            gov = 1
            music.stop_all_sounds()
            stv = 1
            basic.pause(50)
            music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(523, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.IN_BACKGROUND)
            while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                basic.pause(0)
            pos = 3
            basic.clear_screen()
            score = 0
            music.stop_all_sounds()
basic.forever(on_forever)

def on_forever2():
    global shootx
    shootx = pos - 1
basic.forever(on_forever2)

def on_forever3():
    if pos == 5:
        led.plot(4, 4)
basic.forever(on_forever3)

def on_forever4():
    if pos == 4:
        led.plot(3, 4)
basic.forever(on_forever4)

def on_forever5():
    if stv == 1 or stv2 == 1 or stv3 == 1:
        radio.send_number(score)
basic.forever(on_forever5)

def on_forever6():
    if pos == 3:
        led.plot(2, 4)
basic.forever(on_forever6)

def on_forever7():
    global score, next_speed, speed
    if 1 == stv:
        if sv == 1 and shootv == 1:
            if randomov == 1:
                if (enemy_posx == pos - 1 or enemy_posx - 1 == pos - 1) and shooty == enemy_posy:
                    score = score + 1
                    music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
                        music.PlaybackMode.IN_BACKGROUND)
                    if score == next_speed:
                        next_speed = next_speed + 3
                        if 120 < speed:
                            speed = speed - 120
                    while (enemy_posx == pos - 1 or enemy_posx - 1 == pos - 1) and shooty == enemy_posy:
                        basic.pause(0)
            if randomov == 2:
                if (enemy_posx == pos - 1 or enemy_posx + 1 == pos - 1) and shooty == enemy_posy:
                    score = score + 1
                    music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
                        music.PlaybackMode.IN_BACKGROUND)
                    if score == next_speed:
                        next_speed = next_speed + 3
                        if 125 < speed:
                            speed = speed - 75
                    while (enemy_posx == pos - 1 or enemy_posx + 1 == pos - 1) and shooty == enemy_posy:
                        basic.pause(0)
basic.forever(on_forever7)

def on_forever8():
    global gameov, currscore
    if 1 == stv:
        if enemy_posy == 4:
            if enemy_posx == pos - 1 and gameov != 1:
                basic.clear_screen()
                gameov = 1
                currscore = -1
                music.play(music.string_playable("B - G E D E - - ", 200),
                    music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever8)

def on_forever9():
    global gameov
    if 1 == stv2:
        if droposy == 4 or droposy2 == 4 or droposy3 == 4:
            if (dropposx == pos - 1 or dropposx2 == pos - 1 or dropposx3 == pos - 1) and gameov != 1:
                basic.clear_screen()
                gameov = 1
                music.play(music.string_playable("A E G E F D - - ", 200),
                    music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever9)

def on_forever10():
    global hitv, enemy_posx, enemy_posy
    if stv3 == 1:
        if gameov != 1:
            hitv = 0
            enemy_posx = randint(0, 4)
            enemy_posy = randint(0, 3)
            led.plot(enemy_posx, enemy_posy)
            basic.pause(pausev)
            led.plot_brightness(enemy_posx, enemy_posy, 0)
            hitv = 1
basic.forever(on_forever10)

def on_forever11():
    global gameov
    if 1 == stv3:
        if input.logo_is_pressed():
            basic.clear_screen()
            gameov = 1
            music.play(music.string_playable("- F G F G - - - ", 200),
                music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever11)

def on_forever12():
    global score, pausev
    if stv3 == 1:
        if pos - 1 == enemy_posx and shooty == enemy_posy:
            score = score + 1
            while pos - 1 == enemy_posx and shooty == enemy_posy:
                basic.pause(0)
            if 500 < pausev:
                pausev = pausev - 100
basic.forever(on_forever12)

def on_forever13():
    global img, droposy, dropposx, droposy2, dropposx2, gov, gameov, pause1, pos, pause2, pause3, droposy3, dropposx3, stv2, score
    if menusel__1 == 2:
        if stv2 != 1 and gameov == 0:
            radio.set_group(37)
            led.set_brightness(0)
            img = images.create_image("""
                # # # # #
                # # # # #
                # # . # #
                # . . # .
                . . . . .
                """)
            led.plot_brightness(2, 2, 0)
            droposy = 0
            dropposx = -1
            droposy2 = 0
            dropposx2 = -1
            gov = 0
            gameov = 0
            pause1 = 500
            pos = 7
            pause2 = 0
            pause3 = 0
            droposy3 = 0
            dropposx3 = -1
            img.show_image(0)
            music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            led.set_brightness(36)
            basic.pause(50)
            music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            led.set_brightness(72)
            basic.pause(50)
            music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            led.set_brightness(100)
            basic.pause(50)
            music.play(music.tone_playable(466, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            led.set_brightness(136)
            basic.pause(50)
            music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            led.set_brightness(172)
            basic.pause(50)
            music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            led.set_brightness(200)
            basic.pause(50)
            music.play(music.tone_playable(294, music.beat(BeatFraction.BREVE)),
                music.PlaybackMode.IN_BACKGROUND)
            led.set_brightness(255)
            while not (input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B)):
                basic.pause(0)
            gov = 1
            music.stop_all_sounds()
            stv2 = 1
            basic.pause(50)
            music.play(music.tone_playable(294, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(587, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.IN_BACKGROUND)
            while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                basic.pause(0)
            pos = 3
            basic.clear_screen()
            score = 0
            music.stop_all_sounds()
basic.forever(on_forever13)

def on_forever14():
    global pausev, shootv, img, img2, img3, gov, gameov, pos, enemy_posx, enemy_posy, stv3, score
    music.set_volume(83)
    if menusel__1 == 3:
        if stv3 != 1 and gameov == 0:
            pausev = 1200
            shootv = 0
            radio.set_group(37)
            img = images.icon_image(IconNames.TARGET)
            img2 = images.icon_image(IconNames.SMALL_DIAMOND)
            img3 = images.icon_image(IconNames.DIAMOND)
            led.plot_brightness(2, 2, 0)
            gov = 0
            gameov = 0
            pos = 7
            enemy_posx = 0
            enemy_posy = 0
            img2.show_image(0)
            music.play(music.tone_playable(277, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(311, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            img3.show_image(0)
            music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(370, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(415, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            img.show_image(0)
            while not (input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B)):
                basic.pause(0)
            gov = 1
            music.stop_all_sounds()
            stv3 = 1
            basic.pause(50)
            music.play(music.tone_playable(277, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.IN_BACKGROUND)
            basic.pause(50)
            music.play(music.tone_playable(554, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.IN_BACKGROUND)
            while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                basic.pause(0)
            pos = 3
            basic.clear_screen()
            score = 0
            music.stop_all_sounds()
basic.forever(on_forever14)

def on_forever15():
    global dropposx3, droposy3, pause3, score
    if stv2 == 1 and gameov == 0:
        if pause3 != 0:
            if dropposx3 == -1:
                dropposx3 = randint(0, 4)
                basic.pause(pause3)
            else:
                led.plot(dropposx3, droposy3)
                basic.pause(pause3)
                for index in range(5):
                    led.plot(dropposx3, droposy3)
                    droposy3 = droposy3 + 1
                    basic.pause(100)
                basic.pause(100)
                droposy3 = 4
                for index2 in range(5):
                    led.plot_brightness(dropposx3, droposy3, 0)
                    droposy3 = droposy3 - 1
                    basic.pause(100)
                basic.pause(100)
                if pause3 > 200:
                    pause3 = pause3 - 20
                dropposx3 = -1
                droposy3 = 0
                score = score + 1
basic.forever(on_forever15)

def on_forever16():
    global dropposx, droposy, score, pause1, pause2
    if stv2 == 1 and gameov == 0:
        if dropposx == -1:
            dropposx = randint(0, 4)
            basic.pause(pause1)
        else:
            led.plot(dropposx, droposy)
            basic.pause(pause1)
            for index3 in range(5):
                led.plot(dropposx, droposy)
                droposy = droposy + 1
                basic.pause(100)
            basic.pause(100)
            droposy = 4
            for index4 in range(5):
                led.plot_brightness(dropposx, droposy, 0)
                droposy = droposy - 1
                basic.pause(100)
            basic.pause(100)
            dropposx = -1
            droposy = 0
            score = score + 1
            if pause1 > 200:
                pause1 = pause1 - 20
            if pause1 == 300 and pause2 == 0:
                pause2 = 500
                pause1 = 500
basic.forever(on_forever16)

def on_forever17():
    global dropposx2, droposy2, score, pause2, pause1, pause3
    if stv2 == 1 and gameov == 0:
        if pause2 != 0:
            if dropposx2 == -1:
                dropposx2 = randint(0, 4)
                basic.pause(pause2)
            else:
                led.plot(dropposx2, droposy2)
                basic.pause(pause2)
                for index5 in range(5):
                    led.plot(dropposx2, droposy2)
                    droposy2 = droposy2 + 1
                    basic.pause(100)
                basic.pause(100)
                droposy2 = 4
                for index6 in range(5):
                    led.plot_brightness(dropposx2, droposy2, 0)
                    droposy2 = droposy2 - 1
                    basic.pause(100)
                basic.pause(100)
                dropposx2 = -1
                droposy2 = 0
                score = score + 1
                if pause2 > 200:
                    pause2 = pause2 - 20
                if pause2 == 300 and pause3 == 0:
                    pause2 = 500
                    pause1 = 500
                    pause3 = 500
basic.forever(on_forever17)

def on_forever18():
    global stv, pos
    if gameov == 1:
        stv = 0
        pos = 7
        radio.send_string("Gameo")
    else:
        radio.send_string("")
basic.forever(on_forever18)

def on_forever19():
    if stv == 1:
        if gov == 0 and highscore != 0:
            radio.send_value("high", highscore)
    if stv2 == 1:
        if highscore2 != 0:
            radio.send_value("high", highscore2)
basic.forever(on_forever19)

def on_forever20():
    global highscore, highscore2
    if stv == 1:
        if highscore < score:
            highscore = score
    if stv2 == 1:
        if highscore2 < score:
            highscore2 = score
basic.forever(on_forever20)

def on_forever21():
    global showv
    if menusel__1 == 0:
        if showv == 0:
            basic.show_leds("""
                . # # # .
                # . # . #
                # # # # #
                . # . # .
                # . . . #
                """)
            showv = 1
basic.forever(on_forever21)

def on_forever22():
    global showv
    if menusel__1 == -1:
        if showv == 0:
            basic.show_leds("""
                # # # # #
                # # # # #
                # # . # #
                # . . # .
                . . . . .
                """)
            showv = 1
basic.forever(on_forever22)

def on_forever23():
    global showv
    if menusel__1 == -2:
        if showv == 0:
            pass
        basic.show_leds("""
            . . # . .
            . # # # .
            # # . # #
            . # # # .
            . . # . .
            """)
        showv = 1
basic.forever(on_forever23)

def on_forever24():
    global menusel__1, showv
    if menusel__1 == 0:
        if input.logo_is_pressed():
            menusel__1 = 1
            showv = 0
        if input.button_is_pressed(Button.A) and not (input.button_is_pressed(Button.B)):
            wait()
            menusel__1 = -1
            showv = 0
        if input.button_is_pressed(Button.B) and not (input.button_is_pressed(Button.A)):
            wait()
            menusel__1 = -2
            showv = 0
basic.forever(on_forever24)

def on_forever25():
    global menusel__1, showv
    if menusel__1 == -1:
        if input.logo_is_pressed():
            menusel__1 = 2
            showv = 0
        if input.button_is_pressed(Button.A) and not (input.button_is_pressed(Button.B)):
            wait()
            menusel__1 = -2
            showv = 0
        if input.button_is_pressed(Button.B) and not (input.button_is_pressed(Button.A)):
            wait()
            menusel__1 = 0
            showv = 0
basic.forever(on_forever25)

def on_forever26():
    global menusel__1, showv
    if menusel__1 == -2:
        if input.logo_is_pressed():
            menusel__1 = 3
            showv = 0
        if input.button_is_pressed(Button.A) and not (input.button_is_pressed(Button.B)):
            wait()
            menusel__1 = 0
            showv = 0
        if input.button_is_pressed(Button.B) and not (input.button_is_pressed(Button.A)):
            wait()
            menusel__1 = -1
            showv = 0
basic.forever(on_forever26)

def on_forever27():
    global enemy_posx, currscore, randomov, enemy_posy
    if 1 == stv:
        enemy_posx = 0
        currscore = score
        randomov = randint(1, 2)
        if randomov == 1:
            enemy_posx = 0
            for index7 in range(6):
                if score == currscore:
                    basic.pause(speed)
                if score == currscore:
                    led.plot(enemy_posx, enemy_posy)
                led.plot_brightness(enemy_posx - 1, enemy_posy, 0)
                enemy_posx = enemy_posx + 1
            if score == currscore:
                led.plot_brightness(4, enemy_posy, 0)
                enemy_posx = 0
        if randomov == 2:
            enemy_posx = 4
            for index8 in range(6):
                if score == currscore:
                    basic.pause(speed)
                if score == currscore:
                    led.plot(enemy_posx, enemy_posy)
                led.plot_brightness(enemy_posx + 1, enemy_posy, 0)
                enemy_posx = enemy_posx - 1
            if score == currscore:
                led.plot_brightness(0, enemy_posy, 0)
                enemy_posx = 0
        if score == currscore:
            if enemy_posy != 4:
                enemy_posy = 1 + enemy_posy
            else:
                enemy_posy = 0
basic.forever(on_forever27)

def on_forever28():
    global shootv, sv, shooty
    if 1 == stv or 1 == stv3:
        if input.button_is_pressed(Button.AB):
            shootv = 1
            sv = 1
            shooty = 4
            for index9 in range(5):
                led.plot(pos - 1, shooty)
                shooty = shooty - 1
                basic.pause(100)
            shooty = 5
            basic.pause(100)
            shootv = 0
            shooty = 3
            for index10 in range(4):
                led.plot_brightness(pos - 1, shooty, 0)
                shooty = shooty - 1
                basic.pause(0)
            sv = 0
            basic.pause(speed * 1.5)
basic.forever(on_forever28)

def on_forever29():
    if pos == 2:
        led.plot(1, 4)
basic.forever(on_forever29)

def on_forever30():
    global pos
    if 1 == stv or 1 == stv2 or 1 == stv3:
        if input.button_is_pressed(Button.B) and not (input.button_is_pressed(Button.AB)) and not (input.button_is_pressed(Button.A)) and pos < 5 and not (sv == 1):
            if pos == 1:
                led.plot_brightness(0, 4, 0)
            if pos == 2:
                led.plot_brightness(1, 4, 0)
            if pos == 3:
                led.plot_brightness(2, 4, 0)
            if pos == 4:
                led.plot_brightness(3, 4, 0)
            if pos == 5:
                led.plot_brightness(4, 4, 0)
            pos = pos + 1
            while input.button_is_pressed(Button.B):
                basic.pause(0)
basic.forever(on_forever30)

def on_forever31():
    if pos == 1:
        led.plot(0, 4)
basic.forever(on_forever31)

def on_forever32():
    global pos
    if 1 == stv or 1 == stv2 or 1 == stv3:
        if input.button_is_pressed(Button.A) and 1 < pos and not (input.button_is_pressed(Button.B)) and not (input.button_is_pressed(Button.AB)) and not (sv == 1):
            if pos == 1:
                led.plot_brightness(0, 4, 0)
            if pos == 2:
                led.plot_brightness(1, 4, 0)
            if pos == 3:
                led.plot_brightness(2, 4, 0)
            if pos == 4:
                led.plot_brightness(3, 4, 0)
            if pos == 5:
                led.plot_brightness(4, 4, 0)
            pos = pos - 1
            while input.button_is_pressed(Button.A):
                basic.pause(0)
basic.forever(on_forever32)
