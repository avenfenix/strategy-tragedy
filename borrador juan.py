def check_distance(self, target1, target2):
    col_= False
    self.h1 = target1.hitbox.h
    self.w1 = target1.hitbox.w
    self.h2 = target2.rect.h
    self.w2 = target2.rect.w
    self.x1 =  target1.hitbox.center[0]
    self.y1 =  target1.hitbox.center[1]
    self.x2 =  target2.rect.center[0]
    self.y2 =  target2.rect.center[1]
    distance = ((self.x1-self.x2)**2 + (self.y1-self.y2)**2)**(1/2)
    max_distance = (((self.h1+self.h2)/2)**2 + ((self.w1+self.w2)/2)**2)**(1/2)
    if (abs(self.x1-self.x2) == (self.w1+self.w2)/2):
        if distance < max_distance:
            col_ = True
    elif (abs(self.y1-self.y2) == (self.w1+self.w2)/2):
        if distance < max_distance:
            col_ = True
    return col_
    #para cualquier objeto
def distance_for_objects(self, target1, target2):
    col_= False
    self.h1 = target1.hitbox.h
    self.w1 = target1.hitbox.w
    self.h2 = target2.rect.h
    self.w2 = target2.rect.w
    self.x1 =  target1.hitbox.center[0]
    self.y1 =  target1.hitbox.center[1]
    self.x2 =  target2.rect.center[0]
    self.y2 =  target2.rect.center[1]
    distance = ((self.x1-self.x2)**2 + (self.y1-self.y2)**2)**(1/2)
    max_distance = (((self.h1+self.h2)/2)**2 + ((self.w1+self.w2)/2)**2)**(1/2)
    if (abs(self.x1-self.x2) == (self.w1+self.w2)/2):
        if distance < max_distance:
            col_ = True
    elif (abs(self.y1-self.y2) == (self.w1+self.w2)/2):
        if distance < max_distance:
            col_ = True

    return "colisiona: " + str(col_)+ " "+str((self.x1, self.y1)) +str((self.x2, self.y2)) + str(distance) +" "+ str(max_distance)
Charac = Personaje(10, 466)
Cuadrado = Platform(100,600,100,100)
crearColision = colisiones()
run = True
while run:
    time = clock.tick(75)
    Charac.teclado()
    gameDisplay.blit(Background_test, (0, 0))
    Cuadrado.draw(gameDisplay)
    check = crearColision.check_distance(Charac,Cuadrado)
    distance = crearColision.distance_for_objects(Charac,Cuadrado)
    print(distance)