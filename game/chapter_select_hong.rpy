screen chapter_select_hong:
    #scene menu bg.png
    tag menu
    add "Background/menu bg.png"
    frame:
        xpadding 30
        ypadding 30
        yalign 0.1
        xalign 0.5
        text "{size=*2}{color=#cc0066}Alex H Chapter Select:{/color}{/size}"

    frame: 
        xpadding 30
        ypadding 30
        xpos 50
        ypos 50
        textbutton "{color=#cc0066}Return{/color}" action Return()

    hbox:
        yalign 0.5
        xalign 0.5
        grid 1 9:
            frame:
                textbutton "{color=#cc0066}Chapter 1{/color}" action ShowMenu("Alex_H_CH1")
            frame:
                textbutton "{color=#cc0066}Chapter 2{/color}" action ShowMenu("Alex_H_CH2")
            frame:
                textbutton "{color=#cc0066}Chapter 3{/color}" action ShowMenu("Alex_H_CH3_p1")
            frame:
                textbutton "{color=#cc0066}Chapter 4{/color}" action ShowMenu("Alex_H_CH4")
            frame:
                textbutton "{color=#cc0066}Chapter 5{/color}" action ShowMenu("Alex_H_CH5_p1")
            frame:
                textbutton "{color=#cc0066}Chapter 6{/color}" action ShowMenu("Alex_H_ch6_p1")
            frame: 
                textbutton "{color=#cc0066}Chapter 7{/color}" action ShowMenu("Alex_H_CH7")
            frame:
                textbutton "{color=#cc0066}Chapter 8{/color}" action ShowMenu("Alex_H_CH8")
            frame:
                textbutton "{color=#cc0066}Chapter 9{/color}" action ShowMenu("Alex_H_CH9")


        
        
"""
    menu choose:
        "Chapter 1":
            if persistent.hong_ch1:
                jump Alex_H_CH1
            else:
                jump locked
        "Chapter 2":
            if persistent.hong_ch2:
                jump Alex_H_CH2
            else:
                jump locked
        "Chapter 3":
            if persistent.hong_ch3:
                jump Alex_H_CH3_p1
            else:
                jump locked
        "Chapter 4":
            if persistent.hong_ch4:
                jump Alex_H_CH4
            else:
                jump locked
        "Chapter 5":
            if persistent.hong_ch5:
                jump Alex_H_CH5_p1
            else:
                jump locked
        "Chapter 6":
            if persistent.hong_ch5:
                jump Alex_H_ch6_p1
            else:
                jump locked
        "Chapter 7":
            if persistent.hong_ch7:
                jump Alex_H_CH7
            else:
                jump locked
        "Chapter 8":
            if persistent.hong_ch8:
                jump Alex_H_CH8
            else:
                jump locked
        "Chapter 9":
            if persistent.hong_ch9:
                jump Alex_H_CH9
            else:
                jump locked 
    return
"""
"""
#label locked:
#    show text "{color=#cc0066}This Chapter is Locked. Please complete it first.{/color}"

screen chapter_select:
    #if renpy.get_screen("choose_route"):
    text "{size=*5}{color=#cc0066}Gallery:{/color}{/size}"
    vbox: 
        xpos 0.5
        ypos 0.5
        textbutton "{color=#cc0066}Chapter 1: The Chance Encounter{/color}":
            action If(persistent.hong_ch1, Jump("Alex_H_CH1"), NullAction())
        textbutton "{color=#cc0066}Chapter 2: The First Rendezvous{/color}":
            action If(persistent.hong_ch2, Jump("Alex_H_CH2"), NullAction())
        textbutton "{color=#cc0066}Chapter 3: The Soul That Took a Detour{/color}":
            action If(persistent.hong_ch3, Jump("Alex_H_CH3"), NullAction())
        textbutton "{color=#cc0066}Chapter 4: A Candle in the Dark{/color}":
            action If(persistent.hong_ch4, Jump("Alex_H_CH4"), NullAction())
        textbutton "{color=#cc0066}Chapter 5: The First Kiss Never Ends{/color}":
            action If(persistent.hong_ch5, Jump("Alex_H_CH1"), NullAction())
        textbutton "{color=#cc0066}Chapter 6: The Wonders of the World{/color}":
            action If(persistent.hong_ch6, Jump("Alex_H_CH1"), NullAction())
        textbutton "{color=#cc0066}Chapter 7: The Spark and the Flames{/color}":
            action If(persistent.hong_ch7, Jump("Alex_H_CH1"), NullAction())
        textbutton "{color=#cc0066}Chapter 8: Revelation{/color}":
            action If(persistent.hong_ch8, Jump("Alex_H_CH1"), NullAction())
        textbutton "{color=#cc0066}Chapter 9: Sunset{/color}":
            action If(persistent.hong_ch9, Jump("Alex_H_CH1"), NullAction())

return
"""