def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '='))
            result = func(*args, **kwargs)
            print('='*50)
            return result
        return wrapper
    return decorator


class View:
    @add_title('Ожидание пользовательского ввода')
    def wait_user_answer(self):
        print('Доступные команды:\n'
              '1. Добавить рецепт\n'
              '2. Показать все рецепты\n'
              '3. Найти рецепт\n'
              '4. Удалить рецепт\n'
              '5. Завершить работу')
        query = input('Введите команду: ')
        return query

    @add_title('Добавление нового рецепта')
    def get_new_recipe_data(self):
        dict_recipe = {'Название рецепта': None,
                        'Автор рецепта': None,
                        'Тип рецепта': None,
                        'Текстовое описание': None,
                        'Ссылка на видео с рецептом': None,
                        'Список ингредиентов': None,
                        'Название кухни': None}
        for key in dict_recipe.keys():
            dict_recipe[key] = input(f'Введите {key.lower()}: ')
        return dict_recipe

    @add_title('Список рецептов')
    def show_recipe(self, recipe):
        if recipe:
            [print(f'{i}. {art}') for i, art in enumerate(recipe, 1)]
        else:
            print('Нет ниодного рецепта!')

    @add_title('Поиск рецепта')
    def get_keywords_to_find_recipe(self):
        key_words = input('Введите список слов для поиска через пробел: ').split()
        return key_words

    @add_title('Название рецепта')
    def get_recipe_name(self):
        recipe_name = input('Введите название рецепта: ')
        return recipe_name.strip()

    @add_title('Дополнительная информация')
    def get_deletion_context(self):
        number = int(input('Введите номер статьи для удаления: '))
        return number

    @add_title('Дополнительная информация')
    def get_deletion_context(self):
        number = int(input('Введите номер статьи для удаления: '))
        return number

    @add_title('Результат удаления')
    def return_delete_recipe(self, result):
        print(result)

    @add_title('Ошибка загрузки')
    def throw_an_error(self, e):
        print('При загрузке базы данных произошла ошибка:', e)