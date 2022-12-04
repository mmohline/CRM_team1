def index(): return dict(message="hello from tables.py")

def contacts():
    grid = SQLFORM.grid(db.contacts)
    return dict(grid=grid)

def companies():
    grid = SQLFORM.grid(db.companies)
    return dict(grid=grid)

def game_types():
    grid = SQLFORM.grid(db.game_types)
    return dict(grid=grid)

def games():
    grid = SQLFORM.grid(db.games)
    return dict(grid=grid)

def activites():
    grid = SQLFORM.grid(db.activities)
    return dict(grid=grid)

def lifecycle():
    grid = SQLFORM.grid(db.lifecycle)
    return dict(grid=grid)

def active_sales():
    grid = SQLFORM.grid(db.active_sales)
    return dict(grid=grid)

def states():
    grid = SQLFORM.grid(db.states)
    return dict(grid=grid)

def locations():
    grid = SQLFORM.grid(db.locations)
    return dict(grid=grid)

def lead_source():
    grid = SQLFORM.grid(db.lead_source)
    return dict(grid=grid)