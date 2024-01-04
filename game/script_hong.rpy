# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

#persistent
"""
$persistent.hong_ch1 = False
$persistent.hong_ch2 = False
$persistent.hong_ch3 = False
$persistent.hong_ch4 = False
$persistent.hong_ch5 = False
$persistent.hong_ch6 = False
$persistent.hong_ch7 = False
$persistent.hong_ch8 = False
$persistent.hong_ch9 = False 
$persistent.hong_end = False
"""

#favorability variable
default hong_fav = 0
default hong_good_end = False
image calc_share = "cg/calc share.png"
image hong_hand_scene = "cg/hong hand scene.png"
image hong_kiss = "cg/hong kiss.png"
image hong_sadwalk = "cg/hong sadwalk.png"
image hong_piano = "cg/hong piano.png"
image hong_book = "cg/hong book.png"

#HONG ROUTE START-----------------------------------------------
label Alex_H_CH1:
    scene black screen
    show text "{color=#cc0066}Chapter 1{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 1{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3"
    scene stats
    show ta at right
    "At this moment, a middle aged man wearing basketball shorts over leggings walks into the class."
    show hong at left
    "[hong] walks over to the middle aged man smiling."
    hong "Teacher A! We have a new student in our AP Stats class. Do you wanna introduce yourself to him?"
    you "{i}Outside of meeting Lucas, this is the first time I’ve seen him smile so brightly.{i}"
    "Teacher A loops his arm around [hong] and walks over to me."
    ta "Oho~ Mr. President, you're with a girl and you’re specially introducing her to me. Is something going on between you two?"
    show hong flustered
    "[hong]" "W-what are you talking about Teacher A? We just met today..."
    

menu hong_ch1_choice:
    "{i}W-what is he talking about? We just met today...{i}":
        "I-it’s like what [hong] said. We just met today and he was told to show me around the school."
        show hong
        "I’m [you] and I’m a new student in your AP Stats class..."
        #$persistent.hong_ch1 = True
        $ hong_fav = hong_fav +1
        $ hong_ch1_correct = True
    "...":
        show hong
        "Teacher A Slaps [hong]’s back and walks away."
        #$persistent.hong_ch1 = True
        $ hong_ch1_neutral = True
    "{i}Let's tease him a bit. {i}":
        scene stats
        show hong
        "Yep! We fell in love at first sight! Isn't that right darling~."
        show hong annoyed
        hong "...Teacher A, it's not like that. She's just joking."
        show ta at left
        show hong annoyed at right
        "Teacher A" "Ahh.. alright."
        scene stats
        show hong annoyed
        hong "Don't make jokes like that in front of him next time."
        #show hong annoyed
        #$persistent.hong_ch1 = True
        $ hong_fav=hong_fav-1
        $ hong_ch1_correct = False

label Alex_H_CH1_p2:
    scene stats
    show hong
    hong "You transferred to TMO High pretty early on so you haven’t missed much in Stats class. But here, you can take a picture of my notes just in case." 
    hong "We just started learning about normal distributions. Teacher A posts these on the AP Stats team so you can check the powerpoints on there."
    "[you]" "Alright, thank you!"
    show hong flustered at left
    show ta at right
    ta "Do you guys want randomized seats today? Actually, let’s not. We should let [hong] and [you] get to know each other better, yknow?"
    hide ta
    show hong flustered at center
    "The whole class turns to look at us."
    show hong sigh
    "From the corner of my eye I saw [hong] sighing as he shook his head, face tilted down with a hand over his mouth."
    stop music fadeout 1.0
    play music "audio/romantic.mp3" fadein 1.0
    scene powerpoint_s1
    show ta
    ta "We ended at calculating z-scores in the last class. Copy the z-score formula down in your notes." 
    ta "We standardize our distributions and our observation x to find the z-score. It helps us find how many standard deviations our observation is from the mean."
    ta "Take out your graphing calculators everyone."
    hide ta
    show hong
    you "[hong]... I don't have a graphing calculator. Can I share with you?"
    #if hong_ch1_correct:
    hong "Mmm sure."
    
    "He pulls out his graphing calculator and leans over towards me so both of us can see."
    hide hong
    show ta
    ta "Press 2nd VARS and select Normalcdf. You can enter your lower bound, upper bound, mean and median to calculate the area under the curve from the lower bound to the upper bound."
    #if not hong_ch1_correct:
    scene powerpoint_s2
    show ta
    ta "Here, calculate these with the person next to you."
    hide ta
    show hong
    hong "Here. 2nd VARS and then normalcdf. You should remember this when you get a graphing calculator."
    scene calc_share
    $persistent.calc_share_scene_unlocked = True
    "I look up, about to ask him what type of graphing calculator I should get. But our eyes accidentally meet each other and our faces are only centimeters. I can feel his breath softly brushing against my lips and the heat creeping up my cheeks."
    "In his eyes I see a reflection of a rose red face, as if I was his whole world. The shock in his eyes is evident as he quickly looks away, apologizing. The few seconds where our eyes were locked felt like forever."
    hong "I-I didn’t know you were so close. Sorry..."
    you "...Ah- It’s fine."
    you "{i}Ahhhh that’s so embarrassing, why is my heart beating so fast?!! I hope he forgets about this soon.{i}"
    ta "OK everyone, first question. Here’s the solution."
    "As Teacher A continued teaching the class, I couldn’t focus at all. The moment where my eyes met [hong]’s kept replaying in my head like a scene from one of my romcoms." 
    "From the occasional glance I dared to peep at him, I could tell that he was flustered too with how he was red from the tip of his ears to the back of his neck."
    scene stats
    stop music fadeout 1.0
    play music "audio/happy bgm.mp3" fadein 1.0
    "Person A" "Teacher A, class is over..."
    show ta
    ta "Oh ok, we’ll continue this next class."
    "Teacher A's words brought me back to reality."
    you "I barely took any notes..."
    "I turn to tap on [hong]’s shoulder."
    hide ta
    show hong
    you "[hong]... can I take a picture of your notes?"
    show hong flustered
    hong "I didn’t take too many notes either... I think we’ll both have to rewatch the in class recording."
    you "Alright. Also, I wanted to ask earlier, what type of graphing calculator should I get?"
    show hong
    hong "I have a Ti-83 but Teacher A says Ti-84’s are better. I have to go to my next class now, I’ll see you around."
    $persistent.hong_ch1 = True
    stop music
    jump Alex_H_CH2

label Alex_H_CH2:
    scene black screen
    show text "{color=#cc0066}Chapter 2{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 2{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3"
    scene hallway
    show shadow_bai
    you "I need a graphing calculator. I’ll ask [bai] to come with me to buy one at Best Buy."
    play sound "audio/phone ringing.mp3" volume 0.5
    ""
    stop sound
    bai "Hello?"
    you "I need a graphing calculator. Can you come with me afterschool?"
    bai "Uhhhh, sure. Let's meet at the front entrance afterschool."
    you "Ok see you later."
    scene moscrop entrance
    show bai
    you "[bai]!"
    bai "Oh you're here. Let's go."
    stop music fadeout 1.0
    play music "audio/shopping bgm.mp3" fadein 1.0
    scene best buy
    show bai
    bai "What type of graphing calculator did you want?"

menu hong_ch2_choice:
    "{i}[hong] said to buy a Ti-84. I should probably listen to him and buy that.{i}":
        "[hong] said Ti-84’s should be good."
        bai "You're choosing it because Kaichou said it's good?"
        $ ti84 = True
        $ hong_fav=hong_fav+1
        jump Alex_H_CH2_p2
    "{i}[hong] said to buy a Ti-84. But he has a Ti-83. I wanna match with him so I’ll buy that too.{i}":
        "[hong] has a Ti-83 so I’ll buy a Ti-83."
        bai "You want to match with Kaichou?"
        $ ti84 = False
        jump Alex_H_CH2_p2

label Alex_H_CH2_p2:
    you "Yes... is there something wrong with that?"
    show bai crazy
    bai "No... there's nothing wrong."
    show bai
    "We grab the graphing calculator and pay."
    bai "It’s pretty late now. How about we go grab a meal at the Metrotown food court."
    you "Should we go to Crystal Mall instead? Don't you like Chinese food more?"
    bai "Uhhh ya... But it's fine because you prefer fast food right?"

menu hong_ch2_choice2:
    "{i}If he’s fine with fast food then we should just go to the Metrotown food court.{i}":
        you "Awwww. You're being so sweet today. Let's go."
        show bai flustered
        bai "W-what are you talking about? I came here with you so I should be doing what you like."
        $ hong_fav += 1
        $ food_court = True
        jump Alex_H_CH2_metro
    "{i}He likes Chinese food. We should go to Crystal Mall.{i}":
        "[you]" "I feel like eating Chinese food today. Let's go to Crystal Mall."
        $ food_court = False
        jump Alex_H_CH2_crystal

label Alex_H_CH2_metro:
    scene metro foodcourt
    show bai
    you "I want to eat fries. I'll go line up."
    hide bai
    "I walk into the lineup for \"New York Fries\" and choose what I want from the menu."
    show shadow_hong
    shadow_hong "[you], you’re here too?"
    stop music fadeout 1.0
    play music "audio/romantic.mp3" fadein 1.0
    hide shadow_hong
    show hong
    "I turn around to see [hong] standing behind me. He suddenly grabs my shoulder and pulls me aside before I have any time to react. Some guy who was behind me walked right past saying \"excuse me\"."
    hong "Be careful, someone was trying to walk by."
    "Somehow I had accidentally walked out of the line when I turned around."
    you "Oh sorry. I didn't notice him."
    hong "Watch where you’re going. What’re you doing in Metrotown?"
    you "I came here to buy a graphing calculator."
    hong "Alone?"
    you "No. I came here with someone else."
    stop music fadeout 1.0
    play music "audio/shopping bgm.mp3" 
    show shadow_bai at left
    show hong at right
    shadow_bai "[you]!"
    "I turn and see [bai] walking over from across the food court and waving at me. Seeing [bai], [hong] looked a little disappointed and shook his head slightly."
    hong "Oh so you came here with him... to buy a graphing calculator for Stats?"
    show hong annoyed
    hong "You could’ve asked me to come with you instead...” He mumbles."
    you "{i}Is it just me or seems a little jealous...{i}" 
    you "Well I don’t have your phone number or anything so I couldn’t ask you anyways..."
    show hong flustered
    hong "I’ll give you my number right now."
    "He takes my phone and adds his number to my contacts just as [bai] walks over."
    show bai at left
    show hong at right
    bai "Oh! Kaichou you’re here as well? What’re you guys mumbling about?"
    hong "It’s nothing."
    you "Have you eaten yet? If not, you can eat with us."
    hong "Alright."
    "I finish ordering, grab my food and follow [bai] to the table where we sit. [hong] follows me like a lost puppy."
    you "{i}I asked him to eat but why didn’t he order food?{i}"
    stop music
    jump Alex_H_CH3_p1

label Alex_H_CH2_crystal:
    scene crystal mall
    show bai
    you "I feel like eating Xiao long bao, so I’ll go line up over there. Let’s meet at that empty table over there when we get our food."
    hide bai
    "I go over to the long line of people waiting to buy Xiao Long Bao, staring intently at the menu."
    show shadow_bai
    shadow_bai "Hey, you’re still in line? I’ve already grabbed my food."
    "I turn around and see [bai] holding his plate of Chow Mein."
    hide shadow_bai
    show bai
    you "Yeah, the lineup is so long. But it works out since I haven’t decided on what to eat yet."
    you "Do you think I should get the Grass Xiao Long Bao? [hong] said it was pretty good."
    stop music fadeout 1.0
    play music "audio/night bgm.mp3" fadein 1.0
    show bai crazy with Dissolve(1.5)
    "[bai]’s face darkens for just a moment before returning to normal."
    show bai
    bai "Sure I guess? I don’t really like Grass Xiao Long Bao though."
    you "Oh really? Then I guess I’ll get a different one."
    show bai crazy with Dissolve(1.5)
    "We walk toward an empty table and sit down. I notice that [bai] seems unusually happy and keeps glancing at me." 
    show bai flustered
    you "{i}Why does he keep looking at me like that?{i}"
    you "Well you seem awfully happy about something. Are you happy to eat Chinese food?"
    show bai
    bai "Haha, it’s nothing its nothing."
    you "Well if you say so... Anyway, do you want to do anything after we eat since we’re here?"
    bai "Hmm... There's nowhere in particular that I want to go. Is there anywhere that you want to go to?"
    you "Well maybe we can visit this one shop, [hong] said he saw the limited edition character keychain I like is sold there."
    show bai crazy
    "[bai]’s face visibly turn into a scowl and he explodes out of nowhere."
    bai "Why do you talk about Kaichou so much? Do you like him or something? I’m the one that’s hanging out with you right now but you keep going \"Kaichou this Kaichou that\". It’s really putting me off you know?!"
    you "{i}Had I really been talking about [hong] that much? But even if I had, isn’t it strange to have this big of a reaction?{i}"
    you "Oh... I’m sorry. I didn’t realize that I had been mentioning him so much. Uhh we can go somewhere else then, I can get the keychain another time."
    show bai annoyed
    bai "Forget it, you’re probably just going to come back with Kaichou another day. If you want to get the character so bad I’ll go with you right now. Let’s go."
    you "No, no you really don’t need to force yourself. [hong] isn’t interested in this kind of stuff, my friend likes this character too so I’ll go with her tomorrow."
    bai "I said, let’s go. We can just get the character now so you won’t have a reason to go with anyone else, much less Kaichou."
    #You’re shaken by the unfamiliar tone that [bai] talked to you in. He’s never spoken to you in such a controlling way, making you suddenly feel unsafe around him. You go along with him to try and calm him down before trying to find an opportunity to slip away. 
    you "S-sure. We can go right now then."
    show bai
    bai "Hey why do you look so uncomfortable, I’m not going to eat you or anything like I do with dogs. I do admit that I went a bit far earlier, but I’m just sad that you seem to only care about Kaichou. C’mon smile for me."
    show bai crazy with Dissolve(0.25)
    hide bai crazy with Dissolve(0.25)
    "His grin sends chills down my spine he asks me to smile. There's something off about [bai]."
    play sound "audio/phone ringing.mp3" volume 0.5
    ""
    stop sound
    "My phone rings just in right time. The call feels like a lifesaver as I pick it up immediately."
    you "Oh hey, Mom! Where am I? I’m at Crystal mall with a friend right now. You want me home right now? Oh, fine, fine, I’ll be home in 10 minutes."
    "I hang up the call and turn to [bai], with a sad expression on the outside while secretly being delighted. I found the perfect excuse to leave."
    you "[bai] I’m so sorry but my mom called just now and said that I had to go home and help her with something. We can hang out another time. I’ll see you in class!"
    bai "Okay, get home safe. See you in class!"
    "[bai] waves and gives his usual smile as I leave, but I can’t help but feel an eerie chill from it."
    $persistent.hong_ch2 = True
    stop music
    jump Alex_H_CH3_p2
        

label Alex_H_CH3_p1:
    scene black screen
    show text "{color=#cc0066}Chapter 3{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 3{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/shopping bgm.mp3" fadein 1.0
    scene metro foodcourt
    show bai at left
    show hong at right
    you "[hong] you didn’t order food?"
    bai "Kaichou doesn’t eat. He’s the emo skeleton of an ancient immortal."
    hong "..."
    hong "I’m just not really hungry right now..."
    bai "Kaichou, why are you at Metrotown?"
    hong "I came here to shop with Lucas to buy games."
    bai "Lucas is here too? Where is he?"
    hong "He left already."
    bai "Oh ok.. I’ll go to the bathroom first."
    you "If he didn’t come here to eat then why is he at the food court?"
    hide bai
    show hong at center
    stop music fadeout 1.0
    play music "audio/romantic.mp3" fadein 1.0
    "I watch as [bai] walks away to the boys bathroom and I turn to [hong] to question him."
    you "[hong], you didn’t come here to eat so why were you at the food court?"
    show hong flustered
    hong "...I was just walking by the food court. A-anyways just keep eating."
    "I could tell he was lying because of his nervous expression and shifting eyes. But I continued eating anyways because it didn’t seem like he’d tell me what he was doing here."
    "All of a sudden I feel a large and warm hand on my cheek. [hong]’s finger brushes against my cheek and my heart speeds up."
    scene hong_hand_scene
    $persistent.hong_hand_scene_unlocked = True
    you "{i}W-what’s he doing?{i}"
    hong "You had something on your cheek."
    
    you "Oh really? T-thank you."
    scene metro foodcourt
    show hong flustered with Pause(1.5)
    "What I didn’t notice was [bai] walking back with a dark look on his face, indicating that he saw everything."
    hide hong
    show bai crazy with Dissolve(2.5)
    hide bai 
    stop music
    
label Alex_H_CH3_p2:
    scene black screen
    if not food_court:
        show text "{color=#cc0066}Chapter 3{/color}" with Dissolve(3.0)
        hide text "{color=#cc0066}Chapter 3{/color}" with Dissolve(3.0)
    show text "A week later in Statistics class..." with Dissolve(3.0)
    hide text "A week later in Statistics class..." with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3"
    scene stats
    show ta
    ta "Do the questions on the board with your partner and use invT to find the solutions. If you don’t have a Ti 84 and you’ve got money then uhhh buy one."
    ta "If not then you’ll have to find a video on designing your own function."

    if ti84:
        hide ta
        you "{i}If I remember correctly, [hong] doesn't have a Ti-84{i}"
        show hong
        you "[hong], I have a Ti-84. Do you want to share with me for now?"
        hong "Alright, let’s share."
        "I hold up the calculator and copy the numbers on the board."
        you "Okay, so we need to find the T-score..."
        show hong flustered
        "[hong] scooches over closer to me, and I could feel my face heating up. I can’t tell if it’s because of his hot breath on my cheeks or because my face has become a blooming rose."
        "But my ears ring and my heart leaps into my throat, leaving me breathless."
        you "..."
        hong "Okay, T-Score equals 1.296?"
        "As he pulls away, I’m once again surrounded by a sharp chill. Even more so than before, because I’ve felt his warmth."
        you "{i}Why was he so close... was that really necessary?{i}"
        "I didn’t like how I had spent more class time filled with thoughts of him than I did of the lesson."

    if not ti84:
        hide ta
        you "{i} I don’t have a Ti 83 but neither does [hong]. That means we both have to code a function onto our calculator... For now I think I’ll have to share with someone else..."
        show anne
        "I look around the room and I see Anne who was randomized to sit to my right. I turn to her and ask her if I can share a calculator with her."
        you "Anne, can we share calculators?"
        anne "Hmm? Ahh ok let’s share."
        "Anne was very good at explaining and my previous confusion with Statistics was resolved."
        hide anne

    "Towards the end of Statistics, Teacher A starts digressing and tells us a story about a movie date incident with his then girlfriend and now wife."
    you "Hmm, a movie..."
    show hong
    "Intrigued by the idea, I look at [hong] beside me, and an idea began to form inside my head."
    "In the heat of the moment I blurt out..."
    $persistent.hong_ch3 = True
    stop music
    jump Alex_H_CH4_p1

label Alex_H_CH4_p1: 
    scene black screen
    show text "{color=#cc0066}Chapter 4{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 4{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3"
    scene stats
    show hong
    you "Do you wanna go watch a movie afrerschool?"
    hong "What movie?"
menu Alex_H_CH4_c1:
    "{i} I want to watch a romance movie. {i}":
        you "How about we watch a romance movie?"
        $ horror = False
    "{i} [hong] likes horror movies and I wanna watch something he likes even if it's scary.":
        you "How about we watch a horror movie?"
        $ horror = True
    
label Alex_H_CH4_p2:
    hong "Sure. Let’s watch it at the Landmark? At New West? They have great seats."
    you "Okay, then it’s a date."
    show hong flustered
    hong "Yeah I guess, we’ll go together after Human Geo then."
    "Afterschool he waited for me to pack things up in class and we left together to go to the movie theaters."
    
    stop music fadeout 1.0
    scene skytrain
    play music "audio/shopping bgm.mp3" fadein 1.0
    p1 "Hey hey, the guy over there is so handsome."
    p2 "Right?? He looks so cool and mysterious, just my type."
    p1 "You should ask for his number."
    you "{i}The girls are whispering so loud. Well he IS good looking so it makes sense. If I can hear them then [hong] can definitely hear them as well.{i}"
    show hong
    "I look up to see [hong]’s reaction but instead I see him looking down and staring at me."
    "Our eyes meet for a second before he quickly averts his gaze guiltily. As if I had just caught a child stealing candy from the cabinet."
    you "{i}Why was he staring at me? Do I have something on my face? Whatever...{i}"
    show hong flustered
    hong "..." 
    scene theatre_hall
    cashier "That’ll be $30 for two tickets."
    you "I’ll pay for it."
    show hong 
    hong "No! It’s fine, I'll pay."
    you "I asked you out to the theaters so I insist on paying."
    hong "Alright..."
    "After getting the tickets, we decide to buy some popcorn and then find our seats inside the theater."
    if not horror:
        jump Alex_H_CH4_Romance
    if horror:
        jump Alex_H_CH4_Horror

label Alex_H_CH4_Romance:
    stop music fadeout 1.0
    play music "audio/romantic.mp3" fadein 1.0
    you "{i}Oh no, maybe I shouldn’t have chosen a romance movie. A boy and a girl watching a romance together is awkward.{i}"
    you "{i}Also I don’t even know if he likes romance movies.{i}"
    you "Are you sure you’re okay with watching a romance movie?"
    hong "Mhm, I already agreed earlier. You don’t want to watch it anymore?"
    you "Nonono, I do I do..."
    "My voice gets quieter as I speak, until it’s eventually a whisper."
    "I think [hong] sensed my hesitation because in the next second he grabs my hand and pulls my body towards his beating heart."
    you "...!"
    "My head rests on his shoulder while he whispers into my ear."
    hong "Let’s go watch the romance movie, okay?"
    scene theatre
    "On the screen, the male lead tenderly held the female lead in his arms as she professed her love for him under the pouring rain."
    "Her head was buried in his shoulders as she cried, overwhelmed by the relief of finally communicating her feelings."
    show hong flustered
    "I feel [hong]’s gaze on me, seemingly wanting to say something to me but hesitating. As I turn to him, he says something."
    hong "[you]... You, what do you think about me?"

menu Alex_H_CH4_Romance_c1:
    "{i}He's really nice!{i}":
        $ hong_fav+=1
        you "I-I think you're a good person..."
        jump Alex_H_CH4_Romance_p2
    "{i}He's skinny.{i}":
        you "You're a dissapearing twig."
        show hong sigh
        hong "..."
        jump Alex_H_CH4_Romance_p2
    "{i}He's goofy.{i}":
        you "You're a goofy dog."
        $ hong_fav-=1
        show hong annoyed
        hong "What are you talking about?"
        you "{i}He didn't get the joke... {i}"
        you "Nevermind..."
        jump Alex_H_CH4_Romance_p2
    
label Alex_H_CH4_Romance_p2:
    "Movie Dialogue" "I love you! I love you so much, please be with me forever!"
    scene theatre
    "I look at the screen and instantly shield my eyes from the montage of the main characters kissing."
    you "Ah... I’m sorry I didn’t know it would get so intense."
    "Embarassed to the point of exploding, I quickly make an excuse to leave."
    you "Sorry, I have to go to the washroom. You don’t have to wait for me."
    stop music fadeout 1.0
    scene theatre_hall
    play music "audio/shopping bgm.mp3" fadein 1.0
    you "{i}Oh my god! That's so embarassing to watch...{i}"
    you "{i}I'm not sure I can continue watching that with him... I should just make an excuse to go home early.{i}"
    show hong with Dissolve(3.0)
    "But before I can give him a text, I see him walk out of the theatre."
    show hong flustered 
    hong "That movie was a bit... much."
    you "I guess you thought so too, I'm never watching a romance ever again."
    hong "Haha yeah, I think it's time to go home. I'll walk you back."
    stop music fadeout 1.0
    scene dark street
    play music "audio/romantic.mp3" fadein 1.0
    show hong
    you "This is my place, you can drop me off here. See you tomorrow!"
    hong "Wait!"
    show hong flustered
    hong "Y-you know, after spending time together with you both in and out of class, I think I li-"
    you "Oh no that’s my dads car! He’s home, I gotta go."
    show hong
    you "{i}Oh no I interrupted him. I hope he wasn’t saying anything too important.{i}"
    "He finally lets go of my hand as my Dads car turns into the driveway."
    hong "Alright then, watching the movie was fun today, let’s go again some other time."
    "He looks a little dissapointed as he watches me walk into my house."
    $persistent.hong_ch4 = True
    stop music
    jump Alex_H_CH5_p1

label Alex_H_CH4_Horror:
    stop music fadeout 1.0
    scene theatre_hall
    play music "audio/suspense.mp3" fadein 1.0
    show hong
    you "{i}Ughhh the movies are starting soon. I don’t know if I’ll survive this movie. I'm kind of scared.{i}"
    hong "Your face looks pale, are you okay?"
    you "I’m fine. I’m just a little nervous about watching a horror movie."
    hong "If you’re not good with horror movies then why did you choose to watch one?"     
    you "Well... you said you like horror movies, so I chose horror."
    show hong sigh
    hong "Alright, if you think it’s too much throughout then tell me."
    you "Ok..."
    "We walk into the movie theater, my stomach churns with anxiety."
    scene black screen
    scene jump_scare with Dissolve(1.0)
    scene black screen
    you "Ah!"
    "I quickly cover my mouth in horror, afraid of both the mutated corpse on screen and of [hong] hearing my scream."
    "Slowly, I feel a warm hand creep over mine and he intertwines our fingers."
    scene theatre
    stop music fadeout 1.0
    show hong flustered
    play music "audio/romantic.mp3" fadein 1.0
    hong "Don’t be scared, I’m right next to you. Focus on me instead."
    show hong_kiss
    "Before I can react, his face is right in front of mine and our lips are touching."
    you "Mmph-"
    hong "..."
    hide hong_kiss
    $persistent.hong_kiss_scene_unlocked= True
    "Unable to react in time, he eventually pulls away from me awkwardly. I can still feel his lingering warmth on my lips."
    show hong flustered
    hong "Sorry..."
    you "..."
    "He doesn't say anything more for the rest of the movie but our fingers are intertwined the whole time."
    "Unable to focus on the movie after that kiss, I think about him for the rest of the film just like he told me to."
    scene theatre_hall
    show hong
    "After the movie, he leads me out, still holding onto my hand."
    hong "How was the rest of the movie?"
    you "It was fine..."
    you "{i}Because I was too busy thinking about you...{i}"
    hong "Mmm, that’s good then. It’s already late out. I’ll bring you home."
    scene dark street
    show hong
    you "We’re almost at my place. You can just drop me off here."
    hong "No, it’s dangerous at night. I’ll bring you all the way back."
    you "{i}He’s kissed me already but he hasn’t even confessed. What are we?{i}"
    show hong flustered
    if food_court:
        hong "Y-you know that day we met at the food court? I wasn’t hungry. I followed you into the food court because I wanted to see you. I li-"
    else:
        hong "Y-you know, after spending time together with you both in and out of class, I think I li-"
    you "Oh no that’s my dads car! He’s home, I gotta go."
    show hong
    you "{i}Oh no I interrupted him. I hope he wasn’t saying anything too important.{i}"
    "He finally lets go of my hand as my Dads car turns into the driveway."
    hong "Alright then, watching the movie was fun today, let’s go again some other time."
    "He looks a little dissapointed as he watches me walk into my house."
    $persistent.hong_ch4 = True
    stop music
    jump Alex_H_CH5_p1

label Alex_H_CH5_p1:
    scene black screen
    show text "{color=#cc0066}Chapter 5" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 5" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3" fadein 1.0
    scene langille
    you "{i}What was last night about? I don’t know if I’ll be able to face [hong] properly today.{i}"
    show hong
    "As I worried, [hong] takes a seat next to me in Calculus."
    hong "Good morning [you]."
    you "{i}He doesn’t sit here normally. Why’s he sitting here today? How am I gonna ignore him today if he sits here?{i}"
    you "Uhh [hong], someone else sits there..."
    hong "Oh... I’ll move..."
    "But instead of moving to another group of tables, he shifts to the seat across from me where no one sits."
    show hong flustered
    hong "Did you sleep well last night?"
    you "Y-yeah."
    hong "Do you wanna go to the library with me afterschool."
    show hong
    you "I’m busy..." 
    you "{i}I’m too nervous to look him in the eye. I think I should stay away from him for the time being or else I’ll die from anxiety.{i}"
    "Seeing that my responses to him were minimal compared to my responses to others, he eventually stops talking to me and instead focuses on the limits worksheet that was handed out."
    scene hallway
    "For the next few days, I continued ignoring him. His text messages became more desperate as I avoided eye contact and any encounters with him."
    stop music fadeout 1.0
    play music "audio/romantic.mp3" fadein 1.0
    scene hong_sadwalk
    $persistent.hong_sadwalk_scene_unlocked = True
    "One day during school, I spot him trudging through the hallways to his next class. His repeated efforts to grab my attention had failed so far, causing him great grief and anguish." 
    "I overheard him talking with his friends, and it was clear my lack of presence was a tough blow to his usual calm and composed demeanor."
    you "{i}I feel so bad for avoiding him. I should’ve talked with him right after, now he thinks it’s all his fault. I should really apologize, and try talking with him again.{i}"
    "I opened my phone to look at my chats with [hong]. \"[you], are you free right now?\" His last sent message still lingered fresh on my screen as I scrolled up to see what he’d sent over the past few days I’ve been ghosting him."
    you "{i}No...This will only make things more awkward. What was that during the movie? Was it an accident... or on purpose!?{i}"
    "My mind whizzes through the countless possibilities in my head. Some possible, mostly improbable."
    you "{i}Could it be... a confess- {i}"
    "I snap myself back to reality. There is no way that could possibly be the reason. We just met each other, we’re mere friends. There’s no way he would fall for someone like me, right...right?"
    you "{i}Argh, I need to think about this more before I talk to him. {i}"
#CHOICE 2: {i} I need to talk to him right now{i}
    scene hallway
    "I carefully scurry through my remaining classes, avoiding him once more. Whenever I catch brief glimpses of him in the hallways, I see his deeply distraught expression, which spoils his otherwise attractive facial features."
    "His fierce eyes were as dark as night and his face unreadable, like he was trying desperately to save someone, yet could only watch as they drifted away from him."
    you "{i}I hope he’ll be alright...{i}"
    "I sigh as I leave the school behind. Another day of the same classes. Another day of meeting the same people..."
    "And another day of meeting him."
    scene sidneys
    stop music fadeout 1.0
    play music "audio/argument.mp3" fadein 0.5
    show bai
    "[bai] seemed to notice my anxiety throughout the past few days. Worried, they asked me about what had happened."
    bai "I think you need to confront him."
    you "Yeah, but that’d be really awkward... Also I’ve ignored [hong] for the past week, I can’t bring myself to face him yet."
    bai "It’s his fault. You should know that. Stop being apologetic over something that wasn’t your fault."
    show bai annoyed
    you "That’s true... but I’ve been ignoring him recently. I haven’t really given him a chance to talk..."
    bai "No, but if he was really apologetic, he would bust down the doors and shout out his apology with a loudspeaker. The reason he’s hesitant is because he DOESN’T MEAN IT."
    you "Alright, alright, lets not go there. I’m sure [hong] does feel guilty about this, and didn’t have bad intentions back then..."
    show bai crazy
    bai "IT DOESN’T MATTER! HE’S SHOWN HE’S WILLING TO TAKE ADVANTAGE OF [you]! IT DOESN’T MATTER IF HE HAS GOOD OR BAD INTENTIONS."
    you "I know [hong] is a good person at heart, and I’m sure he means no harm, but his... his kiss really caught me off guard. I really don’t know how to respond."
    show bai annoyed
    bai "Well, may I get something clear first?"
    bai "Do you like him, perchance?"
    you "{i}I felt my face immediately turn red at the thought. Flustered and caught off guard, I stuttered.{i}"
    you "Well...I..."
    bai "C’mon, spit it out. We don’t got all day."
    
menu ending_c1:
    "I... guess I do like him...":
        $ hong_fav+=1
        $ neutral_end = False
        jump Alex_H_CH5_p2
    "I hate men. The kiss was disgusting. Bloody patriarchy.":
        $ neutral_end = True
        jump hong_neutral

label Alex_H_CH5_p2:
    show bai
    bai "More than a friend?"
    you "Yeah... I do like [hong] in a romantic way."
    you "I should clear up any misunderstandings. I was taken aback by him last time, but I want to talk to him, and get to know his true intentions."
    hide bai
    show shadow_hong
    shadow_hong "[you]!"
    hide shadow_hong
    show hong
    "A voice calls you from a distance. As I turn back, I spot a small figure running towards you. As the figure grows bigger, I notice the distinct features of one I’d fallen in love with." 
    show hong at left
    show bai annoyed at right
    bai "Oh for fricks sake!"
    hong "[you]! I’ve been so worried about you! You haven’t replied to my texts and you have been ignoring me whenever I try talking to you. Are you okay?"
    stop music fadeout 1.0
    scene sidneys
    play music "audio/romantic.mp3" fadein 1.0
    show hong
    "His genuine concern for me only makes me more ashamed of myself."
    you "{i}Why didn’t I just listen to him? Now I made him worry.{i}"
    "Too afraid to meet his gaze, I could only stare down at the cold, dark ground, not saying a word. It felt like hours before he finally broke the awkward silence."
    hong "[you]... sorry about the incident."
    you "It’s fine, don’t worry about it."
    hong "Do you... hate me?"
    you "I... I don’t."
    "An uncomfortable silence ensues. I gathered the courage to look up, and was instantly met with [hong]’s pleading gaze."
    show hong flustered
    you "I think... you’re really cool, sweet, and smart."
    "I’ve never actually fallen for someone before and I felt my head get hotter and hotter with each passing second."
    you "But since, you know, the, uh-{i}incident{i}-my thoughts have been such a mess. I haven’t known you for long, but when I see you—my heart beats so fast."
    show hong
    "Upon realizing what I just said, I immediately shut my mouth, praying that he didn’t hear. As I feared, [hong]’s uneasiness had vanished, and what remained was a small, satisfied smile."
    hong "So... will you follow me? I have something I want to show you."
    "Following his request, I noticed his face reverting back to an unreadable expression. While I spotted hints of nervousness, there was also an uncharacteristic desire within him that made his request hard to pass on."
    you "Sure, I'll follow you."
    window hide
    scene black screen with Pause(1.5)
    $persistent.hong_ch5 = True

label hong_neutral:
    if not neutral_end:
        jump Alex_H_ch6_p1
    scene sidneys
    show bai crazy
    bai "Exactly! You should hate him!"
    bai "Kaichou acts like he’s good at everything but in fact he’s just a socially impaired human shell with no heart."
    bai "You shouldn’t bother with him anymore or else he’ll just cause you more grief."
    you "{i}He looks psychotic... I thought he was on good terms with [hong]...{i}"
    hide bai
    "Listening to [bai], I decided to just leave things be and end my relationship with [hong]."
    scene black screen
    "A few days later there was an email sent to every student's family. It said that [hong] had committed suicide from jumping off the school building."
    "The reason as to why he jumped was unknown."
    "The whole school mourned the loss of him and I couldn't help but wonder whether part of his death was because of me."
    hide black screen with Dissolve(2.0)
    show text "The End... or is it?" with Dissolve(1.0)
    hide text "The End... or is it?" with Dissolve(1.0)
    hide black screen with Pause(2.0)
    stop music
    $persistent.hong_ch6 = False
    $persistent.hong_ch7 = False
    $persistent.hong_ch8 = False
    $persistent.hong_ch9 = False
    $persistent.hong_end = True
    return

label Alex_H_ch6_p1:
    scene black screen
    show text "{color=#cc0066}Chapter 6{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 6{/color}" with Dissolve(3.0)
    hide black screen
    scene music room
    window show
    show hong 
    "[hong] took me to the music room, where our presence was shared by only a single piano in all its glory, amidst a cold, lonely space. [hong] sat down in front of the piano, then beckoned me to sit beside him."
    "Without any further delay, he started playing. Years of hard work has made him masterful of the skill, as his fingers moved tenderly along the tiles of the piano, producing a majestic, rhythm."
    you "Wow..."
    "His hands gently caresses the keyboard, producing a soothing tone rivaling that of a nightingale’s, and entrancing those fortunate enough to witness it. Without another thought, I inch closer to him."
    "As he plays, the experiences shared between us dance in my mind. Although the time spent together has been short, it has been filled with such wonderful memories." 
    "He has been the center of helping me adapt and transition to this new environment."
    "Looking back at him, he has maintained his cool composure and is still very concentrated in his playing."
    you "After all, it’s this air of calmness and charming charisma that attracts others like a magnet."
    "And thats why I don’t want to lose him."
    scene hong_piano
    $persistent.hong_piano_scene_unlocked = True
    "Without second thoughts I lean my head against him and hold him tightly while doing so. [hong], though surprised at first, quickly regains his concentration as he continues into the ending stretches of his masterpiece."
    "As the song nears its end, I rise from my seat, and whisper in his ear."
    you "I love you."
    "[hong] plays the final notes of the song, and instantly an air of silence surrounds us once more."
    "Before I could comment on his playing, he leaned in and kissed me. Although surprised by his boldness, I close my eyes and fully embrace him."
    "The few seconds of ecstasy seem to last a lifetime, as we were alone in an empty room, sharing our moment. After a while, [hong] departs his lips and grabs my shoulders, forcing me to stare into his jet black eyes."
    hong "[you], I love you too."
    scene music room
    show hong flustered
    "A flurry of emotions floods through me, and I find myself at a loss for words."
    "He looks at me and I look back at him. Not knowing what to do next, he grins at me."
    stop music
    play sound "audio/phone buzz.mp3" loop
    "What seemed like eternity was interrupted by a quiet but noticeable beep coming from his phone."
    play music "audio/argument.mp3"
    show hong
    hong "Someone texted me."
    "He reaches across to grab his phone. After opening up the message, I notice his face growing increasingly pale."
    
    stop sound
    hong "Sorry [you] something just came up. I’ll see you later."
    "Just like that, [hong]astily walked over to the door and left the room, leaving me alone in my vivid fantasies."
    you "I hope he’s all right."
    window hide
    stop music
    $persistent.hong_ch6 = True

label Alex_H_CH7:
    scene black screen
    show text "{color=#cc0066}Chapter 7{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 7{/color}" with Dissolve(3.0)
    hide black screen
    play music "audio/happy bgm.mp3"
    scene house
    window show
    "The next morning I wake up as normal, albeit a bit flustered from yesterday"
    you "Wait so... the kiss. He actually likes me?"
    "And like that, my mind went into turmoil."
    you "Wait so that first kiss at the movies...did he like me then? Or was I delusional? Does this mean he fell in love with me before I did? OMG so many questions I gotta ask him now!"
    "I grab my phone and begin texting him, hoping to get a response as soon as possible. When satisfied with my text message, I press the SEND button."
    you "Oh c’mon you’re like a dinosaur, respond already!!!"
    "Hoping to make time pass faster, I begin rolling around on the bed, anxiously yet excitedly waiting for his response."
    "After an hour, that response never came, and I was there, lying on my bed like an idiot."
    you "Man that guy replies slow... maybe he didn’t notice? If I send him a more heartfelt message, would he respond?"
    you "I wonder if he’s as flustered as me... what if he’s thinking about what to say? Maybe I’ll remind hi-"
    stop music
    play sound "audio/phone ringing.mp3"
    "My thought digression was abruptly interrupted by a phone call from an unknown caller. I answered the call."
    play music "audio/argument.mp3" fadein 1.0
    stop sound
    you "Hello?"
    show shadow_bai
    shadow_bai "Hey is this [you]?"
    "A filtered voice sounds from inside the phone."
    you "Yes... why?"
    shadow_bai "Your beloved kaichou is about to die."
    you "Huh?"
    shadow_bai "Go to Moscrop."
    hide shadow_bai
    play sound "audio/hang up.mp3" volume 0.5
    "The unknown caller hangs up leaving my mind a mess."
    stop sound
    you "{i}Did something bad happen to Alex?{i}"
    "At that thought, I slam the phone down and run out the front door."
    scene moscrop entrance
    show shadow_lucas
    "When I get there, all seems calm. However, I notice someone running towards me. It was [lucas]."
    hide shadow_lucas
    show lucas
    you "{i}Why would [lucas] be at school on a Saturday morning? Isn’t he usually slumbering until 3pm?{i}"
    "[lucas] arrived in front of me, took a few moments to catch his breath."
    lucas "[you]! Thank goodness you’re here! [hong] needs you right now! He told me he's going to jump this morning. You’re his only hope!"
    you "Oh okay, where is he?"
    show lucas sigh
    lucas "On the top of the building."
    you "Oh no!"
    scene stairs
    "I instinctively run up the flight of stairs to the third floor. Although new to the school, I recall [hong] telling me about a secret passage to the top of the school. It should be... here!"
    "I find the ladder in the janitor’s room that leads to a trapdoor opening to the roof of the building. Urgently yet carefully, I climbed up the wooden steps of the ladder."
    scene roof
    stop music fadeout 1.0
    play music "audio/night bgm.mp3" fadein 0.5
    show shadow_hong
    "The opened trapdoor, revealed the clear blue sky, as well as the silhouette of a familiar person near the edge."
    you "[hong]!? [hong]!? IS THAT YOU?"
    hide shadow_hong
    show hong crazy
    "[hong] looks back at me, half surprised yet half relieved. His long, disheveled hair covered his face, and his heart appeared to be distant."
    hong "[you]! You’re here! You’re just about to witness the climax! I’m so glad you have a front seat to my epic conclusion!"
    you "[hong]! Don’t do it! What happened!?"
    hong "Why? Oh that’s not important anymore? Now that you’re here, why don’t you take a seat! I was afraid I was going to start the show without you!"
    "I slowly make my way towards him, step by step to try and distract him."
    you "Come back to us! We can talk this out!"
    "I continue to make progress towards him, the distance between us now halved. [hong], however, didn’t seem to reconsider."
    hong "Sorry, I didn’t come up here just for you to talk me out of this today."
    show hong
    "He then lowers his tone and his lashes droop."
    hong "I also apologize for what I’ve done with you in the past few weeks. I shouldn’t have spent so much time with you. Now, because of my selfish actions, you’re going to suffer once I’m gone."
    you "Then don’t go! Come back to me! I’ll help you with whatever you need! Don’t leave us! Don’t leave me!"
    "Now within arms reach of [hong], I try to grab him. However, I'm one step behind. He had completely tuned and was now one step over the edge."
    hong "Alas, I can finally rest in peace."
    "Summoning all my strength I desperately charge forward and grab [hong]. He regains his balance on the roof, and turns to face me."
    you "Please don’t go! I don’t think I can live without you! Stay with me!"
    if hong_fav <2:
        show hong flustered
        hong "So, you can’t live without me?"
        you "Uh huh." 
        "I nod desperately, pleading for him to listen to me." 
        show hong crazy
        hong "Alright. Commit double suicide with me."
        "I was shocked by his proposal."
        "Bewildered by his suggestion, I stood in front of him motionless. However, he grabs my arm a drags me to the edge with him."
        "I tried to resist my doom, yet was powerless to stop him."
        you "{i}When did [hong] get this strength?!{i}"
        "Looking over the edge of the roof, I see the cold, hard concrete ground below us."
        hong "Alright, see you on the other side."
        "I knew what was going to happen, but as if hypnotized, I did not run away."
        "With a hard shove from behind, I found my body falling forward and I was subjected to freefall."
        "The concrete ground was fast approaching, yet I could do nothing to stop it."
        scene black screen with vpunch
        play sound "audio/splat.mp3"
        "A loud splat was heard around the schoolyard. People who ran over to survey the noise were greeted by two piles of mutated flesh."
        stop sound
        "In the distance [bai] was seem grinning maniacally, seemlingly enjoying the show." 
        stop music
        $persistent.hong_ch7 = True
        $persistent.hong_ch8 = False
        $persistent.hong_ch9 = False
        $persistent.hong_end = True
        return 

    if hong_fav >=2:
        show hong
        "My words seemed to strike him because he was off guard."
        "While he's distracted, I quickly pull him away from the edge to a safer location on the roof."
        "Tears begin streaming down his face as soon as I set him down. It seems the realization finally hits him."
        hong "Sorry [you], I..."
        you "Don’t talk yet. Calm yourself first, and get yourself to a better location. Then, you are obligated to tell me all about what happened."
        hong "Ok..."
        scene elevator
        show hong
        "We leave the rooftop and arrive at the third floor elevator. [hong] takes a seat on the wooden benches."
        "After the crying halted, he finally looks up and his eyes are filled with sadness and anguish."
        you "So, what caused you so much grief that you were going to ascend purgatory?"
        hong "Alright, I’ll talk a bit about myself then..."
        stop music
        $persistent.hong_ch7 = True
        jump Alex_H_CH8

label Alex_H_CH8:
    scene black screen
    show text "Chpater 8: \nRevelation." with Dissolve(3.0)
    hide text "Chpater 8: \nRevelation." with Dissolve(3.0)
    hide black screen
    play music "audio/romantic.mp3"
    scene elevator
    show hong
    hong "My parents were always strict with me and often compared me to my cousin. They trained me as a child in order to be someone successful in the future."
    hide hong
    scene house
    stop music fadeout 1.0
    play music "audio/argument.mp3"
    show young_hong at left
    show hong_mom at right
    young_hong "Mother, may I go outside and play with my friends?"
    hong_mom "No, stay inside and finish your assigned work. Then read “The Outsiders.” After that you must practice piano for another hour."
    hong_mom "Get to it right now!"
    young_hong "Yes, mother."
    scene black screen with Dissolve(1.5)
    scene house
    show hong at left
    show hong_dad at right
    hong_dad "[hong]! What did you get on your recent Math test?"
    hong "I got a 98, father."
    hong_dad "WHY NOT GET 100? WHAT HAPPENED TO THE EXTRA 2 PERCENT? YOU ATE IT DIDN’T YOU! THAT’S WHY YOU'RE SO FAT AND USELESS!)" 
    hong_dad "THAT’S IT, I’M ENROLLING YOU IN K*****!"
    hong "Yes father..."
    hong "{i} I really need to impress my parents, and lose some weight. {i}"
    scene black screen with Dissolve(1.5)
    scene house
    show hong at left
    show hong_mom at right
    hong_mom "[hong]! Why are you so useless! Why can’t you be like your cousin Timmy?"
    hong_mom "He got school highest score, valedictorian AND got into the best pre-med program in the country!"
    hong_mom "What are you? Co-President of the what? Pop Can Recycling Club? Why can’t you be as smart as your cousin? If I knew you would be a failure I would’ve swallowed you back then!"
    hong "Yes, Mother."
    hong_mom "Here, here’s a mirror."
    hong "Okay...why?"
    hong_mom "So you can see how DUMB you look. Go back to your room!"
    window hide
    scene black screen with Dissolve(1.5)
    stop music fadeout 1.0
    play music "audio/romantic.mp3"
    scene elevator
    show hong
    window show
    hong "And thus, my parents raised me to be a Stakhanovite worker relating to academics." 
    hong "That treatment has boosted my grades, but as you can see, made me a failure at everything else."
    you "Don’t call yourself that, you’re not a failure."
    show hong sigh with Dissolve(1.5)
    
    hong "So, prior to my last Calculus test, my parents had gotten quite enough of me, and were on the verge of sending me away to my grandparents back in Korea."
    show hong
    hong "The education system there’s drastically different, and I’d need to go a few grades back to integrate into their school programs, for even a chance to do well on CSAT."
    hong "Of course, I want to stay here. So I told them that if I can get above 95 on my next Calculus exam, I'll be able to stay here and they'll loosen their control over my life."
    hong "If not, I would have to go back and suffer in Korea."
    you "And, from your actions, I’m assuming you didn’t do well?"
    hong"Not even, I got an 82. Not even an A, not even a PASS in my parents’ eyes. When they asked me, I couldn’t lie, they know everything. I told them about my 82."
    you "And they told you to leave?"
    hong "They revealed they knew I would fail, and had prepared a flight beforehand. It is supposed to leave tomorrow night. I didn’t want to go, so I..."
    "[hong] stopped his words, as tears began to well inside his eyes once more."
    you "So you decided that stepping off the edge of the earth was your best solution?"
    hong "Yeah..."
    "An awkward silence gathers between us once more, as I decided not to say what I really wanted to say."
    hong "This morning they were reluctant to let me leave. I told them I would be out buying some souvenirs for my grandparents and they finally let me go. I don’t ever want to go back to Korea." 
    "I slowly pull [hong] into an embrace while patting his head as he slowly breaks down in tears."
    you "{i}Poor guy, having that much pressure mounted on you and being compared to your successful cousin eventually WILL take a toll on someone. I’m just glad I stopped him before he went too far.{i}"
    you "So, if it’s alright with me asking, how do you want to proceed from here on?"
    "[hong] slowly looks up at me with a confused expression."
    you "Do you want to run away from home? Or do you want to confront your parents and ask them to give you another chance?"
    hong "..."
    you "Think carefully, this decision will impact our actions and future drastically."
    "After a long pause, [hong] finally reaches an answer, and nods."
    hong "As fun as running away might sound, I want to live a normal high school teenage life. I’m not ready to live by myself, on the run yet."
    you "Okay, so you want to convince your parents to give you another chance. Any ideas for that yet?"
    hong "No, not yet. I really don’t know. What if I do as bad on the second test?"
    you "Don’t worry, now that I know your situation, I’ll help you study Calculus. Back in my old school I was the top math student, and won all sorts of competitions!"
    hong "Are you sure? I’ve heard others from the school talk about how you were struggling in this and that."
    you "Look, do lions ever concern themselves with the opinions of sheep? Do they? Of course not. So do you want my help or not?"
    "With a menacing gaze, I stare at [hong]. He seems both surprised, frightened, and excited at the same time. I reach my hand out, waiting for him to accept it."
    "[hong] looks down at my outstretched hand, then up at me. After a while, he looks back at me, then firmly shakes my hand."
    you "Good choice. Now it’s time to get you to 100."
    window hide
    $persistent.hong_ch8 = True
    stop music
    jump Alex_H_CH9

label Alex_H_CH9:
    scene black screen
    show text "{color=#cc0066}Chapter 9{/color}" with Dissolve(3.0)
    hide text "{color=#cc0066}Chapter 9{/color}" with Dissolve(3.0)
    show text "A few days later at school..." with Dissolve(3.0)
    hide text "A few days later at school..." with Dissolve(3.0)
    hide black screen
    window show
    play music "audio/happy bgm.mp3"
    scene hallway
    show hong flustered
    hong "Um... about the other day. Thanks for saving me."
    you "Don’t worry about it, what’s up?"
    show hong
    hong "They decided to give me one more chance, but this time they raised the bar."
    you "So you’re telling me..."
    hong "Yes, I must get 100 on my next calculus test. No exceptions"
    you "Well, guess I’ll make sure you get 110 then."
    hong "Please do."
    hide hong
    show hong_book
    $persistent.hong_book_scene_unlocked = True
    "I enter the library carrying 2 calculus workbooks and stack it on top of the 2 I already have on the table."
    #show hong sigh with Dissolve(1.5)
    "[hong] looks at me in disbelief."
    hong "..."
    scene library
    show hong sigh
    you "Unless you want to be deported back to Korea you better stay studying!"
    hong "Damn, aren’t you so harsh."
    you "I’m being realistic here. When’s your test?"
    hong "Next Friday, it’s on Derivatives."
    you "Alright then, by next Friday I’ll train you until you can solve every related rates problem in the textbook blindfolded."
    "[hong] chuckles ats me and continues his work."
    you "So you want to study this first..."
    scene langille
    "At last, the day of the dreaded test arrives. I walk with [hong] to the math classroom, where he, for the millionth time, checked for his graphing calculator." 
    "This was it, his lifesaver, the test that will determine his future."
    show hong
    hong "Well [you], I’m going to go in now. Wish me luck!"
    you "Good luck! You’ve got this! Don’t forget what you’re fighting for!"
    "I watch [hong] walk into the math classroom, in preparation of his test. As I begin heading back, I hear him call me back."
    you "Do you need anything?"
    show hong flustered
    "[hong] comes up to me and embraces me in a tight hug."
    hong "Thank you so much."
    you "Don’t mention it, once you ace this test you’re paying for my therapist bills though!"
    hong "Hahaha, you’re so funny. I’m off then!"
    you "I’ll be in the library waiting for the good news!"
    "I watch him disappear inside the classroom, and I slowly make my way to the library, praying for [hong]'s freedom from mundane matters."
    scene library
    "After a long, brutal ninety minutes of waiting, he finally finished the test. I greet him as he entered the library."
    show hong
    you "How’d it go?"
    hong "I think it went decent, I solved every question with ease, and triple checked each answer. It’s all up to the heavens to decide now."
    scene langille
    stop music fadeout 1.0
    play music "audio/romantic.mp3" fadein 0.5
    "We had found out from a classmate that test marks were out, and were now extremely anxious for the results." 
    "The question remains: upon reading the test mark, will we be greeted by salvation or tragedy?"
    show hong
    hong "Well, we’re here."
    "[hong] walks in to his math classroom while I patiently wait. Inside, I can hear some chatter, but can make nothing of it. After a few minutes, [hong] walks out with an unreadable expression."
    you "So, how was it?"
    "[hong] lifted up his test paper and shows me his test. At the top of the page in red and bold was a perfect score of 100!"
    you "LET’S GO! YOU’RE NOT GETTING DEPORTED!"
    hong "I know! After getting the news, I immediately notified my parents. I don’t need to go back and they say they’ll give me more freedom over my life!"
    you "CONGRATS!"
    "I open my arms for an embrace, but [hong] had other ideas. Swiftly, he leaned his head over and kissed me. This time, it was surely no mistake, or accident, but an act of love."
    hong "So... how much do I owe you for that therapist?"
    you "You owe me the rest of your life."
    window hide
    $persistent.hong_ch9 = True
    $persistent.hong_end = True
    $ hong_good_end = True
    scene black screen
    show text ("The End... \nYou have unlocked the special chapter") with Dissolve(3.0)
    hide text ("The End... \nYou have unlocked the special chapter") with Dissolve(3.0)
    hide black screen
    stop music
    return



