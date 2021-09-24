from stack import Stack


def inf_to_post(expression):
    operators = {
        '*' : 3,
        '/' : 3,
        '+' : 2,
        '-' : 2,
        '(' : 1
    }
    stack = Stack()  # stack with operators
    tokens_output = ""  # output
    prev_token = ''
    for token in expression:
        if token == ' ':  # skip backspaces
            continue

        elif token.isalpha() or token.isdigit():  # if token is a operand, we put it in output
            if prev_token.isdigit() or prev_token.isalpha():  # check ambiguity and more
                tokens_output += f'{token} '
            else:
                tokens_output += f' {token}'

        elif token == '(':
            stack.push(token)

        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                tokens_output += f'{top_token} '
                top_token = stack.pop()

        else:
            try:
                while (not stack.isEmpty()) and (operators[stack.peek()] >= operators[token]):
                    tokens_output += f'{stack.pop()} '
                stack.push(token)
            except KeyError:
                return 'Error with input'

        prev_token = token

    while not stack.isEmpty():
        tokens_output += f'{stack.pop()} '

    return tokens_output.strip()


if __name__ == '__main__':
    # example input ( A + B ) * C or (a+b)*c
    while True:
        out = input(
            'Algorithm converting from infix to postfix notation using a stack based on linked list\n'
            'You can input in different ways.\nFor example: ( А + B ) * C or (a+b)*c\n'
            'Available operations: +, -, /, *\n'
            'Press ENTER to end the program\n'
        )
        if out:
            print(inf_to_post(out))
        else:
            break