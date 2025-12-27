# 🚀 Scraper produktów Kapitan Bomba dla aplikacji Smakers

Automatyczne narzędzie stworzone w **Pythonie**, które skanuje oficjalny sklep pod kątem popularności produktów. Projekt służy do analizy trendów sprzedażowych i wyboru najlepszego asortymentu do bazy danych aplikacji **Smakers**.

## 📊 Co robi ten projekt?
* **Automatyczne skanowanie**: Przeszukuje setki produktów z uniwersum Kapitana Bomby.
* **Ekstrakcja danych**: Pobiera nazwy, ceny oraz – co najważniejsze – **liczbę opinii**.
* **Czyszczenie danych**: Skrypt inteligentnie usuwa duplikaty i formatuje ceny do czytelnej postaci.
* **Raportowanie**: Generuje gotowy plik `.xlsx`, gotowy do analizy biznesowej.

## 🏆 Top 5 najpopularniejszych produktów (na podstawie skanu):
| Produkt | Liczba opinii |
| :--- | :--- |
| Magnes na samochód + 3 naklejki | 1079 |
| Koszulka sportowa RKS Huwdu | 725 |
| Koszulka od zera do klasy średniej | 681 |
| Etykiety samoprzylepne Skurwolańska | 643 |
| Kartki okolicznościowe (5 wariantów) | 640 |

*(Dane pobrane automatycznie przez scrapera)*.

## 🛠️ Użyte technologie
* **Python 3.12**
* **BeautifulSoup4** (analiza kodu HTML)
* **Requests** (pobieranie danych ze stron)
* **Pandas** (zarządzanie bazą w Excelu)

---
*Projekt rozwijany na potrzeby analizy rynku gadżetów kolekcjonerskich.*
