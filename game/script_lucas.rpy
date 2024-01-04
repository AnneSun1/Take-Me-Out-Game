# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
#LUCAS ROUTE START----------------------------------------------
default lucas_fav=0
default lucas_good_end = False

label Lucas_CH1:
    show text "You have chosen [lucas]'s story" with Pause(1.5)
    scene stats
    "At this moment, a middle aged man wearing basketball shorts over leggings walks into the class."
    "[hong] walks over to the middle aged man smiling."
    "[hong]" "Teacher A! We have a new student in our AP Stats class. Do you wanna introduce yourself to him?"
    show hong
    "[you]" "{i}Outside of meeting [lucas], this is the first time I've seen him smile so brightly.{i}"
    "[you]" "Hi Teacher A, my name is [you] and I just transferred into Moscrop today."
    "Teacher A" "Well it's nice to meet you [you]. New student coming right into AP Statistics eh? Must be very smart."
    "Right as he said that, [lucas] walks in late, hair still disheveled from him gym session earlier."
    show lucas
    "[you]" "Wait but [lucas] was in the weight training room earlier. Is he late from working out?"
    lucas "[you]??? I'm surprised to see YOU here."
    "(Teacher A slaps [lucas]' back.)"
    "Teacher A" "Mr. [lucas]! Hey [you] why don’t you sit next to [lucas], maybe he’ll actually behave if he sits next to you. Plus you guys can, y’know, get to know each other better. Right Souza? What do you think, [you]?" 

menu lucas_ch1_choice:
    "{i}[lucas] seems to be a cool guy.{i}":
        $ lucas_fav+=1
        "[you]" "Yeah sure! He seems like a cool guy!"
        "{i} I've been trying to work out too, maybe I could ask him about that. {i}"
        lucas "Do you know what we’re doing in Stats?"
        you "Not really... Today’s my first day."
        lucas "I took this class last year, just ask me if there's something you don't understand."
        you "You took the class last year?? Did you fail or something?"
        lucas "No! it’s because my grade last year wasn't that good."
        you "Then are you sure you know what’s happening in this class..."
        lucas "Of course I do."
        you "Alright..."
        ta "Ok guys, let’s finish up the 2.2 Normal Distribution powerpoint that we didn’t finish last class. Who started on the 2.2 homework?"
        "(Only a few people raised their hands, and [lucas] was not one of them. I look at him skeptically, questioning his previous claim of supposedly “knowing what’s happening in stats”."
        ta "Do you guys want randomized seats today? Actually, let’s not. We should let [lucas] and [you] get to know each other better, yknow?"
        "I look at [lucas] and he sighs as [ta] laughs."
        jump Lucas_CH1_p2

    "{i}He seems fine...{i}":
        "{i} I don't really know him well, he seemed scary earlier, and he seems kinda gross... [hong] seems less intimidating to sit next to... {i}"
        "[you]" "Uhhh alright I guess, he seems fine."
        "(The teacher pats my shoulder comfortingly.)"
        ta "[lucas] is a good guy, I’m sure you guys will get along well!” He nudged [lucas] while raising his eyebrows."
        "([ta] walks away and I pick up my phone. With nothing to do, I text [bai].)"
        lucas "Who’re you texting?"
        you "[bai]. Do you know him?"
        lucas "You know that lil dumpling [bai]?"
        "{i}Dumpling? That's a new nickname.{i}"
        you "Yeah, we’re childhood friends."
        jump Lucas_CH1_p2

label Lucas_CH1_p2:
    scene powerpoint_s1
    ta "Everyone, listen up."
    ta "We ended at calculating z-scores in the last class. Copy the z-score formula down in your notes. We standardize our distributions and our observation x to find the Z-Score."
    ta "It helps us find how many standard deviations our observation is from the mean. Take out your graphing calculators everyone."
    you "I don’t have a calculator. Let me use yours."
    lucas "Sure."
    ta "Press 2nd VARS and select Normalcdf. You can enter your lower bound, upper bound, mean and median to calculate the area under the curve from the lower bound to the upper bound. Do the questions here."
    lucas "Do you need any help?"
    you "No it’s easy."
    lucas "Oh damn you did it already."
    "(I look at [lucas] suspiciously.)"
    you "Do YOU know how to do it?"
    lucas "Yeah of course, I'm just impressed that you picked it up so quickly."
    you "I'm pretty smart you know?"
    lucas "Alright smarty pants."
    you "Ok, then let’s do the questions."   
    "(As we’re doing the questions, Teacher A walks over smirking.)"
    ta "[lucas], are you and [you] getting along?"
    you "Yeah, we’re doing fine."
    ta "Tell me if he ever does something dumb."
    you "Okay, I'll watch over him for you."
    jump Lucas_CH2

label Lucas_CH2:
    scene black screen 
    show text "{color=#cc0066}Chapter 2: ----{/color}" with Dissolve(1.5)
    hide text "{color=#cc0066}Chapter 2: ----{/color}" with Dissolve(1.5)
    hide black screen
    scene hallway
    "{i}Class is finally over! [bai] told me he’s got weight training class during period 1. Maybe I’ll catch a glimpse of him working out if I get there fast enough.{i}"
    "(I rush out the math wing and down three flights of stairs. Recalling the path to the weight training room I rush past the crowds of people.)"
    hide hallway with Dissolve(0.25)
    scene weight training room with Dissolve (0.25)
    "(Entering the weight training room, I look around searching for [bai] but he’s nowhere to be seen.)"
    show shadow_lucas
    shadow_lucas "[you]?"
    show lucas
    "(I jerk my head around to the doorway from where my name was called only to find [lucas] walking in.)"
    you "{i}Oh, it’s just [lucas]. He’s such a gym addict. He worked out in the morning and he’s back here to work out again? Do his muscles not hurt?{i}"
    you "[lucas]. You’re in this class as well?"
    lucas "No, I’ve got a free block next block. You rushed out of class to come here?"
    you "Well I’ve got weight training this period..."
    lucas "You know there's a break first before class right."
    "{i}Ugh why does he keep questioning me.{i}"
    you "I know. I just wanted to get here fast. You’re so dedicated to working out that you even do it during break?"
    lucas "No, I'm staying here to work out during period 2 as well."
    you "Does the teacher not get mad if you’re not in his class?"
    lucas "He’s known me for a while and he doesn’t care if I drop by as long as I’m exercising. He’ll only get mad at you if you’re like [bai] who just sits there and reads manga."
    you "Oh, I wanna lose some weight. You work out a lot don’t you? What should I do to make my back thinner?"
    lucas "You’re like a twig. You don’t need to lose weight."
    you "..."
    lucas "You can do some seated cable rows, they’ll target the middle part of your back. You know what those are?"
    you "No clue. I don’t work out as you can probably tell."
    lucas "I shouldn’t have asked. I guess I’ll show you."
    lucas "Place your feet on these rests here, grip the attachment with your knuckles facing out, and do a pulling motion. Try not to pull with your arms too much."
    "I sat down and positioned my legs on the rest. I gripped the handle like [lucas] instructed, attempting to repeat what he did. However I found myself unable to lift the weight up."
    "Suddenly I feel someone sit down behind me. [lucas] loops his arms around mine and holds my hands in his as he helps me lift the thing."
    "I can feel his hard, toned, muscular chest pressing against my back. I can't help but stare at the prominent veins on his forearms that trailed onto the back of his hands complimented by his numerous rings." 
    "My face heats up as the memory of his sweaty countenance this morning unconsciously makes its way into my mind."
    you "Why am I thinking about [lucas]? I should be thinking about [bai] instead!"
    lucas "Your posture is so bad." 
    "His blunt words interrupt my daydreams almost immediately, calming down my beating heart."
    you "..."
    lucas "That's why I'm helping you."
    you "Ok..."
    "{i}He’s too blunt for me to be daydreaming about him.{i}"
    "I continue the next few reps with my hands in his, constantly helping me adjust my hand placement and feet positioning. Except this time my heart is as calm as the waters in a roadside puddle after a rainstorm storm."
    "{i}There’s no way I’d ever feel anything for a man like this.{i}"
    lucas "Try by yourself now."
    "He gets off the chair and looks at me. I reluctantly pull my arms back to try to lift the weights, praying that my positioning is right. I watch as his brows furrow in confusion as to why I’m unable to pull the chord?"
    lucas "Your positioning is correct..."

menu Lucas_CH2_choice:
    "{i}This weight is way too heavy for me.{i}":
        you "I think... that this might be a bit too heavy."
        lucas "Oh sorry, I forgot to change the weight for you."
        jump Lucas_CH2_p2
    "{i}I gotta make sure I don't have feelings for him. I need him to help me again.{i}":
        $ lucas_fav+=1
        you "Are you sure my positioning is correct? I feel like it's still wrong."
        lucas "Y-yeah, it should be right..."
        show lucas flustered
        you "Maybe you can try helping me again."
        lucas "Sure- Oh wait I forgot to change the weights!"
        jump Lucas_CH2_p2

label Lucas_CH2_p2:
    scene weight training room
    show lucas
    lucas "Here, 20lbs should be good enough to start off with."
    "I try doing the same motion again, this time I could pull the weight a lot more easily."
    lucas "You wanna exercise and lose weight right? Want me to help you out during your weight training class? I’ll act like your personal trainer."
    you "Really?! You’ll help me?! This is perfect! I needed someone to help me pull [bai]!"
    lucas "You like [bai]?!"
    "{i}Oh shoot! I accidentally blurted that out.{i}"
    you "Hmm? Did you say something?"
    show lucas sigh
    lucas "Don’t act dumb. I heard you say you like [bai]." 
    you "Tsk. Guess you know now."
    show lucas
    lucas "You guys are childhood friends but you said you guys don’t contact each other much."
    you "Yeah that’s true but... I’ve liked him since elementary school. Also we do see each other because our parents are friends."    
    "I turn my red face away from [lucas], feeling embarrassed as I say this. Even though I think that it’s ridiculous how I’ve liked [bai] for so long. But it's not like I can stop liking someone so easily."
    lucas "Damn. And you’ve managed to hide this from him for so long without confessing?"
    you "Well... It’s hard to confess. We’ve been friends for so long that confessing will make things so awkward. Also he’s like a wooden stick that doesn’t care about girls."
    lucas "That’s true."
    you "You’re close with [bai] right? Since you already know about this... could you help me?"
    lucas "Help with what? Making [bai] fall for you?"
    you "Yeah..."   
    lucas "... What do I get in return?"
    you "What do you want?"
    lucas "Give me some time to think. I’m not sure yet."
    lucas "To start, we need you to spend more time with [bai]. But since you’re new here you were probably gonna go find [bai] at lunch anyways right?"
    you "Yeah. You know where he eats? I’m worried he’ll find me bothersome if I ask so I wanted to accidentally find him."
    lucas "I eat with him at lunch. I’ll bring you there and you can eat with us."
    you "Okay."
    jump Lucas_CH3

label Lucas_CH3:
    scene black screen 
    show text "{color=#cc0066}Chapter 3: ----{/color}" with Dissolve(1.5)
    hide text "{color=#cc0066}Chapter 3: ----{/color}" with Dissolve(1.5)
    hide black screen
    scene weight training room
    show lucas
    lucas "Class is over, follow me."
    "At this moment, I feel my phone vibrating in my pocket. I open it up to see a text from [bai]."
    hide lucas
    show shadow_bai
    bai "{i}I eat lunch in room 220 with some other people. Wanna join? I’ll come find you if you don’t know where to go.{i}"
    hide shadow_bai
    show lucas
    lucas "[bai] texted you where to eat lunch? I've never seen him act this nice, guess you won't need me then."

menu Lucas_CH3_choice:
    "{i}{i}":
        jump Lucas_CH4
    "{i}He's nice to people he's friends with, but it's ridiculous how he's so dense when it comes to other people's feelings. {i}":
        you "He's only doing this because I'm new and he knows I've moved around a lot which makes making friends difficult."
        "My expression couldn't help but turn into a wry smile of self ridicule. [lucas] could probably tell I was upset because he placed his arm around my shoulder to comfort me."
        show lucas flustered
        lucas "It's fine. Our goal is to make him like you. I'll beat that lil dumpling up if he doesn't like you."
        you "Hahaha! Don't do that, he won't stand a chance against you."
        show lucas
        lucas "You finally smiled. I'm glad."
        you "You said that to make me laugh"
        show lucas flustered
        lucas "Yeah..." 
        you "Thanks for cheering me up."
        "{i}Lucas is actually nicer than most men out there...{i}"
        show lucas at left
        show shadow_bai at right
        shadow_bai "[lucas], why're you standing outside the class."
        hide shadow_bai
        show bai annoyed at right
        "[lucas] and I turn around to see [bai] staring at us from behind. [lucas] quickly removes his arm from my shoulder as if he had been caught red handed."
        show bai at right
        bai "[you], you're here too? You and [lucas] met each other already?"
        you "Yeah... we had classes together this morning."
        "[bai] grins and walks up to [lucas], patting his back."
        bai "Good luck [lucas]."
        hide bai
        show lucas flustered at center
        "After that he walks into the class. I look at [lucas] and he looks back at me. We didn't need telepathy to read each other's minds. We instantly thought the same thing:"
        you "There's been a little misunderstanding here..."
        jump Lucas_CH4

label Lucas_CH4:
    scene black screen 
    show text "{color=#cc0066}Chapter 4: ----{/color}" with Dissolve(1.5)
    hide text "{color=#cc0066}Chapter 4: ----{/color}" with Dissolve(1.5)
    hide black screen
    scene sidneys
    show lucas flustered
    "{i}This dense idiot!{i}"
    you "Things just got worse... Now he thinks we like each other."
    lucas "It's fine. This can be a strategy. We can make him jealous of me."
    you "... Won't that ruin your friendship?"
    lucas "Trust me, a female isn’t enough to ruin a man's friendships."
    you "Ok... then how do we make him jealous?"
    lucas "I haven’t used up my end of the deal but I’ve thought of something just now. What if you act as my fake girlfriend?"
    you "...ew."
    lucas "Hey, we don’t need to tell others that we’re “dating”. We just need to act close in front of [bai] to make him jealous. On the other hand, we go on “dates” with each other to research and practice when we start dating other people. Whatever I do to help you, you’ll do the same when I have someone I like."
    you "Hmm... that doesn’t sound bad. You’ll tell me when you find someone you like right?"
    lucas "Yeah, we’ll help each other prepare for when we actually date."
    you "Ok, it’s a deal then."
    "The two of us walk in room 220. A few familiar faces were already sitting at the tables, one of which was [hong] and some guy from the earlier AP Statistics class."
    show lucas at center
    show anne at right
    "Hey guys!"
    "A familiar girl wearing flashy silver jewelry walks into the class."
    lucas "Oh, [anne]"
    show bai at left
    bai "Uhhhh we have a new student. Her name is [you] and we went to the same elementary school."
    anne "Oh, I remember you! You’re that one girl who had a thing with [bai] back in 5th grade."
    you "W-what? I had a thing with him in 5th grade?"
    "{i}I wish.{i}"
    anne "Huh? I swear you guys were always holding hands though."
    show bai flustered at left
    bai "Anyways... What are you two doing here? Also how about we introduce ourselves to [you]."
    anne "You probably remember from Elementary School but I’m [anne]."
    anne "Guys we need to figure out our airbnb for the trip... I’ve already sent you guys some of the airbnbs that we can choose from. A lot of the nicer and cheaper ones are further from the downtown area though."
    "But since the week after next is coming up so we need to hurry and decide. We also need to hurry and make an itinerary on where to go."
    you "I lived in Victoria for a while and I actually have a friend who’s parents own a house that’s listed for airbnb renting near the downtown area. Their airbnb is huge and it looks like quite a few of you are going. If you guys are interested I can ask them about it and possibly get you guys a discount as well."
    """
    Anne: “Really?? That would be great! I’m poor as hell right now anyways!”

    [lucas] “Dumbass, just come with us to Victoria. Since you’ve lived there, you can also guide us around.”

    [lucas] looks at me meaningfully.


    [you] “Who’s going? And wouldn’t I be intruding?”  If [bai] is going then this is a good opportunity!


    Annika: “Me, [lucas], Anne, the Alexes, the guy with glasses Sam and Amy who’s not here today are going. I think it’d be great if you came. We get a tour guide and we’ll get to know each other better.”

    The rest of the crowd nods in agreement.

    [lucas] “See most of us are okay with it.”

    [you] “Well if you guys are okay with it then I’d love to join you guys!”
    Perfect, I can’t wait to spend more time with [bai].

    [you] “my friends airbnb should be able to fit 8 people, we just might need to share beds if that’s okay with you guys.”

    Annika: 'It's fine, we were planning on sharing beds anyways.’
    [you]: “I’ll go ask them about it. When are we planning to go?”

    Annika: “We’re planning on getting there on the morning of September 22nd and back here on the afternoon of the 25th. The 23rd is pro-d so we’ll only be missing school on the 22nd.”

    [you] “Okay, I’ll tell you when they respond.”

    At the end lunch:

    [you] “[lucas], I’m surprised you were smart enough to invite me on this trip.”

    [lucas] “I’m not stupid. You better thank me later.”

    [you] “How about I treat you to a meal. I can also prepare for the trip.”

    [lucas] “Ok I have time over the weekend. What’s your number?”

    He hands me his phone, which looked like it had been through a lot, and I type my number in.

label Lucas_CH5:
    """
    return