from model import Model, DecodeError
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        try:
            self.model = Model('recipe.txt')
        except DecodeError as e:
            self.view.throw_an_error(e)

    def run(self):
        query = None
        while query != '5':
            query = self.view.wait_user_answer()
            self.resolve_user_answer(query)

    def resolve_user_answer(self, query):
        if query == '1':
            recipe_data = self.view.get_new_recipe_data()
            self.model.add_new_recipe(recipe_data)
        elif query == '2':
            recipe = self.model.recipe
            self.view.show_recipe(recipe)
        elif query == '3':
            key_words = self.view.get_keywords_to_find_recipe()
            recipe = self.model.find_recipe(key_words)
            self.view.show_recipe(recipe)
        elif query == '4':
            recipe_name = self.view.get_recipe_name()
            recipe = self.model.find_recipe(recipe_name)
            result = self.model.delete_recipe(recipe)
            if result == 'Слишком много статей!':
                self.view.show_recipe(recipe)
                number = self.view.get_deletion_context()
                result = self.model.delete_recipe([recipe[number - 1]])
            self.view.return_delete_recipe(result)
