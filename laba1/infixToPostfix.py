from stack import Stack

def inf_to_post(expression):
    operators = {
        ')' : 3,
        '*' : 3,
        '/' : 3,
        '+' : 2,
        '-' : 2,
        '(' : 1
    }
    stack = Stack() # стек куда складываем наши операторы
    tokens_output = "" # вывод
    prev_token = ''
    for token in expression:
        if token == ' ':
            continue

        elif token.isalpha() or token.isdigit(): # если токен - операнд, сразу кладем в вывод
            if prev_token.isdigit() or prev_token.isalpha():
                tokens_output += f'{token} '
            else:
                tokens_output += f'{token}'

        elif token == '(':
            stack.push(token)

        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                tokens_output += f'{top_token} '
                top_token = stack.pop()

        else:
                try:
                    while not stack.isEmpty() and operators[stack.peek()] >= operators[token]:
                        tokens_output += f'{stack.pop()} '
                    stack.push(token)
                except KeyError:
                    return 'Неправильный ввод'
        prev_token = token

    while not stack.isEmpty():
        tokens_output += f'{stack.pop()} '

    return tokens_output

if __name__ == '__main__':
    # пример ввода ( A + B ) * C
    while True:
      out = input(
                    'Алгоритм перевода из инфиксной нотации в постфиксную, используя стэк на основе связаных списков\n'
                    'Каждый символ вводите через пробел. Пример ( А + B ) * C\n'
                    'Доступные операции: +, -, /, *\n'
                    'Операнды - любые буквы или цифры\n'
                    'Для завершения программы нажмите ENTER\n'
                )
      if out:
          print(inf_to_post(out))
      else:
          break
