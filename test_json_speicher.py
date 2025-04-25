from json_storage import JsonSpeicher

# Speicherinstanz erstellen – mit der Datei 'movies.json'
speicher = JsonSpeicher("movies.json")

# Test: Film hinzufügen
print("🎬 Film hinzufügen...")
speicher.film_hinzufuegen("Inception", 2010, 8.8, "https://example.com/inception.jpg")

# Test: Alle Filme anzeigen
print("\n📃 Filme auflisten:")
filme = speicher.filme_auflisten()
for titel, details in filme.items():
    print(f"{titel}: {details}")

print("\n✅ Test abgeschlossen.")