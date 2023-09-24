# A constructor
# If it has the self keyword, it is a method that i a part of a class
# Color is the parameter of the constructor
class Cookie:
    def __init__(self, color):
        self.color = color
    
    #getter
    def get_color(self):
        return self.get_color
    
    #setter
    def set_color(self, color):
        self.color = color

cookie_one = Cookie('Green')
cookie_two = Cookie('Blue')

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())