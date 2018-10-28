# Main app
from BungieApi import BungieAPI


def main():

    print("HEY")

    api = BungieAPI()
    api.Get_Characters('4611686018468519685')


if __name__ == '__main__':
    main()