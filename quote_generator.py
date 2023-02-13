""" Generate random number and write an inspirational quote to quote-service.txt """

import random


class Quote:
    """ Represents a collection of inspirational quotes """
    def __init__(self):
        self._quotes = {1: '“It’s the gymnasium of life where you get the workout, '
                           'the resistance, and you find out things about yourself '
                           'that you didn’t know.” - Bishop T.D. Jakes',
                        2: '“Live in each season as it passes; breathe the air, '
                           'drink the drink, taste the fruit, and resign yourself '
                           'to the influence of the earth.” - Henry David Thoreau',
                        3: '“What lies behind us and what lies before us are tiny '
                           'matters compared to what lies within us.” - Henry Stanley Haskins',
                        4: '“Nothing is impossible. The word itself says '
                           '‘I’m Possible!’” - Audrey Hepburn',
                        5: '“Life is like riding a bicycle, to keep your balance, '
                           'you must keep moving.” - Albert Einstein'
                        }

    def get_quote(self, index: int) -> str:
        """ Return a quote from self._quotes using an integer that corresponds
        to the key for a quote

        :param index (int) number that corresponds to key of quote
        :return (str) inspirational quote
        """
        return self._quotes[index]


def main():
    """ Run quote generator server """
    print("quote_generator.py listening...")

    while True:
        with open("quote-service.txt", "r+") as quo_serv:
            file_content = quo_serv.read()

            # generate random number when "quote" is in file
            if file_content == "quote":
                print("request received")

                # generate random number
                random_num = random.randint(1, 5)

                # erase "quote" form quote-service.txt
                quo_serv.seek(0)
                quo_serv.truncate()
         
                # send response - write quote to quote-service.txt
                quote = Quote()
                random_quote = quote.get_quote(random_num)

                quo_serv.write(random_quote)


if __name__ == "__main__":
    main()
