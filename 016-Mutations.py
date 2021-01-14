def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':