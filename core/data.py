import requests


def export_details():
    url = 'http://www.tsetmc.com/tsev2/data/MarketWatchPlus.aspx'
    data = requests.get(url)
    content = data.content.decode('utf-8')
    parts = content.split('@')
    inst_price = parts[2].split(';')
    market = []
    for item in inst_price:
        item = item.split(',')
        market.append(
                    dict(
                        id=item[0],
                        code=item[1],
                        symbol=item[2],
                        name=item[3],
                        first_price=item[5],
                        close_price=item[6],
                        last_price=item[7],
                        count=item[8],
                        volume=item[9],
                        value=item[10],
                        min_traded_price=item[11],
                        max_treaded_price=item[12],
                        yesterday_price=item[13],
                        eps=item[14],
                        base_volume=item[15],
                        c2=item[16],
                        table_id=item[17],
                        group_id=item[18],
                        max_allowed_price=item[19],
                        min_allowed_price=item[20],
                        type_of_symbol=item[22],
                        all_count_of_symbol=item[21]
                        )
                    )
    return market
