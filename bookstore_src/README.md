
# Emily Zhang - README

## Bookstore Description

This example creates a small bookstore database in SQLite and then uses Python to interact with it through a command-line interface. The database stores categories and books, and the Python CLI allows users to view, search, add, update, and delete bookstore records.

The bookstore includes eight categories and twenty books. It contains the example starter categories and books as well as four additional categories: Autobiographies, Science Fiction, Romantic Comedy, and Horror.

## Files

- `createTables.sql` - creates the tables
- `insertRows.sql` - inserts sample categories and books
- `bookstore_cli.py` - Python CRUD program
- `bookstore.db` - database file you will create by running the commands below

## Database Structure

This project uses two tables:

### `category`
- `categoryId` - integer primary key
- `categoryName` - text, required, unique
- `categoryImage` - text, required

### `book`
- `bookId` - integer primary key
- `categoryId` - integer, required, foreign key to `category(categoryId)`
- `title` - text, required
- `author` - text, required
- `isbn` - text, required, unique
- `price` - real, required, must be greater than or equal to 0
- `image` - text, required
- `readNow` - integer, required, must be either 0 or 1


## Sample Data

The database includes:
- 8 categories
- 20 books

Categories include:
- Biographies
- Learn to Play
- Music Theory
- Scores and Collections
- Autobiographies
- Science Fiction
- Romantic Comedy
- Horror


## Create the database

Run these commands in the terminal:

```bash
python3 - <<'PY'
import sqlite3
sqlite3.connect('bookstore.db').close()
PY
```

Then load the SQL files using SQLite in Python or DB Browser for SQLite.

If your environment has the `sqlite3` shell installed, you can run:

```bash
sqlite3 bookstore.db < createTables.sql
sqlite3 bookstore.db < insertRows.sql
```

## Run the Python CLI

```bash
python3 bookstore_cli.py
```

## CLI Features

Required features:

- View all categories
- View all books
- View books in a category
- Search books by title
- Add a new book
- Update a book price
- Delete a book
- Quit

Additional features:

- Search books by author
- Show only books with readNow = 1
- Show books within a price range
- Count books per category

## Notes

- This example uses parameterized queries in Python.
- The `image` field stores the filename only.
- Foreign keys are enabled in SQLite.
- The actual images can be reused later in the Flask web app.
