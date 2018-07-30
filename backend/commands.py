import json

COCKTAILS = {'margarita':{}, 'negroni':{}, 'elderflower martini':{}, 'whiskey sour':{}, 'thing1':{}, 'thing2':{}, 'thing3':{}, 'thing4':{}, 'thing5':{}, 'thing6':{}, 'thing7':{}, 'thing8':{}, 'thing9':{}, 'thing10':{}}

class Make:
    def __init__(self, cocktail):
        if not isinstance(cocktail, str): raise TypeError('__name__: selection must be a string')
        
        self.cocktail = (cocktail+'.')[:-1]
        
    def print_cocktail(self):
        if self.cocktail in COCKTAILS.keys():
            print(self.cocktail)
                
        

class GenMenu:
    pass


class NewRecipe:
    pass
