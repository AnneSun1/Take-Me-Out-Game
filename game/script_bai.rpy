# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

#persistent

#favorability variables
default bai_fav = 0
default bai_good_end = False
default fight_ch3 = False
default tease_bai_ch5 = False
define jason = Character("Jason")
define ricky = Character("Ricky")

#images


#BAI ROUTE START------------------------------------------------
label Alex_B_CH1:
    scene black screen
    show text "{color=#cc0066}Chapter 1\nYou have chosen [bai]'s story{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 1\nYou have chosen [bai]'s story{/color}" with Dissolve(3.0)
    hide black screen 
    play music "audio/happy bgm.mp3"
    scene counsellors office
    "Looking at my period 1 class I see the words \"WEIGHT TRAINING\" on it. I only chose this class because I needed another class and my Dad insisted that I get some exercise." 
    "To be honest, I’m not looking forward to this class. My impression of [lucas] is that he’s intimidating and I assumed the other gym guys to be just like him."
    "[you]" "I have weight training during period 1..."
    show bai
    "[bai] who was waiting in the counselors for me chimed in."
    bai "Weight training? I have weight training in block 1 as well. [hong] you can head to class, I’ll bring [you] with me."
    scene weight training room
    show bai
    "[bai] and I walked into the class together."
    you "You know, I never expected you to take weight training."
    bai "Well uhhh I didn’t expect YOU to take weight training either."
    you "Well, I thought I needed some exercise and I might as well lose some weight too."
    bai "You? lose weight? But you’re as skinny as a twig, you’re fine the way you are right now. Well either way, we don’t really do anything in this class. I usually just read manga."
    "I look around the room and I see people sitting around talking and walking in and out of the room. Very few people were actually working out."
    you "{i}I wanna workout but no one else is, I don’t wanna stand out.{i}"
    you "Oh... I wanted to exercise though..."
    "[bai] seemed to panic a bit after seeing my disappointed expression."
    show bai flustered
    bai "Argh- Fine, I’ll help you train."
    show bai

menu Alex_B_CH1_c1:
    "{i}I want him to help{i}":
        $ bai_fav +=1
        you "Can you please spot my barbell squats?"
        jump Alex_B_CH1_p2

    "{i}...{i}":
        you "No... It’s ok I’ll go ask someone else! Don’t worry about it Alex!"
        show bai annoyed
        bai "I said I could help you though... Whatever it’s fine ."
        you "If you insist... I guess you can help me with barbell squats."
        jump Alex_B_CH1_p2

label Alex_B_CH1_p2:
    show bai flustered
    bai "Barbell squats?! I-isn’t that too uhhh... nevermind, I’ll do it."
    show bai
    "I walk to pick up the cold metal bar. As I lift it to my chest and haul it over my head, he stops right behind me and holds up the bar for me so I can get a good grip of it." 
    "I feel the air warm around my shoulders as he hovers his arms behind mine."
    you "I’m ready."
    bai "Ok."
    "I do a few reps before I feel my thigh muscles tightening up, indicating an incoming cramp. I quickly finish my squat and lift the barbell back onto the squat rack."
    bai "Hm? Why are you stopping?"
    you "Hss. I think I got a thigh cramp."
    bai "Are you ok? Sit down, I’ll bring you some water."
    "Alex grabs my arm and helps me to the nearest bench."
    bai "Stay put there okay?"
    "He speeds out of the weight training room and comes rushing back with a bottle of water in hand."
    bai "Here, drink this and stretch out your leg."
    "He sits down next to me. His uni-brow was furrowed the whole time as he stares at me worriedly." 
    "I could feel his anxiety level rise whenever I winced in pain from the cramp."
    you "{i}Why is he so worried about me? He was quite attentive back in elementary school, but it’s been so many years already.{i}"
    you "Alex, I’m fine, don't worry too much."
    show bai flustered
    bai "Huh? Who said I’m worried, I’m not."
    you "{i}He still gets shy like he did when we were kids. That’s so cute. I’ll tease him a bit more.{i}"
    you "Hmmmm really?"
    bai "Ya! I’m not worried, I’m just uhh trying to make sure you’re alright."
    "He shifts his gaze away from me. I could tell my teasing was effective because of the red blooming on the tip of his ear."
    show bai
    bai "Class is ending, we should get ready to leave. Do you have time after school?" 
    bai "You’re already in shape but you’re still working out. You should eat more, I’ll take you to eat Chinese food after school."
    you "Alright, see you after school then."
    stop music 
    jump Alex_B_CH2

label Alex_B_CH2:
    scene black screen
    show text "{color=#cc0066}Chapter 2{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 2{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3" fadein 1.0
    scene hallway
    you "He told me to wait here after school... I wonder what class this is."
    show bai
    bai "Hey [you]! Come on, let’s go. Y’know, I am very well-informed on the Chinese restaurants around here."
    you "{i}I see a large group of students swarming around the teacher’s desk and notice the message “TEST NEXT CLASS” written on the whiteboard.{i}"
    you "Hey, there’s a group of people asking the teacher questions. Don’t you want to stay behind?"
    bai "Nah, that’s Teacher D. I don’t like his calculus class, plus his lessons never help with tests."
    you "{i}[bai] seems like he’s in a bad mood. I hope I’m not bothering him too much...{i}"
    stop music fadeout 1.0
    scene chinese restaurant
    play music "audio/romantic.mp3" fadein 1.0
    #edit
    show bai
    bai "We’re here!"
    you "...Huh I’ve never been to this restaurant before."
    hide bai
    you "{i}As we walk into the restaurant, a waiter greets us and leads us to our table.{i}"
    show bai
    bai "Hey uh are you okay, [you]? You keep putting your head down."
    you "Yeah, I’m fine!"
    you "{i}Why does he keep worrying about me? He’s the one who just had a bad calculus test.{i}"
    bai "Sooo, have you been to this restaurant before?"
    you "No, actually, what do you think I should order?"
    bai "Really!? You’ve never been? This is my favorite restaurant to go to after a big test, the dumplings here are amazing! My friends even told me my head is shaped like one."
    you "...I’m not sure if that’s a compliment."
    bai "Huh?"
    you "Nothing..."
    "After our food arrives, we awkwardly eat in silence, only exchanging glances every few minutes amidst the lively dining room."
    "Why is he so quiet? I thought he was the one that invited me to this restaurant in the first place! Maybe I should have just gone straight home instead..."
    show bai flustered
    bai "So... uh... how’s your little brother doing?"
    "My little brother, Jason. He was really young when we moved away, so he doesn’t remember much about this town, but he does remember [bai]’s brother, Ricky."
    "In fact, while communications between me and [bai] decreased over the years, our little brothers have only increased. So much so to the point where they attend each other's birthdays yearly despite distance keeping them apart."
    you "Jason’s doing alright. He’s still adjusting to his new school, but he’s really looking forward to hanging out with Ricky more."
    show bai
    bai "That’s good to hear. Maybe you can bring Jason over to our house sometime and they can hang out."
    you "Sure."
    you "{i}I haven’t been to Alex’s house since we played together as kids, those were good times. We used to be best friends, just like our siblings, but time made us drift apart. {i}"
    bai "Are you finished eating yet? You don’t want to become a pig like [hong], do you?"
    "I secretly laugh at his ridiculous comments. I see that’s one thing that hasn’t changed about him."
    you "Haha yeah, I’m finished. The food here was delicious."
    bai "Okay, let’s head out." 
    scene dark street
    "As we walk outside, we notice the harsh September rain pouring over the street, it was dark already. A typical autumn evening. Suddenly, I feel a large jacket wrap around my shoulders."
    show bai flustered
    bai "T-take it. It looks like you need that more than I do."
    "A blush creeps up his ears and he looks away."
    you "I-I wasn’t even that cold, but thank you."
    you "{i}I've never seen him act this gentlemanly, afterall he's usually awkward and makes weird jokes... I guess he's grown up in the past few years.{i}"
    show bai
    bai "Let’s walk to the Skytrain station together, ok? I’m the only one with an umbrella, and I don’t want you to get sick."
    
menu bai_ch2_choice1:
    "Ok...":
        $ bai_fav+=1
        scene dark street
        "I slowly follow him down the busy street. Even with all the noise around us, I could somehow hear his every breath. I fumble over my words and fail to hold a conversation."
        you "{i}This feeling is so weird. Isn’t he just my childhood friend?{i}"
        "Maybe it was just my imagination, but I think I saw him smiling as we walked."
        bai "We're here. Get home safe okay?"
        "He walks off before I get the chance to return him his jacket."
        scene black
        scene house
        #show phone with vpunch
        play sound "audio/phone buzz.mp3" fadein 1.0
        "A message from [bai] pops up on my phone."
        stop sound
        show shadow_bai
        bai "Did you get home safe?"
        "I unconsciously smile as I reply."
        you "Yes, thanks for walking me to the station. You forgot your jacket though."
        bai "It's fine, you can keep it."
        you "Oh... Ok."
        "Our texting ends there, but I'm unable to stop thinking about him for the rest of the night."
        stop music

    "No, I’m fine walking myself home. It's not that far from here anyways.":
        bai "Ok then, I’ll see you around at school then. Good night [you]."
        you "Good night..."
        stop music
 
label Alex_B_CH3:
    scene black screen
    show text "{color=#cc0066}Chapter 3{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 3{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3" fadein 1.0
    scene hallway
    you "{i}After our meal last time, I haven't seen [bai] alot... I think he's avoiding me.{i}"
    "My mind goes back to yesterday..."
    scene hallway_dark
    you "[bai], how were your classes today?"
    show bai flustered
    bai "They were fine... hey uh I have something planned with [lucas], gotta go." 
    you "Oh... ok..."
    "I looked at him dejected from his obvious avoidance of me. He looked back at me guiltily but that didn't stop him from leaving."
    #end flashback here
    hide bai
    scene hallway
    you "{i} He always makes an excuse to avoid me. I thought that we had gotten close again after I came to this school..."
    scene sidneys
    "At lunch I walk into the Chemistry classroom, hoping to find Anne to review some calculus with me."
    "Instead, I see a bunch of guys huddled around [bai]."
    show bai at left
    show lucas annoyed at right
    lucas "What?! How did I lose to you?!"
    bai "Haha! Loser."
    you "Um... sorry to interrupt but is Anne here?"
    show lucas at right
    lucas "No, I think she went to a club meeting today. What do you need her for?"
    you "I wanted to ask her some calculus questions."
    lucas "I can help explaining to you if you want."
    
menu bai_ch3_choice:
    "{i} [lucas] wasn't that bad at explaining things the last time I asked him for help...{i}":
        $ fight_ch3 = True
        jump Alex_B_CH3_jealous
    "{i} I can't have [lucas] helping me! The last time I asked him for help, he was so bad at explaining!":
        $ bai_fav+=1
        jump Alex_B_CH3_library

label Alex_B_CH3_jealous:
    scene sidneys
    show bai annoyed at left
    show lucas flustered at right
    stop music fadeout 1.0
    play music "audio/argument.mp3" fadein 0.5
    you "Really?! That would be really helpful!"
    lucas "No worries, we can go to the library right now."
    bai "You'd let [lucas] explain calculus to you? He's awful at explaining though."
    you "I think he's fine. It's not like you're able to help me or anything anyways." 
    show lucas at right
    "I become more angry as I speak to him."
    you "You won't even hold a proper conversation with me these days! Why's that?"
    show bai flustered at left
    bai "T-that's none of your business..."
    hide bai
    show lucas at center
    you "Let's go [lucas], there's no use talking to this guy."
    stop music
    jump Alex_B_CH4

label Alex_B_CH3_library:
    scene sidneys
    show bai at left 
    show lucas at right
    you "Uhh... It's fine I can have [bai] help me instead!"
    "I grab [bai] by the arm and drag him out of the room."
    stop music fadeout 1.0
    scene hallway
    play music "audio/romantic.mp3" fadein 0.5
    show bai flustered
    bai "W-wait, what're you doing I'm not even in AP Calculus!"
    "I reply to him as I drag him upstairs into the library."
    you "Shush! [lucas] is so bad at explaining, I'd rather just figure it out myself."
    scene library
    show bai
    bai "You've been studying for a while now, if there's no use for me... can I leave now?"
    you "N-no! Don't leave yet!"
    bai "What do you want."
    you "U-um... Since you're in Teacher D's class and you guys are going at the same pace as us, maybe you can help me..."
    "I look up at him pleadingly."
    show bai flustered
    bai "H-huh? But I don't think I could help you..."
    show bai annoyed
    you "{i}Does he really dislike me that much? Even though we were fine just a few days ago?{i}"
    you "Fine. Then you can leave! Afterall, all you've been doing is avoiding me lately!"
    show bai
    bai "I'll stay. I'll try to help you."
    you "R-really?"
    bai "Yeah, afterall you're dumber than me."
    you "W-what? Who says I'm dumber!!!!!"
    stop music

label Alex_B_CH4:
    scene black screen
    show text "{color=#cc0066}Chapter 4{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 4{/color}" with Dissolve(3.0)
    hide black screen
    if fight_ch3:
        jump Alex_B_CH4_make_up
    play music "audio/happy bgm.mp3"
    scene house
    show jason
    "Today Jason's going to Ricky's house."
    jason "Big sister, it's time to go to Ricky's house!"
    you "Ok, let's go."
    scene bais_house
    show jason
    jason "Ricky! I'm here to play!"
    you "Hey! Don't scream, you're gonna disturb the neighbours!"
    show jason at left
    show ricky at center
    show bai at right
    ricky "Jason, you're here! Come inside, let's go play!"
    hide jason
    hide ricky
    show bai at center
    you "Sorry, Jason's too loud. I think he's just really excited to see Ricky again."
    bai "Yeah, afterall it's been a while since they've met each other."
    you "Well I'm gonna go then. I'll be back tonight to pick Jason up."
    bai "W-wait!"
    "[bai] grabs my hand and stops me as I'm about to leave."
    you "What's wrong?"
    show bai flustered
    bai "Do you wanna stay over and we can hangout. Afterall it's been a while since you've been over at my place."
    you "{i}He's inviting me over to his place?? Guys don't just do this with any girl right?!{i}"
    you "S-sure!"
    stop music fadeout 1.0
    play music "audio/romantic.mp3" fadein 0.5
    jump Alex_B_CH4_p2

label Alex_B_CH4_make_up:
    play music "audio/happy bgm.mp3" fadein 1.0
    scene house
    you "{i} Dad and Mom are busy today so I need to bring Jason over to Ricky's house. {i}"
    you "{i} What do I do? I haven't made up with [bai] yet after our argument last time. {i}"
    "Jason's voice pulls me out of my thoughts."
    show jason
    jason "Big sister, it's time to go to Ricky's house!"
    you "Ok, let's go."
    scene bais_house
    show jason
    jason "Ricky! I'm here to play!"
    you "Hey! Don't scream, you're gonna disturb the neighbours!"
    show jason at left
    show ricky at center
    show bai at right
    ricky "Jason, you're here! Come inside, let's go play!"
    hide jason
    hide ricky
    stop music fadeout 1.0
    play music "audio/romantic.mp3" fadein 0.5
    show bai
    you "{i}This is awkward, I don't know what to say to him.{i}"
    you "Well... since I've dropped him off I'm gonna go now."
    bai "Wait!"
    "[bai] grabs my hand and stops me as I turn around and leave."
    bai "About last time in the Chemistry class, I'm sorry I got upset with you."
    you "Oh, it's ok."
    show bai flustered
    bai "So how about you stay and hangout with me since Jason's here and all."
    you "Okay..."
    jump Alex_B_CH4_p2

label Alex_B_CH4_p2:
    scene bais_room
    you "{i}It's been so long since I last came to his room. He's got so many anime posters.{i}"
    show bai
    bai "Uhh you can sit on the bed."
    you "Okay..."
    bai "There's nothing much to do here. We can play some games, watch anime or read manga."
    you "Hmm..."
    you "You have a whole shelf of manga there, can I check it out?"
    bai "Sure, although a lot of them are Japanese light novels."
    "As I walk towards his shelf, I notice a particularly eyecatching series: Green Spring Ride."
    you "{i}This was my favourite series back in elementary school. Does he like it too?{i}"
    you "Hey [bai], you like Green Spring Ride too?"
    show bai flustered
    bai "Huh? I-it's okay I guess."
    "A smirk spreads across my face, this was the perfect chance to tease him."
    you "I didn't know you like shoujo manga as well. You have the heart of a maiden~"
    bai "No I don't!"
    you "You totally do, otherwise why would you have the whole series?"
    show bai annoyed
    bai "I-it's only because the person I like likes this series!"
    you "Y-you have someone you like?!"
    "I could visibly see the horror set into his expression. He knew he accidentally let something slip out that he shouldn't have."
    show bai flustered
    bai "Forget I said anything."
    you "No way - you hint at such juicy gossip and now you refuse to tell me."
    bai "I'm serious... I can't tell you more."
    you "Fine."
    "I give up on interrogating him and instead reach to grab the first volume of a Green Spring Ride book."
    "However, just as I take the book out of it's place on the highest shelf, a shower of other books come raining down."
    bai "[you] watch out!"
    scene black with vpunch
    play sound "audio/crash.mp3"
    play music "audio/romantic.mp3" fadein 1.5
    #scene bai protect
    ""
    stop sound
    "Before I can even react, I feel [bai]'s body closing in on me to protect me from the books." 
    "When I open my eyes again, his face is right in front of mine with his arm protecting my head."
    bai "[you], are you okay?"
    you "Y-yeah..."
    "I feel my face heating up as my eyes unconsciously look towards his lips."
    bai "..."
    you "..."
    bai "[you], you know the girl that I said I like from earlier?"
    you "Y-yeah..."
    bai "I've known her for a long time. We've known each other since childhood and I've liked her since childhood."
    bai "But I don't know what she thinks about me, because we've been seperated from each other for so long."
    bai "I don't know if I have the courage to confess to her yet."
    you "{i}The person he's talking about sounds a lot like me...{i}"
    bai "So [you], w-what do you-"
    scene bais_room with vpunch
    stop music fadeout 1.0
    play music "audio/argument.mp3" fadein 0.5
    show ricky
    ricky "Big brother! Jason disappeared!"
    stop music
    jump Alex_B_CH5

label Alex_B_CH5:
    scene black screen
    show text "{color=#cc0066}Chapter 5{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 5{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/argument.mp3"
    scene bais_room
    show bai at left
    show ricky at right
    you "Hold on, Jason disappeared as in he's lost?"
    "I feel a sense of dread washing over me. Jason had always had an awful sense of direction. Who knew where he would've ran off to."
    ricky "Y-yeah, we went out to play at the park. We were going to play hide and seek and it was his turn to find me."
    ricky "So I hid up a tree, but then after a long time he still hadn't found me so instead I tried to find him."
    ricky "But no matter where I searched in the park, I can't find him!"
    you "W-what do I do! I'ts all my fault Jason disappeared, because we weren't watching the two of them!"
    #enter cg of bai holding mc hand
    "[bai] presses his forehead onto mine."
    bai "[you] calm down first. we'll find your brother together."
    "Despite his usual awkwardness, his words were extremely comforting."
    scene bais_room
    show bai at left 
    show ricky at right
    bai "Ricky, lead us to the park you played at."
    scene park
    show bai at left
    show ricky at right
    ricky "We were playing in this area of the park, but the park is so big he could've wandered off somewhere far."
    bai "Ricky, you can get back home alone right? [you] and I are going to split up to look for Jason."
    ricky "Okay."
    hide ricky
    show bai at center
    bai "Is there a place that Jason's more likely to go when he's lost?"
    you "He tries to go towards our house..."
    bai "Okay, I'll look for him on the path to your house. You can search for him in this neighborhood."
    stop music fadeout 1.0
    scene street
    # make the lighting dusk
    play music "audio/night bgm.mp3" fadein 0.5
    you "Jasonnnnn, where are you?"
    you "{i} It's getting dark out but I still haven't found Jason yet, I hope [bai] has found him.{i}"
    "I text [bai] to see if he's found Jason yet."
    scene mc_house_street
    show bai 
    bai "Jason! There you are! You're sister's so worried for you!"
    show bai at left
    show jason at right
    stop music fadeout 0.5
    play music "audio/argument.mp3" fadein 0.5
    jason "Wuwuwuwuu"
    "[bai] runs towards the crying Jason and holds him in his arms."
    bai "It's okay now Jason, I found you. We can go find your sister now."
    jason "Okay... I didn't mean to disappear. I just got lost..."
    bai "Alright, I get it I get it."
    "[bai] lifts up Jason and carries him in his arms as he walks back to his house."
    stop music fadeout 1.0
    play music "audio/happy bgm.mp3" fadein 1.0
    scene living_room
    show bai at left
    show jason at right
    "Recieving [bai]'s text from earlier that he found Jason, you head back to his house."
    you "[bai] you're back and you found Jason! Thank god!" 
    "A feeling of relief washes over you as you see [bai] carrying Jason in his arms."
    bai "Mhm, Jason make sure to stay in the area you were playing at next time okay?"
    jason "O-okay big brother [bai]."
    bai "Good, let's go back and make dinner."
    you "{i}Contrary to his goofy personality, he's a really good older brother when it comes down to it.{i}"
    "Unconsciously, I smile at the image of him taking care of the two younger children."
    scene kitchen
    show bai
    bai "Okay, since Mom and Dad aren't home today, I'm gonna be the one cooking."
    bai "what do the two of you want to eat?"
    show ricky at left
    show jason at right
    show bai at center
    ricky "Uh oh-"
    hide bai
    "Ricky turns to Jason and I. In a voice loud enough for us but not [bai] to hear he speaks."
    ricky "You guys don't wanna eat his cooking, he nearly burnt down the kitchen last time."
    ricky "Mom and Dad knows he can't cook so they told us to get take out but he's not listening..."     

menu bai_ch5_choice:
    "{i}We should seriously get take-out instead...{i}":
        you "[bai], how about let's get some takeout instead."
        you "We're all tired from what happened today, we can order some good food instead."
        bai "Ricky and Jason, are you okay with that?"
        ricky "Yes! I'd choose anything over your food!"
        bai "Hey! My cooking isn't that bad!"
        jump Alex_B_CH5_takeout
    "{i}His cooking can't be that bad can it? I also wanna see him cooking... I bet he'll look handsome.{i}":
        $ bai_fav+=1
        you "Your brothers cooking can't be that bad right? Worst case scenario I just give him a helping hand later."
        ricky "I'm not kidding, it's actually awful."
        you "It's fine, I'll step in to help him later. Let's just let him cook first."
        jump Alex_B_CH5_cooking
    "{i}Hmmm, maybe I can teach him how to cook.{i}":
        $ bai_fav+=1
        you "How about we cook together?"
        ricky "Yes please! Older brother let [you] cook with you."
        bai "Well sure if you insist..."
        jump Alex_B_CH5_cooking

label Alex_B_CH5_takeout:
    scene living_room
    you "Kids, the food is here come eat!"
    show ricky at right
    show jason at left
    show bai at center

    ricky "Ohh Chinese food! This looks yummy!"
    you "That's good then, let's eat!"
    stop music
    jump Alex_B_CH6

label Alex_B_CH5_cooking:
    $ tease_bai_ch5 = True
    scene kitchen
    show bai at left
    show ricky at right
    bai "Let me ask again, what do you guys want to eat?"
    you "{i}It'll probably be easier to make him cook something easier, in order to avoid disaster.{i}"
    you "How about scrambled eggs and tomato?"
    bai "That's so basic though."
    ricky "No no, it's not basic. At least not for you..."
    bai "Don't slander my cooking! I'm gonna show [you] just how good my cooking is."
    "Ricky sighs and leaves the kitchen to go watch TV with Jason."
    hide ricky
    stop music fadeout 0.5
    play music "audio/romantic.mp3" fadein 1.0
    show bai at center
    
    bai "[you], you can cut the tomatoes and scramble the egg. I'll go cook the rice."
    you "Okay."
    "Just as I begin beating the cracked egg, from the corner of my eye I see him about to start the rice cooker with what I'm sure is unwashed rice..."
    you "[bai]! Did you wash the rice?"
    bai "No... am I supposed to?"
    you "{i}How can anyone be this dumb? Of course he needs to wash the rice!{i}"
    you "Of course you need to wash the rice! What if there's bugs in there? Haven't you seen those posts online?!"
    show bai annoyed
    bai "I'm not a phone addict like you, of course I wouldn't know!"
    you "Just leave the rice to me, you can go crack and beat the eggs."
    bai "Fine."
    show bai
    "I watch him storm over to the half beaten egg and you wash the rice."
    "After starting the rice cooker, I look over only to see him beating eggshells into the bowl."
    you "..."
    you "What are you doing now?"
    bai "Beating eggs?"
    you "Why're there shells in there?"
    bai "Uh..."
    "I pick the shell bits out of the bowl and I grab his hand."
    # add egg beating cg here
    show bai flustered
    you "Look, you beat it like this."
    "I could visibly see his face getting redder and I felt the hotness from his cheeks."
    you "{i}Based on his words from this afternoon and his current reaction, he definately likes me. {i}"
    "His shy reaction made me want to tease him more."
    bai "T-that's enough, I'll go cut the tomatoes instead now..."
    you "Okay."

    scene living_room
    you "Kids, it's time to eat!"
    jason "Okay coming!"
    show jason at left
    show ricky at right
    show bai at center

    ricky "Ohh this actually tastes good! [you] you did a good job teaching [bai]."
    you "Hehe, that's good then."
    stop music
    jump Alex_B_CH6

label Alex_B_CH6:
    scene black screen
    show text "{color=#cc0066}Chapter 6{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 6{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3"
    scene living_room
    show jason
    you "Jason, it's time to leave."
    jason "No! I wanna stay with Ricky!"
    you "Come on, you've already caused so many problems today."
    show jason at left 
    show bai at right
    bai "It's alright, Jason can stay and sleep over if he wants."
    you "Are you sure it's okay? I'm sorry for how spoiled he is."
    bai "They haven't seen each other for a while so just let him stay and have fun."
    you "I'll come by and pick him up tomorrow then."
    bai "Sure."
    jason "Yay!"
    show jason with moveoutleft
    show bai at center
    you "Well I'm gonna get going then, it was good hanging out with you today."
    bai "I'll walk you home since it's dangerous outside."
    stop music fadeout 0.5
    play music "audio/romantic.mp3" fadein 1.0
    scene dark street
    "We walk back in silence. But as we walk, I can't help but think about everything that had happened today."
    "It had been a long day, but what did [bai]'s actions mean?"
    show bai
    bai "Thanks for cooking for us today, both Ricky and Jason enjoyed it lots."
    you "No worries, I enjoyed spending time with you guys too, even though all of that happened today."
    bai "[you]."
    "[bai] suddenly stops walking and turns around to look at me."
    show bai flustered:
        #ease .5 
        zoom 1.5 ypos 2000
    bai "You might've been able to guess but... "
    bai "I've liked you for a long time now."
    you "..."
    bai "Y-you don't need to reply now."
    bai "I just wanted you to know that I really like you, since I met you."
    bai "Those years when you moved away for me were the hardest. The only reason that I only tell you now was because we didn't talk for the past few years."
    bai "I'm awkward and don't know how to properly talk to girls, but I thought that it's be a good chance to get closer to you again since you moved back."
    bai "I just wanted to say all of this, you can reply to me when you feel like you have an answer."
    you "Okay..."
    show bai:
        zoom 1.0 ypos 1440
    bai "Well, we're here now. Think a bit about what I've said today. Good night."
    "I wave at [bai] and just as I turn around to leave, I catch a glimpse of an expression I've never seen before from him."
    show bai crazy
    scene house
    you "{i}Do I like him back?{i}"
    you "{i}He's been so nice to me ever since I moved back. It's completely different from how he was as a child.{i}"
    you "{i}Also I did have a slight crush on him when I was younger.{i}"
    you "{i}Being with him makes me happy, maybe I do like him, I just need to find a romantic time to confess.{i}"
    stop music
    if bai_fav>=2:
        jump Alex_B_CH7
    else:
        jump bad_end


label bad_end:
    scene black screen
    show text "{color=#cc0066}Chapter 7{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 7{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3" 
    scene hallway
    "Ever since [bai]'s confession, I had been thinking about how to reply. I made a magnificent plan to respond to his confession on his birthday."
    show lucas
    you "[lucas], there you are! I know it's [bai]'s birthday soon, do you know what he might like?"
    lucas "Hmm, we can go to the mall afterschool today to find something for him. Probably something anime related."
    play sound "audio/school bell.mp3" volume 0.5
    ""
    stop sound
    you "I gotta go to my next class, we can talk about this later at lunch."

    scene sidneys
    "I walk into the classroom and as usual, I see [lucas], [bai] and [hong] huddled around each other playing games."
    show lucas
    you "[lucas], what's the plan for later today?"
    lucas "Let's meet outside the entrance afterschool."
    stop music fadeout 1.0
    play music "audio/argument.mp3" fadein 0.5
    show lucas at left
    show bai at right
    bai "What's happening, where are you two going today?"
    you "{i} Shoot, I gotta make an excuse so he doesn't know our plans.{i}"
    you "W-well, me and [lucas] planned to go to the gym afterschool today!"
    hide lucas
    show bai crazy at center
    bai "You chose to ask [lucas] but not me??"
    you "{i}Why's he mad, it's just going to the gym.{i}"
    you "He just happened to be there when I planned to go to the gym afterschool, so I asked him."
    show bai annoyed
    bai "Let me come along."
    you "You can't! It's a, um, private gym that you need to sign up for!"
    you "We can go together to another one some other time."
    show bai 
    bai "..."
    bai "Fine."
    you "{i}He seems to have calmed down although unwillingly, I wonder what was up with him?{i}"
    you "{i}Everyone's looking at us because of what happened just now. I should probably leave...{i}"
    show lucas at left
    show bai at right
    you "Well [lucas] I'll see you afterschool then. Bye!"
    lucas "O-oh, bye."
    stop music fadeout 1.0
    play music "audio/happy bgm.mp3" fadein 0.5
    scene moscrop entrance
    show lucas
    "[lucas] and I meet up at the entrance and proceed to go to the bus stop."
    hide lucas
    show shadow_bai with moveinleft
    hide shadow_bai with moveoutright

    scene metro foodcourt
    show lucas
    you "I hope [bai] will like this hardcopy version of his favourite manga that I bought."
    lucas "To be honest, I think he'd like whatever you give him." 
    show shadow_bai with moveinleft
    hide shadow_bai with moveoutright
    you "{i}I keep feeling like there's someone following us...{i}"
    hide lucas
    "I look around but I don't see anyone familiar."
    you "{i}I guess it's just my imagination{i}"
    stop music fadeout 1.0
    play music "audio/night bgm.mp3" fadein 0.5
    show black screen with Dissolve(0.5)
    show dark street with vpunch
    show bai
    bai "[you]!"
    you "[bai], w-what are you doing here?"
    bai "Ah... I was just walking around."
    you "{i}I've felt someone following me all afternoon and now he shows up as I walk home alone... What is he up to?{i}"
    you "This late at night? Isn't that dangerous?"
    bai "No. I'm fine, but isn't it very dangerous for you?"
    you "Well, this is the only path home for me."
    bai "Since I'm here, let me walk you home."
    you "No, I think I'm fine..."
    show bai crazy
    show bai crazy:
        zoom 1.5 ypos 2000
        #ease .5 zoom 1.20 ypos 1500
    bai "Don't worry I'll bring you home."
    you "{i}This doesn't feel safe, I should find a way to leave...{i}"
    you "Seriously. I cant get home alone."
    show bai annoyed:
        zoom 1.0 ypos 1440
    bai "You go out on a date with [lucas] but you won't even let me walk you home?!"
    you "So it was you?!"
    bai "So you noticed me?"
    show bai crazy
    bai "YET YOU STILL ACT ALL CLOSE WITH HIM!"
    you "No! I don't have any feelings for him!"
    you "Today I only went with him to-"
    show bai crazy: 
        zoom 1.5 ypos 2000
    show bai crazy with vpunch
    play sound "audio/stab.mp3" volume 0.5
    "Before I'm able to finish my sentence, I feel something cold through my stomach."
    stop sound
    "I look down and I see [bai]'s hand on a knife that had pierced me."
    "I feel a body weaken and as I slump down, I force out the rest of my unfinished sentence."
    you "-buy you a present..."
    # street blur
    stop music
    $persistent.bai_end = True
    scene black screen
    show text "The End... or is it?" with Dissolve(3.0)
    hide text "The End... or is it?" with Dissolve(3.0)
    hide black screen
    return

label Alex_B_CH7:
    scene black screen
    show text "{color=#cc0066}Chapter 7{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 7{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3" 
    scene hallway
    "Ever since [bai]'s confession, I had been thinking about how to reply."
    "I seemed to be unable to get him out of my head."
    "No matter what I was doing, I would think about him non-stop."
    "I had planned to respond to his confession and surprise him on his birthday with a dinner and gift, and my love."
    "But before I confess, I had to test and see if his love for me was just as strong as my love for him..."
    show lucas
    you "[lucas], there you are! I know it's [bai]'s birthday soon, do you know what he might like?"
    lucas "Hmm, we can go to the mall afterschool today to find something for him. Probably something anime related."
    play sound "audio/school bell.mp3" volume 0.5
    ""
    stop sound
    you "I gotta go to my next class, we can talk about this later at lunch."
    scene sidneys
    "I walk into the classroom and as usual, I see [lucas], [bai] and [hong] huddled around each other playing games."
    show lucas
    you "[lucas], what's the plan for later today?"
    lucas "Let's meet outside the entrance afterschool."
    stop music fadeout 1.0
    play music "audio/argument.mp3" fadein 0.5
    show lucas at left
    show bai at right
    bai "What's happening, where are you two going today?"
    you "{i} Shoot, I gotta make an excuse so he doesn't know our plans.{i}"
    you "W-well, me and [lucas] planned to go to the gym afterschool today!"
    hide lucas
    show bai crazy at center
    bai "You chose to ask [lucas] but not me??"
    you "{i}Why's he mad, it's just going to the gym.{i}"
    you "He just happened to be there when I planned to go to the gym afterschool, so I asked him."
    show bai annoyed
    bai "Let me come along."
    you "You can't! It's a, um, private gym that you need to sign up for!"
    you "We can go together to another one some other time."
    show bai 
    bai "..."
    bai "Fine."
    you "{i}He seems to have calmed down although unwillingly, I wonder what was up with him?{i}"
    you "{i}Everyone's looking at us because of what happened just now. I should probably leave...{i}"
    show lucas at left
    show bai at right
    you "Well [lucas] I'll see you afterschool then. Bye!"
    lucas "O-oh, bye."
    stop music fadeout 1.0
    play music "audio/happy bgm.mp3" fadein 0.5
    scene moscrop entrance
    show lucas
    "[lucas] and I meet up at the entrance and proceed to go to the bus stop."
    hide lucas
    show shadow_bai with moveinleft
    hide shadow_bai with moveoutright

    scene metro foodcourt
    show lucas
    you "I hope [bai] will like this hardcopy version of his favourite manga that I bought."
    lucas "To be honest, I think he'd like whatever you give him." 
    show shadow_bai with moveinleft
    hide shadow_bai with moveoutright
    you "{i}I keep feeling like there's someone following us...{i}"
    hide lucas
    "I look around but I don't see anyone familiar."
    stop music fadeout 1.0
    play music "audio/night bgm.mp3" fadein 0.5
    show black screen with Dissolve(0.5)
    hide black screen with Dissolve(0.5)
    show dark street with vpunch
    show bai
    bai "[you]!"
    you "[bai], w-what are you doing here?"
    bai "Ah... I was just walking around."
    you "{i}I've felt someone following me all afternoon and now he shows up as I walk home alone... So it was him.{i}"
    "A small smile creeps up my face but I quickly hide it."
    you "This late at night? Isn't that dangerous?"
    bai "No. I'm fine, but isn't it very dangerous for you?"
    you "Well, this is the only path home for me."
    bai "Since I'm here, let me walk you home."
    you "..."
    you "N-no I think I'm okay."
    show bai crazy
    show bai crazy:
        zoom 1.5 ypos 2000
    bai "Don't worry I'll bring you home."
    you "Seriously. I cant get home alone."
    show bai annoyed:
        zoom 1.0 ypos 1440
    bai "You go out on a date with [lucas] but you won't even let me walk you home?!"
    you "So it was you who followed us."
    show bai crazy
    bai "So you noticed me?"
    you "You followed me..."
    you "...just as I wanted you to."
    show bai annoyed
    bai "Huh?!"
    stop music fadeout 1.0
    play music "audio/happy bgm.mp3" fadein 0.5
    you "I just wanted to make sure your love for me is strong enough."
    you "Well, we're at my house now. I'll see you next time."
    "I walked away leaving a dumbfounded [bai] standing there."
    stop music
    jump Alex_B_CH8

label Alex_B_CH8:
    scene black screen
    show text "{color=#cc0066}Chapter 7{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 7{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3"
    scene hallway
    "After the day [bai] followed me home, we continued our daily lives as if nothing happened."
    "It soon came time to be his birthday."
    scene sidneys
    "As soon as lunch begins, I rush to the Chemistry classroom to go find [bai]."
    you "[bai], Happy Birthday!"
    show bai flustered
    bai "Ah, thanks."
    you "I was wondering if you could come to the gym with me afterschool. We can do something afterwards for your birthday."
    bai "Okay, let's meet at the entrance afterschool."
    scene moscrop entrance
    show bai
    you "Ah! I forgot my gym clothes at home today, can you come home with me real quick to grab them?"
    show bai annoyed
    bai "You asked me to go out but you forgot your stuff?"
    you "Ahhh, I'm really really sorry!"
    show bai 
    bai "Ugh fine, let's go."
    stop music fadeout 1.0
    play music "audio/romantic.mp3" fadein 0.5
    hide moscrop entrance 
    scene black 
    bai "Gosh, why is it so dark!"
    you "Hold on, let me turn on the lights..."
    scene black with vpunch
    scene house with Dissolve(0.5)
    you "Surprise!"
    show bai flustered
    bai "W-what is this?"
    you "It's a surprise birthday dinner for you!"
    bai "Oh wow, thanks..."
    you "And there was also something else that I wanted to tell you..."
    you "I like you. Let's date."
    $persistent.bai_end = True
    stop music
    scene black screen
    show text "The End." with Dissolve(3.0)
    hide text "The End." with Dissolve(3.0)
    hide black screen 