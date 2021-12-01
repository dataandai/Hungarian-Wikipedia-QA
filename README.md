# Hungarian-Wikipedia-QA
Kérdés-válasz a magyar Wikipédia oldalakon többnyelvű transzformer segítségvel.

A használatbevétel API requesten keresztül történik. 
A megoldás két modellt tartalmaz, egy spacy magyar entitás felismerőt, illetve egy kérdés-válasz feladatokra tanított többnyelvű, de magyarul is tudó nyelvmodellt.

A megoldás CPU és GPU környezetben is futtatható. 


Mielőtt elindítod, töltsd le az alábbi magyar nyelvű spacy modellt: hu_core_ud_lg 
Ezt másold be a letöltött könyvtárba.
Ezután indíthatod a szükséges csomagok telepítését.

pip3 install -r requirements.txt


python api.py

Ezután curl segítségével tudsz POST requesteket küldeni: 

curl --location --request POST 'localhost:8000/qa' \
--header 'Content-Type: application/json' \
--data-raw '{
    "question": "Ki volt Rommel tábornok a II. világháborúban?"
}'



Ajánlott a GPU használata, mert különben egy perc is lehet a latencia ideje.
