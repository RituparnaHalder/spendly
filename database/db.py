import os
import sqlite3
from datetime import date

from werkzeug.security import generate_password_hash

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "spendly.db")


def get_db():
    """Return a SQLite connection with row access by name and FK enforcement on."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Create all tables if they do not already exist."""
    conn = get_db()
    try:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                name          TEXT    NOT NULL,
                email         TEXT    NOT NULL UNIQUE,
                password_hash TEXT    NOT NULL,
                created_at    TEXT    NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS expenses (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL REFERENCES users(id),
                amount      REAL    NOT NULL,
                category    TEXT    NOT NULL,
                date        TEXT    NOT NULL,
                description TEXT,
                created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
            );
            """
        )
        conn.commit()
    finally:
        conn.close()


def seed_db():
    """Insert sample data for development. No-op if any user already exists."""
    conn = get_db()
    try:
        count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        if count > 0:
            return

        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            (
                "Demo User",
                "demo@spendly.com",
                # pbkdf2 explicitly: werkzeug's default (scrypt) is unavailable on Python 3.9.6 here.
                generate_password_hash("demo123", method="pbkdf2:sha256"),
            ),
        )
        user_id = cursor.lastrowid

        # Dates fall within the current month, capped at today so none are in the future.
        today = date.today()

        def day(n):
            return today.replace(day=min(n, today.day)).isoformat()

        sample_expenses = [
            (user_id, 12.50, "Food", day(1), "Lunch with colleagues"),
            (user_id, 45.00, "Transport", day(2), "Monthly metro pass top-up"),
            (user_id, 120.00, "Bills", day(3), "Electricity bill"),
            (user_id, 35.00, "Health", day(4), "Pharmacy refill"),
            (user_id, 30.75, "Entertainment", day(5), "Movie night"),
            (user_id, 89.99, "Shopping", day(6), "New running shoes"),
            (user_id, 64.20, "Food", day(7), "Weekly groceries"),
            (user_id, 15.00, "Other", day(8), "Miscellaneous fee"),
        ]
        conn.executemany(
            "INSERT INTO expenses (user_id, amount, category, date, description) "
            "VALUES (?, ?, ?, ?, ?)",
            sample_expenses,
        )
        conn.commit()
    finally:
        conn.close()
