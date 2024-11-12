def test_function():
    def inner_function():
        print('Я в области видимости test_function')

    inner_function()


test_function()
# Возникает ошибка т.к. inner_function существует в области test_function
inner_function
