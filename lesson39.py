# Декораторы
def make_title(func):
    def func_wrapper():
        title = func()
        title.capitalize()
        title.replace(',', '')
        return title
    return func_wrapper()


@make_title
def hi():
    return 'hello world'

print(hi())