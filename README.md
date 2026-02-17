# Pokemon Search <img width="35" height="35" alt="image" src="https://github.com/user-attachments/assets/b1bdd341-babf-4c14-a8f4-26bca942769b" />

## Description
A Pokemon search tool powered by the [PokeAPI](https://pokeapi.co/). Search any Pokemon by name to see its Pokedex number, types, height, weight, and sprite image. Started as a CLI script and now includes a Django web interface.

## Web App
1. Clone the repo
2. Install dependencies:
   ```
   pip install django requests python-decouple
   ```
3. Create a `.env` file in `pokemon_web/` with your secret key:
   ```
   SECRET_KEY=your-secret-key-here
   ```
4. Run migrations and start the server:
   ```
   cd pokemon_web
   python3 manage.py migrate
   python3 manage.py runserver
   ```
5. Visit `http://127.0.0.1:8000/`

## CLI
```
python3 pokemon_search.py
```

## Screenshot
<img width="1701" height="955" alt="Screenshot 2026-02-16 at 9 57 57 PM" src="https://github.com/user-attachments/assets/33e5b420-7497-4fae-a4dd-656d605f14e5" />

