from Menu import Menu

if __name__ == '__main__':
    menu = Menu()
    while True:
        menu.showMenu()
        choice = menu.getChoiceFromUser()
        if not menu.handleUserChoice(choice):
            break