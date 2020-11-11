print('''
*******************************************************************************
 .        .
           \'.____.'/
          __'-.  .-'__                         .--.
          '_i:'oo':i_'---...____...----i"""-.-'.-"\\
            /._  _.\       :       /   '._   ;/    ;'-._
           (  o  o  )       '-.__.'       '. '.     '-."
            '-.__.-' _.--.                 '-.:
             : '-'  /     ;   _..--,  /       ;
             :      '-._.-'  ;     ; :       :
              :  `      .'    '-._.' :      /
               \  :    /    ____....--\    :
                '._\  :"""""    '.     !.   :
                 : |: :           'www'| \ '|
                 | || |              : |  | :
                 | || |             .' !  | |
                .' !| |            /__I   | |
               /__I.' !                  .' !
                  /__I                  /__I   fsc
*******************************************************************************
''')
print("Welcome to Cow Island.")
print("Your mission is to find the happy cow.") 

choice1 = input('You landed on a farm. Type "left" or "right" to move\n').lower()
if choice1 == "left":
  choice2 = input('You are in front of the barn door. Type "open" or "wait" to see what happens\n').lower()
  if choice2 == "open":
    choice3 = input('The barn is dark. Type "light" to open the lantern, "run" to exit the barn, or "wait" to stay in the dark\n').lower()
    if choice3 == "light":
      print("Congrats, you found the happy cow!\n")
    elif choice3 =="run":
        print("You fell into a trap outside the barn. Game Over!\n")
    elif choice3 == "wait":
          print ("The haystack absorbed you from the ground. Game Over!\n")
  else:
      print("An angry cow hit you. Game Over!\n")
else:
  print("A swarm of bees stung you. Game Over!\n")
      

        
   
    



  