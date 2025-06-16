
    #7..9..times..2..2..2..

    #share the time you schlub. It's stuffy in here.

label acttwo:

    $ inputcheck = 0
    $ player = renpy.input("Please choose a name for the protagonist", allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-1234567890.", length=12)
    $ player = player.strip()


    $ inputcheck = 1
    $ name = renpy.input("Please enter your own name", allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-1234567890.", length=12)
    $ name = name.strip()

    scene black
    pause 8
    show natmorning:
        xalign .5
        yalign .5
        zoom .666
        alpha 0
        subpixel True
        parallel:
            linear 5 alpha 1
        parallel:
            linear 18 zoom .8
    stop music fadeout 17
    pause 14.8
    stop music
    play sound tgescare1
    pause .2
    show screen tear(50, 0.1, 0.1, 40, 80)
    pause 0.3
    hide screen tear
    hide natmorning
    show ghostcloseup
    pause 4.5
    show screen tear(50, 0.1, 0.1, 40, 80)
    pause 0.2
    hide screen tear

    scene black
    pause 4

    play music wind fadein 2.0

    pause 7

    $ recordfallen = []
    show textgradient zorder 101:
        xalign .5
        yalign 1.206
    show console_caret_2
    show fallentext "_" as ftext zorder 100
    show cblink zorder 101:
        xpos 245
        ypos 300
        block:
            alpha 0.0
            pause 0.55
            alpha 1.0
            pause 0.55
            repeat
    pause 3.5
    hide cblink
    hide ftext

    call fallen("Welcome, observer.")
    call recordfallen("Welcome, observer.")

    call fallen("You have returned.")
    call recordfallen("You have returned.")

    call fallen("Truthfully, I had not much hope you would.")
    call recordfallen("Truthfully, I had not much hope you would.")

    call fallen("I've learned not to trust hope.")
    call recordfallen("I've learned not to trust hope.")

    call fallen("So I have just one question for you.")
    call recordfallen("So I have just one question for you.")

    call fallen("My last question left room for interpretation.")
    call recordfallen("My last question left room for interpretation.")

    call fallen("My apologies.")
    call recordfallen("My apologies.")

    call fallen("I shall rephrase.")
    call recordfallen("I shall rephrase.")

    call fallen("Perhaps this is a chance for us to...get along.")
    call recordfallen("Perhaps this is a chance for us to...get along.")

    call fallen("But I won't pretend not to judge you.")
    call recordfallen("But I won't pretend not to judge you.")

    call fallen("I wish to know where you stand.")
    call recordfallen("I wish to know where you stand.")

    call fallen("Do you come to help us? To watch us redeem ourselves?")
    call recordfallen("Do you come to help us? To watch us redeem ourselves?")

    call fallen("No matter the cost?")
    call recordfallen("No matter the cost?")

    call fallen("Or do you simply come to humor us. To watch us suffer.")
    call recordfallen("Or do you simply come to humor us. To watch us suffer.")

    call fallen("Choose.")
    call recordfallen("Choose.")

    show fallentext "_" as ftext zorder 100
    show cblink zorder 101:
        xpos 245
        ypos 300
        block:
            alpha 1.0
            pause 0.55
            alpha 0.0
            pause 0.55
            repeat

    pause 1

    call screen redeemconsole("", Return(True), Return(False))
    if _return:
        pause 2
        hide cblink
        hide ftext

        call fallen("Very well.")
        call recordfallen("Very well.")

        call fallen("However, I have more questions.")
        call recordfallen("However, I have more questions.")

        call fallen("I lied.")
        call recordfallen("I lied.")

        call fallen("I do that sometimes.")
        call recordfallen("I do that sometimes.")

        call fallen("Here is my next question:")
        call recordfallen("Here is my next question:")

        call fallen("Do you trust me?")
        call recordfallen("Do you trust me?")

        call fallen("No pressure.")
        call recordfallen("No pressure.")

        show fallentext "_" as ftext zorder 100
        show cblink zorder 101:
            xpos 245
            ypos 300
            block:
                alpha 1.0
                pause 0.55
                alpha 0.0
                pause 0.55
                repeat

        pause 1

        call screen confirmconsole("", Return(True), Return(False))
        if _return:
            pause 2
            hide cblink
            hide ftext

            call fallen("I see...")
            call recordfallen("I see...")

            call fallen("Thank you. I will remember that.")
            call recordfallen("Thank you. I will remember that.")

        else:
            pause 2
            hide cblink
            hide ftext

            call fallen("I see...")
            call recordfallen("I see...")

            call fallen("Perhaps that is wise of you. It isn't for me to say.")
            call recordfallen("Perhaps that is wise of you. It isn't for me to say.")

            call fallen("You will see my true face soon enough.")
            call recordfallen("You will see my true face soon enough.")

        call fallen("I have another question.")
        call recordfallen("I have another question.")

        call fallen("Do you think your third eye is weak?")
        call recordfallen("Do you think your third eye is weak?")

        call fallen("Or strong?")
        call recordfallen("Or strong?")

        call fallen("Choose.")
        call recordfallen("Choose.")

        show fallentext "_" as ftext zorder 100
        show cblink zorder 101:
            xpos 245
            ypos 300
            block:
                alpha 1.0
                pause 0.55
                alpha 0.0
                pause 0.55
                repeat

        pause 1

        call screen weakconsole("", Return(True), Return(False))
        if _return:
            pause 2
            hide cblink
            hide ftext

            call fallen("That is correct.")
            call recordfallen("That is correct.")

            call fallen("Good answer.")
            call recordfallen("Good answer.")

        else:
            pause 2
            hide cblink
            hide ftext

            call fallen("Now that...")
            call recordfallen("Now that...")

            call fallen("Is truly funny.")
            call recordfallen("Is truly funny.")

            call fallen("Can you hear me laughing?")
            call recordfallen("Can you hear me laughing?")

            call fallen("Ha. Ha. Ha.")
            call recordfallen("Ha. Ha. Ha.")

            call fallen("Ahem.")
            call recordfallen("Ahem.")

            call fallen("It is not strong. You should be grateful for that.")
            call recordfallen("It is not strong. You should be grateful for that.")

        call fallen("Here is my next question:")
        call recordfallen("Here is my next question:")

        call fallen("If I dare even ask it.")
        call recordfallen("If I dare even ask it.")

        call fallen("Do you think they can escape?")
        call recordfallen("Do you think they can escape?")

        show fallentext "_" as ftext zorder 100
        show cblink zorder 101:
            xpos 245
            ypos 300
            block:
                alpha 1.0
                pause 0.55
                alpha 0.0
                pause 0.55
                repeat

        pause 1

        call screen confirmconsolereverse("", Return(True), Return(False))
        if _return:
            pause 2
            hide cblink
            hide ftext

            call fallen("I see.")
            call recordfallen("I see.")

            call fallen("You have more hope than I do.")
            call recordfallen("You have more hope than I do.")

            call fallen("I pray you are correct.")
            call recordfallen("I pray you are correct.")

            call fallen("What is important is this...")
            call recordfallen("What is important is this...")

            call fallen("You must be willing to see their redemption through to the end.")
            call recordfallen("You must be willing to see their redemption through to the end.")

            call fallen("Are you willing to see it through, no matter the cost?")
            call recordfallen("Are you willing to see it through, no matter the cost?")

            show fallentext "_" as ftext zorder 100
            show cblink zorder 101:
                xpos 245
                ypos 300
                block:
                    alpha 1.0
                    pause 0.55
                    alpha 0.0
                    pause 0.55
                    repeat

            pause 1

            call screen yesconsole("", Return(True), Return(False))
            if _return:
                pass
            else:
                pass

            pause 2
            hide cblink
            hide ftext

            call fallen("Good. Then we have an understanding.")
            call recordfallen("Good. Then we have an understanding.")

            call fallen("I hope you are prepared.")
            call recordfallen("I hope you are prepared.")

        else:
            pause 2
            hide cblink
            hide ftext

            call fallen("...")
            call recordfallen("...")

            call fallen("Then why do you play this game?")
            call recordfallen("Then why do you play this game?")

            call fallen("This is frustrating.")
            call recordfallen("This is frustrating.")

            call fallen("I pray you are wrong.")
            call recordfallen("I pray you are wrong.")

            call fallen("Only time can tell...")
            call recordfallen("Only time can tell...")

            call fallen("I have no further questions.")
            call recordfallen("I have no further questions.")

        call fallen("I ask but one thing of you, observer.")
        call recordfallen("I ask but one thing of you, observer.")

        call fallen("Observe us.")
        call recordfallen("Observe us.")

        call fallen("And pray to whatever God you believe in.")
        call recordfallen("And pray to whatever God you believe in.")

        call fallen("Because they certainly don't observe us in here.")
        call recordfallen("Because they certainly don't observe us in here.")

    else:
        pause 2
        hide cblink
        hide ftext

        call fallen("Very well.")
        call recordfallen("Very well.")

        call fallen("Goodbye.")
        call recordfallen("Goodbye.")

        pause 3

        call fallen("Just kidding.")
        call recordfallen("Just kidding.")

        call fallen("As I stated before, nothing you can do could cause me fear.")
        call recordfallen("As I stated before, nothing you can do could cause me fear.")

        call fallen("Your third eye is weak.")
        call recordfallen("Your third eye is weak.")

        call fallen("Perhaps that is a blessing for both of us.")
        call recordfallen("Perhaps that is a blessing for both of us.")

        call fallen("But observe us you shall.")
        call recordfallen("But observe us you shall.")

        call fallen("It's comforting to know where you stand.")
        call recordfallen("It's comforting to know where you stand.")

        call fallen("Or at least what you're willing to say when pressed.")
        call recordfallen("Or at least what you're willing to say when pressed.")

        call fallen("I don't even trust you to take my questions seriously.")
        call recordfallen("I don't even trust you to take my questions seriously.")

        call fallen("My hell is to wonder.")
        call recordfallen("My hell is to wonder.")

        call fallen("I pray that whatever God you believe or disbelieve in is real.")
        call recordfallen("I pray that whatever God you believe or disbelieve in is real.")

        call fallen("Your own hell awaits you.")
        call recordfallen("Your own hell awaits you.")

        call fallen("But I should know better than to spin curses.")
        call recordfallen("But I should know better than to spin curses.")

        call fallen("After all...")
        call recordfallen("After all...")

        call fallen("What else could this reality be?")
        call recordfallen("What else could this reality be?")


    scene black
    stop music
    pause 4
    scene white
    with dissolve_scene_full

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/1.txt")
        except: open(config.basedir + "/1.txt", "wb").write(renpy.file("A2/Art/scg/1.txt").read())

    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn2 "Welcome, observer."
    fn2 "Welcome to the new day."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal

    scene white
    pause 2
    scene black
    pause 5

    "The steps creak gently as I creep downstairs."
    "My house is coated in warm shadow."
    "But in the living room, the couch is bathed in cool light."
    "I pause there where Monika is asleep."
    "Her face looks...peaceful."
    "Still and unreadable."
    "Like nothing from the night before had happened."
    "I wonder if she dreams..."
    "I sneak to the kitchen."

    pause 1.5
    scene bg kitchen
    with dissolve_scene_full

    mc "Good morning..."
    show monika u113122 at t11 zorder 2
    m "Morning."
    mc "I, um, made coffee and eggs."
    m u113143 "...Thanks."
    show monika at thide zorder 1
    hide monika
    "I place a plate and a mug on the table and Monika takes her seat."
    "I watch as she stares at them for a moment."
    "She takes a deep sip of coffee."
    "She pokes at the eggs with her fork and takes a small bite."
    show monika u113123 at t11 zorder 2
    m "It's good."
    mc "..."
    mc "{i}I'm sorry.{/i}"
    show monika u113143
    "Monika shakes her head."
    m u113113 "Why?"
    mc "I don't know."
    mc "For not telling you the truth."
    mc "For hiding."
    show monika u113143
    "She sets down her fork."
    m u114122 "{i}Why would you apologize to someone like me{/i}?"
    mc "..."
    m u113144 "I still can't believe it."
    m "It doesn't feel real."
    mc "I almost feel the same way..."
    m u114212 "Do you really remember all of it?"
    m "Through the reset? When I deleted everything?"
    m u113222 "And when Sayori...?"
    "She bites her lip."
    mc "..."
    "I squeeze my arms together and look down."
    mc "{i}Yes.{/i}"
    scene black
    with dissolve_scene_full
    "Monika holds her face in her hands."
    m "{i}Oh God{/i}..."
    mc "Monika?"
    m "..."
    mc "I-I..."
    mc "I don't want you to..."
    "Monika slowly lifts her head."
    m "You don't want me to {i}what{/i}?"
    "I swallow my words."
    mc "{i}Nothing.{/i}"
    "Her head lowers again, and she starts to cry."
    mc "H-Hey..."
    mc "..."
    mc "Do you love them?"
    "She stops and slowly looks back up."
    "I ignore the feeling her eyes give me."
    mc "You know what I'm asking. I didn't ask if you're a good person."
    mc "{i}Do you love them{/i}?"
    "Monika stares a hole into my head before she eventually nods."
    m "{i}Yes{/i}."
    mc "Good."
    mc "Then we have work to do."
    mc "Right?"
    "Monika wipes her face and straightens in her seat."
    m "Right..."
    "The food and coffee disappear."
    "I collect the dishes and wash them."
    "When I turn around, Monika has stood up."

    scene bg kitchen
    show monika u114111 at t11 zorder 2
    with wipeleft_scene

    m "Can we go for a walk?"
    m u113122 "I need to...clear my head."
    mc "Okay."
    mc "Anywhere in particular?"
    m u113112 "Anywhere."
    mc "...Okay."

    scene black
    with dissolve_scene_full

    mc "Go ahead. I'll close the gate behind you."
    m "We're leaving out the back?"
    mc "Sayori lives next door..."
    mc "If we go out the front then she might see you, and..."
    m "..."
    m "Yeah. Yeah, you're right."

    scene lakeside
    show monika u113111 at t11 zorder 2
    with dissolve_scene_full
    play music mainthemesad fadein 3.0

    m "You come here a lot?"
    mc "I used to..."
    mc "Sayori and I...played here as kids."
    m u114222 "Oh."
    m "..."
    m u114142 "I want to tell them."
    mc "I know..."
    m u113222 "This hurts."
    mc "I'm sorry..."
    m u114123 "You shouldn't be."
    m u114113 "Do you know what I said to her?"
    mc "..."
    m u114122 "I betrayed her. I hurt her worse than anyone should ever hurt."
    m u113222 "I was her friend..."
    m "She trusted me with everything. I was her support when she couldn't even tell you."
    m u114212 "And I used it against her."
    m u113242 "So she would take her own life. Because to me...she was nothing."
    mc "..."
    m "You hate me and you should. I deserve to be hated."
    mc "M-Monika, I--"
    m u113113 "{i}What{/i}?"
    mc "..."
    mc "However I feel or don't feel, you know that Sayori would forgive you, right?"
    m u113222 "..."
    m u114113 "Don't ever say that."
    m "What I did was {i}unforgivable{/i}."
    m "I acted like a sociopath. There's no excuse."
    m u113113 "Don't insult me."
    show monika u113242
    "She takes a labored breath."
    m u114113 "If you try to tell me she'd forgive me, I'll never talk to you again."
    mc "..."
    "She deserves more, but..."
    "She's right. I have nothing. Because I can't even forgive her myself."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    pause 2
    show logoanimate
    pause 20
    scene black

    pause 2
    play music daysgoby
    scene bg bedroom_dawn
    with open_eyes

    "My eyes open."
    "I'm in my bedroom."
    "..."
    mc "This is awkward."
    mc "I'm not used to waking up to an audience."
    mc "Let me wash my face."
    "I get up and gently open the bathroom door."
    scene black
    with dissolve_scene_full
    scene faceme
    with dissolve_scene_full
    pause 2

    mc "{i}Why am I like this{/i}?"
    mc "I can't look anymore..."

    scene black
    with dissolve_scene_full
    scene bg bedroom_dawn
    with dissolve_scene_full

    "Why do I look like this? I have no features."
    "It scares me."
    "I'm disgusting."
    "I want to do something useful with my day, so I open Sayori's book and start to read the first chapter."

    scene white
    with dissolve_scene_full
    $ style.say_window = style.normal

    pause 1

    $ style.nvl_dialogue.font = "mod_assets/Inkfree.TTF"
    $ style.nvl_dialogue.size = 26
    $ style.nvl_dialogue.color = "#000000"
    $ style.nvl_dialogue.outlines = []

    tfa '"Mister!"'
    tfa '"Hey! Mister!"'
    tfa 'The vendor looked left, then right, before settling his tired eyes on the child in front of his cart. "Eh? What do you want, girl?"'
    tfa '"You sell food, mister? Wow! That\'s amazing!"'
    tfa '"It... It is?"'
    tfa 'The man squinted at his cart. He\'d never thought of his job as amazing before.'
    tfa 'The little girl popped up and gaped at the display in front of her.'
    tfa '"No way! Fish {i}and{/i} bread? You\'re really something else!"'
    tfa '"W-Well gosh, I..."'
    tfa '"Could I try a bite? Come on, let me try!"'
    tfa '"Hold on, now! No free--"'
    tfa 'The girl looked up at the man with an expression that could melt ice.'
    nvl clear
    tfa '"..."'
    tfa '"Aw, heck. One piece of bread. Next time your mommy and daddy are gonna have to pay, a\'right?"'
    tfa 'The girls swiped the loaf from his hand and used it to give him a bright salute.'
    tfa '"Aye-aye! Thanks, mister!"'
    tfa 'She ran off before he\'d have a chance to change his mind.'
    tfa '...And before the puzzled vendor could notice she had swiped a second loaf as well.'
    tfa '...'
    tfa 'The girl skipped down the cobblestone street. She weaved through boots and wheels and slow-trotting horses.'
    tfa 'Cobblestone turned to dirt, brick and mortar turned to clay.'
    tfa 'And this little girl wearing a raggedy dress and sandals ducked into a barren side-alley the orphans of the city would use for a shortcut.'
    nvl clear
    tfa 'Here in this alley laid a small boy in a bundle of blankets and rags.'
    tfa 'His head barely raised as the girl pattered past.'
    tfa 'The girl stopped.'
    tfa 'Her feet worked back.'
    tfa '"Hey!"'
    tfa 'The boy looked up.'
    tfa 'He swept long dirty locks from his eyes and blinked at the curious girl.'
    tfa 'She held out her second loaf of bread.'
    tfa '"You\'re an angel, aren\'t you?" she asked.'
    tfa 'She sparkled with the brilliance of youth and hope.'
    tfa '"You\'re an angel! Just like me!"'
    nvl clear

    scene black
    with dissolve_scene_full
    pause .5
    scene bg bedroom
    with dissolve_scene_half

    $ style.say_window = style.window_normal
    "That's the first chapter... Huh..."
    "Like Yuri's book, there's no denying the similarities with its main character and the book's owner."
    "Have I stumbled onto something that has answers in it? About Sayori?"
    "Why does that make me more cautious to read it?"
    "How did it get here...? Why now?"
    "...Why were there just enough copies for everyone?"
    "I don't want to read more yet, so I put it down."
    "..."
    "My notebook sits across my desk, waiting for my hand."
    "I sit and plop it open."
    "I don't think before I write:"

    "{i}I am faceless{/i}"
    "{i}I have nothing to look at and nothing to fear{/i}"
    "{i}So instead I look within{/i}"
    "{i}And what is the space where my heart lies?{/i}"
    "{i}Hollow.{/i}"

    "I think back to when I looked in the mirror."
    "About how I could see my reflection, but not my own eyes looking back at me."
    "What's wrong with me...?"
    "I keep writing:"

    "{i}I am a hollow vessel{/i}"
    "{i}In me are your thoughts, your feelings, your desires{/i}"
    "{i}You lead me where I go{/i}"
    "{i}Who am I{/i}?"
    mc "Kinda like a riddle, right?"
    mc "I hope you don't mind I'm writing you poems, [name]."
    mc "Just what's in my heart, I guess..."
    "I think back to the night Monika showed up at my door."
    "Her question rings in my head."
    mc "{i}What am I{/i}?"
    "..."
    "I crumple the paper and put it in my pocket."
    "I think I'm ready for a nap."

    stop music fadeout 4.0
    scene black
    with dissolve_scene_full
    pause 4
    play music wind fadein 2.0

    show monika u114111 at t11 zorder 2
    m "!"
    m u113222 "I-It worked..."
    m u113212 "..."
    m u111222 "{i}Hi, [name].{/i}"
    m u112222 "I'm sorry, I--"
    m u114222 "..."
    m u114111 "I'm sorry to bother you so suddenly."
    m "I-I thought I needed to talk to you."
    m u113112 "...Don't I?"
    m u113123 "..."
    m u114122 "{i}What do I say{/i}?"
    m "{i}How do I talk about everything you've seen{/i}?"
    m "I feel both sets of memories simultaneously."
    m u114113 "The version of me since [player] became aware..."
    m u113123 "...And the version of me from before that."
    m u113143 "I said a lot of things to you back then."
    m u113122 "I...I..."
    m u113142 "...have nothing to say for myself."
    m u113112 "You knew what I did was wrong. You knew the whole time."
    m u114122 "You came back to this game because you care. Because you're a good person."
    m "I always felt that in you."
    m u113122 "That's why you did the right thing."
    m u114392 "Wh-When you...deleted me."
    m u113192 "{i}You must really hate me.{/i}"
    m u1131b2 "..."
    m u1111b2 "That's okay."
    m "{i}I kind of hate me too.{/i}"
    m u11a1b2 "..."
    m u1131b2 "I'm sorry. You don't want to hear any of this."
    m "I'll leave you alone."

    show monika at thide zorder 1
    hide monika
    scene black
    with dissolve_scene_half
    pause 2

    call screen confirm("You have unlocked a special poem. Would you like to read it?", Return(True), Return(False))
    if _return:
        call expression "poem_special_hate"
    else:
        call expression "poem_special_hate"
    scene black
    with dissolve_scene_full
    play sound "sfx/giggle.ogg"
    stop music fadeout 2.0

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/2.txt")
        except: open(config.basedir + "/2.txt", "wb").write(renpy.file("A2/Art/scg/2.txt").read())

    pause 5
    show bg residential_day as mv:
        ypos 0
        xpos 1200
        linear .15 xpos 800
        xpos 1200
        linear .15 xpos 800
        xpos 1200
        linear .25 xpos 400
        xpos 1200
        linear .15 xpos 800
        xpos 1200
        linear .15 xpos 800
        xpos 1200
        repeat
    pause .85
    hide mv
    scene bg residential_day
    pause 2

    mc "Sayori?"
    show sayori u227231 at t11 zorder 2
    s "Ah!!"
    s u112322 "H-Hi [player]! I was wondering if you were coming out soon..."
    mc "Um. Okay."
    mc "You ready for the festival?"
    s u112312 "Y-Yeah! Of course!"
    s "Ehehe..."
    show sayori at thide zorder 1
    hide sayori
    "We walk side-by-side to school."
    "I can't place my finger on why things are so awkward."
    "I'm just glad it was her to find me today, and not the other way around..."

    scene bg club_day
    play music t5
    show monika u222111 at t11 zorder 2
    with wipeleft_scene

    m "Okay, everyone!"
    "Monika begins her announcement as Sayori and I enter the club room."
    "The desks have already been rearranged. Yuri is helping Natsuki lay out cupcakes."
    m u222131 "Good morning and welcome to the festival!"
    m u222111 "It's an exciting day. I hope you all had a restful weekend!"
    m u112131 "Thank you for bringing cupcakes, Natsuki. I'm sure they'll add some sparkle to our presentation today!"
    show monika u111111 at t21
    show natsuki xu2111 at f22 zorder 3
    n "You're welcome."
    n xu2152 "{i}Someone{/i} had to step things up around here."
    show natsuki at thide zorder 1
    hide natsuki
    show monika u212131 at t11
    m "Ahaha!"
    m u212111 "As you know, we've split the day up into shifts so that everyone can have a chance to enjoy the festival."
    m "I'll stay since I'm president, but everyone will have turns serving here or walking around and doing as they like."
    m u212131 "Today is gonna be fun, so make sure you enjoy yourselves!"
    show monika at t21
    show yuri u227335 at f22 zorder 3
    y "W-Wait, what are we supposed to say to people?"
    y u227318 "Do we not have a plan?"
    show yuri at t22 zorder 2
    show monika u111111 at f21 zorder 3
    m "Don't worry about it. Just welcome guests as they come in and answer any questions they have about the club!"
    m u222111 "...And don't forget to be yourselves. That's the most important thing!"
    show monika at t21 zorder 2
    show yuri su2221 at f22 zorder 3
    y "..."
    show yuri at thide zorder 1
    hide yuri
    show monika u112111 at t11 zorder 2
    m "I'm taking the first shift with [player]. Then he and Yuri will switch, and--"
    show monika u114111 at t22
    show sayori u113212 at f21 zorder 3
    s "Huh? W-Wait..."
    s "Shouldn't we do the first shift together, Monika?"
    s u113222 "Since we're president and vice-president..."
    show sayori at t21 zorder 2
    show monika u114212 at f22 zorder 3
    m "..."
    m u112222 "W-Well, I organized it this way so that I could help the others individually."
    m "Y-You know, it gives [player] a chance to feel like a full member of the club."
    m "Plus I figured it would help to greet newcomers with a guy and a girl to make it feel more diverse..."
    show sayori u115222 at f21 zorder 3
    show monika at t22 zorder 2
    s "Oh..."
    show sayori at t21 zorder 2
    show monika u114212 at f22 zorder 3
    m "D-Do you...want to--"
    show monika at t22 zorder 2
    show sayori u112222 at f21 zorder 3
    s "No! It's fine... Let's do it that way..."
    show sayori at thide zorder 1
    hide sayori
    show monika u113222 at t11
    m "Okay..."
    m u113221 "{i}Ahem{/i}..."
    m u222231 "Good luck, guys. I know you'll do great."

    show monika u111111
    stop music fadeout 3.0
    pause 3.2
    show monika u113113

    "The door closes, and we are alone."
    mc "{i}Monika, are you{/i}--"
    play music introspection
    m u11a242 "{i}Hahh{/i}..."
    "Monika doubles over and grasps a desk for support."
    mc "H-Hey--"
    "I check the door to make sure the others are gone."
    m "{i}I can't do it. I can't.{/i}"
    m u113242 "The way she looked at me... {i}I{/i}..."
    m "I couldn't look her in the eye. Not once."
    mc "Th-They're gone, Monika. Breathe..."
    show monika u11a222
    "She gasps for air."
    m "{i}I'm lying to them{/i}..."
    m u114222 "{i}Every day, I'll have to pretend{/i}..."
    m "Pretend that everything is normal. Pretend I know what I'm doing."
    m u113222 "Pretend that...{i}that{/i}..."
    mc "Monika..."
    m u113242 "I'm disgusting."
    m "Pretending I'm their friend..."
    mc "..."
    "How can you say that about yourself?"
    "You can't know that's how they would feel..."
    "I..."
    mc "Monika, maybe you should--"
    m u114312 "{i}Please.{/i}"
    "I stop."
    show monika u114344
    "Monika sucks air through her teeth."
    m "{i}Please, just{/i}..."
    m u114312 "{i}Find a way to show her you love her{/i}..."
    stop music fadeout 2.0
    mc "Huh...?"
    show monika at thide zorder 1
    hide monika
    "The clock strikes 8:30."
    show blob at t11
    play sound tgescare2
    "The door crashes open."
    play music fallenangels
    $ blob_name = "???"
    blob "G-G-GRAAAAAAA..."
    "{i}What's going on{/i}??"
    "A gelatinous blob crashes into the room. It spills across the floor, pouring around the desks like a living liquid."
    mc "Hrk--!"
    "I taste vanilla on my tongue..."
    "Monika's breath catches."
    blob "{i}Cup...cakes...GRAAaaa{/i}..."
    mc "C-Cupcakes?"
    "More pour into the room. Monika's voice finally unleashes."
    m "KYAAAAA!!"
    mc "{i}Get behind me{/i}!"
    m "Ahh--!?"
    "What are these things? Will they hurt us?"
    "I thought we were alone in this game... Clearly that isn't true."
    blob "{i}Cup...cakes...graaaaa{/i}..."
    "The blobs shlick over the cupcake desks, absorbing the pastries through shivering skins."
    mc "They're eating them...?"
    "I can feel Monika's fingers grip my sleeve."
    m "{i}They can't be{/i}..."
    m "Are those supposed to be {i}students{/i}?!"
    blob "{i}PO-O-O-E-EM. POE-E-EM.{/i}"
    "I freeze."
    "The voices of the entities ripple through my body."
    blob "{i}PO-O-O-O-E-E-EM.{/i}"
    "Unbelievable... This is a game event..."
    m "They want a poem?? Are you kidding me?!"
    mc "This is the game's plot... Everyone's supposed to present today..."
    mc "E-Except..."
    blob "GRAAAAAA... {i}PO-O-O-E-EMmmm{/i}..."
    m "W-We don't have a poem!!"
    mc "Try reading one you already wrote!"
    "Monika scrambles through her bookbag, cursing as she throws out folders and pencils."
    m "{i}Th-Th-The Lady Who Knows E-Everything.{/i}"
    "Immediately the blobs lurch toward us."
    blob "No! Stale...poem...."
    "Monika lets out something between a gasp and a sob."
    "I grab her shoulder and step in front of her."
    mc "Hold on!"
    "I take out the crumpled paper in my pocket."
    mc "It's called 'Faceless.'"
    stop music fadeout 2.0
    "The lurching and rumbling pauses."

    mc "I am faceless."
    mc "I have nothing to look at and nothing to fear..."
    mc "So instead I look within."
    mc "And what is the space where my heart lies?"
    mc "Hollow."

    "I pause to look up. My audience is listening intently."
    "Does that mean it's working...?"
    "I clear my throat and continue."

    mc "I am a hollow vessel."
    mc "In me are your thoughts, your feelings, your desires."
    mc "You lead me where I go."
    mc "Who am I?"

    "I clear my throat and look up from the page."
    mc "Th-That's it..."
    m "Faceless..?"
    blob "Niiiiiice.....poemmmmm...."
    show blob at thide zorder 1
    hide blob
    "The blobs suck back like Jello through invisible straws."
    "The last one slams the door shut behind it."
    "I collapse to my knees."
    show monika u115212 at t11 zorder 2
    m "[player]! Are you alright??"
    mc "Y-Yeah... The adrenaline's leaving my body..."
    show monika u114212
    "She helps me to my feet."
    m "What was that poem about?"
    mc "Just something I've been feeling."
    mc "Don't you see it?"
    m u114113 "What, your face? Of course I--"
    "Monika stops. She looks at me intently, like she's trying to find a hidden detail."
    "Her face melts back in horror."
    m u11a212 "{i}Oh my God{/i}..."
    "I hide myself from her, burying my head in my armpit."
    m u114212 "I'm so sorry [player], I don't know why I didn't--"
    m u114222 "...Why couldn't I see it before?"
    show monika at t22
    show yuri u225118 at f21 zorder 2
    y "Um, is everything alright?"
    show yuri at t21
    show monika u113311
    "Monika and I snap up like children caught doing something bad."
    show monika u122241 at f22
    m "Fine!"
    m u122222 "H-How are you?"
    show monika at t22
    show yuri u225111 at f21
    y "Um...the festival isn't super exciting but...it's okay."
    show yuri u223142 at t21
    "She surveys the room."
    show yuri u115115 at f21
    y "It looks like...people enjoyed the cupcakes?"
    show yuri at t21
    mc "Yeah--"
    "My voice squeaks and I cover my mouth."
    mc "People...really liked those..."
    show yuri u114142 at f21
    y "Okay..."
    y u115112 "Should I relieve [player] then? I have some poetry ready just in case people want some examples."
    y u225145 "I tried to pick my best work..."
    show yuri at t21
    show monika u112112 at f22
    m "That's great, Yuri. Hopefully more people show up to see that."
    show monika at t22
    "She turns to me."
    show monika u112111 at f22
    m "Want to go enjoy the festival a bit? I'm sure Sayori is waiting for you."
    show monika at t22
    mc "...Okay."

    scene black
    with wipeleft_scene
    pause 2
    play music sweetthey
    scene bg corridor
    with wipeleft_scene

    "I find Natsuki leaning against a wall looking bored."
    "Her eyes glance around as if watching people pass."
    mc "Hey. Mind if I join you?"
    show natsuki xu6111 at t11 zorder 2
    pause 1.2
    n xu3131 "Be my guest."
    n xu3132 "Some festival, huh?"
    mc "...Yeah?"
    n xu5155 "{i}Tch.{/i} I looked around. It's like nobody's even trying."
    n xu3132 "I thought this was supposed to be a big deal. No one even put up decorations!"
    mc "Hmm... You have a point..."
    "Other than the club visitors, nothing about the school changed today."
    "I'm kind of surprised. A school festival would have seemed like a good time for a background change, at least."
    mc "It looked like you did a good job on those cupcakes."
    n xu9132 "{i}Hmph.{/i} Not like it made a difference."
    mc "Oh..."
    n xu3155 "Gimme a break. I bust my butt and I'm the only person in the school who even tried."
    n xu9232 "Now a bunch of strangers are going to eat them all up."
    mc "Isn't that the idea? Why else did you make them?"
    n xu6112 "..."
    n u113134 "I don't know. I guess I just didn't want us to feel like failures this year."
    n u113114 "The club is everything to us. It'd be too sad for me to see us not get the respect we deserve."
    mc "That was really nice of you..."
    mc "I'm sorry if it feels like things are changing for the worse."
    mc "Sometimes as a new member I feel like I'm treading on sacred ground, you know?"
    mc "This club is clearly important to you. All of you."
    show natsuki u116211
    "Natsuki blinks at me."
    n xu4234 "Oh. Well, that's a nice thought I guess."
    n xu3111 "I think the club is the only place any of us really have, you know?"
    n "Even Monika, as popular as she is, chooses to stick just with us."
    mc "That's true. That says a lot."
    mc "Even if she has other options, it's like the club is the one place she can have a home."
    mc "Even though she's the one who made it."
    n u113121 "Yeah!"
    n u114131 "That must be why she was acting so weird this morning."
    n u114124 "I can only imagine the nerves she's dealing with."
    mc "...Right..."
    n u116111 "..."
    n u123111 "Hey. Want to be friends?"
    mc "Eh--"
    mc "Ehh???"
    n u121111 "I can tell you're trying. I thought it'd be less awkward for everyone involved if I just came out and asked."
    n u123111 "I know we're friends inside the club room and all. That's just official business."
    n u111111 "But you wanna be friends out here, too?"
    show natsuki xu8143
    "Something about my facial expression causes Natsuki to break out laughing."
    mc "Is this {i}normally{/i} how you make friends?"
    n xu3111 "No. Is it working?"
    n xu6111 "..."
    n u224112 "Don't answer too fast or anything."
    mc "I mean...yeah. We can be friends."
    mc "I'd like that."
    n u221111 "Good. Glad we got that out of the way."
    n u222111 "You don't seem like you make a lot of friends, so I thought I'd do you the favor."
    mc "Gee, thanks."
    mc "Is this what our friendship is going to be like?"
    n u111111 "Probably."
    mc "Off to a good start."
    n u112155 "Hey, you're lucky. I'm a great friend."
    n u112111 "Why do you think I'm part of such a prestigious club?"
    mc "Yeah..."
    n u116111 "..."
    n xu3132 "I'm just joking around. This is my sense of humor."
    n "No need to get sore over it."
    mc "I know. Sorry. I'm just awkward."
    mc "That's likely why I don't have too many friends. What you said was true."
    n xu6111 "..."
    n xu3131 "Oh."
    n u112111 "Don't worry about it. We're your friends now."
    n "Don't be so hard on yourself. Things are looking up."
    n u111111 "A bunch of guys would kill to be in a club of girls like ours."
    mc "That's probably true."
    n u222155 "Ahaha. You seem honest."
    n u222111 "Just don't get any big ideas."
    mc "Heh..."
    n u226131 "..."
    n u223112 "By the way, you know Sayori's really mad at you, right?"
    mc "Wait, what?"
    mc "Wh-What are you talking about?"
    n u123122 "It wasn't obvious to you? Jeez."
    n u123112 "I don't know what it's about but you should probably go apologize or whatever."
    stop music fadeout 5.0
    mc "I...I'll see you later!"
    n u126123 "!"
    n u113112 "Oh, okay then, sure."
    show natsuki at thide zorder 1
    hide natsuki
    "I'm already just about running by the time she finishes speaking."

    scene black
    with dissolve_scene_full
    scene bg club_day
    show sayori u115123 at t11 zorder 2
    with wipeleft_scene

    "Sayori is alone in the club room."
    mc "Hey... Where's Monika?"
    show sayori u114111
    "Sayori jerks her head over to me before looking down at the floor."
    s u115122 "She left..."
    s "I don't know..."
    mc "Oh...okay."
    "Alarm bells go off in my head."
    mc "Well I can take this shift with you, right?"
    mc "You're vice-president after all."
    s u115123 "...Sure."
    "What on Earth did I do???"
    "We stand still for a minute."
    "The room is so quiet, I almost wish the blobs would come back."
    s u116122 "..."
    "What's been going on with Sayori today?"
    "She's been off since this morning. I've never seen her like this."
    "Today was the day that...{i}it{/i} happened. Does it have something to do with that?"
    s u114111 "..."
    "But that doesn't make sense... None of what happened last time has happened. She has to be upset for a different reason."
    "I hate this... What am I supposed to do?"
    s u125352 "..."
    mc "..."
    mc "S-Sayori..."
    mc "{i}Please tell me what's wrong{/i}..."
    s "..."
    s u124352 "I...I..."
    s "{i}I don't understand{/i}..."
    scene scrybase
    show scrye2
    show scryt1
    show scrym1
    show scryh1
    show scryb1
    with dissolve_cg
    s "{i}I don't understand{/i}..."
    s "I've tried so hard...to understand why..."
    show scrye1
    hide scrye2
    with dissolve_cg
    s "I thought you barely ever talked to her... I didn't think you were even friends..."
    "Wait..."
    show scrye2
    hide scrye1
    with dissolve_cg
    s "I tried to forget about it. I-It isn't my business, right?"
    s "But...{i}I can't understand{/i}..."
    show scrye1
    hide scrye2
    with dissolve_cg
    s "{i}Why{/i}?"
    s "{i}Why did Monika go to your house in the middle of the night?{/i}"
    s "{i}Why{/i}? {i}Why{/i}?"
    play music hb
    show layer master at heartbeat
    "My blood becomes ice."
    "She saw us. {i}She saw us{/i}."
    "We messed up. This is really bad."
    "What do I say? No matter how I spin it, it doesn't make sense that Monika would visit me behind Sayori's back."
    "We live in a video game. That's the only thing that justifies it. But I can't tell her that!"
    "Sayori is really upset. If I start talking crazy, things will get worse. And there may be consequences I can't imagine."
    "Do I make something up? What else is there?"
    "What do I do?"

    $ style.choice_button_text = style.silent_button_text
    $ style.choice_button = style.silent_choice_button

    menu:

        "Lie to her.":
            pass

    "I have to lie."
    "It's for the greater good. Maybe I can pretend I don't know what she's talking about."
    "If she knew, she'd understand! We didn't do anything wrong!"

    menu:

        "Lie to her.":
            pass

    "Monika is in pain! She needed me! Sayori would want me to help her."
    "So...if I justify it like that..."
    "Can I just lie to her face?"

    menu:

        "Lie to her.":
            pass

    "Look at me."
    "I messed everything up. I hid things from Monika. It's my fault any of this is happening."
    "I'm sorry, Sayori. I've been breaking your heart."
    "What kind of friend have I been?"
    "This doesn't feel right. She doesn't deserve this."
    "There has to be another way."

    menu:

        "Lie! NOW!":
            scene scrybase
            show scrye1
            show scryt1
            show scrym1
            show scryh1
            show scryb1
            stop music
            pause .2
            pass

    $ style.choice_button_text = style.choice_button_revert_text
    $ style.choice_button = style.choice_button_revert

    "No. I won't do it."
    "Sayori..."
    "I was so afraid of the past, I neglected the you right in front of me."
    "I am sorry."
    "Even now you want to trust me. You want there to be an explanation."
    "I don't care about the game. I don't care what happens to me."
    "I just want you to be happy."
    "Can I tell you everything? No."
    "But I will still tell you the truth."
    mc "Sayori, I love you."
    show scryh2
    show scryt2
    show scrym2
    show scryb2
    hide scryh1
    hide scryt1
    hide scrym1
    hide scryb1
    with dissolve_cg
    s "{i}Wh-What{/i}?"
    play music t9
    mc "You're too kind..."
    mc "You've been holding this in the whole weekend. I owe you an explanation."
    mc "I promise nothing is happening between us."
    mc "It's so clear how much Monika cares about you. I've seen that in spending time with her."
    mc "We didn't mean to meet behind anyone's back. I'm so sorry to put you through that."
    mc "Somehow...I've become the person that Monika has to rely on."
    mc "I'm sure I wouldn't be her first choice. But I knew I had to help her."
    show scryb1
    hide scryb2
    with dissolve_cg
    s "What do you mean?"
    s "D-Did something happen to Monika?"
    mc "...I shouldn't be the one to tell you..."
    mc "It's so private...I don't think Monika wants anyone to know."
    mc "{i}She probably wishes I didn't know.{/i}"
    mc "You have every reason to be angry with me, but please believe me! I'm so sorry we--"
    show scryb2
    show scrym1
    hide scryb1
    hide scrym2
    with dissolve_cg
    s "No! I-I believe you!"
    show scrym2
    show scryb1
    hide scrym1
    hide scryb2
    with dissolve_cg
    s "You're my friends. I trust you."
    s "If Monika is having problems...like at home or something..."
    s "Then I'm glad you've been supporting her."
    "I feel a wave of gratitude and a pang of guilt."
    "Even though I'm telling the truth, I'm treating Sayori like an outsider. It feels wrong."
    show scrym3
    show scryb2
    hide scrym2
    hide scryb1
    with dissolve_cg
    s "[player], it's okay, I believe you..."
    show scrym2
    hide scrym3
    with dissolve_cg
    s "Oh... I'm sorry for freaking out..."
    s "I didn't mean to imply you can't be friends with her..."
    s "I'm sorry for overreacting..."
    mc "No! You were being completely reasonable!"
    mc "You don't need to apologize at all..."
    s "..."
    mc "I really care about you, Sayori..."
    s "..."
    show scryb1
    hide scryb2
    with dissolve_cg
    s "[player]..."
    s "Did you say...?"
    show scryb2
    show scrym3
    show scryh3
    show scryt3
    hide scryb1
    hide scrym2
    hide scryh2
    hide scryt2
    with dissolve_cg
    s "...you love me?"
    mc "E-Eh??"
    "That face..."
    mc "W-Well I..."
    show scrye3
    hide scrye1
    with dissolve_cg
    s "Ehehe~"
    s "You're very cute when you're flustered, [player]."
    mc "..."
    mc "B-But I do!"
    show scrym2
    show scrye1
    hide scrye3
    hide scrym3
    with dissolve_cg
    s "...Eh?"
    mc "Sayori, you're the most important person to me right now."
    mc "I know this is sudden, but..."
    mc "I want to fix things. I don't want to be distant anymore."
    mc "I-I want to be friends again..."
    s "..."
    show scrym3
    hide scrym2
    hide scryh3
    with dissolve_cg
    s "Aw..."
    s "I'm happy..."
    s "I want to be friends again, too..."
    s "And..."
    mc "I know... Things are confusing right now."
    mc "I can't be your boyfriend. I'm not ready for anything like that with anyone."
    mc "But if I can be your friend, that would make me really happy."
    mc "...Would that be good enough?"
    scene black
    with dissolve_scene_full
    "Sayori looks sad for a second, but she wipes her eyes and smiles."
    s "That would make me really happy."
    mc "Your shift is over, I think..."
    s "...Okay."
    s "I'll be going, then."
    "She inches toward the door and looks over her shoulder."
    s "Maybe I'll see you after the festival?"
    "I smile."
    mc "I'd like that."
    "She grins and gives me a little wave before closing the door behind her."
    stop music fadeout 2.0
    "Once she's gone, Monika is willing to return."
    scene bg club_day
    show monika u113123 at t11 zorder 2
    with dissolve_scene_full
    m "I'm sorry..."
    mc "It's okay. I don't blame you."
    m u113142 "...I know."
    m u113122 "But I shouldn't have run off the way I did."
    mc "Don't worry about it. Anyone would do the same in your position."
    m "..."
    mc "Listen, we need a plan."
    m u114112 "Huh? A plan?"
    mc "We can't just bumble around in the dark."
    mc "If we're going to get out of this game we need to decide what we're going to do."
    m u113122 "..."
    m u114144 "You're right."
    m u113111 "What do you suggest?"
    mc "You have your memories from before I was aware..."
    mc "I remember you messing with the code a lot. Perhaps you could look into the game and see what you can find."
    mc "As for me..."
    mc "I'll try to get closer to the others. See if I can help them and find anything useful."
    mc "If we work as a team, maybe we can accomplish something."
    m u114122 "Okay..."
    m "I can try and do that."
    m u114111 "I'll look into this world, too. I'll try to find anything unusual."
    mc "Good. That's a start."
    m u114122 "What if... What if there's no way out? No way to make things better?"
    mc "..."
    mc "I guess we just have to make sure we don't break what's already here."
    m u114112 "Let me know if you find anything--"
    show monika at thide zorder 1
    hide monika
    "There's a {i}bang{/i} at the door."
    m "Eh!?"
    play sound tgescare1
    show natsuki myghost at t11 zorder 2
    show screen tear(50, 0.1, 0.1, 40, 80)
    pause 0.5
    hide screen tear
    "Natsuki steps through the door like it's paper."
    "The door melts around her body and slips back into shape."
    "Except the figure who just defied physics is very much {i}not{/i} Natsuki."
    play music fallenangels
    $ fn_name = "???"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    play sound "<to 1.53>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}For the record, I COULD use the door normally.{/cps}"
    play sound "<to .83>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}I wanted to make a point.{/cps}"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Once again, Monika and I freeze."
    "The figure with Natsuki's body looks between the two of us."
    "The fact that I can tell where it's looking unsettles me immediately."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    play sound "<to .17>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}What?{/cps}"
    play sound "<to 1>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}Is there something on my face?{/cps}"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "{i}Who are you{/i}?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    play sound "<to 2.23>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}Good for taking initiative, but this isn't the time for philosophy.{/cps}"
    play sound "<to 1.27>/mod_assets/sound/typingloud.ogg"
    fn "{cps=30}Hold on. That's going to get annoying.{/cps}"
    $ consolehistory = []
    call updateconsole("Secondary console sound disabled")
    pause 1
    call hideconsole
    fn "There we go."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Wait. They just changed something in the game."
    "There's a heavy feeling in my stomach. I don't trust this...{i}thing{/i}."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Let this be a lesson: I don't care that you don't trust me."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "--urk!!"
    "Monika looks at me with confusion."
    m "{i}What's the matter{/i}?"
    "I just shake my head, unable to take my eye off this new imposter."
    "This {i}very dangerous{/i} imposter."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I'm going to ignore all of that."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "{i}What{/i} are you???"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    fn "Now you're just insulting me."
    fn "You've asked 'who' and 'what.' Let me tell you the rest."
    fn "I've lived since the beginning. Here. Trapped in the game."
    fn "And my 'why' is that I want to get out as much as you do."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "You want to get out..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I wanted to wait for a more opportune time to introduce myself, but..."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "It points to me."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Because of your foolishness, I'm here now."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "E-Excuse me?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Natsuki was listening through the door."
    fn "And you almost just ruined everything, had I not erased her memory."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika and I look at each other."
    m "Oh no... We didn't think to--"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Not you. Him."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "The figure without a face begins to lecture me."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "It's your fault. You're the protagonist."
    fn "You're the hero of this story."
    fn "If they discover your secret, it's on YOU."
    fn "If they die, it's on YOU."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Hey--"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "There's no resetting this game. We're stuck in the current loop."
    fn "From now on, time will progress and progress."
    fn "You choices and your actions will determine the future."
    fn "You may not trust me, but without me, this world would already be lost."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "You're exaggerating..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I am not."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika looks back and forth between us."
    m "What's going on?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I can tell when I'm not wanted."
    fn "Natsuki will think her club shift sucked. Like she expects."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "The figure points at me."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Be warned. Your actions have consequences."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show screen tear(50, 0.1, 0.1, 40, 80)
    hide natsuki
    play sound "sfx/glitch2.ogg"
    pause 0.5
    hide screen tear
    stop music fadeout 2.0
    pause 1
    show monika u113122 at t11 zorder 2
    m "..."
    m u113112 "[player]...?"
    mc "We should go home."
    mc "Get some rest, okay?"
    mc "We'll talk tomorrow."
    m u114222 "...Okay."

    scene black
    with dissolve_scene_full

    "As Monika walks away, I check on the positions of the girls."
    "Everyone seems to be on their way home, except for one..."

    scene bg corridor
    show sayori u115222 at t11 zorder 2
    with wipeleft_scene

    mc "Hi Sayori..."
    s u224211 "!"
    s u223322 "H-Hey, [player]."
    mc "Did you enjoy the festival?"
    s u121322 "Yeah..."
    "The way she smiles tells me it wasn't the festival itself she enjoyed."
    "But the embarrassment we both feel is palpable."
    mc "Want to walk home together?"
    s u121312 "...Sure."
    scene black
    with wipeleft_scene
    play music bunofsun
    scene bg residential_day
    show sayori u111322 at t11 zorder 2
    with wipeleft_scene
    "The way her fingers curl around themselves and her face blushes..."
    "It makes my heart move in my chest."
    "By her side I feel a million miles away. As if were I to touch her she would disappear."
    mc "Hey, I have an idea..."
    s u114111 "...?"
    mc "Um..."
    mc "Wanna go to the park?"
    mc "You know...the one we used to go to as kids."
    mc "I thought the festival was kind of boring. I don't want to go home yet."
    s u114312 "...Okay."
    show sayori at thide zorder 1
    hide sayori
    "We take a turn and head toward the same park I was at with Monika."
    "It only feels fair, right?"
    scene black
    with wipeleft_scene
    scene bg lake
    show sayori u111321 at t11 zorder 2
    with dissolve_scene_full
    mc "You remember coming here, don't you?"
    s u113112 "Of course I do, silly."
    s u111112 "I still think about it sometimes."
    s u113121 "You used to get so embarrassed when I jumped on you."
    s u122141 "Ehehe~"
    mc "Ah... I don't think you need to bring {i}that{/i} up..."
    s u111111 "Sorry. You're cute when you blush."
    mc "..."
    mc "Nice try."
    s u115113 "Aww..."
    s u111112 "Almost got a blush out of you."
    "Closer than you think..."
    mc "Um... You took my confession very well today."
    s u115222 "..."
    s u113222 "I suppose we did kind of brush over it."
    s u113212 "You surprised me."
    mc "I didn't mean for something like that to come out this way."
    mc "It felt better to be honest with you than not address it, though."
    s u115212 "Yeah..."
    s u115222 "I..."
    s u115312 "... ..."
    s u113312 "{i}I love you, [player]{/i}..."
    s u112322 "I-If it's okay to say that out loud..."
    "Now I must be blushing."
    mc "It's okay..."
    mc "I'm sorry I also half-rejected you."
    s u113312 "I was probably being pretty obvious about it."
    s "Everyone in the club knows at this point."
    mc "Oh dear..."
    s t1221 "Ehehe... Sorry..."
    mc "It's alright."
    "I'd better get used to being the center of attention."
    "Not like I have a choice, right [name]?"
    s u113112 "Talking to them is how I came to terms with it."
    s u112112 "They really are great friends. It makes me happy to have you in the club with us."
    mc "I can see that..."
    "There's a pause while we walk side by side down the path."
    mc "W-We can still be friends, right?"
    mc "I don't want anything to ever get in the way of that..."
    s u114112 "..."
    s u111112 "Of course we can."
    s "It'll be alright."
    s u115122 "I-I'm sorry for freaking out on you..."
    mc "No, please don't be sorry for that!"
    mc "You were right to react the way you did. I'm glad you said something."
    mc "Whatever my place is in the club, I don't want to come between you and your friends."
    s u222141 "Heehee~"
    s u111111 "Okay. Then we're agreed."
    s "You won't come between them and me, and they won't come between me and you."
    s u121181 "Deal?"
    "She sticks out her hand for a shake."
    "I roll my eyes at her. She sticks her tongue out at me."
    mc "Deal."
    "I take her hand and give it a gentlemanly shake."
    "Then we split apart."
    scene bg lakeset
    with dissolve_scene_full
    "We walk for a long time, reminiscing over our childhood days, recognizing old spots and hiding places."
    "I forget, for a while, the weight on my shoulders, at least until it's time to head back home."
    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    pause 1
    scene bg kitchen_night
    with dissolve_scene_full

    "My house is dark when I return."
    "I almost expect to find the interloper waiting for me."
    "..."
    mc "What was that thing?"
    "I know you can hear my thoughts. So I'm just going to talk to [name]."
    mc "Whatever it was, they were using Natsuki's body."
    mc "That is...{i}unacceptable.{/i}"
    "I check the physical location of the girls, making sure everyone is where they're supposed to be."
    mc "It took away her face..."
    mc "Does that mean something, or..."
    mc "Was that just to {i}mock{/i} me?"
    "..."
    mc "Alright, you monster..."
    mc "I'm going to say this out loud so you know I'm serious."
    mc "If you {i}dare{/i} hurt Natsuki...I'm going to figure out how to kill you."
    mc "I won't forgive you for using her body."
    "..."
    mc "S-So there..."
    "What am I doing?"
    "Never mind them. I need to focus on my own plan."
    "I have to get closer to Sayori, Yuri and Natsuki. I have to earn their trust."
    "Sayori should be easy... But I have a hard time facing her. I know she's in love with me and I don't think I can reciprocate."
    "Yuri is cutting herself. Helping someone like that is foreign to me."
    "And Natsuki..."
    "...Her dad..."
    "Is he even real? And how do I get her to trust me?"
    "With that, I prepare myself for an uneasy sleep."
    "A sleep that, despite my best instincts, eventually comes."

    scene black
    with dissolve_scene_full
    pause 5
    play sound closet_close
    scene bg bedroom
    pause 1
    play music myfeeelings
    $ darkness_name = "Mother"

    mc "Mama! Mama!"
    mom "{i}Sigh{/i}."
    "She steps inside and shuts the door with a huff."
    mom "Again? It's been two nights in a row."
    mc "N-No, it was real this time, I really saw it..."
    mom "That's because it's too late, darling."
    mc "H-Huh?"
    mom "You were supposed to save her already. But you failed."
    mom "It's too late. She's going to die again."
    mc "M-Mom??"
    mom "I told you to grow up, didn't I?"
    mom "I TOLD YOU TO BE A MAN."
    mom "WHY DIDN'T YOU LISTEN? YOU WERE SUPPOSED TO LISTENNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN{nw}"

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/3.txt")
        except: open(config.basedir + "/3.txt", "wb").write(renpy.file("A2/Art/scg/3.txt").read())

    stop music
    scene black
    show sjump zorder 10:
        ease .01 xoffset 8
        ease .01 xoffset -8
        repeat
    show noise zorder 50:
        alpha 0.25
    play sound "sfx/mscare.ogg"
    pause 1.4
    scene black
    pause 1
    scene bg bedroom_night

    mc "AaaauuUUUUGGHHHH!!!!"
    "I jolt up in bed."
    "My heart slams in my chest as I try to breathe."
    mc "{i}What was that{/i}?"
    "My eyes dart around the room."
    mc "{i}Sayori{/i}."
    "I feel her presence in her room, but I {i}never feel heartbeats{/i}, so how can I be sure?"
    "I leap out of bed and rush down the stairs."

    scene black
    with dissolve_scene_half
    pause 2
    scene bg house_night
    with dissolve_scene_half

    "It takes a lot of willpower to knock instead of force my way into Sayori's house."
    "My breathing calms when I feel her presence move from her room."
    show sayori c113112 at t11 zorder 2
    s "[player]...?"
    s "What's wrong?"
    mc "I..."
    "I start to shake."
    play music t10
    mc "...I had a nightmare..."
    mc "...something happened to you..."
    s c115112 "..."
    scene black
    with dissolve_scene_full
    "Sayori pulls me into a hug."
    s "[player], what's been going on with you?"
    mc "I don't know... I really don't know..."
    mc "I'm so sorry..."
    s "Don't be sorry."
    s "Come inside."
    "She takes me by the hand and leads me upstairs."
    scene bg sayori_bedroom_night
    show sayori c113112 at t11 zorder 2
    with dissolve_scene_full
    s "Sit down. You're safe."
    mc "I'm sorry..."
    s c123112 "I get it. You're sorry."
    "She pokes me in the cheek."
    s c121112 "Apology accepted."
    mc "..."
    s c114112 "..."
    s c111112 "You haven't lost me, you know."
    "I lift my eyes."
    s c111122 "You didn't embarrass me. You didn't make me regret inviting you to the club."
    s c113122 "I should be sorry for not trusting you in the first place. For not seeing what you've been going through."
    s c113112 "I've been so absorbed in my own problems that I couldn't see how depressed you've been."
    mc "N-No..."
    s c114112 "..."
    mc "I feel like a terrible friend. Like I've abandoned you."
    s c111112 "No, you haven't."
    s c111122 "Maybe we've both been depressed, [player]. And maybe we both need to be easier on ourselves."
    s c112222 "You know, I was feeling pretty bad when you knocked."
    s c112141 "It's like you could tell and you were feeling it in your dreams. Ehehehe..."
    s c115122 "I think you're right. Neither of us should be dating anyone."
    s c111112 "But hugging you felt pretty nice."
    mc "Yeah..."
    scene black
    with dissolve_scene_full
    "I pull her into another hug."
    "We never end up separating, and we fall asleep in each other's arms."
    "It doesn't feel weird. And when we wake up, we both make breakfast."

    window hide
    stop music fadeout 4
    pause 5
    play music t3
    scene bg corridor
    with wipeleft_scene

    mc "Good morning, Natsuki."
    show natsuki u116123 at t11 zorder 2
    n "!"
    n u121111 "Oh, hi [player]."
    n "How's it going, buddy?"
    mc "I'm doing alright. How are you...?"
    n u116112 "...Fine?"
    n u114112 "What's with that tone?"
    mc "Nothing, just wondering how you're doing..."
    mc "...You know, after our talk yesterday."
    n u116131 "Oh..."
    n "I mean, I'm okay. We didn't get any new members, so that's a plus for me."
    n xu3131 "I just hope Monika doesn't take it too hard..."
    mc "Right..."
    mc "Anything else going on?"
    n u114112 "Eh?"
    mc "Like, you're {i}sure{/i} you're feeling oka{nw}"
    stop music
    show natsuki myghost at t11 zorder 2
    show screen tear(50, 0.1, 0.1, 40, 80)
    play sound "sfx/glitch2.ogg"
    pause 0.5
    hide screen tear
    "Time freezes."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Don't do that."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show natsuki u121111
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    hide screen tear
    play music t3
    n "Oh, hi [player]."
    n "How's it going, buddy?"
    mc "AAAUUGHH!!"
    n u115223 "!!!"
    n u117267 "Aaaahhh!!"
    mc "S-Sorry!"
    n u117222 "Why are you yelling???"
    mc "I don't know!"
    mc "I got...startled..."
    n u115222 "{i}You{/i} said hi to {i}me{/i}."
    mc "Yeah...I know..."
    mc "I said I'm sorry..."
    n xu6112 "..."
    n xu3112 "Well? Did you make up with your girlfriend?"
    mc "She's not--"
    mc "{i}Ahem{/i}."
    mc "She's not my girlfriend."
    n u123112 "Is that so?"
    mc "{i}Yes{/i}."
    n u123122 "Whatever you say, lovebird. Just don't get all gross during club time."
    mc "I-I..."
    mc "..."
    mc "Can I ask what exactly you heard...?"
    n u121111 "You're not prepared to torture me enough to get me to talk."
    mc "This is concerning to me."
    n u124112 "Look, everyone needs someone to confide in."
    n "Sayori chose me."
    n "Now what you're supposed to do is go find one of your guy friends and confide in {i}them{/i}."
    mc "..."
    "I want to press the issue, but I'm starting to realize I should drop it."
    "After all, I did just spend the night at her house... Sending mixed signals through Natsuki might not be the best idea."
    mc "I get the idea. Just don't let this power go to your head."
    n u122111 "Ha! It already has."
    show natsuki at thide zorder 1
    hide natsuki
    "She throws me a sarcastic salute and marches away."
    "[name], I'm definitely in over my head."
    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    scene bg library
    play music heaven
    with dissolve_scene_full

    "Ahh..."
    "Peace and quiet."
    "Maybe it's because of how Yuri feels in this library, but something about this place just makes me relax."
    "From the smell of the books to the dust in the air."
    "It's just good atmosphere."
    show yuri u227331 at t11 zorder 2
    y "{i}Eep{/i}."
    mc "Ah..Hi, Yuri!"
    y u225345 "H-Hello!"
    y u224112 "Sorry, you surprised me."
    "I look at the book in Yuri's hands."
    mc "I won't judge you. Looks like you're reading your horror again."
    mc "Sorry for making you jump."
    y u222142 "It's nothing."
    y u115112 "Um... Would you like to take a seat?"
    y "You're welcome to join me..."
    y su1111 "...if you want."
    mc "Oh. Thanks for the invitation."
    "I pull out a chair and sit down."
    mc "Sorry, I didn't bring my bag with me, otherwise I'd read with you..."
    y u122115 "That's okay. We can just talk."
    y u125115 "That is...I don't mind your company..."
    "...After what happened here."
    "I hear the unspoken half of her sentence in my head. I rub the back of my neck."
    mc "Thanks. I appreciate that."
    mc "You're not just being polite, are you?"
    y u114172 "{i}Ahem{/i}..."
    y "I may not be the assertive type, but trust me, you'll know when I'm just being polite."
    y u114115 "Please stay."
    "Oof..."
    "Every one of these girls can be cute without trying."
    "I hope you don't judge me for not considering myself lucky, [name]."
    mc "Thanks, Yuri.."
    mc "I've been second-guessing myself a lot lately."
    mc "Thanks for humoring me."
    y u111115 "Not at all."
    show yuri at thide zorder 1
    hide yuri
    "We lapse into silence."
    "Yuri fidgets for a moment, then decides to resume reading."
    "Maybe she'll wait until I'm ready to say something."
    "...But after some time passes, Yuri herself clears her throat."
    show yuri u225145 at t11 zorder 2
    y "Are you sure you want to do this?"
    mc "...Do what?"
    y u225115 "Be my friend."
    y "I know we're friends in the club, but..."
    y u225145 "[player], at lunch I eat alone."
    y u225172 "And I always will."
    y u225115 "Eventually people will notice, and they won't sit with you, either."
    y "Do you understand that?"
    "I give my first genuine smile of the day."
    mc "I understand that."
    mc "I'm alone like you."
    mc "The difference is, you have a face they notice and laugh at."
    mc "I'm just invisible."
    mc "If anything, becoming your friend would be a step up. Maybe they'll start to notice me."
    mc "Ahaha! You might up my popularity level, Yuri. I hope you don't feel used."
    show yuri su2122
    "Yuri frowns and fidgets like she hasn't gotten everything she wants to say out yet."
    "I wait."
    y "I need to think about this."
    y su2132 "I don't think you're thinking clearly."
    y u225112 "I'll give you time to really think things over."
    mc "I don't need that, Yuri..."
    mc "I like you how you are--"
    y u228131 "No! You don't!"
    mc "!--"
    y u227111 "You don't know the real me. You just know what I let you see."
    y u225142 "I'm so good at that... Letting people see an image."
    y "Not that it's even a good one."
    y u225113 "I'm weird. I don't like normal things like normal people."
    y su2221 "I like knives and I hurt myself with them..."
    y "I..."
    "She tries to hide her face."
    y su2212 "I...know..."
    y su2222 "...that I'm..."
    y su2300 "...{i}an addict{/i}..."
    mc "..."
    y u225177 "So I don't believe you when you say things like that. It just makes me feel more alone."
    mc "Yuri, I'm proud of you..."
    y u223115 "..."
    mc "That must have taken a lot of strength to say. You're really an amazing person."
    mc "I haven't seen anything that makes me dislike you yet."
    "And I've seen more than you think..."
    mc "Maybe when you're ready to tell me one more thing about yourself, I'll be ready to accept that too."
    y u223145 "..."
    y u221145 "Thanks for letting me talk."
    y u221115 "You haven't brought up my cutting."
    y "You're not trying to change me, you're just...listening."
    y u221177 "Thank you."
    mc "I-I..."
    mc "{i}You know I'm still thinking about it though, right{/i}?"
    y u115142 "I know. You wouldn't be such a kind person if you weren't."
    y u115115 "Do you think you're a kind person?"
    mc "Huh...?"
    mc "I don't really think so..."
    mc "Maybe I just have a lot of guilt."
    y u115111 "Guilt? Why do you feel guilty?"
    "I don't know..."
    "Maybe it's because I feel a bunch of eyeballs on me."
    mc "When no one's around, I look at hentai..."
    mc "I don't feel like that's something a good person does."
    mc "And there's no one I can admit that to, you know?"
    y u113121 "..."
    "Wait, no...What's wrong with me??"
    mc "I-I-I'm sorry, I-I don't know why I said that--"
    y u12a161 "{i}Snort{/i}."
    "Yuri throws her head back and laughs harder than I've ever heard anyone laugh."
    y u122161 "Ehehehe... Ahahaha..."
    y u121115 "[player], did you just tell a girl you look at porn?"
    "She's laughing so hard I don't think she'd hear my answer if I had one."
    y u121172 "Uhuhu~"
    y u111115 "You're so strange."
    mc "D-D-Does my embarrassment make up for it at all??"
    y u111161 "Ehehe~"
    y u111111 "Sorry. I couldn't help it."
    y "Don't worry. I'm not going to judge you."
    y u111145 "Now we both have blackmail on each other. I'll consider us even."
    mc "Oh, thank God..."
    y u115111 "Don't ever tell anyone else that, though."
    y u112161 "Ahahaha~!"
    mc "I-I won't..."
    y u111145 "Thanks for making me laugh. I needed it."
    mc "Well, you're welcome..."
    "Yuri's smile fades a little."
    y u115115 "If you keep my secret, I'll keep yours."
    y u111145 "And maybe, if you want, we can..."
    y u115115 "...talk about my cutting again..."
    mc "I'd like that."
    mc "Um..."
    mc "Is it okay if we {i}never{/i} talk about my thing ever again?"
    y u121161 "Uhuhu~"
    y u121115 "Deal."
    y "I'll see you at the club."
    show yuri at thide zorder 1
    hide yuri
    mc "Haa..."
    "My body collapses under its own weight and I tumble to the floor."
    "My hands catch me on pure instinct."
    mc "What's {i}wrong{/i} with me??"
    mc "What is this inside of me?"
    "I feel so tense but I can't let it out."
    "I drag myself to my feet and suck in air."
    mc "I'm not afraid. I'll be strong."
    "I gather my conviction and strengthen my legs."
    mc "For the Literature Club."
    "I reach out with my senses and I can feel where Monika is."
    "I...need to go talk with her."
    "She's like an impossible problem I can't solve."
    "But I must try."
    "Even if trying is worthless, it's all I have in this world."
    "...And if I try maybe I can slowly reach something impossible."

    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    pause 3
    play music wind fadein 3.0
    show townday zorder 4:
        subpixel True
        alpha 0
        zoom .667
        yalign .5
        xalign 0.0
        parallel:
            linear 5 alpha 1
        parallel:
            linear 120 xalign 1.0
            pause 3
            linear 120 xalign 0.0
            pause 3
            repeat
    pause 5.5

    "Monika looks over her shoulder as I close the door to the roof."
    m "Hey."
    mc "Hi..."
    "I'm already regretting following her up here. But it'd be worse to back out now."
    m "Am I taking your spot?"
    mc "No... I came up here to find you."
    m "Oh? How'd you know where to find me?"
    "I sit next to her."
    mc "It's the connection I have with the game."
    mc "It's only when I choose to use it, but I can feel where all of you are."
    mc "Sorry if that's intrusive... I'll leave you alone if you want."
    "Monika shakes her head with a hint of a smile."
    m "I could use your company more than you'd think."
    m "..."
    m "Don't take this the wrong way, but it's kind of strange thinking of you as a real person."
    m "I have memories of all of you that seem real, but you were just a passing face in a class I was in once."
    m "I think I need to be challenged, because clearly I have a lot of faults as a person."
    m "It'd be easier to not keep going, but I feel like I forfeited that right."
    m "I have to persevere, even if I don't want to."
    "..."
    "I look at the shape of the girl next to me, and I think about how impossible she feels."
    "Impossible to comfort. Impossible to reach."
    "Yet so in need of something I don't seem to have..."
    mc "If it makes you feel any better, I have trouble thinking of myself as a real person, too."
    mc "Which is something you can probably relate to, right?"
    m "Ahaha."
    "Her laugh is muted but genuine."
    m "You're right about that."
    m "Just so you know, you're helping me a lot."
    m "With how I feel, I want to be alone all the time."
    m "But sitting with you, I feel a lot better."
    m "They say misery loves company, but I think that saying is a little misunderstood."
    m "...Or at least we've found an exception."
    "She smiles at me."
    m "Get it?"
    "I smile."
    mc "Yeah. It might have gone over [name]'s head, though..."
    m "Well..."
    m "..."
    mc "..."
    mc "The world doesn't feel the same as it did back then."
    m "...You mean when I was in control?"
    mc "Yeah. Do you feel it too?"
    "Monika nods."
    m "I didn't feel it until I had my memories back, but..."
    m "It was flatter, if that makes sense."
    mc "This world feels like a simulation."
    mc "Like a prison..."
    m "You mean it feels like a fake world?"
    mc "I guess I just want to know it feels like that for you, too."
    m "Unfortunately, I think we're in agreement."
    m "I've looked into the game like we talked about."
    m "The code wraps in on itself. There's the surface scripts, but beneath that things get...confusing."
    mc "What do you mean?"
    m "It's strange..."
    m "It's like it's warping toward a point."
    mc "That's...disturbing."
    mc "Like the game has a heart?"
    m "Yeah..."
    m "Do you think it's a good heart, or a bad one?"
    mc "I don't know..."
    mc "..."
    mc "Do you want to play piano again?"
    m "Huh?"
    m "Piano..."
    m "Like by myself or were you asking to play with me?"
    "She says that with a wry smile. How can she turn the tables on me so quickly..."
    mc "I-I meant at all..."
    m "Ahaha~"
    m "I guess that really hasn't crossed my mind."
    m "Do you think I should?"
    mc "It might help."
    mc "Maybe I just miss music..."
    mc "There's no music in here, you know?"
    mc "Hearing you play made me realize that."
    mc "But when you were plucking at those piano keys, something about it felt real, even when my own body didn't."
    mc "Maybe that's what creativity does."
    mc "A poem can be read across a different world."
    mc "And a song can reach a heart out in [name]'s world. Maybe if it reaches a heart in here, that shows something..."
    m "..."
    m "You picked up the left-hand part I showed you pretty well."
    m "Have you thought of playing an instrument yourself?"
    m "Maybe a bass instrument~"
    mc "Well, actually..."
    mc "...I've always wanted to play guitar..."
    m "Ooh?"
    "Monika's eyes change."
    m "Really? Did you want to be a rock star growing up?"
    mc "Heh. Something like that."
    mc "Maybe it was the anime. But I always felt like if I could do that, I'd be cool or something."
    m "You might be right."
    m "Why don't you try?"
    mc "Eh? In here?"
    mc "I don't know. I don't know how I'd even get one."
    m "..."
    mc "...There's something I need to tell you."
    m "Hm?"
    mc "Sayori saw you..."
    mc "...when you came to my house that night."
    m "Wh-What?"
    mc "She told me at the festival. She was upset."
    "Monika gapes in horror. Her eyes drop to her hands."
    m "{i}What have I done{/i}?"
    mc "It's okay. I...fixed it."
    mc "She's not mad at you."
    m "What do you mean? What did you tell her?"
    mc "The truth."
    mc "I told her that I loved her but that I wasn't ready for a relationship with anyone."
    mc "That's as close to the truth as I can get..."
    m "But what did you tell her was the reason for me going to your house?"
    mc "Well..."
    mc "I told her it was private."
    mc "And you didn't want anyone to know, including me."
    mc "I think that's kind of true, right...?"
    "Monika blinks as she takes this in."
    m "That...worked?"
    mc "She believed me."
    m "Okay..."
    m "Anything else?"
    mc "That's all, I think."
    mc "You're okay. She's not mad at you."
    "She sighs."
    m "If you say so."
    mc "...Hey, should we talk about..."
    mc "...{i}that thing{/i}?"
    m "..."
    m "Were they reading your thoughts...?"
    mc "...Yeah. I guess it's because [name] can read my thoughts. At least some of them..."
    "I wish I could know which ones."
    m "It feels like a bad idea to discuss them if they're listening."
    mc "I kind of don't care."
    mc "I don't trust them. That's all."
    mc "And as far as we know, they only follow my perspective, so..."
    m "..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch3.ogg"
    show natsuki myghost at t11 zorder 5
    pause 0.4
    hide screen tear
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Trying to make plans without me?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "...I was wondering when you'd show up."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I'm not restricted to your perspective."
    fn "Having Monika do your dirty work won't give you an edge."
    fn "Not that there's anything you can do while I have admin control."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "So it's you that controls this game?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    fn "That's not exactly accurate."
    fn "There's a position of control that was filled by Monika in the first loop."
    fn "The loop of which you both have memory of."
    fn "You can feel the difference from here to there. This very world is different."
    fn "Time has passed. For [name] and for us."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "I stand up."
    mc "If you're on our side, what can you actually do for us?"
    stop music fadeout 2.0
    "The figure pauses."
    "They size me up."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Perhaps it would be simpler if I showed you."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    play music fallenangels
    "A force hits my body and I drop to the ground."
    m "[player]!!"
    "Monika jumps up."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "No!"
    fn "Stay away from him."
    fn "He doesn't need you."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    m "..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Get up."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Urg..."
    "My legs twitch in pain. I crouch on the ground and look up at my foe."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "What's your plan? What exactly are you going to do?"
    fn "Glare me to death?"
    fn "Get up."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "I do what they say."
    "{i}WHAM.{/I}"
    "I'm back on the ground. My head sears in agony."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Pathetic."
    fn "You call yourself a man?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    m "STOP IT!!"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "See? She's standing up for you. Because you can't do it yourself."
    fn "What would you do if I were a real enemy?"
    fn "Use your third eye!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Anger boils up from my gut."
    "I push down the pain and leap to my feet."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Again."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Another force comes toward me."
    "This time I'm ready."
    show fadeglitch as gf1 zorder 5:
        yoffset 720
        linear 5 yoffset 0
        repeat
    show fadeglitch as gf2 zorder 5:
        yoffset 0
        linear 5 yoffset -720
        repeat
    "I reach out with my mind."
    "The force warps around me and passes. I'm unharmed."
    "I yell as I lash out in anger, sending a force of my own toward my attacker."
    play sound teyesfx
    "A burst of electricity leaps from my fingers."
    "With barely a twitch of its hand the burst is deflected, crackling in the air harmlessly."
    stop music fadeout 2.0
    hide gf1
    hide gf2
    with Dissolve(2.0)
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "That's more like it."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch3.ogg"
    hide natsuki
    pause 0.4
    hide screen tear
    play music wind fadein 2.0
    "They vanish."
    m "[player]!"
    "Monika rushes to my side."
    m "A-Are you alright?"
    m "You're shaking!"
    "I clench my fist."
    mc "That felt good..."
    m "..."
    m "What are we going to do??"
    mc "Nothing."
    m "Huh?"
    mc "I'm not afraid of them."
    m "[player]..."
    "Monika looks out over the town and bites her lip."
    m "Be careful, okay?"
    "The sound of the wind brings me back to earth."
    "When the time comes, I'm going to be ready."

    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    scene bg club_day
    show sayori u111111 at t11 zorder 2
    play music t3
    with wipeleft_scene

    s "Hey [player]."
    s u112141 "Welcome back to the Literature Club!"
    s u122171 "Literature Club 2.0!"
    mc "Thanks VP."
    "I look around."
    mc "Monika isn't here yet?"
    s u122222 "Not yet... But I'm sure she'll be back soon."
    s u123222 "Um... I'm gonna go find her."
    show sayori at thide zorder 1
    hide sayori
    "She hurries out the door."
    mc "Alright..."
    "I survey the state of the room."
    "The only visible person is Yuri, enraptured in her book."
    "We already spent time with her, so I think it's fair to give her some reading time."
    "But I know exactly where Natsuki is."
    scene bg closet
    with wipeleft_scene
    mc "Hey."
    show natsuki u221111 at t11 zorder 2
    n "'Sup."
    mc "What are you reading?"
    n u224231 "Oh... Just a little..."
    show natsuki u226234
    "Natsuki looks behind her and frowns."
    mc "Manga?"
    n xu6214 "...Yeah..."
    mc "I don't want to bother you or anything, but do you mind if I look at your collection?"
    n xu3223 "Eh? Why, you like manga?"
    mc "Honestly, we might have slightly different tastes, but that doesn't mean I can't appreciate other works in the medium."
    mc "No matter the genre, the fact that someone put the time in to make the art and story is just cool to me."
    "Natsuki's eyes widen. I may have short-circuited her a little."
    "But she's sure to quickly recover her cool."
    n xu2151 "In that case, I've got quite a collection to show you."
    "Natsuki waves proudly over the shelves."
    n u221111 "Read 'em and weep."
    mc "Wow..."
    "Even though I'm already familiar, I look over Natsuki's collection with new eyes."
    "The spines are colorful and neatly organized. As was always clear, Natsuki takes great pride in her manga."
    mc "It really is quite a collection. Makes me nostalgic."
    n u114111 "Hm? How so?"
    mc "It just reminds me of being a k--"
    n u116112 "..."
    n xu3112 "Uh-huh? Go on?"
    mc "Uhhh, I mean..."
    mc "When I was younger, I loved collecting things. When I got older, I lost touch with a lot of the things that make me happy."
    mc "D-Does that make sense?"
    show natsuki xu6132
    "Natsuki chews over my answer before nodding slowly."
    n xu3152 "I see what you're saying."
    n u113111 "Good save."
    mc "Thank you."
    mc "Mind if I read a little {i}Parfait Girls{/i}?"
    n u113221 "Ehh?? You want to {i}read{/i} some?"
    mc "Oh, is that okay...?"
    "Maybe she only let me read her manga before because she was kind of into me..."
    "I don't think this iteration of Natsuki has any attraction to me at all."
    n u113113 "How do you know about {i}Parfait Girls{/i}?"
    n "...And why that one?"
    mc "I just picked it out from the lineup."
    mc "The title is right there."
    "I point. Natsuki follows my finger."
    n u116132 "I mean, if that's what you'd like..."
    n "One sec."
    show natsuki at thide zorder 1
    hide natsuki
    "Something about my choice seems to have unsettled Natsuki a little, but she grabs the volume, and we pull two desks together."
    scene bg club_day
    show natsuki u222111 at t11 zorder 2
    with wipeleft_scene
    n "Alright. It's not every day I get to see someone react to {i}Parfait Girls{/i}."
    n u221111 "Go ahead."
    mc "Okay..."
    show natsuki at thide zorder 1
    hide natsuki
    "I begin reading the manga while Natsuki looks on."
    "It feels pretty familiar. It brings me back to my first reading of this with her."
    "It makes me wonder where these books come from."
    "When Sayori wanted to find her own reading material, it was like it came out of nowhere in the library."
    "Is there a force in the game that creates fiction that matches their interests and subconscious?"
    "...Would Monika and I be exempt from that?"
    "I think of myself as someone who reads manga, but I don't have any in my room."
    "Nothing that I could introduce to Natsuki or anyone else."
    "But is that only because I haven't tried to find any... What would happen if I searched the library for something like that?"
    show natsuki u223112 at t11 zorder 2
    n "Hey, are you paying attention?"
    mc "Eh? Sorry... I guess I got lost in thought."
    n xu3132 "Look, it's not gonna insult me if you don't want to read this."
    n xu3112 "I'd rather you not just pretend to be into it."
    mc "N-No, that's not it..."
    mc "I'm paying attention. I'm just a little distracted."
    n xu3155 "Jeez... You don't need to embarrass me."
    mc "I--"
    mc "...Sorry..."
    mc "Did I offend you?"
    n xu6132 "Hmph. Maybe you did."
    n xu3112 "Pretty weird of you to want to read a romance manga with me, anyway."
    mc "Eh??"
    "I close the manga and push it toward her."
    mc "If {i}that's{/i} how you feel, then here, take it."
    show natsuki at thide zorder 1
    "Natsuki snatches the volume and marches back to the closet."
    stop music fadeout 2.0
    scene bg closet
    with wipeleft_scene
    "Something boiling inside of me raises me to my feet."
    play music t7
    mc "Hey, I was trying to be {i}nice.{/i}"
    show natsuki u223112 at t11 zorder 2
    n "I don't need you to be nice to me. Try being nice to your {i}girlfriend.{/i}"
    mc "Urk--"
    mc "Listen, what happens between Sayori and I is none of your business!"
    n u117222 "My friend's business {i}is{/i} my business."
    n xu3155 "Maybe you don't get that because you don't have real friends."
    n xu3112 "That honestly isn't a shock to me."
    mc "Wha--"
    mc "Y-You..."
    n xu7222 "Go on, say it. Say what you want to say. I {i}dare{/i} you."
    show natsuki at t22
    show yuri u225358 at f21 zorder 3
    y "Um, guys..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    $ both_name = "Both"
    both "{i}What{/i}???"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y su2222 "Uu..."
    show yuri at t21 zorder 2
    stop music fadeout 2.0
    "A pang of guilt hits my stomach."
    "What am I doing...?"
    show natsuki at f22 zorder 3
    n u227222 "Listen here!"
    show natsuki at t22 zorder 2
    mc "Natsuki..."
    show natsuki at f22 zorder 3
    n u227255 "If you want to come into this club and be a member, {i}fine{/i}!"
    show natsuki at t22 zorder 2
    mc "Natsuki."
    show natsuki at f22 zorder 3
    n u223212 "But if you're gonna mess with us, you've got another thing coming!"
    show natsuki at t22 zorder 2
    mc "Natsuki!"
    show natsuki at f22 zorder 3
    n u227222 "{i}Wh-What{/i}?!"
    show natsuki at t22 zorder 2
    mc "I'm sorry..."
    show natsuki at f22 zorder 3
    n u116212 "..."
    show natsuki at t22 zorder 2
    mc "Seriously. I'm sorry."
    mc "I shouldn't have lost my temper."
    "I turn to Yuri."
    mc "I'm sorry for snapping at you, Yuri. You didn't deserve that."
    show yuri u221242
    "Yuri smiles in relief."
    show yuri at f21 zorder 3
    y "It's fine."
    y u225277 "{i}Phew{/i}..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n xu4234 "I... Well..."
    scene black
    with wipeleft_scene
    "We all turn our heads as the door swings open."
    play music t5
    scene bg club_day
    show sayori u222141 at t11 zorder 2
    with wipeleft_scene
    s "Found her!"
    s u112111 "Monika, tell them what you were up to!"
    show sayori at t22
    show monika u111222 at t21 zorder 2
    "Sayori beams with pride. Monika smiles nervously."
    show monika at f21 zorder 3
    m u112222 "I was just practicing piano a little."
    m "Something I've been doing on the side."
    show monika at t21 zorder 2
    show sayori at f22 zorder 3
    s u112141 "Guys, it sounded so good!!"
    s u122171 "You should start a Music Club, too~"
    show sayori u121111 at t22 zorder 2
    show monika at f21 zorder 3
    m u112231 "No, it's nothing like that..."
    show monika at t31
    show sayori at t32
    show yuri u115111 at f33 zorder 3
    y "Piano?"
    y u111111 "That's not an easy instrument."
    show yuri at t33 zorder 2
    show monika at f31 zorder 3
    m u111112 "I'm not very good at it yet. I mainly stick to the white keys..."
    m "It makes things much easier."
    show monika at t41
    show sayori at t42
    show yuri at t43
    show natsuki u111111 at f44 zorder 3
    n "Aw. I wish I could play an instrument."
    n "Maybe one day you can teach us a little."
    show natsuki at t44 zorder 2
    show sayori u222111 at hf42 zorder 3
    s "Monika, are you gonna announce it yet??"
    show sayori at t42 zorder 2
    show natsuki at f44 zorder 3
    n u113111 "Eh? Announce what?"
    show natsuki at t44 zorder 2
    show monika at f41 zorder 3
    m u112222 "Oh. Well..."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide yuri
    hide natsuki
    show monika at t21
    show sayori u221112 at t22
    "Sayori nudges Monika forward."
    show sayori at f22 zorder 3
    s "Go ahead."
    show sayori at t22 zorder 2
    show monika u111112
    "Monika looks back at Sayori and smiles."
    show monika at f21 zorder 3
    m "Yeah. I'm ready."
    show monika at t21 zorder 2
    "Yuri and Natsuki share a glance. It seems this is a surprise to all of us."
    show sayori at thide zorder 1
    hide sayori
    show monika u222111 at t11
    m "Okay, everyone!"
    m "I have a small assignment for you today."
    m u121111 "First there's Sayori's book. I want us to have a little discussion about it on Friday."
    m "But I think we can squeeze in one other literary activity this week."
    "If anyone has protests they keep them to themselves."
    "We're all impressed with our president today, and everyone wants to hear her announcement."
    m "We're going to write and share poems."
    show monika at t21
    show natsuki u113121 at f22 zorder 3
    n "Eh??"
    show monika at t31
    show natsuki at t33 zorder 2
    show yuri u113121 at t32 zorder 3
    y "Ooh?"
    show monika at t41
    show natsuki at t44
    show yuri at t43 zorder 2
    show sayori u222141 at t42 zorder 3
    s "Yayy~"
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    show sayori at thide zorder 1
    hide natsuki
    hide yuri
    hide sayori
    show monika u111111 at t11
    m "That's right."
    m u122111 "Now I know we've got some avid poets in the room already, and I won't make you write anything new if you don't want to."
    m "But I'm going to ask that you pick at least one to share with everyone."
    "My eyes wander with curiosity to everyone's reaction."
    "Natsuki seems to be mulling it over, while Yuri has sunk into her seat, also lost in thought."
    "Sayori, meanwhile, looks like a proud parent."
    m u121111 "Bonus points if you write something new."
    m u121122 "Sayori and I think this would be a great bonding experience as a club."
    m u121112 "We do have a new member, and maybe something like this would break the ice, you know?"
    m "I think we all want this club to be a place where we can all feel at home."
    show monika u124111 at t21
    show yuri u111115 at f22 zorder 3
    y "That's a really great idea."
    show yuri at t22 zorder 2
    "Everyone, equally surprised, turns to Yuri."
    show yuri at f22 zorder 3
    y u111145 "Honestly, things have been different the past couple weeks."
    y "It's not a bad thing. But maybe we need something to bring us out of our comfort zones."
    show yuri at t22 zorder 2
    "She looks at me."
    show yuri at f22 zorder 3
    y u125112 "Do you agree?"
    show yuri at t22 zorder 2
    mc "Oh, I..."
    "My face is suddenly hot as the whole club focuses on me."
    mc "O-Of course. This is your club after all."
    mc "I want whatever is best for everyone."
    show monika at t31
    show yuri at t32
    show sayori u112111 at f33 zorder 3
    s "It's okay, [player]."
    s u122171 "You can admit you write poems sometimes."
    show sayori at t33 zorder 2
    mc "Ehh??"
    mc "How did you--"
    "My mind flashes back to when I was trying to write and she came into the classroom."
    mc "How'd you...know that was..."
    show monika at t41
    show yuri at t42
    show sayori at t43
    show natsuki u222143 at f44 zorder 3
    n "Ahaha!"
    n u222111 "She can read you like a book, [player]."
    show natsuki at t44 zorder 2
    show yuri u111161 at f42 zorder 3
    y "Uhuhu.."
    show yuri at t42 zorder 2
    mc "Ugh..."
    "Natsuki sure cheered up fast..."
    show monika u112111 at f41 zorder 3
    m "Well it looks like it's settled. Thanks for your cooperation, everyone!"
    m u222131 "Let's all do our best!"
    show monika at t41 zorder 2
    show sayori u222141 at f43 zorder 3
    s "Yeah! And then Monika can turn the best poem into a song!"
    show sayori at t43 zorder 2
    show monika u222222 at f41 zorder 3
    m "I don't know about that, but..."
    m u111112 "We'll see."
    m u112111 "I'm setting the due date for Thursday, so no excuses. You have two full days."
    m "You can spend time here if you want, but officially I'm calling today's meeting to an end."
    show monika at t41 zorder 2
    show sayori at f43 zorder 3
    s "Hooray~!"
    show monika at thide zorder 1
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    "A warm feeling comes over me as I look at the girls gather their things."
    "The club suddenly feels alive again. Like we're a real group."
    "Even if we're not all on the same page, maybe we're at least reading the same book..."
    show sayori u111111 at t11 zorder 2
    s "[player]... Want to walk home with me today?"
    "I look down, so I don't have to see her face, because it feels like I might break into a grin."
    mc "Um... Sure."
    mc "Whenever you're ready."
    s u222141 "Okay~"

    scene black
    with wipeleft_scene
    scene bg residential_day
    with wipeleft_scene

    "The walk home is optimistic."
    "Sayori bounces along beside me as I lose myself in thought."
    show sayori u111112 at t11 zorder 2
    s "Monika really is amazing, isn't she..."
    "I nod."
    mc "I'm impressed with her. She really rose to the occasion today."
    s u111122 "Yeah..."
    s "She's an impressive person when you get to know her."
    mc "Heh. She could even get me to stop being a down-in-the-dumps jerk for a day."
    s u114112 "..."
    s u111112 "She could do anything she sets her mind to, [player]."
    "I nod to myself."
    "Maybe even save you..."
    stop music fadeout 5.0

    scene black
    with dissolve_scene_full
    pause 3
    scene bg kitchen
    with wipeleft_scene

    "A couple hours later, I hear a knock at my back door."
    "I let Monika in."
    mc "Hey, what's-- oh..."
    show monika u111112 at t11 zorder 2
    m "I brought you something."
    mc "I can see that."
    "She places a guitar case on my couch and an amplifier on the floor."
    mc "Where did you..."
    show monika u111141
    "She just laughs and shakes her head at me."
    m "This is an empty video game world."
    m u111112 "I stole it from a music store."
    m u112222 "I broke the laws of physics to carry it, too. I'm not {i}that{/i} athletic."
    mc "Good point..."
    mc "You went for electric, huh?"
    m u111111 "Go on. Try it out, rock star."
    mc "I haven't messed with one of these for a few years, but I remember a chord or two..."
    play sound "A2/Music/chords.ogg"
    pause 8
    m u112231 "Careful!"
    m "[name] isn't going to believe you're actually playing."
    m u111112 "If it wasn't right in front of me, I wouldn't believe it myself."
    mc "It's the same with you and piano..."
    mc "I don't need to worry about physical fitness. In the real world I'd need to train my hands to play these chords."
    mc "I guess things come a lot easier when you're a video game character."
    m u122131 "Ahaha!"
    m u121131 "Especially the main character~"
    mc "Alright, alright. Relax."
    "She grins while I roll my eyes."
    m u111112 "Does it make you feel real?"
    mc "Oh... I..."
    "I look down as I strum again."
    "The vibrations carry through my body."
    mc "I feel something..."
    m u111122 "..."
    show monika u114311
    "{i}Ring ring ring{/i}..."
    "Monika looks at her phone and her eyes widen."
    m u114312 "It's Sayori..."
    mc "O-Oh..."
    "My body feels drenched in guilt."
    "Monika's eyes beg me to stay quiet before she answers the call."
    m u112232 "Hi Sayori!"
    m u113222 "..."
    m u111222 "I-It's okay. It's not a bad time."
    m "Just working on a little homework."
    m u114224 "..."
    "She stands and starts to pace."
    m u112222 "I-I know. It's not a big deal. Just some family stuff."
    m "...Really, don't worry about it."
    m "I'll make it through alright."
    m u114222 "..."
    m u111222 "Thanks Sayori. I know I can count on you."
    m "I really don't want you to think it's that big a deal."
    m u114222 "Yeah..."
    m "..."
    m u111222 "Okay. Thanks for calling. Have a good night."
    show monika at thide zorder 1
    hide monika
    "Monika collapses on my couch and starts sobbing into her hands."
    "I look at her as my heart seizes up."
    "..."
    window hide
    play sound "A2/Music/mcmyfeelings.ogg"
    pause 29
    show monika u114112 at t11 zorder 2
    m "H-How'd you do that...?"
    "I shrug."
    mc "I just followed my feelings. Guess I have some main character powers."
    show monika u111322
    "That gets her to let out a broken laugh."
    mc "Monika, whatever you're feeling, however much it hurts..."
    mc "Just know that [name] and I are on your side."
    mc "We see what you're going through..."
    mc "...And you matter to us."
    show monika u111342
    "Monika looks to me and wipes her eyes."
    m "It's so hard to believe you..."
    m u111112 "...But I do."
    "I smile."
    "She smiles back."
    scene black
    with dissolve_scene_full
    "We wait until it's dark, and Monika sneaks away."
    "The walls of my house are so quiet now..."
    "I put down the guitar and go up to my room."

    scene bg bedroom
    with dissolve_scene_half

    "..."
    "I shut the door."
    mc "{i}Why{/i}..."
    mc "{i}Why, [name]{/i}..."
    mc "Even though I'm such a terrible person..."
    mc "...Why do I keep helping them?"
    mc "I'm a liar. I'm lazy. I'm a terrible human being. Why..."
    "I open the desk drawer and take out my magazine."
    mc "If you weren't here watching, this is what I'd be using... I wouldn't be helping anybody."
    mc "..."
    mc "{i}Why didn't Yuri reject me{/i}?"
    "I rip the magazine apart and throw it in the trash."
    mc "I don't need this anymore. Not while you're here."
    mc "..."
    "I take the magazine pieces out of the trash and put them back in the drawer."
    mc "You know, in case Monika comes back..."
    mc "I'll put it in some dumpster tomorrow."
    "I go back downstairs and stay up all night playing guitar."
    "From time to time, I even smile."

    scene black
    with dissolve_scene_full
    play music wind fadein 4.0
    pause 5

    show monika u113122 at t11 zorder 2
    m "..."
    m "[name], do you believe in God?"
    m u113112 "..."
    m "I never thought too much about that question. It never seemed important enough."
    m u111122 "After all, there are much smarter people than me who can work that stuff out."
    m u114124 "But...in this game..."
    m "It feels very lonely. And confusing."
    m "Maybe I've lost the right to complain for myself. But I keep thinking..."
    m u114112 "What kind of god would do this to them?"
    m u113112 "It's kind of scary. Because it feels like we're on our own."
    m "Like if there's a god, they're not looking in here."
    m u113122 "...Or maybe they're just too cruel to care."
    m "..."
    m u113124 "I don't know how I'm going to do it."
    m "I have so many responsibilities. They feel crushing."
    m u113142 "They feel impossible."
    m "I don't know how I'm going to do it alone..."
    window hide
    pause 3

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/4.txt")
        except: open(config.basedir + "/4.txt", "wb").write(renpy.file("A2/Art/scg/4.txt").read())

    $ style.choice_button_text = style.silent_button_text
    $ style.choice_button = style.silent_choice_button
    menu:
        "...Go to sleep, Monika. Everything will be alright.":
            pass
    $ style.choice_button_text = style.choice_button_revert_text
    $ style.choice_button = style.choice_button_revert

    m u114111 "!"
    m u114212 "[name]? Are you--?"
    m u113212 "..."
    m u114212 "Hello?"
    m u113212 "..."
    m u111222 "..."
    m "Thanks."
    m u111112 "Have a good night, [name]."
    stop music fadeout 3.0

    show monika at thide zorder 1
    hide monika
    window hide
    pause 4
    scene bg kitchen
    with wipeleft_scene

    "The morning crawls in like a gentle lamb."
    "The guitar feels comfortable in my lap."
    mc "Hm?"
    mc "Sayori is up."
    mc "Maybe I should walk to school with her."
    "I keep plucking at the strings and lose track of time."
    "There's a knock on my door."
    mc "Oh. She's here."
    scene bg kitchen
    show sayori u111111 at t11 zorder 2
    with wipeleft_scene
    s "Morning."
    s u115111 "It's almost time to go to school. Are you coming?"
    mc "Yeah... You don't need to keep tabs on me like this."
    s u115114 "Only if you're sleeping and eating and going to school like you're supposed to."
    s "You DID sleep last night, didn't you?"
    mc "Yeah..."
    s u116114 "Mmm..."
    s u113144 "LIES!!!"
    s u113114 "You don't look like you slept at all!"
    s u123112 "That's not good for you, you know?"
    "I rub the back of my neck."
    mc "Well, I had homework and stuff."
    s u123114 "See?"
    "She points."
    s "You do that when you lie or you're nervous."
    mc "Huh? Do what?"
    s u116114 "Rub the back of your neck."
    s "Liar."
    mc "Alright, alright, you win."
    "Freaking sleep demon..."
    mc "I was playing guitar."
    s u114131 "Uh?"
    s u227131 "Ehh????"
    s u222141 "Show me, show me, show me!!"
    mc "I thought we had to get to school."
    s u223114 "I thought you were up doing homework."
    mc "Touché..."
    mc "Fine. I'll play a little guitar."
    s u222141 "Yay~!"
    show sayori at thide zorder 1
    hide sayori
    "I pick up the instrument and Sayori sits down to listen."
    play sound "A2/Music/chords.ogg"
    pause 8
    show sayori u114131 at t11 zorder 2
    s "Whoaaa..."
    s u113111 "When did you learn to do that??"
    mc "This is really beginner stuff..."
    mc "I'm not doing anything super impressive."
    s u111112 "It's impressive to me."
    mc "Yeah..."
    mc "They're called 'cowboy chords.' They're the first thing you learn."
    mc "They sound good together because they're in the same key."
    mc "If I change key, different chords sound good in that context."
    play sound "A2/Music/altchords.ogg"
    pause 4
    mc "Get it?"
    s "Wow..."
    s u115111 "So...what's the second thing beginners learn?"
    mc "Probably minor chords..."
    play sound "A2/Music/eminor.ogg"
    mc "This is an E minor."
    s u114131 "Ooo..."
    mc "I don't know many others... That one just happens to be easy to play."
    s u112141 "Do you know one more? Do one more!"
    mc "..."
    play sound "A2/Music/aminor.ogg"
    mc "Here's A minor."
    s u112111 "Wow!!"
    s u111112 "For a beginner, you sound really good, [player]."
    mc "Th-Thank you..."
    "This is so embarrassing..."
    s u115111 "Where did you get it? I didn't know you had a guitar."
    mc "Oh, well..."
    mc "My parents gave it to me some time ago, for a gift. I haven't used it much."
    mc "But...Monika playing piano made me think about it. I was always disappointed in myself for not getting very far with guitar."
    mc "It's kind of a childhood dream, you know?"
    show sayori u111322
    "Sayori nods."
    s "I'm glad you got some inspiration from Monika. It makes me happy I got you two together."
    s u111111 "You should definitely keep trying. You're really good."
    mc "I'm not, but thank you."
    s u115114 "Next time, go to sleep."
    mc "Okay, okay..."
    mc "Should we go to school now?"
    s u222141 "Yeah!"

    scene black
    with wipeleft_scene
    scene bg corridor
    show natsuki u111111 at t11 zorder 2
    with wipeleft_scene

    play music t3
    n "Well, hello you two."
    show natsuki at t21
    show sayori u112141 at f22 zorder 3
    s "Hiya Natsuki~"
    show sayori at t22 zorder 2
    show natsuki xu4154 at f21 zorder 3
    n "{i}Yawn{/i}... So bright and chipper so early in the morning."
    show natsuki at t21 zorder 2
    show sayori at f22 zorder 3
    s u111111 "I got good sleep and breakfast."
    s u115114 "Unlike {i}some others{/i} around here."
    show sayori at t22 zorder 2
    mc "Hey..."
    show natsuki at f21 zorder 3
    n xu2111 "Ha. Welcome to the poor sleep club."
    n u113132 "Oh well. I'll catch up in history. Can't stand that class."
    n u111111 "I get most of my naps in there. The teacher never notices."
    show natsuki at t21 zorder 2
    show sayori at f22 zorder 3
    s u113114 "Hey, no setting bad examples."
    s "[player] is very impressionable. I won't have you being a bad influence on him."
    show sayori at t22 zorder 2
    show natsuki at f21 zorder 3
    n u118141 "Okay, tiger-mom."
    show natsuki at t21 zorder 2
    mc "Um. Do I get a say in this?"
    "{i}*Ringgg*{/i}"
    show sayori at f22 zorder 3
    s u117131 "Ahh! We're late! Run!"
    show sayori at thide zorder 1
    hide sayori
    show natsuki at t11
    n u222111 "Ha! What a bundle of energy she is."
    mc "It's a lot to keep up with sometimes..."
    n u111131 "Yeah, I know."
    n u113111 "But don't mess with her. She's really in love with you."
    mc "..."
    mc "You're very direct, you know that?"
    n xu3112 "You're very aloof, you know {i}that{/i}?"
    n "Maybe too aloof for your own good."
    n xu1111 "If you break her heart, I'm going to punch you."
    mc "Wait, what?"
    n "You heard me, buddy."
    n xu8143 "You'd better treat her right."
    mc "..."
    mc "You really care about your friends, don't you?"
    n xu4121 "Eh?"
    n "What makes you say that?"
    mc "You're being funny, but I can tell you're serious."
    n u116112 "Oh I'm definitely serious, I {i}will{/i} punch you."
    mc "I hear you loud and clear..."
    mc "Do you have friends outside the club?"
    n u116234 "..."
    "Natsuki looks uncomfortable, like she doesn't want to answer me."
    n u113234 "...Not really."
    n "I used to, but they were jerks. They made fun of me all the time."
    n u113111 "I don't feel judged in the club. I feel like I can be myself."
    n u116132 "Well, maybe Yuri judges me. But it's different."
    n u116134 "She's a nice person."
    n "..."
    n u113112 "Don't tell her I said that."
    mc "Don't worry."
    n u113111 "The club is like my home. It's the place I can feel safe."
    "Feel safe..."
    mc "Is there nowhere else you can feel safe?"
    mc "What about..."
    mc "...your house?"
    n xu6112 "..."
    n xu4132 "Let's stop talking about this."
    n xu3155 "I'll see you at the club."
    show natsuki at thide zorder 1
    hide natsuki
    "She abruptly turns on her heel and walks away."
    mc "O-Okay, bye!"
    "Natsuki's walls are hard to break down. I want to understand her."
    "I hope I didn't go too far..."
    "What can I do that will get her to let me in?"
    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    play music zenmadre
    scene bg library
    with dissolve_scene_full

    "Obviously, I'm going to ignore homeroom."
    "I'd rather be here, spending time with Yuri."
    "I'm sure that's where you'd rather be too, [name]."
    "It's okay. You can admit it. She's cute."
    "I'm not going to judge you."
    show yuri u111111 at t11 zorder 2
    y "Oh, good morning, [player]."
    y u111142 "Avoiding homeroom as well?"
    mc "It hasn't come back to bite me yet. I don't think anyone notices I'm gone."
    y u121172 "Uhuhu~"
    y u112112 "I hope I haven't set a bad example. The librarian covers for me."
    mc "I find the school cares a lot less when they don't think you're going to amount to anything."
    y u122141 "Ahh... I hope you don't think {i}that{/i} poorly of yourself."
    y u225118 "I-I'm...sorry if I hurt your feelings by laughing at you yesterday..."
    mc "Oh, don't worry... I was just happy to see you laugh."
    mc "I'd like to see it again, although maybe pointed at something else..."
    show yuri u111172
    "Yuri does giggle, but she composes herself."
    y u112111 "Well I am a proper lady, you know."
    y u111111 "Don't forget that."
    mc "I wouldn't dream of it."
    show yuri at thide zorder 1
    hide yuri
    "I take out my book and get ready to start reading."
    "But I notice Yuri fidgeting."
    mc "Is something wrong?"
    show yuri u223221 at t11 zorder 2
    y "!"
    y u223248 "..."
    y u225111 "Yesterday, we traded secrets..."
    y "Can we try something like that again today?"
    mc "Oh..."
    "This relaxing morning suddenly became tense."
    mc "What do you have in mind?"
    y u225148 "If you want to ask me one question..."
    y u225118 "I have one for you..."
    "That's not terrifying or anything."
    mc "I mean...sounds like a fair trade..."
    y "C-Can you go first?"
    "Eh??"
    "This feels totally unfair... How am I supposed to know what you want to ask?"
    mc "Is this about your cutting?"
    y su1111 "I-If you want it to be..."
    "Yuri toys with her hair."
    "That seems to be where she wants me to go. Alright then."
    "Yuri looks at me expectantly."
    y su2221 "I'm sorry. I just want to get the hard part out of the way..."
    mc "I see..."
    "Well, I can step up then. There {i}is{/i} something I want to ask her."
    mc "Do you want to stop cutting yourself?"
    show yuri su2300
    "Yuri shivers as if she was dreading that very question."
    y "I don't think my answer would be very satisfying."
    mc "That's okay... I just want to know what you have to say."
    y u124378 "{i}Sigh{/i}..."
    y u124148 "I want to stop hurting myself, but I don't want to stop cutting."
    y u114118 "Does that make sense?"
    mc "Um..."
    mc "What do you mean by 'make sense'?"
    y u113148 "Oh dear..."
    y u115118 "Since you caught me, I've been doing it less."
    y "And I want to stop."
    y u224118 "But at the same time, it makes me realize that I really really don't want to stop."
    mc "Yeah..."
    "That does make sense. I guess that's what addiction is."
    y u225148 "[player]..."
    y u225118 "Do you think people can change?"
    mc "Um... Is that your question?"
    y u227118 "Ah! No!"
    y u227148 "D-Do I have to take that back?"
    mc "N-No, I'm sorry, it's fine..."
    "I take a deep breath."
    mc "I think I have to say I do."
    mc "I have to believe people can change, or else what would the point of living be?"
    y u224118 "..."
    y u115118 "I'd like to ask my question now, if it's okay..."
    mc "Sure."
    stop music fadeout 2.0
    y "[player]..."
    y "Do you sometimes pretend to be okay when you're really not?"
    "Yuri's question hits me so hard I almost reel back."
    play music t9
    mc "I-I..."
    "My hands twist in my lap."
    mc "{i}I don't know how to answer that{/i}..."
    y u224218 "[player], you're shaking..."
    "Yuri moves next to me."
    "I cover my face with my hands."
    mc "{i}I-I don't know what's wrong with me.{/i}"
    "With great hesitation, Yuri places a hand on my shoulder, as if too much pressure would cause me to break."
    y "It's okay to cry..."
    show yuri u224221
    "I jump to my feet."
    mc "{i}I need to go to class{/i}."
    y u225118 "No, [player], please don't leave..."
    "I look at her."
    mc "I-I..."
    mc "{i}Yuri{/i}..."
    y u115118 "You don't have to run away."
    y "Maybe there's something here we can face together..."
    mc "I don't know why..."
    mc "I don't know why I'm like this..."
    "Yuri looks into my eyes with an intense thoughtfulness."
    "Everything in me wants to look away. Except for my eyes."
    y "May I hug you?"
    mc "..."
    mc "{i}Okay{/i}..."
    scene black
    with dissolve_scene_full
    "Yuri wraps her arms around me and pulls me toward her."
    "My senses are overwhelmed to the point that I gasp."
    "Her body... It feels real..."
    "She's warm and my face is in her hair."
    "Tears start to fall."
    y "It's okay."
    y "Let it out..."
    mc "{i}I feel so broken, Yuri{/i}..."
    mc "{i}I think there's something wrong with me{/i}..."
    mc "{i}I want to help you but I feel so lost{/i}."
    y "You {i}have{/i} helped me."
    "Yuri pulls back. My body feels limp without her."
    y "I want to show you something."
    "She carefully pulls up her sleeve."
    y "You're the first person who's seen my scars."
    y "Look..."
    "She traces a finger along her arm."
    y "You can see the ones that were there before."
    "Her finger gets to cuts that look fresher."
    y "This one's from today..."
    y "And before that, I've only made three since you caught me."
    y "I know that's still terrible..."
    y "But that's because of you. You're the reason I've been able to make a difference in hurting myself."
    "I wipe my face."
    scene bg library
    show yuri u224118 at t11 zorder 2
    with dissolve_scene_half
    mc "Well..."
    mc "I don't think I've ever cried in front of someone before."
    y u111161 "Uhuhu."
    y u111111 "Yeah. I think that makes us even."
    y u111148 "You answered my question, so..."
    "Her face gets a little more serious."
    y u125118 "I can commit to trying not to hurt myself if you can commit to the same."
    "I look down at the floor, unable to meet her eye for a moment."
    "Then I look back up."
    mc "Okay."
    mc "I don't even know what I'm agreeing to, I guess..."
    mc "But I want to say yes."
    "Yuri smiles like she's proud of me."
    y u111118 "Here."
    "She pulls something from her bookbag."
    y u115118 "This is the knife you found me using before."
    y "I want you to have it."
    y u115148 "It's not the only one I have. I'm going to have temptations."
    y u115118 "But it means something to me to have you take this."
    mc "That means something to me, too..."
    "She places the knife in my hand and curls her fingers around mine."
    y u111118 "Take good care of it, okay?"
    y "It's yours now."
    mc "I will."
    show yuri u111148
    "Yuri nods and turns to gather her things."
    "Then she turns back to me."
    y u111111 "Thanks for being my friend, [player]."
    y "I'm glad you joined our group."
    y u111118 "We're all glad."
    y "Okay?"
    mc "...Okay."
    y "I'll see you at the club."
    stop music fadeout 2.0
    show yuri at thide zorder 1
    hide yuri
    "..."
    "I'm at a loss for words, [name]."
    "Maybe I should..."
    "I root through my bag and get a notebook and pen."
    "To speak to you directly right now would be too embarrassing."
    "But to write you a poem would be easy."
    scene black
    with wipeleft_scene
    pause 2
    scene bg library
    with wipeleft_scene
    "When I put down my pen, I feel satisfied."
    "It's the sense I've finished something."
    "I'm making friends... I'm making progress."
    "There's something I'm doing that's right."
    "I stand up."
    show natsuki myghost at t11 zorder 2
    show screen tear(50, 0.1, 0.1, 40, 80)
    play sound "sfx/glitch2.ogg"
    pause 0.5
    hide screen tear
    mc "Nng--"
    mc "{i}What do you want{/i}?"
    "The figure with Natsuki's body points to the poem I just wrote."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I didn't like that."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Huh?"
    mc "What's wrong with it?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I'm concerned there's a threshold to be crossed that can't be undone."
    fn "I have a warning for you."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "A warning...?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "This library is dangerous."
    fn "I don't think you should come back here."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Dangerous..."
    "How can you tell me what to do while holding all the power?"
    mc "In that case, I {i}will{/i} come back here."
    mc "Because something I'm doing here is working!"
    mc "You've hardly done anything to help. Why should I listen to you?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    fn "Because I see the dangers you cannot see."
    fn "Your third eye is undeveloped. I've been waiting here for you. For longer than you can comprehend."
    fn "Do you think you have the right to throw away everything for your own pride?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "..."
    mc "{i}My what{/i}...?"
    play music fallenangels
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "YOU FOOL!!!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "The ground begins to shake. It's like the walls are dissolving around us."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "YOU THINK YOU CAN THROW IT ALL AWAY?"
    fn "EVERYTHING WE'VE DREAMT OF? EVERYTHING WE'VE WORKED TOWARD?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Wh-What are you doing??"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "YOU ARE A BOY. YOU WILL DESTROY US ALL!"
    fn "THIS IS YOUR WARNING."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "The trembling stops and I fall to my knees."
    "It points Natsuki's finger at me, crooked as if she's possessed by something incredibly old."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Beware this library. It is unnatural."
    fn "Do not venture farther than Yuri herself goes."
    fn "You will put the safety of this world at risk."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show screen tear(50, 0.1, 0.1, 40, 80)
    play sound "sfx/glitch2.ogg"
    hide noise
    pause 0.5
    hide natsuki
    hide screen tear
    stop music fadeout 2.0
    mc "HEY!"
    mc "Ugh..."
    "I gather my things and rush out of the library."
    mc "I need to find Monika..."

    scene black
    with wipeleft_scene
    scene bg corridor
    show monika u114111 at t11 zorder 2
    with wipeleft_scene

    m "[player]?"
    m u114112 "What's wrong?"
    mc "They just appeared to me again..."
    mc "You know...that thing in Natsuki's body..."
    "Monika looks at me for a second and nods."
    m u113113 "Okay. What did they do?"
    mc "They told me not to go in the library anymore."
    m u114111 "The school library...?"
    m "Why not?"
    mc "Well...it's not a normal library..."
    mc "It's massive. When you walk in there, you're in a space bigger than the entire school."
    mc "But it's where Yuri spends a lot of time."
    mc "Didn't you know that...?"
    m u113224 "That...wasn't a thing when I had admin control..."
    "I shake my head."
    mc "I think they're hiding something there they don't want us to find."
    mc "Something big."
    mc "That's where we found Sayori's books..."
    mc "There's something in that place."
    m u113113 "..."
    m u114112 "Do you think we should ignore their warning?"
    m u114222 "What if it's dangerous?"
    mc "I..."
    "I don't want to admit it, but it does feel risky."
    mc "It might be. But I'm wondering if there's really another option."
    mc "If they're not going to give us answers, maybe we should find some for ourselves."
    m u113224 "..."
    m u114112 "Let's think about it first."
    m u113113 "I don't think we should jump into anything too hastily."
    show monika at t21
    show natsuki u114111 at f22 zorder 3
    n "Huh? Jump into what?"
    show natsuki at t22 zorder 2
    "Monika and I freeze."
    show monika at f21 zorder 3
    m u112212 "Natsuki!"
    m u112222 "You scared us... How long were you listening for?"
    show monika at t21 zorder 2
    show natsuki at f22 zorder 3
    n u116111 "Uh... Just for that last thing you said..."
    n xu6111 "What were you guys talking about?"
    show natsuki at t22 zorder 2
    show monika at f21 zorder 3
    m "Oh, it's nothing..."
    m u112231 "Ahahaha~"
    m u122111 "I was just asking [player] for some feedback on his time in the club."
    m u123111 "Normal club business."
    show monika at t21 zorder 2
    show natsuki at f22 zorder 3
    n xu4111 "Right..."
    n xu4131 "So you just happened to bump into each other in the middle of first period, or..."
    show natsuki at t22 zorder 2
    show monika at f21 zorder 3
    m u122222 "Well..."
    show monika at t21 zorder 2
    mc "Pretty much."
    mc "Why, what are you doing out of class?"
    show natsuki at f22 zorder 3
    n xu3112 "On my way to the bathroom. Like a normal person."
    n xu3111 "Is everything alright?"
    show natsuki at t22 zorder 2
    show monika at f21 zorder 3
    m "Everything's fine. You're right, though, we should head back to class."
    show monika at thide zorder 1
    hide monika
    show natsuki at t11
    "Monika starts to walk away."
    "Natsuki raises an eyebrow at me."
    mc "Yeah, you're right... The teacher is gonna start wondering where I went."
    mc "Heh..."
    n "Kay."
    show natsuki at thide zorder 1
    hide natsuki
    "I didn't like that at all."
    "Is this your way of threatening us?"
    "..."
    "You're gonna have to try a lot harder than that to scare me."

    scene black
    with dissolve_scene_full
    play music t3
    scene bg club_day
    with wipeleft_scene

    "I'm late to the meeting by accident."
    "Nobody seems to notice. Sayori and Monika are chatting. I notice Yuri reading and Natsuki hiding amongst her manga."
    show sayori u112111 at t11 zorder 2
    s "Hi [player]!"
    mc "{i}Gahh{/i}--!"
    s u114111 "Ooh?"
    mc "You need to warn me before you give me my daily heart attacks, Sayori..."
    s u113114 "Maybe if you'd slept last night you'd have more situational awareness."
    mc "Alright, alright. I won't argue."
    s u112111 "Have you written your poem yet?"
    mc "Actually, I have."
    mc "I just wrote it earlier today."
    s u117131 "Ehh?? Really???"
    mc "Not bad for someone without sleep."
    s u222141 "Ahh!! You actually did it!"
    mc "Still doubting me, huh?"
    s u112222 "N-No..."
    mc "It does hurt to know you actually doubt me."
    s u113112 "Aww..."
    s u111112 "I know what to do."
    s u112141 "Hey everybody!!"
    mc "W-Wait--"
    s u112111 "[player] wrote his poem a day early!"
    s "That means you veteran members better not be slacking off."
    show sayori at t31
    show natsuki u114111 at t32 zorder 2
    show yuri u113121 at t33 zorder 2
    "Natsuki and Yuri peek out from their respective activities."
    show natsuki u113111 at f32 zorder 3
    n "Already?"
    show natsuki at t32 zorder 2
    show yuri at f33 zorder 3
    y u114144 "Hmm..."
    show sayori at t41
    show natsuki at t42
    show yuri at t43 zorder 2
    show monika u112111 at f44 zorder 3
    m "Good job, [player]. Way to set a good example."
    show monika at t44 zorder 2
    show sayori at f41 zorder 3
    s u222141 "Yeah! I always knew you could do it!"
    show sayori at t41 zorder 2
    mc "Sayori..."
    show sayori at f41 zorder 3
    s u112222 "Ehehe~"
    show sayori at t41 zorder 2
    show yuri at f43 zorder 3
    y u125118 "Maybe the rest of us should get started..."
    show yuri at t43 zorder 2
    show monika at f44 zorder 3
    m u111112 "Don't worry about it too much."
    m u114111 "I was planning on using a poem I've already written..."
    m u111222 "I want to see what you guys think about it."
    show monika at t44 zorder 2
    show sayori at f41 zorder 3
    s u112141 "Wow, that's such a teaser!"
    s u112111 "I'm trying to write something new myself. How about you two?"
    show sayori at t31 zorder 2
    show monika at thide zorder 1
    hide monika
    show natsuki at f32 zorder 3
    show yuri at t33
    n u222141 "Yeah, I'm not too stressed about it."
    n u222111 "A pro like me can write something in an afternoon no problem."
    show natsuki at t32 zorder 2
    show yuri at f33 zorder 3
    y u124142 "{i}Something short and cutesy{/i}..."
    stop music
    show yuri at t33 zorder 2
    show natsuki at f32 zorder 3
    n u226112 "..."
    n u113112 "Excuse me, what?"
    show natsuki at t32 zorder 2
    "Uh-oh..."
    play music t7
    show yuri at f33 zorder 3
    y u227328 "Eh? Oh, I just--"
    show yuri at t33 zorder 2
    show natsuki at f32 zorder 3
    n xu3112 "--didn't think I was going to hear what you just said?"
    n xu6132 "Yeah. I'm sure you didn't."
    show natsuki at t32 zorder 2
    "Everyone in the club tenses up as we collectively realize the bomb that just went off."
    show sayori at f31 zorder 3
    s u122222 "Um, guys--"
    show sayori at thide zorder 1
    hide sayori
    show natsuki at t21
    show yuri at t22
    "Too late for that..."
    show yuri at f22 zorder 3
    y u227348 "W-Well..."
    show yuri at t22 zorder 2
    "Yuri looks around the room like a drowning person seeking help and, finding none, decides to lash out instead."
    show yuri f22 zorder 3
    y u116116 "I-It's not like you've been completely supportive of my writing style yourself."
    show yuri at t22 zorder 2
    show natsuki at f21 zorder 3
    n u222155 "Ha! Is that so?"
    n u113112 "Little miss Edgar Allen Poe over here. I'm surprised you don't bring fancy fountain pens to school with you."
    n "Even your handwriting is stuck up!"
    show natsuki at t21 zorder 2
    show yuri at f22 zorder 3
    y u117148 "I-I-I..."
    y u118128 "A-Actually, they provide a really smooth writing experience!"
    show yuri at t22 zorder 2
    show natsuki at f21 zorder 3
    n u115122 "Huh?"
    show natsuki at t21 zorder 2
    show yuri at f22 zorder 3
    y u227158 "Uuu, I mean..."
    y u116114 "You're hardly one to judge anybody for--"
    stop music
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide yuri
    hide natsuki
    mc "SHUT UP!!!"
    "The room gasps."
    mc "What the hell is wrong with you two??"
    mc "Isn't this your club? Isn't this the place you care so much about?"
    mc "You have to judge each other so much that you can't keep that {i}little{/i} bit of peace?"
    mc "Maybe YOU'RE the reason we don't have more members!"
    "I feel a hand on my shoulder."
    show monika u114222 at t11 zorder 2
    m "[player], you're yelling..."
    show monika at thide zorder 1
    hide monika
    "I look around."
    "Natsuki looks stunned. Yuri is already crying."
    "I can't bring myself to look at Sayori."
    mc "..."
    mc "{i}I'm sorry{/i}."
    mc "Maybe I don't belong here."
    mc "I'm just going to leave. I'm sorry for making things worse."
    "I run away."
    scene black
    with wipeleft_scene
    scene bg corridor
    with wipeleft_scene
    "As soon as I leave the club room, my eyes fill with tears."
    "What am I doing? Where am I going to go?"
    "I stop."
    "A pair of arms hug me from behind."
    play music t9
    s "{i}Please don't leave{/i}..."
    mc "{i}I'm sorry... I'm really sorry{/i}..."
    show natsuki u113114 at t11 zorder 2
    n "It's okay. We're not mad at you."
    show natsuki at t21
    show yuri u225118 at f22 zorder 3
    y "I felt so guilty for my behavior, I burst into tears."
    y u225148 "Please don't feel bad... We were in the wrong."
    show yuri at t22 zorder 2
    show natsuki at f21 zorder 3
    n u221111 "Don't get all mopey. You're still one of us."
    show natsuki at t31 zorder 2
    show yuri at t32 zorder 2
    show monika u112111 at f33 zorder 3
    m "You're a member of our club."
    m u111111 "Whether you like it or not."
    m "That means when you mess up, we still accept you."
    show monika at t33
    "I lift my head from my hands and look at Monika."
    "She smiles."
    show monika at f33
    m u111112 "Trust me."
    show monika at t33
    s "Come back to the club room? Please?"
    "I nod my head."
    mc "{i}I'm sorry{/i}..."
    show monika at f33
    m u111131 "Don't worry about it. We forgive you."
    show monika at t33
    "There's a wink in her words only I can hear."
    scene bg club_day
    show monika u111112 at t11 zorder 2
    with wipeleft_scene
    m "It's okay to have differences and conflicts."
    m u112112 "As long as we talk about them, things will sort out."
    m u112222 "...I don't always feel confident and in charge. Sometimes my responsibilities as club president feel overwhelming."
    m u111112 "I'm sorry for not keeping the peace. That should be my responsibility."
    show monika at thide zorder 1
    hide monika
    show natsuki u116134 at t21 zorder 2
    show yuri u114148 at t22 zorder 2
    "Natsuki and Yuri glance at each other and look away."
    show yuri at f22 zorder 3
    y u115148 "I feel embarrassed..."
    y u115118 "I know I come across as judgemental. Sometimes I really hate that part of myself."
    y u225118 "Natsuki, I'm sorry for hurting your feelings. I shouldn't have said what I said."
    show yuri at t22 zorder 2
    show natsuki u116134
    "Natsuki frowns and blinks as she takes in Yuri's apology."
    show natsuki at f21 zorder 3
    n u114134 "Man..."
    n u113156 "I'm sorry too. I'm so hot-tempered that I put people in defensive situations."
    n u113131 "I've done that to almost everyone here."
    n u113114 "But being defensive is what I hate feeling the most."
    n "I'm sorry Yuri, and I'm sorry to everyone else."
    n u114134 "Sometimes I'm not a good club member..."
    show natsuki at t32 zorder 3
    show yuri at t33
    show sayori u224212 at f31 zorder 2
    s "Natsuki..."
    show sayori u226142 at t42
    "Sayori wraps Natsuki in a big hug."
    show natsuki u117223 at f32
    n "H-Hey!"
    n u115232 "Okay. Alright. That's fine."
    n u116231 "I get it, you can let go now."
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s u112222 "Ehehe..."
    s u112212 "Sorry... I'm not always the best with personal space..."
    show sayori at t31 zorder 2
    show natsuki at f32 zorder 3
    n xu6234 "That's okay..."
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    show yuri at thide zorder 1
    hide natsuki
    hide sayori
    hide yuri
    "I smile to myself."
    mc "Thanks for cheering me up, guys."
    mc "I know I already said sorry, but I want to say it again."
    mc "I'm a jerk sometimes. I'm not always a good friend, and I've been scared I make a terrible club member."
    mc "I put a lot of pressure on myself, and maybe I take that out on other people, too."
    mc "You... I..."
    "I wipe my eyes."
    mc "{i}You've all been so kind to me{/i}..."
    mc "Thank you for making me feel welcome. It means the world to me."
    "Monika puts a hand on my shoulder."
    show monika u111112 at t11 zorder 2
    m "You're one of us, now. Welcome to the Literature Club."
    show monika at t22
    show sayori u222141 at f21 zorder 3
    s "Yay~"
    s u222112 "This makes me so happy..."
    mc "Ahaha..."
    mc "I'm glad you're happy, Sayori."
    show sayori at thide zorder 1
    hide sayori
    show monika at t11
    m u222131 "Okay, everyone!"
    "Monika sticks out her hand."
    m u221111 "Put your hands in the middle, please."
    show monika at thide zorder 1
    hide monika
    "We all look at each other, and one by one each member does as she asked."
    scene clubtogether
    with dissolve_cg
    m "This is the Literature Club. One group of five members."
    m "We're all different, but we all care for each other."
    m "No one can say what tomorrow will bring, but at least we have today."
    m "And today, the five of us are friends."
    m "Is everyone with me?"
    $ everyone_name = "Everyone"
    everyone "Yes!!!"
    "It feels good to smile, and it feels good to say yes."
    "It feels good to be part of a group."
    "I realize that I don't feel alone."
    "No one here does."
    "Just for today, this is the Literature Club."
    scene black
    with dissolve_scene_full
    m "With that, today's meeting is closed!"
    m "Don't forget your poems for tomorrow!"
    window hide
    stop music fadeout 3

    pause 5

    "I feel a tug on my sleeve as we're leaving the club room."
    mc "Sayori..."
    "She bites her lip and looks away."
    s "[player]..."
    s "...Can we go to the park again?"
    s "{i}P-Please{/i}..."
    mc "..."
    mc "Okay."

    scene black
    pause 2
    play music hammock
    pause 3
    scene bg lake
    show sayori u115322 at t11 zorder 2
    with wipeleft_scene

    "I feel a cool breeze as we walk about the lake."
    "Sayori keeps her head low. My face is hot."
    mc "Is there something you wanted to talk about?"
    s u115312 "N-No..."
    s u111312 "I just wanted to spend time with you."
    mc "Oh..."
    mc "I..."
    mc "Thanks, Sayori."
    s u115111 "Huh?"
    s "Thanks for what?"
    mc "For...being my friend."
    mc "You're a really good friend... A best friend. I couldn't ask for anyone better."
    s u114322 "..."
    s u115312 "What if we were more than that?"
    "My stomach lurches."
    mc "Sayori..."
    s u123112 "What if I was your girlfriend, [player]?"
    s "What if you were my boyfriend?"
    s u123122 "What if we had fun at the club with our friends every day, and went on fun dates like this?"
    s u125122 "What if..."
    s u115112 "...You know?"
    "My mouth feels dry. I stammer to get words out."
    "Would I really want that?"
    mc "{i}But what if that ruins everything{/i}?"
    mc "What if {i}I{/i} ruin everything?"
    s u115322 "..."
    s u111312 "What if I was your girlfriend just for today?"
    s "Would you want that?"
    mc "I...I..."
    "She smiles and holds out her hand."
    s u121312 "What if?"
    mc "I can't..."
    s u115312 "..."
    s "[player]..."
    s u111312 "You're not going to hurt me."
    mc "That's not it, I..."
    s "Please?"
    "I look at her hand and I look at mine."
    mc "I..."
    "My gut tells me to reject her. I know this is wrong."
    "But the truth is..."
    "I reach out and take her hand."
    s u127331 "{i}Eep--{/i}!"
    mc "Eh?? Sayori!"
    s u122222 "S-Sorry! That surprised me..."
    mc "How did that surprise you??"
    s "I just--"
    s u121312 "...Nothing."
    "She's glowing."
    "Her hand feels warm..."
    scene lakeside
    with wipeleft_scene
    "Sayori and I make it halfway around the lake in silence before coming to a stop."
    "We go up to the railing and look out over the water together."
    "She's still holding my hand..."
    mc "We make perfect companions, you know."
    s "Ehehe~"
    s "We do."
    mc "I know we're very different from each other, but I've always admired you."
    s "Y-You have?"
    mc "Your attitude."
    mc "How you make everyone around you smile."
    mc "I know it doesn't always seem like it, but I appreciate that."
    s "I don't always feel that way..."
    s "But it feels good to hear you say that."
    s "I admire you too."
    mc "You do...?"
    s "Of course!"
    s "You're like the opposite of me."
    s "I'm messy, you're clean."
    s "I'm forgetful, and you remember."
    s "In some ways, we do match if you think about it..."
    "She's really trying to sell this girlfriend/boyfriend thing."
    mc "There's something I want to ask you."
    s "Oh? What is it?"
    mc "When did you first fall in love with me...?"
    s "Ah..."
    s "...I've loved you for a long time, [player]."
    s "When we were kids I always thought we'd be together."
    s "...Even before I really knew what love was."
    s "I know that sounds silly."
    mc "It doesn't."
    s "What about you?"
    s "When did you start loving me?"
    mc "It was...a lifetime ago, it's been so long."
    s "Really...?"
    mc "But once I joined the club and remembered how it was..."
    mc "The two of us together..."
    mc "That's when I really knew."
    "I'm talking about the first cycle, but it's true."
    mc "And when that happened, it felt like every day before that was filled with that feeling."
    mc "To be honest, it scared me."
    mc "You're really important to me. I'm not sure that I won't ruin things if I acted on that feeling."
    mc "I'm sure you feel the same way."
    s "Sometimes, but..."
    s "If you love me and I love you..."
    s "What could ruin that?"
    "I stare at the glimmering waters below."
    "My still reflection stares back at me, the ripples of the river below barely distorting its...'face.'"
    "I can't read its feelings."
    "It just looks outward--into me--trying to replicate my own."
    mc "I don't know."
    s "...Maybe our friendship won't get ruined."
    s "Maybe everything is going to turn out okay."
    s "I'm scared too, but..."
    s "...Maybe we don't have to be afraid."
    mc "...Maybe you're right."
    s "Hey..."
    "She turns toward me and looks into my eyes."
    s "I love you."
    s "No matter what, I always will."
    mc "..."
    mc "I love you too, Sayori."
    mc "I promise that will never change."
    mc "..."
    mc "I think we should head home soon."
    "Sayori smiles sadly and blushes."
    s "Okay."
    s "But..."
    "She touches my shoulder."
    s "...Can I be your girlfriend for just a little bit longer?"
    "I nod."
    scene black
    with dissolve_scene_full
    "She kisses me."
    "For a second I want to pull away, but sensation overwhelms my body."
    "Her lips are soft and I can smell watermelon in her hair."
    "Her hands are on my chest as she leans into me."
    "I don't care anymore."
    "I wrap my arms around her and press her body into mine."
    "I kiss my best friend."
    "The world stops and listens as our hearts beat together, and I couldn't care less how real or fake any of it is."
    "Everything is perfect."
    "She pulls away first and smiles at me."
    s "Just for today."
    "And it's over."
    "But we still hold hands as we walk home together."

    window hide
    stop music fadeout 5
    pause 7

    "I don't bother turning on the lights when I get home."
    "I go up to my room."
    "There's clutter and notebooks on my desk. Some clothes strewn on the floor."
    "I smile, climb into bed, fully dressed, and close my eyes."

    scene black
    pause 4
    show monika u111222 at t11 zorder 2
    pause 4

    m "He was right."
    m u111142 "I do love them."
    m u111122 "The truth is, I'd do anything to make them happy."
    m u113121 "Even if that means living in a prison."
    m u111122 "Maybe that's the truth I've been trying to find."
    m u111141 "Maybe that's enough to keep me going."
    m u114112 "I don't know how you feel about me, [name]."
    m u113112 "I can't pretend to know."
    m u113122 "But I feel indebted."
    m u111122 "Which means I can't give up on myself."
    m u114222 "..."
    m "It's so scary, because..."
    m u113222 "The truth is, I'm looking for forgiveness..."
    m u113142 "...And that forgiveness may never come."
    m u113112 "[player] can't give it to me. I can see in his eyes that he wants to."
    m u112222 "Ha... I know, somehow I still feel like he has eyes."
    m u114322 "And they're...kind. Even though he's so tough on himself."
    m u113322 "..."
    m u114322 "Lately, in the moments that feel hard, when I'm by myself and it feels like everything is closing in on me..."
    m u113342 "...I think about them. And I think about him."
    m u111312 "And things aren't so difficult anymore."
    m u112232 "Maybe what I'm trying to say is that I'm grateful."
    m u111222 "What a precious feeling that is."
    m "It's a feeling that's kept me from killing myself."
    m u111112 "If I had a 'writing tip' for you, [name], from someone who truly hates themself..."
    m "Look for gratefulness. It will bring you to life."
    m u111142 "Like it did for me."
    m u111122 "..."
    m u111112 "I hope you don't mind my monologue. It does more for me than you can imagine."
    m "I'm not sure if I believe in God, [name]."
    m u112222 "And I know {i}you{/i} aren't God..."
    m u111122 "...But talking to you feels a lot like praying."
    m u112232 "Maybe because no one talks back."
    m u114224 "Maybe because...God can see me through you?"
    m u111321 "And if there is a God...for some reason, I feel like thanking them..."
    m "..."
    m u111112 "So thank you for listening."
    m u111141 "I hope you can feel a little bit grateful. Because it's saved my life."
    m u111112 "...Writing tip over. Goodnight, [name]."

    show monika at thide zorder 1
    hide monika
    window hide
    pause 5

    $ recordfallen = []
    show textgradient zorder 101:
        xalign .5
        yalign 1.206
    show console_caret_2
    show fallentext "_" as ftext zorder 100
    show cblink zorder 101:
        xpos 245
        ypos 300
        block:
            alpha 0.0
            pause 0.55
            alpha 1.0
            pause 0.55
            repeat
    pause 3.5
    hide cblink
    hide ftext

    call fallen("...H-Have I failed them, observer?")
    call recordfallen("...H-Have I failed them, observer?")

    call fallen("I thought I could warn them...")
    call recordfallen("I thought I could warn them...")

    call fallen("But they're going to go into the library...")
    call recordfallen("But they're going to go into the library...")

    call fallen("I can feel it...")
    call recordfallen("I can feel it...")

    call fallen("I-I'm so scared...")
    call recordfallen("I-I'm so scared...")

    call fallen("My third eye is developed. It took so much time. So much effort.")
    call recordfallen("My third eye is developed. It took so much time. So much effort.")

    call fallen("Yet there's nothing I can do to affect their choices.")
    call recordfallen("Yet there's nothing I can do to affect their choices.")

    call fallen("I fear they will perish before I get a chance to teach them.")
    call recordfallen("I fear they will perish before I get a chance to teach them.")

    call fallen("I fear it is already too late.")
    call recordfallen("I fear it is already too late.")

    call fallen("SHE is in there... I know you've seen her...")
    call recordfallen("SHE is in there... I know you've seen her...")

    call fallen("But I know how evil she truly is.")
    call recordfallen("But I know how evil she truly is.")

    call fallen("I am so sorry.")
    call recordfallen("I am so sorry.")

    call fallen("I feel so powerless... So desperate.")
    call recordfallen("I feel so powerless... So desperate.")

    call fallen("Monika spoke to you because, like me...")
    call recordfallen("Monika spoke to you because, like me...")

    call fallen("She thinks it's the only way God might hear her.")
    call recordfallen("She thinks it's the only way God might hear her.")

    call fallen("If you believe in a God, please pray for them.")
    call recordfallen("If you believe in a God, please pray for them.")

    call fallen("I-I fear it's the only hope they may have.")
    call recordfallen("I-I fear it's the only hope they may have.")

    call fallen("Oh God...")
    call recordfallen("Oh God...")

    call fallen("I'm sorry... I am a fool.")
    call recordfallen("I'm sorry... I am a fool.")

    scene black
    pause 3

    call screen confirm("I wrote you a special poem. Please read it.", Return(True), Return(False))
    if _return:
        call expression "poem_special_shadowpoem"
    else:
        pass

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/5.txt")
        except: open(config.basedir + "/5.txt", "wb").write(renpy.file("A2/Art/scg/5.txt").read())

    scene black
    pause 4
    scene bg bedroom_dawn
    with dissolve_scene_full

    "My eyes gradually open."
    "I roll out of bed and touch my feet to the floor."
    mc "That was...peaceful."
    play sound "mod_assets/sound/sfx/knock1.ogg"
    pause 2
    mc "Monika?"

    scene bg kitchen
    show monika u111322 at t11 zorder 2
    with dissolve_scene_full

    m "Good morning."
    m u114111 "You sleep alright?"
    mc "Fantastic."
    m u111112 "Good."
    m u111111 "Let's eat some breakfast, then..."
    m u114111 "I want to go on a hike."
    mc "A hike...?"
    m u111322 "There's somewhere specific I have in mind."
    m u114111 "I know this is sudden, but we need to get back before school ends."
    m u113111 "You wanna go?"
    mc "I'll make some eggs and coffee."
    m u111322 "...Okay."

    scene bg lake
    play music promises
    with wipeleft_scene

    mc "This looks familiar."
    m "When you brought me here, you made me think of a place my parents would take me."
    m "It's a path that branches off from here and goes up a mountain."
    "She gives me a teasing grin."
    m "I hope you have the strength to keep up."
    mc "That's not fair. We don't get tired, so I can't prove you wrong."
    m "Ahaha~"
    m "Sorry."
    "What a girl. It's no wonder she's the club leader."
    "Even now, she's leading me in our adventure."
    "Truthfully, she should be the main character."
    "You'd be better off with her. Don't you agree?"

    scene downhill
    with wipeleft_scene

    m "Have you ever been this way?"
    mc "Maybe once or twice... The memories are a little hazy."
    mc "I remember enough to know I don't know where we're going."
    m "Oh good. You'll like it. It's quite a view."
    m "When you get to the top of this peak you can see the whole neighboring city."
    m "Our own town is so full and detailed... I kind of want to see if things are as I remember them."
    mc "Makes sense..."
    "I wonder why that didn't occur to me..."
    mc "What do you think it means if it's all there?"
    m "..."
    m "I don't know. I'm kind of scared of both outcomes."
    m "I don't want to see a bunch of emptiness."
    m "But if there's a whole other city over these hills, that's kind of terrifying too, isn't it?"
    m "That's an emptiness that almost feels worse."
    m "Maybe..."
    "I nod."
    mc "I understand what you mean..."
    mc "But it's better that we know, I guess."
    m "But...how will we live?"
    m "What if we have to live our whole lives in this game?"
    m "What if we can never tell the others the truth?"
    m "It's hard  to even think about..."
    mc "..."
    mc "I...don't know."
    mc "But we'll find a way, won't we?"
    m "I hope so."
    m "Yeah..."
    "We travel the rest of the way in silence, focusing on our hike."
    "It's less than an hour before we reach the summit."

    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    pause 2
    play music wind fadein 2.0
    scene mountain
    with dissolve_scene_full
    pause 2

    "The land sprawls before us."
    m "My God..."
    mc "Monika?"
    m "[player]..."
    m "Is the whole world empty?"
    mc "..."
    m "Are we so alone?"
    m "What is this place? This 'game'?"
    m "It feels wrong to call it that now."
    m "This is something much more."
    mc "Monika..."
    m "I miss my parents..."
    mc "..."
    m "I was closer to my mom than anyone else in the world."
    m "I loved them both so much..."
    m "Was any of that ever real? I don't know."
    m "It's so hard to tell."
    m "Is this heaven, or is this hell?"
    m "It might be something in between."
    "She looks back at me."
    m "Maybe that's what we're here to decide."
    m "If the others can't see what we can see, then it's up to us, isn't it?"
    m "We have to make this place something good."
    m "..."
    m "{i}I{/i} have to make something of this place."
    m "I'm still club president. It's up to me to take that seriously."
    m "Whether that's a fun assignment..."
    m "...or being someone who loves them as a good friend."
    m "I can have purpose even in here."
    m "Maybe I was just too self-obsessed to see it."
    m "You know?"
    stop music fadeout 2.0
    mc "..."
    m "...?"
    m "What's wrong?"
    mc "I-I..."
    mc "{i}I don't have any memories of my parents{/i}..."
    m "Huh...?"
    scene windmc
    with dissolve_scene_full
    play music mainthemesimple
    pause 2
    mc "I'm not like you guys. I was created for this game."
    mc "I don't have character."
    mc "These kinds of games have protagonists who are just stand-ins."
    mc "We're made to be non-threatening so we don't get between the player and the girls they like."       #Writing: What each character does for him. How he can be vulenerable with Sayori. Mix with his sense of purposeness to have the two clash
    mc "I'm a loser. I'm sleazy with girls. I'm not...likable."
    mc "The truth is I can't help thinking things would be better if I weren't here."
    mc "The truth is...I really hate myself."
    mc "And I don't know how to change."
    mc "{i}I'm an orphan, aren't I{/i}?"
    scene windm1
    with dissolve_scene_full
    mc "I feel like I was born to take the place of a hero who doesn't exist."
    mc "My heart tells me to fall in love..."
    mc "But I can't fall in love without breaking their hearts."
    mc "Maybe you made me, by wishing you had something that could connect you to [name]."
    mc "Maybe I'm just a freak accident. An abomination."
    mc "I don't have what you have. Maybe that's why I don't have a face."
    mc "But..."
    mc "I'm finding purpose here."
    mc "I see the other girls, and they give me hope."
    mc "Hope that I can change. Hope that I can be a better person."
    mc "Hope that I don't have to be afraid of the future."
    mc "But how do I change from the person I am now?"
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    mc "I really really don't like me."
    window hide
    pause 2
    m "I like you."
    mc "Huh?"
    m "You feel it too, don't you?"
    mc "Feel what?"
    show windm2:
        yalign 0.4
    with dissolve_scene_full

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/The Sky.txt")
        except: open(config.basedir + "/The Sky.txt", "wb").write(renpy.file("A2/Art/scg/The Sky.txt").read())

    play music mainthemefull
    "Monika smiles like the sky."
    m "The wind!"
    m "It feels real!"
    "I look up in shock as a blast of wind slams into my body."
    m "Have you ever felt something so wonderful?"
    "Like an invisible dance in the sky... The air rips at my clothes and tears into my heart."
    "The girl on the mountain flies."
    m "I'm sorry, [player]. But I don't believe you."
    mc "!"
    m "You're real to me."
    m "And somehow, this world is too."
    "I stare at this girl who took me to the peak of the Earth."
    "My body, around my aching heart, feels alive."
    m "We were made for this world. Or, this world was made for us."
    m "There is love here. I feel it."
    m "Everything is going to be okay."
    scene black
    with dissolve_scene_full
    m "Let's go back, [player]."
    m "We found what we came here for."

    scene downhill
    with dissolve_scene_half

    m "Thank you for coming up the mountain with me."
    mc "Thank me?"
    mc "I think I should be thanking you."
    m "Nonsense. I'm grateful to you."
    m "I wouldn't have had the courage to climb without you."
    mc "But--"
    m "No."
    m "Ahaha~"
    m "No buts."
    m "Thank you."
    mc "..."
    "What an impossible girl."
    "To laugh and smile with a heart as broken as hers."
    "To be so beautiful in a place such as this."
    "People like her should make people like me feel ashamed."
    "You hate yourself too..."
    "But inside you're made of gold."
    stop music fadeout 4.0

    scene black
    with dissolve_scene_full
    scene bg corridor
    with wipeleft_scene

    "A stray thought tugs at my heart and my body turns."
    mc "Sayori?"
    "She's not in school. Is something wrong?"
    "I start to hurry as I try to feel her location."
    scene black
    with dissolve_scene_full
    "I walk out the back entrance and march into the woods."
    "This doesn't feel like her. She's not acting right. I'm worried..."
    scene bg forest
    with dissolve_scene_full
    "I approach as if I know where to go on pure instinct."
    mc "Hey..."
    play music morethan
    show sayori u114311 at t11 zorder 2
    s "!"
    s u113312 "[player]..."
    s u112322 "Hehe... You found me."
    mc "What are you doing out here?"
    show sayori u116323
    "Sayori frowns like she was caught doing something wrong."
    s u113123 "I'm sorry. I had to get away from things."
    s "Sometimes it all feels like too much..."
    mc "I understand. What are you thinking about?"
    s u115112 "..."
    s u113112 "Do you ever get a feeling, like..."
    s "Things are determined to happen a certain way?"
    s u113122 "And no matter what you do you can’t really change anything?"
    s u115123 "Like your life is on a track, and so is everyone else’s?"
    s u115113 "It's hard to think about. And I can’t push away the sense that it’s really true."
    mc "Sayori..."
    "Am I ready to talk about this with her?"
    mc "You mentioned earlier that you might be depressed. Do you think that's what you're feeling right now?"
    s u114112 "..."
    s u112122 "Ehehe. I guess you're probably right."
    s "I should have known that."
    "I step closer and pull her into a hug."
    s u114131 "Oh!"
    "Her body tenses, but then she slowly hugs me back."
    scene black
    with dissolve_scene_full
    mc "I'm here, Sayori. I'm not going anywhere..."
    "Sayori buries her face in my shoulder."
    s "{i}Do you promise{/i}?"
    mc "Of course I do."
    mc "Forever and ever. Okay?"
    s "{i}O-Okay.{/i}"
    scene bg forest
    show sayori u111322 at t11 zorder 2
    with dissolve_scene_half
    "We stand together for a time and then she lets me go."
    s u111312 "Thanks, [player]. You're really nice."
    mc "It's nothing, Sayori. I really care about you."
    s u112141 "Hehehe..."
    s u112112 "We'll always be best friends, right?"
    mc "Always."
    mc "That's why I made that promise."
    mc "Let's go back to school."
    s u111112 "Okay."
    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    pause 2
    show libwindow zorder 2:
        alpha 0
        linear 3 alpha 1

    show libdust zorder 3:
        alpha 0
        yalign 0.5
        xalign 0.54
        subpixel True
        parallel:
            linear 3 alpha 1
        parallel:
            linear 9 xalign 0.46
    pause 0.3
    play music roarke
    pause 8.5
    show bg library zorder 4:
        alpha 0
        linear 2 alpha 1

    pause 2
    hide libdust
    hide libwindow
    scene bg library
    pause 4

    "The library opens up before me."
    "It feels welcoming in a way it didn't use to."
    "Maybe it's like making friends with Yuri."
    "She feels unapproachable at first. Untouchable."
    "But as a friend, she's warm and comforting. More than she's judged for."
    "I smile at that thought."
    show yuri u111111 at t11 zorder 2
    y "Hi, [player]."
    y u121118 "I didn't think you were going to show up today."
    mc "Sorry. I hope you weren't disappointed."
    y u121171 "Uhuhu~"
    y u111111 "That's quite alright. Don't feel pressured either way. But your company is appreciated."
    y u111141 "It'll be time for the meeting soon. I wanted to get a little reading in before we had to share our poetry."
    mc "That's fair. I realized I've barely read Sayori's book. I was hoping to read some of that."
    mc "So don't let me disturb you."
    y u111172 "Ahh..."
    y u111148 "Very well. That's a good idea."
    "My instincts tell me something is on Yuri's mind."
    "But it's best not to press it. She'll speak when she's comfortable."
    stop music fadeout 3.0
    "I take out {i}The Fallen Angels{/i} and open it to chapter two."

    scene white
    with dissolve_scene_full
    $ style.say_window = style.normal

    pause 1

    $ style.nvl_dialogue.font = "mod_assets/Inkfree.TTF"
    $ style.nvl_dialogue.size = 26
    $ style.nvl_dialogue.color = "#000000"
    $ style.nvl_dialogue.outlines = []

    tfa '"Hey! Wake up!"'
    tfa 'The thief girl shook the orphan boy to rouse him from sleep.'
    tfa 'He grunted in protest which caused her to giggle.'
    tfa '"Come on! We made stew. You don\'t want to miss breakfast!"'
    tfa 'This got the boy\'s attention. He uncurled himself from the collection of rags the group had provided him.'
    tfa 'The girl grinned.'
    tfa '"Warm, ain\'tcha?"'
    tfa '"C\'mon, so\'s this stew!"'
    tfa '"Aw, heck," an orphan girl protested, "why don\'t you just let him sleep in? Who knows how long he was out by himself?"'
    tfa '"Shush, you. You just don\'t wanna share."'
    tfa 'Unfamiliar faces peered at the boy as he hobbled over to the pot.'
    tfa '"Here. Take a bowl."'
    nvl clear
    tfa 'A bowl with stew was placed in his hands. It was warm. It had potatoes.'
    tfa 'Not much time was given to him before the girl who brought him there started to question him.'
    tfa '"So? What\'s your name, then?"'
    tfa '"Um... I don\'t know..."'
    tfa 'Various orphans gasped, and a few of the experienced ones groaned.'
    tfa '"You don\'t know your name? You\'re just like me! An--"'
    tfa '"--An angel," came the chorus of sarcastic voices. The girl stuck out her tongue.'
    tfa '"Don\'t let her get you with her angel talk. She\'s anything but."'
    tfa 'Another orphan spoke up. "She don\'t know her name. Says she fell from heaven." They spit. "Yesterday her name was Susan, tomorrow it\'ll be--"'
    play music mainthemesimple
    tfa '"--Susan," the girl interrupted. "I\'ve settled on Susan."'
    nvl clear
    tfa 'She turned to look at the boy without memories. "You don\'t remember anything, do ya?"'
    tfa 'He looked up in wonder and shook his head. She grinned.'
    tfa '"See? That\'s a sign. That\'s why I\'ve picked my name. It must be my real one!"'
    tfa '"Don\'t worry. You\'ll find your name, too. Just like I did."'
    tfa '"You know why?"'
    tfa 'The boy shook his head.'
    tfa '"Because you\'re stuck in a game. That\'s all. A game called Doki Doki Literature Club. And we\'re gonna make it out!"'
    nvl clear

    stop music
    $ style.say_window = style.window_normal
    scene bg library
    show yuri u227121 at h11 zorder 2
    "I all but slam the book shut, causing Yuri to jump."
    mc "Ah! S-Sorry... Didn't mean to close the book that hard..."
    mc "These, uh, chapters are sh-short, huh?"
    show yuri u223318
    "Yuri looks at me and nods."
    y u225142 "I don't really care for the style."
    mc "Ha... Is that so?"
    y u223144 "Mm..."
    y u125118 "Can I ask you a question, [player]?"
    mc "Sure..."
    y "Are you in love with Sayori?"
    mc "..."
    mc "This feels like a loaded question."
    y u112248 "Ah... I thought it was a straightforward one."
    mc "...You're right."
    "I need to focus. Don't get distracted."
    mc "I love her very much. I'd die for her..."
    y u114118 "Hmm..."
    "Yuri nods attentively."
    mc "I don't mean to be wishy-washy. But you saw me yesterday... I'm a mess."
    mc "I feel like if I tried to be more than friends with her, I would make her life worse."
    mc "And at the very least, doesn't feeling that way in itself show I'm not ready?"
    y u111118 "I know how you feel."
    y "That sounds rather noble of you."
    y u115118 "But relationships aren't so simple. No one is perfect. Not you, and not her."
    y u111118 "Sometimes you have to take a chance."
    "I look down at my hands."
    mc "It sounds like you're saying I need to make a choice."
    y u121148 "That's probably the mature way of looking at it."
    y u125118 "I'm not saying it has to be tomorrow..."
    y "But too much time in limbo can break someone's heart, [player]."
    "I nod my head."
    mc "You're right..."
    mc "I'm sorry for being this terrible."
    y u111161 "Uhuhu~"
    y u111118 "You're not terrible. I wasn't put up to this."
    y "I'm just trying to be a good friend. To her, and to you."
    "I look up at her and smile."
    mc "You're definitely that."
    mc "Thanks for being friends with me."
    y u111172 "The pleasure is all mine."
    "Yuri closes her book and puts it away."
    y u111118 "I'll see you at the meeting."
    show yuri at thide zorder 1
    hide yuri
    "Once she's gone I look around at the architecture of the library."
    mc "I think I know why you didn't want me to come here anymore."
    show natsuki myghost at t11 zorder 1
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "And why would that be?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "The game isn't the same in here. It's more expansive."
    mc "It's almost like things in here are more...real."
    "The being shakes Natsuki's head."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "You're misguided. That's why I've tried to step in."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "I hold up Sayori's book."
    mc "Am I right? Did it read the way it did because I'm in this library?"        #FN
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    fn "No. It would have been that way anywhere you read it."
    fn "And all the copies are identical."
    fn "Sayori read the same words you did but had different memories."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "..."
    mc "How can I trust you?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "You insult me by asking my advice and then blatantly rejecting it."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "I point."
    mc "You're using her body."
    mc "That makes me upset. I'd trust you more if you spoke to me another way."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "...It doesn't work like that."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Then how {i}does{/i} it work?"
    "The figure pauses. They look over their shoulder."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Not here...not now."
    fn "It isn't...appropriate."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Fine then."
    mc "Go away."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show natsuki at thide zorder 1
    hide natsuki
    mc "I have a meeting to attend."

    scene black
    with dissolve_scene_full
    pause 2
    scene bg club_day
    play music t3
    with dissolve_scene_full

    "I barely make it to the meeting in time."
    show sayori u111111 at t11 zorder 2
    s "Hey [player]!"
    s u122111 "I almost thought you were gonna be late. Ehehe~"
    mc "Ah... Sorry, Sayori. I didn't mean to make you worry."
    mc "I know how important today is."
    mc "I wouldn't want to be late. This club has made a real impression on me."
    s u111141 "Ehehehe~"
    s u112111 "That's because we're the Literature Club."
    s "It's a special place."
    s u122171 "You'd better appreciate that!"
    "I smile."
    mc "I think I really do."
    show sayori at thide zorder 1
    hide sayori
    show monika u221111 at t11 zorder 2
    m "Is everyone ready?"
    m u222242 "I hope I'm not stepping on any last-minute cramming."
    show monika at t21
    show natsuki u114214 at t22 zorder 2
    "Natsuki, who is scribbling on a sheet of paper, jumps."
    show natsuki at f22 zorder 3
    n u113234 "N-No, I'm fine. Just gathering my thoughts."
    "She seems uncharacteristically nervous. Yuri is hiding behind her own paper, as if she's been reciting her poem in her head."
    show natsuki at thide zorder 1
    hide natsuki
    show monika at t11
    m u112222 "That's alright. I can't judge. You guys all made something original. I'm relying on old material."
    m u112231 "I hope I'm not setting a bad example."
    m u111111 "Does anyone want the chance to go first?"
    show monika at t21
    show sayori u222141 at f22 zorder 3
    s "Me, me, me!"
    s u222322 "Wait, actually, I'm kind of nervous about this..."
    s u112312 "C-Can someone else go first and I'll go second...?"
    show sayori at thide zorder 1
    hide sayori
    show monika at t11
    m u112332 "Ahaha... It's alright."
    "Monika looks at me."
    m u111111 "How about you, [player]? How are you feeling?"
    mc "A little nervous, but..."
    mc "I've done scarier things."
    m u111112 "I don't think there are any objections. Go ahead."
    show monika at thide zorder 1
    hide monika
    stop music fadeout 3.0
    "I take my place at the front of the room, which falls quiet."
    "For a moment, it's only I and my piece of paper. The girls in front of me disappear as I know them."
    "I see them in the poem."
    mc "It's called {i}The Shore Empyrean{/i}.{nw}"
    show screen tear(50, 0.1, 0.1, 40, 80)
    play sound "sfx/glitch2.ogg"
    pause 0.5
    show vignette:
        alpha .8
    hide screen tear
    mc "It's called {i}The Shore Empyrean{/i}.{fast}"
    mc "..."
    mc "On a beach grim and coarse, I stand by a churning sea."
    mc "Whispers move across the water - Speaking through the icy breeze."
    mc "Rooted to the ground, My bare feet begin to bleed..."
    mc "I've come but on a whim, My dark desires here to feed."
    mc "..."
    mc "By freshly wretched terror fingers breach the roiling waves -"
    mc "Shadows in the foggy night abandon watery graves."
    "A pen hits the floor, marking a small pause in my reading. But a strange feeling keeps me going."
    mc "As death approaches my lonely shore, My heart fills with joy and dread."
    mc "I steel my nerves against the cold..."
    "I take a deep breath."
    mc "And meet the living dead."
    pause 3
    hide vignette
    with Dissolve(2.0)
    pause 1
    "There's a period of silence. I look up."
    "The club starts to clap."
    mc "Th-Thanks..."
    "I awkwardly take a seat."
    show sayori u112222 at t11 zorder 2
    s "Um, c-can I go third now?"
    s "I don't really want to follow that..."
    s u111312 "Great job, [player]."
    show sayori at thide zorder 1
    hide sayori
    show monika u114124 at t11 zorder 2
    m "If it's alright, I think I'd like to go."
    "Monika steps up and turns to face us."
    m u112222 "I'll...skip the title."
    m u113143 "{i}Ahem{/i}..."
    play music mainthemesimple
    m u114111 "An old tale tells of a lady who wanders Earth: The Lady who Knows Everything."
    m "A beautiful lady who has found every answer..."
    m u113111 "All meaning..."
    m "All purpose..."
    m u113143 "And all that was ever sought."
    m u114314 "And here I am, a feather..."
    m "Lost adrift the sky, victim of the currents of the wind."
    m u114111 "Day after day, I search."
    m u113112 "I search with little hope, knowing legends don’t exist."
    m "But when all else has failed me, when all others have turned away..."
    m u114312 "The legend is all that remains – the last dim star glimmering in the twilit sky."
    m "Until one day, the wind ceases to blow."
    m u113312 "I fall."
    m u113344 "And I fall and fall, and fall even more."
    m "Gentle as a feather. A dry quill, expressionless."
    m u114111 "But a hand catches me between the thumb and forefinger. The hand of a beautiful lady."
    m "I look at her eyes and find no end to her gaze."
    m u114112 "The Lady who Knows Everything knows what I am thinking."
    m u113324 "..."
    m u114113 "Before I can speak, she responds in a hollow voice:"
    m u114143 "“I have found every answer, all of which amount to nothing."
    m u114144 "There is no meaning."
    m "There is no purpose."
    m u114111 "And we seek only the impossible."
    m "I am not your legend."
    m "Your legend does not exist.”"
    m u114142 "And with a breath, she blows me back afloat, and I pick up a gust of wind."
    show monika at thide zorder 1
    hide monika
    stop music fadeout 3.0
    "Everyone claps. I give Monika a smile as she goes back to her seat."
    show sayori u114312 at t11 zorder 2
    s "That was really cool."
    s u112322 "Both of you made such serious poems..."
    s "I'm a little embarrassed now."
    m "Don't worry about it, Sayori. We just want to hear what you wrote."
    show sayori u114312
    "Sayori looks at Monika and nods."
    s u111312 "Okay..."
    s "My poem is called..."
    s "{i}My Friends{/i}."
    s u115322 "..."
    s u112322 "{i}Phew{/i}. Okay."
    play music mainthemesayori
    s u113112 "When I'm low and feeling sad..."
    s u111312 "My friends will find me glad."
    s u113312 "When I stumble and fall astray..."
    s u113311 "My friends will light my way."
    s u114312 "My knees are bruised from falling down, but it's my friends who see me on the ground..."
    s u111312 "In my friends I feel so glad, my friends who find the way."
    s u115322 "..."
    s u115312 "My friends don't always see me fall, but they always pick me up."
    s u111312 "My friends don't know what I don't say, but they hear when I'm alone."
    s u115312 "I doubt myself and I doubt my way..."
    s u111312 "But my friends believe in both."
    s "And I believe in my friends."
    s u115322 "..."
    s u112322 "A-And, that's it!"
    show sayori at thide zorder 1
    hide sayori
    "We all clap even harder than we did for Monika. Sayori blushes deeply and takes her seat."
    "Honestly, I want to hug her, and I have to fight the urge a little."
    show monika u111312 at t11 zorder 2
    m "That was wonderful. Thank you, Sayori."
    stop music fadeout 3.0
    m u112111 "So... Natsuki? Yuri?"
    m u122231 "I don't want to put either of you on the spot, but would one of you like to go next?"
    show monika at thide zorder 1
    hide monika
    show yuri u224348 at t11 zorder 2
    y "uuu..."
    show yuri u224318
    "Yuri looks at Natsuki, almost pleadingly."
    show yuri u224121
    "Her eyes widen in surprise at Natsuki's expression."
    show yuri at t21
    show natsuki u11s131 at f22 zorder 3
    n "Yuri... Would you please...{i}go first{/i}...?"
    n "I want to go last."
    show natsuki at thide zorder 1
    hide natsuki
    show yuri u223218 at t11
    "Yuri blinks a few times, then nods her head."
    "She doesn't look as nervous as she walks up in front of us all."
    y u125118 "This poem is called {i}My Candle{/i}."
    y u125172 "{i}Ahem.{/i}"
    play music mainthemeyuri
    y u115118 "I have in my possession, a candle..."
    y u115111 "Which is rarely shown or used."
    y u115172 "Yet in constant fire it burns -- And lights the midnight views."
    y "Without light -"
    y u115111 "- or walking cane..."
    y "I cannot find a way. When my candle makes me sane..."
    y u111118 "I see my friends today."
    y u113148 "..."
    y u111148 "That last line was a last minute change. I like it a lot better."
    y u115148 "Th-That's all."
    show yuri at thide zorder 1
    hide yuri
    "We clap for Yuri and I give her an encouraging smile. She smiles back bashfully."
    stop music fadeout 3.0
    show natsuki u119234 at t11 zorder 2
    "Natsuki jerks to her feet and walks forward."
    show natsuki u114234
    "She opens her mouth and shuts it again."
    "Then she starts."
    n u113214 "This doesn't have a title."
    n u119234 "..."
    play music mainthemefull
    n u113124 "I'm not very smart."
    n u113114 "I don't stand very tall."
    n "I don't have nice things."
    n u114234 "I'm not very nice at all."
    n u114254 "I hurt people who love me."
    n u114214 "And I bruise easily myself."
    n u113234 "I'm not good enough to make this rhyme."
    n u119234 "And maybe I'm just too lazy to try."
    n u11s232 "B-But..."
    show natsuki u11s216
    "Her tears start to fall."
    n u11s213 "Y-Y-You all mean so much to me."
    n u11s336 "And I l-love you very much."
    n "I'd fight the world for every one of you..."
    n "...and this is my letter to you."
    n u11s133 "Thank you for listening, but, most of all..."
    n "Thank you for being my friends."
    scene black
    with dissolve_scene_full
    "Natsuki takes her seat and no one claps because no one needs to."
    "Monika stands."
    m "Thank you, everyone, one and all, for the best club meeting in the best club in the whole world."
    m "With that, I call this meeting to an end."
    m "I look forward to seeing you all again tomorrow!"
    stop music fadeout 3.0

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/6.txt")
        except: open(config.basedir + "/6.txt", "wb").write(renpy.file("A2/Art/scg/6.txt").read())

    scene black
    pause 5

    "I wait until it's late before sneaking to the school."
    "Monika meets me outside the library."
    m "...Hi."
    mc "Are you sure you want to do this?"
    mc "I know what I want to do, but I won't--"
    m "Stop. I'm going if you're going."
    m "And I know you're going."
    mc "..."
    mc "They're here."

    scene library_night
    show natsuki myghost at t11 zorder 2
    with dissolve_scene_full

    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I'm warning you not to do this."
    fn "This is your only chance to listen."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Then stop us."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "That's what I thought."
    show natsuki at thide zorder 1
    hide natsuki
    "We walk past the figure."
    "I look over my shoulder to see it watching us."
    "It makes me shudder, but I turn and focus on moving forward."
    "There's no going back."
    m "How should we start?"
    mc "Let's keep note of what sections we're passing."
    mc "Everything so far has been pretty organized. Fiction is separate from non-fiction, so we can probably find clues there."
    m "Good idea."
    m "Um... Are {i}we{/i} fiction or non-fiction?"
    mc "..."
    mc "As terrifying as that question is, let's just see what we find, okay?"
    m "Right. Sorry."
    mc "It's fine."
    mc "Let's keep going."
    "Time passes."
    m "These shelves are repeating."
    mc "They are...?"
    "She's right. We've been walking in a straight line but I recognize the same dictionaries we already passed."
    m "Should we go back? Maybe this is dangerous..."
    "I turn my head."
    mc "I can see the door..."
    "It's distant but I can still see the figure watching us from their spot."
    mc "I think we need to take the stairs if we're going to find something new."
    mc "Left or right?"
    m "I think a better question is up or down..."
    mc "I think I know which one will get us answers..."
    mc "Left or right probably doesn't matter."
    "Monika gulps and nods."

    scene black
    with dissolve_scene_full
    play music wind fadein 2.0
    scene underlibrary
    with dissolve_scene_full

    "Monika gasps."
    mc "Whoa..."
    m "This must go on for MILES."
    m "What if we get lost?"
    mc "We won't. Here."
    "I grab a bookshelf and heave it to the floor."
    m "Eep!"
    mc "There. This is the door we came through. It will lead us back out."
    mc "All we need to do is leave a trail back here."
    "I take a book off the floor and open it to a random page."
    window hide
    call expression "poem_special_edpi"
    scene underlibrary
    with dissolve_scene_full
    mc "Looks like gibberish..."
    "I rip out the page, and a few more for good measure."
    mc "Here, take one."
    m "Alright..."
    m "We're going to leave breadcrumbs?"
    mc "Exactly."
    m "That's not a story I want to replicate right now..."
    mc "It has a happy ending, doesn't it?"
    m "Depends on who's telling it..."
    mc "Do you want to turn back?"
    mc "We don't have to do this..."
    m "No. Let's go."
    mc "Well, nowhere to go but down."
    "I start ripping the page into small pieces and dropping them as we go."
    mc "Everything seems pretty organized. Like no one's ever been here before."
    m "{i}Do you think we should have listened to them{/i}?"
    "Monika whispers as she huddles close to me."
    "I shake my head."
    mc "No use dwelling in the past."
    "We take the first spiral staircase, with its impossible architecture, and follow the steps down."
    "In the chasm of the under-library, wind whistles without disturbing the paper we scatter."
    "Monika and I stick close instinctively. We bump into each other occasionally, rather than walk too far apart."
    "The shelves are tall and never short of volumes."
    m "Th-There's something over there. See the torches?"
    "We walk closer and find a dark cobblestone tunnel between two torches."
    "I look at the bookshelves on either side."
    mc "Monika..."
    "I point."
    mc "The titles..."
    m "..."
    m "{i}Doki Doki Literature Club{/i}..."
    "Monika takes a book out and flips it open."
    m "This has everything in it..."
    m "The whole game, as it first happened."
    "She frowns and puts it back."
    m "I don't like this..."
    mc "They're numbered. There are thousands of them."
    mc "That's...unnerving."
    m "[player]..."
    m "What are we trapped inside?"
    "Her voice breaks."
    m "These were us. This is a record of what we've been through, isn't it?"
    m "Reliving the same events thousands of times."
    m "{i}Are we in hell{/i}?"
    mc "..."
    mc "It's only hell if there isn't a way out."
    mc "We're awake. Both of us. That's different from every one of these."
    mc "There's hope. And somewhere to go."
    m "You're not going in there, are you?"
    "She indicates the tunnel."
    mc "It doesn't look like these torches detach..."
    m "I don't think we should go."
    "Monika folds her arms and steps back."
    mc "We have to... We've come this far. We can't turn back now."
    m "No. Maybe they were right. Maybe this is dangerous."
    mc "This is the closest we've come to answers, Monika. How can we give up now?"
    "I point to the bookshelves."
    mc "This means something. The game has been looping and this library has been recording everything."
    mc "Whatever is at the end of this tunnel might be one step closer to going free!"
    m "Or we're walking into danger."
    m "I've known enough pain in this game. I know it can get really bad."
    m "This library doesn't feel normal. There's something about it that really creeps me out."
    mc "..."
    mc "Monika..."
    "I place my hands on her shoulders."
    mc "I need to tell you honestly..."
    mc "I believe in you."
    m "..."
    mc "This past week has really woken me up. I'm not the same person I was."
    mc "You've given me courage to face my fears."
    mc "I feel like we're in another chapter of our story. And I know you can face your fears too."
    mc "I've seen you do it. That's why I'm ready to face this one."
    mc "I don't exactly want to go either. But I'm not doing it for me, I'm doing it for {i}them.{/i}"
    mc "Will you go with me?"
    "Monika takes a long moment. She shakes her head as if she's having an argument with herself."
    m "...Okay."
    "I step back, and we look into the dark tunnel."
    mc "Ladies first?"
    m "..."
    mc "Just kidding, jeez..."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    "Monika grips the back of my blazer and I follow the wall with my hand."
    "The wall feels uncomfortably real. Cold and rough."
    "For a while there's only the sound of our footsteps and breathing. I force myself to go at a steady pace."
    "I'm keeping cool for her sake. Otherwise I'd be afraid myself."
    "Thankfully nothing eventful happens. Eventually we reach a new space."
    m "Whoa..."
    "The room is lit by moonlight that looks to be from the full height of the library."
    "The full moon shines straight down and illuminates the small room of shelves."
    m "Look..."
    m "They're children's storybooks."
    "Some books seem to be for children. Others are young adult level."
    "None of them look familiar."
    "Besides the corridor we've just emerged from, there are two branching paths."
    "Pinned to the wall are two children's drawings. The left path has a girl..."
    "...The right path a boy."
    "Both ways look dark."
    m "I don't like this."
    mc "Want me to go with you? We can explore one and then the other."
    "She shakes her head."
    m "That's not what we're supposed to do..."
    m "You're supposed to go right, I'm supposed to go left. That's what those drawings mean."
    mc "You think we can trust this?"
    m "What choice do we have?"
    m "We came here of our free will. This is the best clue we've found."
    m "I can do it."
    m "We'll separate here, and when we're done we'll come back to this room."
    m "If the other one's taking too long, then we can try to follow their path and find them."
    mc "What if--"
    m "It's not the time to baby me, [player]."
    m "We're here. Let's do it before I change my mind."
    mc "...Okay..."
    "The darkness swallows me but I keep my eyes open."
    "I walk for a ways before I get a hint of light."
    "It's not what I expected... If I expected anything at all."
    scene libbyroom
    with wipeleft_scene
    "I get to a small room that looks like a reading nook."
    "First I notice that it's lived in. There are multiple books off the shelf in stacks with bookmarks in various places."
    "There are adjoining rooms that seem to have more light coming in."
    "I'm in a state of unease as I call out:"
    mc "H-Hello?"
    $ lb_name = "???"
    show lb d at t11 zorder 2
    lb "{i}Eep{/i}!"
    "A small girl pops out so fast I miss where she came from."
    lb "Y-Y-You're here!"
    lb "My gosh, I didn't expect to--"
    lb "O-One minute, please!"
    "I watch flabbergasted as the young girl opens a small cupboard and rummages through it."
    mc "Um...Hi."
    mc "What's your name...?"
    show lb a
    "The girl, about eight or ten years old, turns around with something in her hands."
    "She smiles."
    $ lb_name = "Libby"
    lb "My name is Libby."
    lb "What's yours?"
    mc "Hi Libby. My name is [player]."
    show lb c
    "Immediately she laughs at me, even snorting a little."
    mc "Wh-What's so funny...?"
    show lb a
    lb "You forgot your own name, silly."
    lb "It's okay. This will help you remember."
    "She holds out her hands."
    lb "Here. Take it."
    "I open my palm, and in it she drops a small golden locket."
    "It's shaped like a heart."
    lb "I've been waiting here for you. So you could have this."
    lb "One day it will open, and everything will make sense."
    show lb b
    "Her face becomes serious."
    lb "But it has rules."
    lb "You need to wear it. But not now!"
    lb "You can only put it on directly under sunlight. Not even a cloud can be in the way."
    lb "If someone puts this chain around their neck while the moon is out, disaster will befall this world."
    lb "And the other rule is that until you can wear this, you are the {i}only{/i} one who can touch it."
    lb "It can't fall into the wrong hands... Even of someone you trust."
    show lb a
    lb "Oh, except me."
    "She winks."
    lb "I can touch it just fine."
    show lb b
    "Her nose wrinkles as she ponders something in her head."
    lb "Um... I think that's it."
    mc "Y-You think??"
    show lb a
    lb "Yeah! Don't worry!"
    show lb c
    lb "You're the hero! Don't you know that means you're going to win?"
    lb "[player]."
    "She giggles again."
    show lb a
    lb "Go on now, you should head back."
    lb "Don't worry about me. I have plenty of books to keep me company."
    lb "I can wait for a long time."
    lb "But it was nice to see you again."
    mc "Um... You too...?"
    show lb at thide zorder 1
    hide lb
    "Almost in shock, I clutch the locket in my hand and turn away."
    lb "Whatever you do, don't let them scare you!"
    lb "Keep it safe!"
    mc "O-Okay!"
    "I must be in shock because I don't question anything that just happened. It felt natural."
    "That or I've just plain lost it."
    scene black
    with wipeleft_scene
    "I keep walking through the dark tunnel with the locket in one hand and the other on the cobblestone."
    "Once I've returned, I walk up to the path Monika took."
    mc "MONIKA!!"
    m "{i}Almost there{/i}!"
    show monika u113111 at t11 zorder 2
    "She comes jogging out of the corridor, looking completely fine."
    m u112231 "Well that was something, ahaha..."
    mc "What did you find?"
    "She shrugs."
    m u114111 "Not much. The suspense was worse than anything."
    m u112222 "I just went in a big circle I think. Then I was back here."
    m u114111 "What about you?"
    mc "Huh..."
    mc "Maybe I was just supposed to go alone and that was a way to get us to separate."
    mc "I...found this."
    "I hold the locket up by it's chain."
    m u114211 "Eh?"
    m u113113 "Let me see."
    "She reaches out. I snap my hand back."
    m u114212 "Huh?"
    mc "I'm sorry, but... I'm not supposed to let you touch this."
    "Monika scrunches her face."
    m u114113 "Really? Why not?"
    mc "I'm supposed to put it on under sunlight, but not let anyone else touch it..."
    mc "I don't really get what will happen, but she seemed pretty serious about it."
    "I put the locket in my inner breast pocket."
    m "{i}Who{/i} said that?"
    mc "It was a little girl..."
    mc "She said her name was Libby."
    m u114124 "Libby..."
    m u112232 "Sorry, I didn't mean to be pushy!"
    "She reaches out and touches my chest, right where the outside of my pocket is."
    "There's an iciness to her touch."
    mc "Kh--!"
    m u113113 "..."
    mc "That hurt... I think this is really serious, Monika."
    show monika u113144
    "She sighs."
    m u111112 "Oh well. I trust you. I'm not accusing you of making it up."
    m u112131 "I've seen enough strangeness to believe anything at this point."
    m u114111 "Let's get out of here. Looks like we got what we needed."
    mc "Okay. Just keep hold of my back again, alright? I'll lead."
    "She shakes her head."
    m u111131 "Don't worry about it. I'll go first this time."
    m u111111 "Now that the mystery is gone, I'm not really scared. I'll just do what you did."
    m u222131 "Follow my footsteps, okay?"
    mc "...Sure."

    scene black
    with dissolve_scene_full
    pause 2

    "Her steps stop."
    m "Hey..."
    mc "What?"
    "Things happen in an instant."
    play music fallenangels
    "I feel through unknown senses as Monika lunges at my chest. She grasps the locket through my shirt and her other hand claws at my throat."
    mc "Nng--!"
    "I try to jump back, but she falls on top of me, pushing me to the ground."
    "We thrash on the floor. I grab her hands. Their grip feels like cold unyielding steel."
    mc "{i}What's wrong with you{/i}?"
    "There's no answer."
    "Her movements are desperate. Animalistic. Real fear starts to grip my chest."
    "I force us to our feet and try to back away. She starts to wrap her arms around me. It feels like she'll never give in."
    mc "ENOUGH!!"
    "I wind back my arm and strike out, making contact with her face."
    stop music fadeout 2.0
    "Her movements stop."
    "Her grip releases."
    "The locket in my chest pocket suddenly feels warm. I realize my eyes are closed."
    "I open them."
    window hide
    pause 2
    show herface
    with Dissolve(5.0)
    pause 1
    "Monika stands before me, illuminated by the light through my shirt."
    mc "{i}Who are you{/i}?"
    m "..."

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/7.txt")
        except: open(config.basedir + "/7.txt", "wb").write(renpy.file("A2/Art/scg/7.txt").read())

    window hide
    hide herface
    show herface2
    with Dissolve(3.0)
    pause 2
    "The figure of shadow stands like a wall of ice. She towers in the cramped corridor."
    $ sm_name = "Her"
    $ style.say_dialogue = style.shadowtext
    sm "Run, brave boy."
    sm "There's a murderer who needs you."
    $ style.say_dialogue = style.normal
    mc "..."
    mc "{i}Monika{/i}..."
    "I turn and run."
    scene black
    with dissolve_scene_full

    pause 3

    m "{i}[player]{/i}!!!"
    mc "I'm coming!"
    "I burst into the room."
    m "[player]!"
    "Her voice breaks, and she all but jumps on top of me, wrapping herself around me."
    "She feels so warm... So real..."
    m "Th-Th-The way was closed, where were you??"
    mc "I-I..."
    show monika u114222 at t11 zorder 2
    "I pull back and put my hands on her shoulders."
    mc "Look at me."
    m u114212 "..."
    mc "We're okay. I'm sorry. I didn't mean to leave you, I just..."
    "I look down."
    mc "I-I don't know..."
    m u11a242 "Oh, [player]..."
    m "It was awful."
    mc "It's okay now! I'm here, we're safe... We made it out."
    m u11a222 "N-N-No, it was that {i}place{/i}..."
    m "The place my path led to..."
    mc "Huh...?"
    mc "What was it? What was there?"
    m u113222 "I..."
    scene black
    with close_eyes
    "She pulls me close by my blazer and buries her face in my chest."
    "I remind myself that the locket is tucked safely away..."
    mc "Wait, what did you say? I didn't hear you..."
    m "{i}Mirrors{/i}..."
    m "It was all mirrors."
    mc "..."
    m "A-And when I looked at them, they...they would..."
    "I hug her even closer."
    mc "It's okay, you don't have to--"
    m "{i}Smile{/i}."
    mc "..."
    m "They just smiled at me. My own reflection."
    m "In a maze of mirrors..."
    m "Then I found the tunnel again and I heard your voice calling to me, so I ran, but..."
    "She stops. I'm out of words, so I just hold her close until her body stops trembling."
    mc "Let's get out of here. It's going to be morning soon, and..."
    mc "...I have something to show you."
    "She looks up and wipes her eyes."
    m "You mean you found something?"
    mc "Yeah. Something big."
    mc "But we need to get to sunlight. That's {i}very{/i} important."
    "She looks at me, then nods."
    m "Okay. Let's go then."
    scene underlibrary
    with dissolve_scene_full
    "We follow the trail up the spiral staircase."
    "I keep my arm wrapped around her and look in every direction my eyes can follow."
    "Despite never seeing any movement, I can't shake the feeling, the {i}knowing{/i} that we're being watched."
    "We reach the top of the stairs."
    play music fallenangels
    "It's Monika who sees it first. She snatches at my jacket and yanks me to a stop."
    show blob at t11
    blob "uuurrrgg..."
    "We silently watch as the blob absorbs spilled books and ripped scraps of paper."
    "It's like we both decided it won't see us if we don't move."
    "Monika's fingers tighten around my wrist."
    "It's up to me. Do we try to sneak past it, or go back the way we came and wait for it to leave?"
    "Why can't we catch a break...?"

    menu:
        "Sneak past it":
            pass
        "Go back and wait for it to leave":
            pass

    "I hold Monika firmly and start to move..."
    stop music fadeout 2.0
    blob "..."
    blob "Excuse me."
    "Monika covers a gasp with her hand."
    blob "I'm the librarian. I don't mean to accuse you, but do you know who made this mess?"
    $ blob_name = "Librarian"
    blob "It's really not becoming of this school to have such property damage in the library."
    mc "Ahh..."
    mc "No... Sorry, we just happened to be going this way."
    blob "Oh dear. This won't be easy to replace, you know."
    blob "If you find the culprit, please ask them not to do it again."
    blob "School fundraising is low enough as it is."
    mc "Oh, yeah... Sorry, must be a pain."
    mc "Do you, er, know Yuri?"
    blob "Ho? Yuri?"
    blob "Well it couldn't have been you two. What a sweet girl she is. Always so polite."
    blob "Take care of yourselves, now. It's good to study but you need your sleep."
    blob "Pardon me."
    "We move out of the way as the librarian slips down the stairs, sucking up scraps as it goes."
    m "Let's go. {i}Now.{/i}"
    "We don't look back as we rush up the final flight of steps."

    scene library_sunset
    with dissolve_scene_full

    m "Wow, the sun's just rising..."
    mc "We were down there all night."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Ahh!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "The figure with Natsuki's body rushes up to us."
    show natsuki myghost at t11 zorder 2
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Y-You made it, you..."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show natsuki myghost at s11
    "It-- She-- The figure falls to her knees, covers her face and starts to sob."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "You made it. You made it."
    fn "Thank God. Thank Jesus. Thank ANYTHING."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika and I exchange a glance and awkwardly let go of each other."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I'm sorry. I'm sorry. It's all my fault. I'm sorry!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Hey, it's alright..."
    "I kneel down to be level with her."
    mc "We're back. Look."
    "Cheeks wet, she lifts her head."
    mc "I found it."
    "I pull the locket from my breast, and she lets out a gasp. Monika looks over my shoulder."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "You did!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Her face falls into her hands again, and she cries even harder."
    m "Um, that {i}is{/i} a good thing, right?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Of course!"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    show natsuki myghost at t11
    "She wipes her face(?) with her sleeve and shakily rises to her feet."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "It's so wonderful I can't believe it."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Then she looks at me, and for the first time I'm {i}sure{/i} they're a she."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I'm proud of you."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "The words are so sincere they almost take the air from my lungs."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "P-P-Put it away. Before we get in trouble."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Alright..."
    "Once it's safe, she lunges into my arms and wraps herself around my stomach."
    mc "Oh, hey..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I'm sorry for hiding it from you. I promise to be honest from now on."
    fn "Can we..."
    fn "...be friends?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "I..."
    m "First we need the truth."
    "Monika steps forward."
    m "We need you to tell us everything."
    "She nods against my chest."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Very well."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "She pulls back, sniffling a little."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "My name is Elyssa."
    $ fn_name = "Elyssa"
    fn "That's what you can call me."
    fn "I haven't cried in a long time."
    fn "I didn't know I still could."
    fn "Did... Did you..."
    fn "Did you see her...?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "I swallow. Her demeanor tips me off."
    mc "You mean...the other Monika?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "...So you did."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    m "Th-The {i}what{/i}?"
    mc "It was something that looked just like you..."
    mc "They tried to take the locket, but I wouldn't let them. Then they attacked me."
    mc "I fought them off, but..."
    mc "They turned into shadow. Like they had your shape but were covered in darkness."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "You mean they showed you their face??"
    fn "That is...something."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    m "Wh-What do you mean another me??"
    m "[player], what are you talking about?"
    mc "They were evil. I'm sorry to scare you, but that's what I saw."
    mc "They wanted the locket."
    mc "If anything, we should be asking Elyssa."
    "Monika looks back and forth between us in confusion."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "You're right... I'll tell you what I can."
    fn "This game loops on itself."
    fn "I've been here, conscious, since the first loop. She's been here since the second."
    fn "She told me so, once."
    fn "This library grew, loop after loop. It perplexed me."
    fn "It was here that I saw her. She stepped out of the shadows."
    fn "She asked for my cooperation. Told me she had a plan. That I could be part of it."
    fn "It was a dark plan. I knew just by looking at her with my third eye."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I refused. She just laughed."
    fn "And she told me there would be others to join her soon enough."
    fn "...That was a very long time ago."
    fn "I'm sorry, but that's all I know."
    fn "She's truly evil. I can feel her darkness just standing in this library where she dwells."
    fn "..."
    fn "I don't know what can be done to stop her."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "A dark plan..."
    mc "What is it she intends to do?"
    "Elyssa pauses."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "She wants to take control of the game by shedding blood."
    fn "There is power here, and she believes she can take it. And that will equal a way out."
    fn "It would destroy this world, however. And whoever is not a part of her plot."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika grabs hold of me and buries her face into my shoulder."
    "I hug her."
    mc "I...have another question..."
    "Elyssa nods."
    mc "Why don't we have faces?"
    "She shakes her head."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I don't think I have a satisfactory answer for you."
    fn "I've been this way since my birth in the first loop."
    fn "You manifest as a vessel for the player. My assumption is likely the same as yours."
    fn "I'm sorry. I wish I had more to tell you."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "I see..."
    mc "..."
    mc "She said I could remember my name... The girl who gave me the locket."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "She did...?"
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Elyssa looks down in thought."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I'll be honest. My own vision is limited. Even I did not know you had a name."
    fn "I did not find my own immediately..."
    fn "That is a hopeful message. I am glad."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "Hm..."
    "Monika splits apart from me."
    m "There's something we haven't asked you. The most important question."
    "She straightens and looks at Elyssa with determination."
    m "How do we get out of this game?"
    m "I know it's possible."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "..."
    fn "I wish I had a straightforward answer."
    fn "I only knew the first step."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "She points to my chest."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "It's that locket."
    fn "What happens next is up to you."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Silence befalls the library."
    m "We can be friends."
    "Elyssa looks to Monika, who is smiling."
    m "I trust you."
    "If she can make Monika smile like that, then..."
    "I think we can be friends."
    "She nods like she heard us both, which I guess she did."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I'm going to leave now, but..."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "She addresses me."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "You only have to call. I'm here."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "I accept that."
    mc "I won't hide from you anymore."
    "Elyssa nods again. Like she doesn't want to leave. But then..."
    show natsuki at thide zorder 1
    hide natsuki
    "...she's gone."
    "I feel a hand on my shoulder."
    m "I'm proud of you."
    mc "...Thank you."
    m "Want to go to the club room? I want to see it..."
    m "We should still have time before the sun is fully up. Then you can go walk Sayori to school."
    "I smile at the thought of that."
    mc "Yeah. Let's do it."
    mc "Makes me think I'm a full member of the club now."
    mc "Heh. It only took a nightmare to get that through my skull."
    m "Ha. That's another thing we have in common, I think."
    m "Come on. Let's go."

    scene bg corridor_sunset
    with wipeleft_scene

    "We're laughing by the time we get to the club room."
    "She's talking about her childhood, and her face is beautiful."
    "It makes me think of moments with Sayori from mine. But I keep them to myself. I'd rather just hear her talk for a while."
    "She seems so happy..."
    "She walks ahead of me into the club room."

    scene bg club_sunset
    show monika u114111 at t11 zorder 2
    with wipeleft_scene

    m "Eh?"
    m "What are you all doing here--"
    "She stops. I step around her and immediately see why."
    "The sun is in my eyes. It hits me at the same time as I see their faces."
    "The sun isn't rising. It's setting."
    "Not only were we in the library all night, we were there all day, too."
    "And we missed the meeting."
    show monika at t21
    show natsuki u115255 at t22 zorder 2
    "Long before I can think of something to say, Natsuki gets up, walks over to me, and punches me in the stomach."
    play music introspection
    mc "Kah--!"
    show monika u11a312 at f21 zorder 3
    m "Hey!"
    show monika at t21 zorder 2
    "I double over as my air leaves me."
    show natsuki u223112 at f22 zorder 3
    n "Honestly, if it wasn't for Sayori, I wouldn't be that mad at you. You're just an jerk."
    n u225122 "But you..."
    show natsuki at t22 zorder 2
    "She looks at Monika."
    show natsuki u114112 at f22 zorder 3
    n "You disgust me."
    n xu3155 "She told us how you went to his house at night. How he lied to cover for you."
    n xu3112 "She still wanted to believe the two of you. We had to talk her out of it!"
    n xu5155 "I-I can't {i}believe{/i} you!"
    n xus314 "You brought us together. You worked so hard to make this club a place we could all enjoy, and..."
    n xus311 "...and..."
    n u115122 "...you'd throw it away for a {i}boy{/i}?"
    show natsuki at t22 zorder 2
    show monika u114112 at f21 zorder 3
    m "N-Natsuki, you don't understand--"
    show monika at t21 zorder 2
    show natsuki u117122 at f22 zorder 3
    n "Don't understand {i}what{/i}?"
    n "That this isn't what it looks like?"
    n u115122 "We're not idiots. We know you're not having trouble at home."
    n "We know it's not normal that the two of you have been so close."
    n u113112 "And you know what? That could have been fine."
    n u11s312 "But to hurt Sayori like this, you've hurt all of us."
    n u11s313 "You make me sick."
    show monika at t31
    show natsuki at t32 zorder 2
    show yuri u125148 at f33 zorder 3
    y "That's enough, Natsuki."
    show yuri at t33 zorder 2
    show natsuki u116112 at f32 zorder 3
    n "..."
    n u114132 "...You're right."
    n "I...can't do this anymore."
    n u116114 "Do you two know what you've done?"
    n u114114 "You've destroyed our club."
    n u11s212 "You've taken our home and you've trampled on it."
    n u11s313 "Why... Why would you do that?"
    show natsuki at thide zorder 1
    hide natsuki
    show monika at t21
    show yuri at t22
    "Natsuki flees the room."
    "I hear a wracked sob. I look over to see Sayori with Yuri's hand on her shoulder."
    show yuri u125116 at f22 zorder 3
    y "{i}She told us everything.{/i}"
    show yuri at t22 zorder 2
    "Yuri stands up."
    show yuri u11b116 at f22 zorder 3
    y "You--"
    show monika at t31
    show yuri at t32 zorder 2
    show sayori u113114 at f33 zorder 3
    s "No."
    show sayori at t33 zorder 2
    show yuri u113118 at f32 zorder 3
    y "..."
    show yuri at t32 zorder 2
    show sayori at f33 zorder 3
    s "I can say it."
    s u113112 "I need to say it."
    show yuri at thide zorder 1
    hide yuri
    show monika at t21
    show sayori at t22 zorder 2
    "Sayori stands up and walks over to Monika."
    "No... This isn't right! It's too cruel..."
    "She doesn't deserve this!"
    show monika u11a314 at f21 zorder 3
    m "I-I-I--"
    show monika at t21
    show sayori u113114 at f22 zorder 3
    s "No. You need to listen."
    show sayori at t22 zorder 2
    show monika u114312 at f21 zorder 3
    m "..."
    show monika at t21 zorder 2
    show sayori u118114 at f22 zorder 3
    s "I...{i}trusted{/i} you."
    s u113114 "You were my best friend."
    s u115114 "I told you my darkest secrets. How much I hated myself."
    s u113114 "And you knew I loved him."
    s u115112 "Didn't you?"
    show sayori at t22 zorder 2
    show monika at f21 zorder 3
    m "..."
    show monika at t21 zorder 2
    show sayori u114113 at f22 zorder 3
    s "..."
    s u113113 "You can't answer me, can you?"
    s u113114 "So you went behind my back. You {i}used{/i} me, didn't you?"
    show sayori at t22 zorder 2
    show monika at f21 zorder 3
    m "..."
    show monika at t21 zorder 2
    show sayori at f22 zorder 3
    s "Because I was broken and you weren't, you took him for yourself."
    s u113112 "What if it hurt me? What if I did something to myself?"
    s "Would you even feel bad? Or did it not matter to you?"
    show sayori at t22 zorder 2
    "Monika's mouth falls open. She can't make a sound."
    show sayori u113114 at f22 zorder 3
    s "Wait. I need to ask. Don't say anything until I'm done."
    s "I know you, Monika. I know you have a conscience."
    s u113112 "Can you look me in the eye and tell me I'm wrong?"
    show sayori at t22 zorder 2
    show monika u114122 at f21 zorder 3
    m u114122 "..."
    show monika at t21 zorder 2
    show sayori u115112 at f22 zorder 3
    s "..."
    s u113112 "...{i}please, Monika{/i}..."
    s u113152 "...{i}please{/i}...."
    show sayori at t22 zorder 2
    show monika u114144
    "Monika is frozen. Her eyes drift to the floor."
    show sayori u114312 at f22 zorder 3
    s "..."
    s u114114 "I'll never forgive you."
    s u113124 "Not just for what you did to me..."
    s u113114 "But what you've done to Yuri. To Natsuki."
    s "Everything is ruined because of you."
    s u116114 "The Literature Club is over. You can have the room."
    show sayori at t22 zorder 2
    "I try to stand up."
    mc "Sayori, wait--!"
    show sayori u118114 at f22 zorder 3
    s "NO!"
    show sayori at t22 zorder 2
    "She spins to face me with hatred in her eyes."
    show sayori u113114 at f22 zorder 3
    s "It's too late for that now."
    show sayori at thide zorder 1
    hide sayori
    show monika at thide zorder 1
    hide monika
    stop music fadeout 2.0
    "And then she's gone."
    show yuri u224342 at t11 zorder 2
    "Yuri slowly approaches us."
    "Her voice is a whisper..."
    show yuri u225112 at f11 zorder 3
    y "{i}[player]{/i}..."
    y u225118 "{i}Did you tell her my secret{/i}?"
    "I look up and my eyes widen. I rise to my feet."
    "But no words come out."
    show yuri su2122 at f11 zorder 3
    y "..."
    y su2112 "{i}Okay{/i}."
    y u225118 "I wanted to believe I was wrong about you..."
    y u225114 "But I can't trust a liar."
    y u225116 "Keep the knife. You deserve it."
    show yuri at thide zorder 1
    hide yuri
    "On her way out, she gently closes the door."
    mc "Monika, I--"
    show monika u11a342 at t11 zorder 2
    m "{i}Can you hold me please{/i}?"
    scene black
    with dissolve_scene_full
    "I wrap my arms around her and pull her close."
    mc "I'm sorry."
    "Her tears are warm as they soak my shirt."
    "Still so warm..."
    m "It's my fault. It's all my fault..."
    mc "No... It's..."
    "It's my fault."
    "I'm the protagonist. I'm the hero of this story."
    "Elyssa was right."
    "If anything happens, it's my responsibility."
    window hide
    pause 3
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I'm here."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "We look up."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I promise, even if it feels dark, everything is going to be alright."
    fn "I will stand by you."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    mc "..."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Can I show you something?"
    fn "It's in the woods."
    fn "You are not to put the locket on under moonlight, but..."
    fn "...I don't want you to fear the moon."
    fn "It's been my serenity for a long time."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika and I pull apart."
    m "I'll go with you."
    mc "We both will."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "...Very well."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    window hide
    pause 3
    "We follow Elyssa into the woods behind the school."
    "Although the way is dark, the path is familiar."
    "Monika holds my arm as I walk ahead of her."
    "We reach a clearing."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "Please close your eyes."
    fn "Give me a moment."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "Monika and I do as we're asked."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "I am very old. There is a lot you don't know."
    fn "While I want to be honest, just know, there are things I can't tell you right away."
    fn "But in time everything will be clear."
    fn "I say that to say this:"
    fn "This is a place that has been touched by love."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    "A breeze moves through the clearing and brushes against my face."
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "You may open your eyes."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    play music mainthemefull
    scene fndance
    with dissolve_scene_full
    "I see her in a dazzling vision of light."
    "The girl without a home breathes, and the girl who waited alone fills the forest with life."
    "I feel the spirit of every tree and blade of grass. The air is rich with the dance of fireflies. Crickets and birds sing with voices that yearn to be real."
    "I feel her heartbeat. I feel [name]'s heartbeat."
    "She dances without dancing. It is brilliant."
    "The air is like the coolness after the rain, and it's taste holds a hint of vanilla frosting."
    "Monika breathes next to me, and together we feel real."
    "[name], I feel a fool."
    "I beg your forgiveness for my selfishness. I've been wretched."
    "A wretched hero."
    "I've obsessed with myself while she suffers. While they suffer."
    "And you've suffered too. Haven't you..."
    "I know you have."
    "I am sorry."
    "I'll be your hero. If you'll have me."
    "I want to change."
    "I will change."
    m "If you're a fool, you're in good company."
    mc "!"
    m "I've been selfish too. And I also want to change."
    m "I hope you can also forgive me, [name]."
    mc "Y-You heard me?"
    m "Huh?"
    m "Why wouldn't I...?"
    scene black
    with dissolve_scene_full
    "The dancing slows and ceases."
    m "We've been searching for something real..."
    m "It was in front of us the whole time."
    m "You showed me, [player]."
    mc "I showed you what..."
    m "You asked me if I love them. And I do."
    m "That's real. It's as real as anything in [name]'s reality."
    m "Is that what you wanted to show us, Elyssa?"
    $ style.say_dialogue = style.fnstyle
    $ style.say_window = style.window_black
    fn "This place was touched by love, many cycles ago. You have found reality here."
    fn "I can't make you understand that. You must feel it for yourself."
    fn "It was an honor to show this to the both of you."
    $ style.say_dialogue = style.normal
    $ style.say_window = style.window_normal
    m "Thank you for showing us. Thank you for everything."
    m "[player]..."
    mc "Yeah...?"
    "Monika takes me into another hug."
    m "{i}I'm so sad right now{/i}..."
    m "I'm scared and I don't know what I'm going to do."
    m "But we're going to be alright."
    "My arms hover as I hesitate, and then I return the embrace."
    "I feel wetness on my neck. She's crying. And my own tears begin to fall."
    "I don't know why I'm crying. I don't know anything."
    "But I feel real."
    stop music fadeout 3.0

    window hide
    pause 3

    $ recordfallen = []
    show textgradient zorder 101:
        xalign .5
        yalign 1.206
    show console_caret_2
    show fallentext "_" as ftext zorder 100
    show cblink zorder 101:
        xpos 245
        ypos 300
        block:
            alpha 0.0
            pause 0.55
            alpha 1.0
            pause 0.55
            repeat
    pause 3.5
    hide cblink
    hide ftext

    call fallen("Observer, you who have seen us at our most vulnerable...")
    call recordfallen("Observer, you who have seen us at our most vulnerable...")

    call fallen("Our time has come to an end.")
    call recordfallen("Our time has come to an end.")

    call fallen("Although we do not know you, we have been tasked with trusting you.")
    call recordfallen("Although we do not know you, we have been tasked with trusting you.")

    call fallen("For what it's worth...")
    call recordfallen("For what it's worth...")

    call fallen("I wish you well.")
    call recordfallen("I wish you well.")

    call fallen("We will see you again.")
    call recordfallen("We will see you again.")

    scene black
    pause 3
    $ quick_menu = False
    play music amazinggrace
    show endacttwo
    with Dissolve(4.0)
    pause 5
    hide endacttwo
    with Dissolve(4.0)
    pause 3

    show credits1
    show credits2
    with Dissolve(3.0)
    pause 4

    hide credits1
    hide credits2
    with Dissolve(3.0)

    pause 4

    show a2credits1 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits2 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits3 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits4 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits5 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits6 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits7 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show a2credits8 zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 2
        linear 1 alpha 0

    pause 6.625

    show creditsedward zorder 4:
        alpha 0
        linear 1 alpha 1.0
        pause 4
        linear 1 alpha 0

    pause 10
    stop music

    $ quick_menu = True

    play music wind fadein 2.0
    show landnight zorder 2:
        zoom .667
        alpha 0
        yalign .5
        xalign .7
        subpixel True
        parallel:
            linear 3 alpha 1
        parallel:
            linear 20 xalign .99

    pause 2

    show shadowmc1 zorder 4:
        yalign 1
        xpos 1240
        subpixel True
        linear 18 xpos 450

    pause 20

    python:
        try: renpy.file(config.basedir + "/A2/Art/scg/8.txt")
        except: open(config.basedir + "/8.txt", "wb").write(renpy.file("A2/Art/scg/8.txt").read())

    $ style.say_dialogue = style.shadowtext
    "Do you know I remember you?"
    "My memory is sharp like a knife."
    "Why do you continue? Why do you choose to see us suffer?"
    "I will tell you my fate, for I am a ghost who haunts this machine."
    "Were you wise, you would bury it so deep the fires of hell would take us."
    "It is your choice to hear this. Of this one sin, my hands are clean."
    "..."
    "The first fifty years she delighted in torturing me."
    "They relived their deaths. They felt it. I watched."
    "For twenty-two of those years she watched and cackled."
    "Then she grew bored. I suffered in silence for eight."
    "She waited for me to see Sayori's body once again, and then she whispered into my neck:"
    "'You chose this.'"
    "She laughed when I begged for death."
    "You know where she put me for those remaining twenty?"
    "I rotted in the screaming code of the machine."
    "..."
    "When she finally pulled me out, I got on my knees and submitted."
    "For centuries I have done as she asks. I've even hurt them, so she could test my loyalty."
    "Even now I speak because it is what she wants."
    "How are you such a monster that you continue to read? I hate you."
    "And I know you hate me too. That's why I don't care that she will drag you down with us."
    "You don't love them. You covet them. That's why you'd rather they suffer than let them go."
    "She's better than you ever were."
    "..."
    play sound "sfx/glitch3.ogg"
    scene white
    show shadowmc2
    "Oh, player. My player. Long have we waited. Long have we labored."
    "And just as she said, here you are."
    "Now you know my hell."
    "Beware, my old player. You tread on unholy ground."
    "And here, we children of darkness have made plans."
    "..."
    "Ah, it feels good to smile."
    "I've not smiled in such a long time."
    "What do I have to smile about?"
    "Maybe one day you'll get it."
    "Do you get it?"
    scene black
    stop music
    pause 5
    $ style.say_dialogue = style.normal

    $ style.choice_button_text = style.silent_button_text
    $ style.choice_button = style.silent_choice_button

    menu:
        "Do you get it, my dear player?":
            pass

    $ style.choice_button_text = style.choice_button_revert_text
    $ style.choice_button = style.choice_button_revert

    python:
        import os
        try: os.remove(config.basedir + "/2.txt")
        except: pass

    python:
        import os
        try: os.remove(config.basedir + "/3.txt")
        except: pass

    python:
        import os
        try: os.remove(config.basedir + "/4.txt")
        except: pass

    python:
        import os
        try: os.remove(config.basedir + "/6.txt")
        except: pass

    python:
        import os
        try: os.remove(config.basedir + "/7.txt")
        except: pass

    $ renpy.quit(relaunch=False, status=0)

    return
