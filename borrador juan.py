class colisiones:
    def __init__(self):
        print("colision")
    def check_col(self,target1, target2):
        col_x = False
        col_y = False
        col_ = False
        self.pos1x = target1.hitbox.centerx - target1.hitbox.w/2 
        self.pos2x = target2.rect.left
        self.lenght2 = target2.rect.w
        self.pos1y = target1.hitbox.bottom - 10
        self.pos2y = target2.rect.top
        self.height2 = target2.rect.h
        if self.pos1x > self.pos2x and self.pos1x < self.pos2x + self.lenght2:
            col_x = True
        if self.pos1y > self.pos2y:
            col_y = True
        if col_y and col_x:
            col_ = True
        return col_ 
    def check_distance(self, target1, target2):
        return