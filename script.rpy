define e = Character("Kat", color = "#9E355B")
define b = Character("Leo", color = "#C65930")

label start:

    scene bg park 

    show girl normal standing at center

    e "Man, I'm starting to feel really bored here."

    e "I guess I'm going after Leo, maybe he'll play with me"
    
    menu: #first choice Menu 
        
            "I shouldn't disturb him today":
                e "Nah, I'll just stay here."
                return
            "Why not?":
                
                  hide girl normal standing
                  show girl standing excited at center
                  
                  e "Maybe if i go to the school rooftop I'll find him"
                  
                  jump meet     #jumping to the label after deciding to meet Leo
                  
        
    label meet: #label with consequences for the first choice
       
       play music bgMusictest fadein 1.0 fadeout 1.0
       queue music bgOther
       scene bg rooftop 
               
       hide girl standing excited
       show girl normal standing at left
       show boy normal standing at right     
       with dissolve
       with Pause(0.1)
        
       e "Hello Leo"   
       b "Hello Kat"
       

    # This ends the game.

    return
