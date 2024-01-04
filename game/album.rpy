init python:
    gallery = Gallery() # class?

    gallery.button("Alex H: Ch1")
    gallery.image("cg/calc share.png")
    gallery.condition("persistent.calc_share_scene_unlocked")

    gallery.button("Alex H: Ch2")
    gallery.image("cg/hong hand scene.png")
    gallery.condition("persistent.hong_hand_scene_unlocked")
    #gallery.unlock("hong hand scene.png")
    gallery.button("Alex H: Ch4")
    gallery.image("cg/hong kiss.png")
    gallery.condition("persistent.hong_kiss_scene_unlocked")
    #gallery.unlock("hong kiss.png")
    gallery.button("Alex H: Ch5")
    gallery.image("cg/hong sadwalk.png")
    gallery.condition("persistent.hong_sadwalk_scene_unlocked")
    #gallery.unlock("hong sadwalk.png")
    gallery.button("Alex H: Ch6")
    gallery.image("cg/hong piano.png")
    gallery.condition("persistent.hong_piano_scene_unlocked")
    #gallery.unlock("hong piano.png")
    gallery.button("Alex H: Ch9")
    gallery.image("cg/hong book.png")
    gallery.condition("persistent.hong_book_scene_unlocked")
    #gallery.unlock("hong book.png")
    gallery.button("Alex B")
    gallery.image("cg/black screen.png")
    gallery.button("Lucas")


screen album:
    tag menu
    add "Background/menu bg.png"
    hbox:
    #the pic turns into a button calle "Alex H"
        xalign 0.5
        yalign 0.5
        
        grid 2 3:
            add gallery.make_button(name="Alex H: Ch1", unlocked="cg/small/calc share.png", locked = "cg/small/calc share dark.png")
            add gallery.make_button(name="Alex H: Ch2", unlocked="cg/small/hong hand scene.png", locked = "cg/small/hong hand scene dark.png")
            add gallery.make_button(name="Alex H: Ch4", unlocked="cg/small/hong kiss.png", locked = "cg/small/hong kiss dark.png")
            add gallery.make_button(name="Alex H: Ch5", unlocked="cg/small/hong sadwalk.png", locked = "cg/small/hong sadwalk dark.png")
            add gallery.make_button(name="Alex H: Ch6", unlocked="cg/small/hong piano.png", locked = "cg/small/hong piano dark.png")
            add gallery.make_button(name="Alex H: Ch9", unlocked="cg/small/hong book.png", locked = "cg/small/hong book dark.png")
    
        grid 2 3:
            add gallery.make_button(name="Alex B", unlocked="cg/small/black screen small.png", locked = "cg/small/black screen small.png")
            add gallery.make_button(name="Alex B", unlocked="cg/small/black screen small.png", locked = "cg/small/black screen small.png")
            add gallery.make_button(name="Alex B", unlocked="cg/small/black screen small.png", locked = "cg/small/black screen small.png")
            add gallery.make_button(name="Alex B", unlocked="cg/small/black screen small.png", locked = "cg/small/black screen small.png")
            add gallery.make_button(name="Alex B", unlocked="cg/small/black screen small.png", locked = "cg/small/black screen small.png")
            add gallery.make_button(name="Alex B", unlocked="cg/small/black screen small.png", locked = "cg/small/black screen small.png")
    frame: 
        xpadding 30
        ypadding 30
        yalign 0.1      
        xalign 0.5
        text "{size=*2}{color=#cc0066}Gallery:{/color}{/size}"
         
    frame:
        xpadding 30
        ypadding 30
        xpos 50
        ypos 50
        textbutton "{color=#cc0066}Return{/color}" action Return()
    

    