import Powerball_Scraper

draw_date = Powerball_Scraper
def extract_dates(table):
    dates = []
    for row in table.find_all('tr'):
        draw_date_text = row.find('td', class_='draw-date').text.strip()
        draw_date = draw_date_text.split(',')[0].strip()
        dates.append(draw_date)
    return dates


dates = extract_dates(table)
for date in dates:
    print(date)