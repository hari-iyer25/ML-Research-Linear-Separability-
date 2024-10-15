import sqlite3
import StringIO
from cnfgen.utils import parse_dimacs
from cnfgen import CNF

def dimacs_to_latex():
    db = sqlite3.connect("insert DB path here")
    cursor = db.cursor()
    rows = cursor.execute("SELECT * FROM linsep_formulas")
    for row in rows:
        with StringIO() as f:
            f.write(row[0])
            f.seek(0)
            print(parse_dimacs(CNF, f).to_latex())
