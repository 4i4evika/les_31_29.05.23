import json


class Recipe:
    def __init__(self, name, author, type, text, link, list, kitchen):
        self.name = name
        self.author = author
        self.type = type
        self.text = text
        self.link = link
        self.list = list
        self.kitchen = kitchen

    def __str__(self):
        return f'{self.name}'


class DecodeError(Exception):
    pass


class Model:
    def __init__(self, filepath):
        self.filepath = filepath
        self.__recipe = {}
        try:
            self.data = json.load(open(self.filepath, 'r', encoding='utf-8'))
            for i in self.data.values():
                self.__recipe[f'{i["name"]}'] = Recipe(*i.values())
        except json.JSONDecodeError:
            raise DecodeError
        except FileNotFoundError:
            with open(self.filepath, 'w') as f:
                f.write('{}')

    @property
    def recipe(self):
        return self.__recipe

    def save_recipe(self):
        dict_recipe = {f'{art.name}': art.__dict__ for art in self.__recipe.values()}
        json.dump(dict_recipe, open(self.filepath, 'w', encoding='utf-8'))

    def add_new_recipe(self, recipe_data):
        new_recipe = Recipe(*recipe_data.values())
        self.__recipe[f'{new_recipe.name}'] = new_recipe
        self.save_recipe()

    def find_recipe(self, key_words):
        recipe = []
        for i in self.__recipe.values():
            for word in key_words:
                if i in recipe:
                    break
                for prop in i.__dict__.values():
                    if prop.isdigit():
                        continue
                    if word.lower() in prop.lower():
                        recipe.append(i)
                        break
        return recipe

    def delete_recipe(self, recipes):
        if len(recipes) == 0:
            return 'Такой статьи не было найдено!'
        elif len(recipes) == 1:
            recipe = recipes[0]
            key = f'{recipe.name}'
            self.__recipe.pop(key)
            self.save_recipe()
            return 'Статья была удалена!'
        else:
            return 'Слишком много статей!'






