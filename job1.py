def draw_rectangle(width,height):
    if width==0 or height==0:
        print("Il faut choisir une valeur positive!")
        return
    print("|"+"-"*(width-2)+"|")
    for _ in range(height-2):
        print("|"+" "*(width-2)+"|")
    if height>1:
        print("|"+"-"*(width-2)+"|")

draw_rectangle(10,6)