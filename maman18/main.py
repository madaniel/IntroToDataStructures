
from maman18.parser import Parser
from maman18.menu import Menu
from maman18.db_api import DbApi


def main():
    menu = Menu(parser=Parser(), db_api=DbApi())

    while menu.parser.is_active:
        # Init variables
        menu.parser.reset_variables()
        # Get input from user
        menu.parser.user_input = menu.get_user_input()
        # Analyze
        menu.parser.analyze_input()
        # Execute
        print(menu.do_operation())


if __name__ == '__main__':
    main()
