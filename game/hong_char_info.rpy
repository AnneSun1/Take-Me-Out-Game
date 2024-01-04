screen hong_char_info:
    tag menu
    add "Background/menu bg.png"
    add "Sprites/hong.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.17 
        ypos 0.5
    frame:
        xpadding 30
        ypadding 30
        xpos 50
        ypos 50
        textbutton "{color=#cc0066}Return{/color}" action Return()
    
    frame:
        hbox:
            yalign 0.75
            xalign 0.5
            
