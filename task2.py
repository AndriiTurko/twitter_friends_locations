import twitter2


def main():
    print('')
    dicti = twitter2.get_json(input('Enter Twitter Account:'))
    while type(dicti) == dict or type(dicti) == list:
        try:
            if type(dicti) == dict:
                print('Choose the key you want to explore: ' +
                      ', '.join(dicti.keys()))
                key = input()
                dicti = dicti[key]
            else:
                length = len(dicti)-1
                if length > 0:
                    print('Choose number between 0 and ' + str(length))
                    num = int(input())
                    dicti = dicti[num]
                elif length == 0:
                    dicti = dicti[0]
                else:
                    dicti = 'supercalifragilisticexpialidocious'
        except:
            print('invalid input')
            continue
    if (dicti == 'supercalifragilisticexpialidocious' or
        dicti is None or len(dicti) == 0):
        print('Empty data')
    else:
        print(dicti)


if __name__ == "__main__":
    main()
