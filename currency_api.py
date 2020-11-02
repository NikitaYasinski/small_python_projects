from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}")  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'xml')
    curr_from_s = soup.find("CharCode", text=cur_from)
    val_from = Decimal(curr_from_s.find_next_sibling('Value').string.replace(",", "."))
    nom_from = Decimal(curr_from_s.find_next_sibling('Nominal').string.replace(",", "."))

    rur = amount * (val_from / nom_from)

    curr_to_s = soup.find("CharCode", text=cur_to)
    val_to = Decimal(curr_to_s.find_next_sibling('Value').string.replace(",", "."))
    nom_to = Decimal(curr_to_s.find_next_sibling('Nominal').string.replace(",", "."))

    result = (rur / val_to) * nom_to
    result = result.quantize(Decimal("1.0000"))
    return result  # не забыть про округление до 4х знаков после запятой
