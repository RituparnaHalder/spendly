 ▐▛███▛█   Claude Code v2.1.329
▝▜██████▀  Haiku 5.5 · API Usage Billing
 ▝▝   ▝▝   ~/Desktop/Ritu_claude/expense-tracker


❯ what is this project all about                                                

  Ran 2 shell commands · 1 failed (ctrl+o to expand)

⏺ No README, so I'll read the actual code.

  Read 2 files (ctrl+o to expand)

⏺ This is Spendly, a personal finance / expense tracker web app, built with
  Flask and Jinja templates. It's an early-stage, step-by-step course project,
  not a finished app.

  What exists now:
  - Landing page (/) with a marketing hero and a mock monthly spending card.
  - Register (/register) and Login (/login) pages. They render forms, but the
    routes only handle GET, and the forms POST to the same paths, so submitting
    does nothing yet.

  What's stubbed out:
  - /logout, /profile, and the expense routes (/expenses/add,
    /expenses/<id>/edit, /expenses/<id>/delete) return placeholder text such as
    "Add expense — coming in Step 7".
  - database/db.py is only a comment describing get_db(), init_db(), and
    seed_db(). It has no code.
  - static/js/main.js is an empty placeholder.

  Stack: Flask 3.1 and Werkzeug, with pytest and pytest-flask for testing. The
  app runs on port 5001 in debug mode. The venv/ folder is a committed Python
  3.9 virtualenv, which is unusual, and .gitignore should probably exclude it.

  The code comments ("students will implement these", "Step 1 — Database Setup")
  suggest this is a guided course where you build features in steps: database,
  auth, profile, then expense CRUD. The repo has a single "initial commit" and
  no README.

  I can help with the next step, such as implementing database/db.py or the
  login and register handlers, if that's what you're after.

✻ Baked for 8s · done 2:52 PM