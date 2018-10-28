# Main app
from BungieApi import BungieAPI


def main():

    print("HEY")

    api = BungieAPI()
    api.get_userid('user')
    api.get_characters('4611686018468519685')


if __name__ == '__main__':
    main()