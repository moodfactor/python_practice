import genanki

chapter_23_summary = [
  ('Modules', 'A module is a self-contained collection of functions, classes, and variables. Modules are used to organize code and to make it easier to reuse code.'),
  ('Importing Modules', 'To import a module, you use the `import` statement. The syntax for importing a module is as follows:'),
  ('Creating Modules', 'To create a module, you create a file with the .py extension. The file should contain the code that you want to include in the module.'),
  ('Packages', 'A package is a collection of modules. Packages are used to organize code and to make it easier to distribute code.'),
  ('Importing Packages', 'To import a package, you use the `import` statement. The syntax for importing a package is as follows:'),
  ('Creating Packages', 'To create a package, you create a directory with the name of the package. The directory should contain the modules that you want to include in the package.'),
  ('Accessing Modules in a Package', 'Once you have imported a package, you can access its modules using the dot notation. For example, the following code imports the `my_module` module from the `my_package` package:'),
  ('Reusing Code', 'Modules and packages are a great way to reuse code. By organizing your code into modules and packages, you can make it easier to find and use the code that you need.'),
]

model_id = 101
model =genanki.Model(
    model_id,
    'Learning Python ch23',
    fields= [
        {'title': 'Description'},
        {'title': 'Description'}
    ],
    templates =[
         {
            'name': 'Card 1',
            'qfmt': '{{Description}}',
            'afmt': '{{Description}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Description}}',
            'afmt': '{{Description}}',
        },
    ]
)

deck_id = 201
deck = genanki.Deck(deck_id, 'Learning Python 5th ed')

for title, describtion in chapter_23_summary:
    note = genanki.Note(model=model, fields=[title, describtion])
    deck.add_note(note=note)

genanki.Package(deck).write_to_file('learning_python_5th_ed.apkg')