from watercooler.config.routes import DB_FILE


def read_history(limit: int = 10):
    with open(DB_FILE, "r") as db:
        lines = db.read().split("\n~~~\n")
        return lines[-limit:]


def clear_history():
    with open(DB_FILE, "w") as db:
        db.write("")


def write_history(entry: str):
    with open(DB_FILE, "a") as db:
        db.write(entry + "\n~~~\n")
