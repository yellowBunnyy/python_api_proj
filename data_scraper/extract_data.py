import pickle
import tabula
import re
import pandas as pd
import download_urls


def get_confirmed(flu_db):
    """get confrimed flu infected in POLAND in integer value"""
    confirmed_ser = flu_db[0].iloc[:, 0]
    confirmed_ser = confirmed_ser[confirmed_ser.str.contains('POLSKA')]
    return int(confirmed_ser.values[-1].split(' ')[1])


def date_parser(date_str):
    """parse date to date from  '15 do 22 grudnia 2019 r' too
    '15-22-12-2020'"""
    # pdb.set_trace()
    months = {'stycz': 1,
              'lut': 2,
              'mar': 3,
              'kwie': 4,
              'maj': 5,
              'czer': 6,
              'lip': 7,
              'sierp': 8,
              'wrze': 9,
              'pa': 10,
              'list': 11,
              'grud': 12}
    corr_date = [ele for ele in date_str.replace('do', ' ').split(' ')[:-1] if ele]
    d = ''
    for ele in corr_date:
        for month in months.keys():
            if ele.isdigit():
                d += ele
                break
            if ele.startswith(month):
                d += str(months[month])
                break
        d += '-'
    return d.strip('-')


def get_date(flu_db):
    """excract date from table in pdf and parse using parser"""
    patt = '( od)([ 0-9a-zźś]+)'
    col_name = flu_db[0].columns[-1]
    date = re.search(patt, col_name)
    if date:
        date = date.group(2).strip()
        print(date)
        return date_parser(date_str=date)


def add_to_df_all_months(urls_list):
    d = {}
    for url in urls_list:
        print(f'Processed url {url} !')
        dfs = tabula.read_pdf(url, pages='all')
        d[get_date(dfs)] = [get_confirmed(dfs), get_hospitalized(dfs), get_deaths(dfs)]
    return d


def create_df(data):
    return pd.DataFrame(data, index=['Confirmed', 'Hospitalized', 'Deaths']).T


def pickle_df(df, f_name):
    with open(f_name, 'wb') as file:
        pickle.dump(df, file)
    return f'saved {f_name}'


def load_pickled_df(pickled_df_name):
    with open(pickled_df_name, 'rb') as file:
        df = pickle.load(file)
    return df


def get_hospitalized(flu_db):
    hospitalized_table = flu_db[1]
    row_hospitalized = hospitalized_table.iloc[6][0].split()
    for ele in row_hospitalized:
        if ele.isdigit():
            return int(ele)
    raise ValueError("Can't read hospitalized ppl propertly!!")


def get_deaths(flu_db):
    death_table = flu_db[2]
    row_death = death_table.iloc[4][0].split()
    for ele in row_death:
        if ele.isdigit():
            return int(ele)
    return 0


def main():
    all_urls = download_urls.get_all_pdf_urls()
    data_from_pdfs = add_to_df_all_months(urls_list=all_urls)
    return create_df(data=data_from_pdfs)


if __name__ == '__main__':
    df = main()
    # print(df)
