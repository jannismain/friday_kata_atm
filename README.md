# ATM Kata

## Aufgabe: Minimale Anzahl von Münzen

Gegeben sei ein Betrag von n Cent und ein unbegrenzter Vorrat an Münzen mit den Werten 1, 2, 5, 10, 20, 50, 100 Cent und 200 Cent. Wir müssen die minimale Anzahl an Münzen finden, die benötigt wird, um den gegebenen Betrag zusammenzustellen.

### Runde 1: Initiale Implementierung (~45 min)

Erstelle geeignete Tests und implementiere die beschriebene Funktion.

### Runde 2: Generalisierung (~30 min)

Die Funktion soll nun so angepasst werden, dass sie mit beliebigen Münzwerten funktioniert.

### Runde 3: Erweiterte Anforderungen (~30 min)

Die Münzwerte sollen nun als externe Abhängigkeit betrachtet werden, wobei eine Schnittstelle definiert wird, die die Münzwerte bereitstellt. Implementiere diese Schnittstelle und passe die Funktion entsprechend an.

## Testing

```sh
uv run pytest atm.py
```

## Referenzen

- [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict)
- [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter)
