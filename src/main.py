# Main app
from BungieApi import BungieAPI

def main():

    print("HEY")

    api = BungieAPI()
    api.Authorize()

if __name__ == '__main__':
    main()