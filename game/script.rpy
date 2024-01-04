# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define you=Character("[you]", color="#ffffff")
define bai= Character("Axelander", color="#69df63")
define shadow_bai = Character("???")
define hong = Character("Axel",color= "#800000")
define shadow_hong = Character("???")
define lucas = Character("Kaz", color="#255782")
define shadow_lucas = Character("???")
define anne = Character("Anne")
define amy = Character("Amy")
define annika = Character("Annika")
define unknown = Character("Unknown")
define ta = Character("Teacher A")
define p1 = Character("Random Girl A")
define p2 = Character("Random Girl B")
#define ra = Character("Person A")
define cashier = Character("Cashier")
define ca = Character("Counsellor")
define hong_mom = Character("[hong]'s Mother")
define young_hong = Character("Young [hong]")
define hong_dad = Character("[hong]'s Father")
define ga=Character("Gangster A")


# Defined persistent
$persistent.chose_lucas = False
$persistent.chose_hong = False
$persistent.chose_bai = False
$persistent.hong_end = False
$persistent.bai_end = False
$persistent.lucas_end = False

#favourability
$ bai_fav=0
$ lucas_fav=0
default you="Player"


# The game starts here.
#PROLOGUE ---------------------------------
label start:
    scene black screen
    show text "{color=#ffffff}Disclaimer: \nEverything in this game is purely fictional and has \nno relation to any real person or place.{/color}" with Dissolve(3.0)
    hide text with Dissolve(3.0)
    show text "{color=#cc0066}Prologue{/color}" with Dissolve(3.0)
    hide text with Dissolve(3.0)
    #gives player a name
    $ you = renpy.input("What is your name?") 
    $ you = you.strip()
    if you == "":
        $ you = "Player"
    play music "audio/happy bgm.mp3"
    scene moscrop entrance
    you "{i}Ahh it’s my final year of highschool. Why did Dad have to move us for work again? Now I have to make friends all over again.{i}"
    you "{i} But hey! At least I have [bai]. Hopefully he’ll help introduce me to some of his friends...{i}"
    scene moscrop office
    "I] walks into TMO High and call [bai]."
    play sound "audio/phone ringing.mp3" volume 0.5
    ""
    stop sound
    show shadow_bai
    bai "Hey [you]. You just got to school?"
    you "I’m at the office right now. They’re telling me to go to the counselor's office to have someone show me around the school."
    bai "Okay, stay right there. I’ll come to you and bring you to the counselor's office."
    hide shadow_bai
    "[bai] is my childhood friend from elementary school. When I moved away in 7th grade due to my Dad’s job, we kept in contact over social media for a while."
    "Sadly, our messages decreased over the years to nothing more than holiday and birthday greetings." 
    "When I found out that I’d be moving to Moscrop this year, I immediately contacted [bai]. After all, I didn’t want to end my last year of highschool with no friends."
    hide shadow_bai
    show bai
    bai "Ah... it’s been so long since I’ve seen you, maybe 5 years? Wow you’ve changed a lot player. Class is starting soon, follow me, follow me."
    you "{i}He's being so awkward and avoiding eye contact. I guess it’ll become that way after so long.{i}"

    scene counsellors office
    show bai
    bai "Here’s the counselor's office, you can talk to Counsellor A and she’ll have someone show you around the school."
    hide bai
    show ca
    ca "Welcome to TMO High [you]. I’m Counsellor A, the head counselor. Your counselor in the future might not be me if your last name doesn't start between the letters H-L." 
    ca "Here's your class timetable and the school schedule. We know it’s difficult that you’re transferring to a new school in grade 12, but everyone here is lovely and I promise you’ll have a great final year."
    scene hallway
    show hong at left
    show bai at right
    "I walk out of the office and I see [bai] talking to a slender guy with a black bomber jacket." 
    "In contrast to his outfit, he wore a pair of thin metal glasses that accentuated his profound, phoenix eyes. However, his thinly pressed lips gave the air around him a sharp chill."
    scene counsellors office
    show ca
    ca "[hong] come here."
    show ca at left
    show hong at right
    ca "This is [hong]. He’s the student council president and he’ll be tasked with showing you around the school."
    hide ca
    show hong at center
    hong "I’m [hong]. [bai] told me that you guys are childhood friends. It’s nice to meet you. I’ll show you around the school. Give me your timetable, I’ll tell you where each of your classes are."
    
    scene weight training room
    show hong
    hong "You probably won’t come here often outside of class, but here's the weight training room."
    "Right as we’re about to leave, someone places an arm around [hong]’s shoulder."
    show lucas at right
    show hong at left
    lucas "[hong]. Who’s that next to you?"
    "I turn around to see a well built guy with curly, unkempt hair." 
    show hong flustered
    "The t-shirt clinging onto his dewy skin made it easy to tell that he just finished working out. The necklace around his neck and the numerous rings on his fingers gave him a rebellious air of disobedience."
    hong "[lucas]! I’m showing the new student around the school. You finished working out?"
    lucas "Yeah, I’m sweaty right now. I’ll go get changed and find you later."
    hong "Mm, ok. I’ll see you later. Let’s go [you]."
    show hong
    "He taps [lucas]’s shoulder lightly and left, leaving me to chase after him."
    scene counsellors office
    show hong
    hong "That’s everything in this school. Class is going to start soon, I’ll bring you to your block 1 class."
    

menu choose_route:
    hong "What class do you have?"
    "AP Statistics":
        stop music
        jump stats
    "Weight Training":
        $persistent.chose_bai = True
        stop music
        jump Alex_B_CH1

label stats:
    scene black screen
    show text "{color=#cc0066}AP Statistics{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}AP Statistics{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3"
    scene counsellors office
    show hong
    "Reading my timetable, I see the words \"AP STATISTICS\"."
    you "I have AP Statistics."
    hong "You have AP Statistics with me? Let’s go, I’ll introduce you to the teacher."
    scene stats
    show hong
    hong "I was gonna introduce you to Teacher A but it seems he's not here yet."
    hong "Where are you gonna sit?"

menu choose_route2:
    "Who do you want to sit beside?"
    "Chair on the right.":
        you "I want to sit on the chair to the right over there."
        hong "Oh! You're sitting next to me."
        $persistent.chose_hong = True
        stop music
        jump Alex_H_CH1
        """
    "Chair on the left.":
        you "I want to sit on the chair to the left over there."
        hong "Do you remember [lucas]? You'll be sitting next to him."
        $persistent.chose_lucas = True
        jump Lucas_CH1
        return #figure smth to return it to the main menu
    """
