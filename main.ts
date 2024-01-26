let gameov = 0
let stv2 = 0
let stv = 0
let stv3 = 0
let score = 0
let currscore = 0
let menusel__1 = 0
let showv = 0
let enemy_posx = 0
let randomov = 0
let speed = 0
let enemy_posy = 0
let shootv = 0
let sv = 0
let shooty = 0
let pos = 0
let img: Image = null
let gov = 0
let next_speed = 0
let shootx = 0
let droposy = 0
let droposy2 = 0
let droposy3 = 0
let dropposx = 0
let dropposx2 = 0
let dropposx3 = 0
let hitv = 0
let pausev = 0
let pause1 = 0
let pause2 = 0
let pause3 = 0
let img2: Image = null
let img3: Image = null
let highscore = 0
let highscore2 = 0
function wait () {
    while (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
        basic.pause(0)
    }
}
input.onButtonPressed(Button.AB, function () {
    if (gameov == 1) {
        basic.clearScreen()
        stv2 = 0
        stv = 0
        stv3 = 0
        score = 0
        gameov = 0
        currscore = -1
        menusel__1 = 0
    }
})
basic.forever(function () {
    if (menusel__1 == -1) {
        if (showv == 0) {
            basic.showLeds(`
                # # # # #
                # # # # #
                # # . # #
                # . . # .
                . . . . .
                `)
            showv = 1
        }
    }
})
basic.forever(function () {
    if (menusel__1 == -2) {
        if (showv == 0) {
        	
        }
        basic.showLeds(`
            . . # . .
            . # # # .
            # # . # #
            . # # # .
            . . # . .
            `)
        showv = 1
    }
})
basic.forever(function () {
    if (menusel__1 == 0) {
        if (input.logoIsPressed()) {
            menusel__1 = 1
            showv = 0
        }
        if (input.buttonIsPressed(Button.A) && !(input.buttonIsPressed(Button.B))) {
            wait()
            menusel__1 = -1
            showv = 0
        }
        if (input.buttonIsPressed(Button.B) && !(input.buttonIsPressed(Button.A))) {
            wait()
            menusel__1 = -2
            showv = 0
        }
    }
})
basic.forever(function () {
    if (menusel__1 == -1) {
        if (input.logoIsPressed()) {
            menusel__1 = 2
            showv = 0
        }
        if (input.buttonIsPressed(Button.A) && !(input.buttonIsPressed(Button.B))) {
            wait()
            menusel__1 = -2
            showv = 0
        }
        if (input.buttonIsPressed(Button.B) && !(input.buttonIsPressed(Button.A))) {
            wait()
            menusel__1 = 0
            showv = 0
        }
    }
})
basic.forever(function () {
    if (menusel__1 == -2) {
        if (input.logoIsPressed()) {
            menusel__1 = 3
            showv = 0
        }
        if (input.buttonIsPressed(Button.A) && !(input.buttonIsPressed(Button.B))) {
            wait()
            menusel__1 = 0
            showv = 0
        }
        if (input.buttonIsPressed(Button.B) && !(input.buttonIsPressed(Button.A))) {
            wait()
            menusel__1 = -1
            showv = 0
        }
    }
})
basic.forever(function () {
    if (1 == stv) {
        enemy_posx = 0
        currscore = score
        randomov = randint(1, 2)
        if (randomov == 1) {
            enemy_posx = 0
            for (let index = 0; index < 6; index++) {
                if (score == currscore) {
                    basic.pause(speed)
                }
                if (score == currscore) {
                    led.plot(enemy_posx, enemy_posy)
                }
                led.plotBrightness(enemy_posx - 1, enemy_posy, 0)
                enemy_posx = enemy_posx + 1
            }
            if (score == currscore) {
                led.plotBrightness(4, enemy_posy, 0)
                enemy_posx = 0
            }
        }
        if (randomov == 2) {
            enemy_posx = 4
            for (let index = 0; index < 6; index++) {
                if (score == currscore) {
                    basic.pause(speed)
                }
                if (score == currscore) {
                    led.plot(enemy_posx, enemy_posy)
                }
                led.plotBrightness(enemy_posx + 1, enemy_posy, 0)
                enemy_posx = enemy_posx - 1
            }
            if (score == currscore) {
                led.plotBrightness(0, enemy_posy, 0)
                enemy_posx = 0
            }
        }
        if (score == currscore) {
            if (enemy_posy != 4) {
                enemy_posy = 1 + enemy_posy
            } else {
                enemy_posy = 0
            }
        }
    }
})
basic.forever(function () {
    if (1 == stv || 1 == stv3) {
        if (input.buttonIsPressed(Button.AB)) {
            shootv = 1
            sv = 1
            shooty = 4
            for (let index = 0; index < 5; index++) {
                led.plot(pos - 1, shooty)
                shooty = shooty - 1
                basic.pause(100)
            }
            shooty = 5
            basic.pause(100)
            shootv = 0
            shooty = 3
            for (let index = 0; index < 4; index++) {
                led.plotBrightness(pos - 1, shooty, 0)
                shooty = shooty - 1
                basic.pause(0)
            }
            sv = 0
            basic.pause(speed * 1.5)
        }
    }
})
basic.forever(function () {
    if (pos == 2) {
        led.plot(1, 4)
    }
})
basic.forever(function () {
    if (1 == stv || 1 == stv2 || 1 == stv3) {
        if (input.buttonIsPressed(Button.B) && !(input.buttonIsPressed(Button.AB)) && !(input.buttonIsPressed(Button.A)) && pos < 5 && !(sv == 1)) {
            if (pos == 1) {
                led.plotBrightness(0, 4, 0)
            }
            if (pos == 2) {
                led.plotBrightness(1, 4, 0)
            }
            if (pos == 3) {
                led.plotBrightness(2, 4, 0)
            }
            if (pos == 4) {
                led.plotBrightness(3, 4, 0)
            }
            if (pos == 5) {
                led.plotBrightness(4, 4, 0)
            }
            pos = pos + 1
            while (input.buttonIsPressed(Button.B)) {
                basic.pause(0)
            }
        }
    }
})
basic.forever(function () {
    if (pos == 1) {
        led.plot(0, 4)
    }
})
basic.forever(function () {
    if (1 == stv || 1 == stv2 || 1 == stv3) {
        if (input.buttonIsPressed(Button.A) && 1 < pos && !(input.buttonIsPressed(Button.B)) && !(input.buttonIsPressed(Button.AB)) && !(sv == 1)) {
            if (pos == 1) {
                led.plotBrightness(0, 4, 0)
            }
            if (pos == 2) {
                led.plotBrightness(1, 4, 0)
            }
            if (pos == 3) {
                led.plotBrightness(2, 4, 0)
            }
            if (pos == 4) {
                led.plotBrightness(3, 4, 0)
            }
            if (pos == 5) {
                led.plotBrightness(4, 4, 0)
            }
            pos = pos - 1
            while (input.buttonIsPressed(Button.A)) {
                basic.pause(0)
            }
        }
    }
})
basic.forever(function () {
    music.setVolume(83)
    if (menusel__1 == 1) {
        if (stv != 1 && gameov == 0) {
            shootv = 0
            radio.setGroup(37)
            img = images.createBigImage(`
                . . . . . . # # # .
                . . . . . # . # . #
                . . . . . # # # # #
                . . . . . . # . # .
                . . . . . # . . . #
                `)
            led.plotBrightness(2, 2, 0)
            gov = 0
            gameov = 0
            currscore = 0
            speed = 700
            next_speed = 3
            pos = 7
            enemy_posx = 0
            enemy_posy = 0
            img.scrollImage(1, 150)
            music.play(music.tonePlayable(233, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(294, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(349, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(523, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(659, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Breve)), music.PlaybackMode.InBackground)
            while (!(input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B))) {
                basic.pause(0)
            }
            gov = 1
            music.stopAllSounds()
            stv = 1
            basic.pause(50)
            music.play(music.tonePlayable(262, music.beat(BeatFraction.Half)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(523, music.beat(BeatFraction.Half)), music.PlaybackMode.InBackground)
            while (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
                basic.pause(0)
            }
            pos = 3
            basic.clearScreen()
            score = 0
            music.stopAllSounds()
        }
    }
})
basic.forever(function () {
    shootx = pos - 1
})
basic.forever(function () {
    if (pos == 5) {
        led.plot(4, 4)
    }
})
basic.forever(function () {
    if (pos == 4) {
        led.plot(3, 4)
    }
})
basic.forever(function () {
    if (stv == 1 || stv2 == 1 || stv3 == 1) {
        radio.sendNumber(score)
    }
})
basic.forever(function () {
    if (pos == 3) {
        led.plot(2, 4)
    }
})
basic.forever(function () {
    if (1 == stv) {
        if (sv == 1 && shootv == 1) {
            if (randomov == 1) {
                if ((enemy_posx == pos - 1 || enemy_posx - 1 == pos - 1) && shooty == enemy_posy) {
                    score = score + 1
                    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
                    if (score == next_speed) {
                        next_speed = next_speed + 3
                        if (120 < speed) {
                            speed = speed - 120
                        }
                    }
                    while ((enemy_posx == pos - 1 || enemy_posx - 1 == pos - 1) && shooty == enemy_posy) {
                        basic.pause(0)
                    }
                }
            }
            if (randomov == 2) {
                if ((enemy_posx == pos - 1 || enemy_posx + 1 == pos - 1) && shooty == enemy_posy) {
                    score = score + 1
                    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
                    if (score == next_speed) {
                        next_speed = next_speed + 3
                        if (125 < speed) {
                            speed = speed - 75
                        }
                    }
                    while ((enemy_posx == pos - 1 || enemy_posx + 1 == pos - 1) && shooty == enemy_posy) {
                        basic.pause(0)
                    }
                }
            }
        }
    }
})
basic.forever(function () {
    if (1 == stv) {
        if (enemy_posy == 4) {
            if (enemy_posx == pos - 1 && gameov != 1) {
                basic.clearScreen()
                gameov = 1
                currscore = -1
                music.play(music.stringPlayable("B - G E D E - - ", 200), music.PlaybackMode.UntilDone)
            }
        }
    }
})
basic.forever(function () {
    if (1 == stv2) {
        if (droposy == 4 || droposy2 == 4 || droposy3 == 4) {
            if ((dropposx == pos - 1 || dropposx2 == pos - 1 || dropposx3 == pos - 1) && gameov != 1) {
                basic.clearScreen()
                gameov = 1
                music.play(music.stringPlayable("A E G E F D - - ", 200), music.PlaybackMode.UntilDone)
            }
        }
    }
})
basic.forever(function () {
    if (stv3 == 1) {
        if (gameov != 1) {
            hitv = 0
            enemy_posx = randint(0, 4)
            enemy_posy = randint(0, 3)
            led.plot(enemy_posx, enemy_posy)
            basic.pause(pausev)
            led.plotBrightness(enemy_posx, enemy_posy, 0)
            hitv = 1
        }
    }
})
basic.forever(function () {
    if (1 == stv3) {
        if (input.logoIsPressed()) {
            basic.clearScreen()
            gameov = 1
            music.play(music.stringPlayable("- F G F G - - - ", 200), music.PlaybackMode.UntilDone)
        }
    }
})
basic.forever(function () {
    if (stv3 == 1) {
        if (pos - 1 == enemy_posx && shooty == enemy_posy) {
            score = score + 1
            while (pos - 1 == enemy_posx && shooty == enemy_posy) {
                basic.pause(0)
            }
            if (500 < pausev) {
                pausev = pausev - 100
            }
        }
    }
})
basic.forever(function () {
    if (menusel__1 == 2) {
        if (stv2 != 1 && gameov == 0) {
            radio.setGroup(37)
            led.setBrightness(0)
            img = images.createImage(`
                # # # # #
                # # # # #
                # # . # #
                # . . # .
                . . . . .
                `)
            led.plotBrightness(2, 2, 0)
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
            img.showImage(0)
            music.play(music.tonePlayable(294, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            led.setBrightness(36)
            basic.pause(50)
            music.play(music.tonePlayable(349, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            led.setBrightness(72)
            basic.pause(50)
            music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            led.setBrightness(100)
            basic.pause(50)
            music.play(music.tonePlayable(466, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            led.setBrightness(136)
            basic.pause(50)
            music.play(music.tonePlayable(440, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            led.setBrightness(172)
            basic.pause(50)
            music.play(music.tonePlayable(349, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            led.setBrightness(200)
            basic.pause(50)
            music.play(music.tonePlayable(294, music.beat(BeatFraction.Breve)), music.PlaybackMode.InBackground)
            led.setBrightness(255)
            while (!(input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B))) {
                basic.pause(0)
            }
            gov = 1
            music.stopAllSounds()
            stv2 = 1
            basic.pause(50)
            music.play(music.tonePlayable(294, music.beat(BeatFraction.Half)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(587, music.beat(BeatFraction.Half)), music.PlaybackMode.InBackground)
            while (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
                basic.pause(0)
            }
            pos = 3
            basic.clearScreen()
            score = 0
            music.stopAllSounds()
        }
    }
})
basic.forever(function () {
    music.setVolume(83)
    if (menusel__1 == 3) {
        if (stv3 != 1 && gameov == 0) {
            pausev = 1200
            shootv = 0
            radio.setGroup(37)
            img = images.iconImage(IconNames.Target)
            img2 = images.iconImage(IconNames.SmallDiamond)
            img3 = images.iconImage(IconNames.Diamond)
            led.plotBrightness(2, 2, 0)
            gov = 0
            gameov = 0
            pos = 7
            enemy_posx = 0
            enemy_posy = 0
            img2.showImage(0)
            music.play(music.tonePlayable(277, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(311, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            img3.showImage(0)
            music.play(music.tonePlayable(330, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(370, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(415, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
            basic.pause(50)
            img.showImage(0)
            while (!(input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B))) {
                basic.pause(0)
            }
            gov = 1
            music.stopAllSounds()
            stv3 = 1
            basic.pause(50)
            music.play(music.tonePlayable(277, music.beat(BeatFraction.Half)), music.PlaybackMode.InBackground)
            basic.pause(50)
            music.play(music.tonePlayable(554, music.beat(BeatFraction.Half)), music.PlaybackMode.InBackground)
            while (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
                basic.pause(0)
            }
            pos = 3
            basic.clearScreen()
            score = 0
            music.stopAllSounds()
        }
    }
})
basic.forever(function () {
    if (stv2 == 1 && gameov == 0) {
        if (pause3 != 0) {
            if (dropposx3 == -1) {
                dropposx3 = randint(0, 4)
                basic.pause(pause3)
            } else {
                led.plot(dropposx3, droposy3)
                basic.pause(pause3)
                for (let index = 0; index < 5; index++) {
                    led.plot(dropposx3, droposy3)
                    droposy3 = droposy3 + 1
                    basic.pause(100)
                }
                basic.pause(100)
                droposy3 = 4
                for (let index = 0; index < 5; index++) {
                    led.plotBrightness(dropposx3, droposy3, 0)
                    droposy3 = droposy3 - 1
                    basic.pause(100)
                }
                basic.pause(100)
                if (pause3 > 200) {
                    pause3 = pause3 - 20
                }
                dropposx3 = -1
                droposy3 = 0
                score = score + 1
            }
        }
    }
})
basic.forever(function () {
    if (stv2 == 1 && gameov == 0) {
        if (dropposx == -1) {
            dropposx = randint(0, 4)
            basic.pause(pause1)
        } else {
            led.plot(dropposx, droposy)
            basic.pause(pause1)
            for (let index = 0; index < 5; index++) {
                led.plot(dropposx, droposy)
                droposy = droposy + 1
                basic.pause(100)
            }
            basic.pause(100)
            droposy = 4
            for (let index = 0; index < 5; index++) {
                led.plotBrightness(dropposx, droposy, 0)
                droposy = droposy - 1
                basic.pause(100)
            }
            basic.pause(100)
            dropposx = -1
            droposy = 0
            score = score + 1
            if (pause1 > 200) {
                pause1 = pause1 - 20
            }
            if (pause1 == 300 && pause2 == 0) {
                pause2 = 500
                pause1 = 500
            }
        }
    }
})
basic.forever(function () {
    if (stv2 == 1 && gameov == 0) {
        if (pause2 != 0) {
            if (dropposx2 == -1) {
                dropposx2 = randint(0, 4)
                basic.pause(pause2)
            } else {
                led.plot(dropposx2, droposy2)
                basic.pause(pause2)
                for (let index = 0; index < 5; index++) {
                    led.plot(dropposx2, droposy2)
                    droposy2 = droposy2 + 1
                    basic.pause(100)
                }
                basic.pause(100)
                droposy2 = 4
                for (let index = 0; index < 5; index++) {
                    led.plotBrightness(dropposx2, droposy2, 0)
                    droposy2 = droposy2 - 1
                    basic.pause(100)
                }
                basic.pause(100)
                dropposx2 = -1
                droposy2 = 0
                score = score + 1
                if (pause2 > 200) {
                    pause2 = pause2 - 20
                }
                if (pause2 == 300 && pause3 == 0) {
                    pause2 = 500
                    pause1 = 500
                    pause3 = 500
                }
            }
        }
    }
})
basic.forever(function () {
    if (gameov == 1) {
        stv = 0
        pos = 7
        radio.sendString("Gameo")
    } else {
        radio.sendString("")
    }
})
basic.forever(function () {
    if (stv == 1) {
        if (gov == 0 && highscore != 0) {
            radio.sendValue("high", highscore)
        }
    }
    if (stv2 == 1) {
        if (highscore2 != 0) {
            radio.sendValue("high", highscore2)
        }
    }
})
basic.forever(function () {
    if (stv == 1) {
        if (highscore < score) {
            highscore = score
        }
    }
    if (stv2 == 1) {
        if (highscore2 < score) {
            highscore2 = score
        }
    }
})
basic.forever(function () {
    if (menusel__1 == 0) {
        if (showv == 0) {
            basic.showLeds(`
                . # # # .
                # . # . #
                # # # # #
                . # . # .
                # . . . #
                `)
            showv = 1
        }
    }
})
