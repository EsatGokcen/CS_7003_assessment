from src.business_logic_layer.initialize_database import initialize_database
from src.presentation_layer.tk_controller import TkController


def main():

    # RUN THIS TO RESET DATABASE TO MOCK DATA
    #initialize_database()

    app = TkController()
    app.start()

if __name__ == '__main__':
    main()