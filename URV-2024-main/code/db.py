import sqlite3

def clear_db(cursor):
    cursor.execute("DELETE FROM formulas")

db = sqlite3.connect("./db/SAT.sqlite")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS linsep_formulas (formula TEXT, num_vars INTEGER, num_clauses INTEGER, num_sols INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS sat_formulas (formula TEXT, num_vars INTEGER, num_clauses INTEGER, num_sols INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS unsat_formulas (formula TEXT, num_vars INTEGER, num_clauses INTEGER, num_sols INTEGER)")

#clear_db(cursor)
db.commit()