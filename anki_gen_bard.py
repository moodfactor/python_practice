from genanki import Note, Deck, Model

# Create a model for the flashcards.
model = Model(
    model_id="chapter_23_summary",
    fields=[
    {'title': 'Description'},
    {'title': 'Description'},
  ],
)

# Create a deck for the flashcards.
deck = Deck(
  id="chapter_23_summary",
  model=model,
)

# Add flashcards to the deck.
for topic, summary in chapter_23_summary:
  note = Note(
    model=model,
    front=topic,
    back=summary,
  )
  deck.add_note(note)

# Export the deck to a file.
deck.write_to_file("chapter_23_summary.apkg")
