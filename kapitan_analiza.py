import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# --- KONFIGURACJA ---
BASE_URL = "https://www.kapitan.pl/?s=bomba&post_type=product"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

def pobierz_dane_produktu(url_produktu):
    try:
        r = requests.get(url_produktu, headers=HEADERS, timeout=10)
        s = BeautifulSoup(r.text, 'html.parser')
        nazwa = s.find('h1', class_='product_title').text.strip()
        
        # WooCommerce: cena aktualna
        cena_tag = s.find('p', class_='price')
        if cena_tag:
            if cena_tag.find('ins'):
                cena = cena_tag.find('ins').text.strip()
            else:
                cena = cena_tag.text.strip()
            cena = " ".join(cena.split())
        else:
            cena = "Brak ceny"

        # Liczba opinii
        opinie_tag = s.find('a', class_='woocommerce-review-link')
        liczba_opinii = "".join(filter(str.isdigit, opinie_tag.text)) if opinie_tag else "0"
            
        return {'Nazwa': nazwa, 'Cena': cena, 'Liczba Opinii': int(liczba_opinii), 'Link': url_produktu}
    except:
        return None

# --- GŁÓWNA PĘTLA SKANOWANIA ---
print("🚀 Rozpoczynam wielkie skanowanie Kapitana Bomby...")
wszystkie_dane = []
url_do_sprawdzenia = BASE_URL 

while url_do_sprawdzenia:
    print(f"📦 Pobieram listę z: {url_do_sprawdzenia}")
    response = requests.get(url_do_sprawdzenia, headers=HEADERS)
    if response.status_code != 200:
        break
        
    soup = BeautifulSoup(response.text, 'html.parser')
    linki = [a['href'] for a in soup.select('ul.products li.product a.woocommerce-LoopProduct-link')]
    
    for link in linki:
        if not any(d['Link'] == link for d in wszystkie_dane):
            print(f"  🔎 Analizuję: {link.split('/')[-2]}")
            dane = pobierz_dane_produktu(link)
            if dane:
                wszystkie_dane.append(dane)
            time.sleep(0.3)

    # SZUKANIE PRZYCISKU "NASTĘPNA"
    nastepna_strona_tag = soup.find('a', class_='next')
    if nastepna_strona_tag and 'href' in nastepna_strona_tag.attrs:
        url_do_sprawdzenia = nastepna_strona_tag['href']
    else:
        url_do_sprawdzenia = None 

# --- ZAPIS DO EXCELA ---
if wszystkie_dane:
    df = pd.DataFrame(wszystkie_dane)
    # Usuwamy duplikaty na wszelki wypadek
    df = df.drop_duplicates(subset=['Link'])
    # Sortujemy po opiniach
    df = df.sort_values(by='Liczba Opinii', ascending=False)
    
    df.to_excel('wszystko_kapitan_bomba.xlsx', index=False)
    print(f"\n✅ KONIEC! Pobrałem {len(wszystkie_dane)} unikalnych produktów.")