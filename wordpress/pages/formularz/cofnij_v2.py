"""Cofa wersje 2 poprawki formularza w pliku (zamiany nowe -> stare z formularz_krotszy_v2.py)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from formularz_krotszy_v2 import ZAMIANY
p = sys.argv[1]
t = open(p, encoding="utf-8").read()
for stare, nowe in reversed(ZAMIANY):
    assert t.count(nowe) == 1, (t.count(nowe), nowe[:60])
    t = t.replace(nowe, stare)
assert ".pdw-form .form-label+br" not in t
open(p, "w", encoding="utf-8").write(t)
print(p, "cofnięto v2")
