
#import chapter_select_screen is not nessecary for renpy
screen choose_route:
    #$persistent.chose_lucas = False
    #$persistent.chose_hong = False
    #$persistent.chose_bai = False
    #cant be clicked unless chose_route=True
    #once chose_route=True the route of the chosen character is turned on, other routes are locked
    #can only select that one route until the ending for one route is completed ($ completed1 = True)
    #once route is completed you can choose the other routes
    tag menu
    #add "imagebutton/lucas dark.png" xpos 0.0 ypos 0.0
    add "Background/menu bg.png"
    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.02
        text "{size=*3}{color=#cc0066}Choose your route:{/color}{/size}"
        
    
    #if renpy.get_screen("choose_route"):
            #textbutton _("Select Route") action ShowMenu("choose_route")
    if (persistent.chose_lucas and (persistent.hong_end or persistent.bai_end)) or (persistent.chose_lucas and (not persistent.chose_hong and not persistent.chose_bai)):
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.17
            ypos 0.5
            idle "imagebutton/lucas_idle.png"
            hover "imagebutton/hover/lucas_hover.png"
            #auto "lucas_%s.png"
            action ShowMenu("chapter_select_lucas")
        
    else:
        add "imagebutton/shadow_lucas.png":
            xanchor 0.5 yanchor 0.5 xpos 0.17 ypos 0.5


    if (persistent.chose_hong and (persistent.lucas_end or persistent.bai_end)) or (persistent.chose_hong and (not persistent.chose_bai and not persistent.chose_lucas)):
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
            idle "imagebutton/hong_idle.png"
            hover "imagebutton/hover/hong_hover.png"
            action ShowMenu("hong_char_info")
       
    else:
        add "imagebutton/hong dark.png":
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    
    if (persistent.chose_bai and (persistent.hong_end or persistent.lucas_end)) or (persistent.chose_bai and (not persistent.chose_hong and not persistent.chose_lucas)):
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.85
            ypos 0.5
            idle "imagebutton/bai_idle.png"
            hover "imagebutton/hover/bai_hover.png"
            #auto "bai_%s.png"
            action ShowMenu("bai_char_info")
    else:
        add "imagebutton/bai dark.png":
            xanchor 0.5 yanchor 0.5 xpos 0.85 ypos 0.5
    frame:
        xpadding 30
        ypadding 30
        xpos 50
        ypos 50
        textbutton "{color=#cc0066}Return{/color}" action Return()