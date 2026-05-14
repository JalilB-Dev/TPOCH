# 🕐 TPOCH

A world clock for the terminal. Built in Python from documentation — no tutorials, no boilerplate.

**Status:** v0.x — pre-release, active development
**Stack:** Python · `zoneinfo` · standard library

---

## What it does

TPOCH displays the current time across multiple cities and regions in a clean terminal interface. Currently shows 12 cities with auto-refresh. Designed to be readable at a glance, run entirely without a GUI, and grow into a fuller environmental dashboard as new features land.

---

## Roadmap

### v1.0 — First Public Release

Everything here ships before the v1.0 tag.

- [ ] Clean, consistent layout — aligned columns, intentional spacing
- [ ] Sorting — alphabetical and by UTC offset
- [ ] Add and remove cities via user input, persisted between runs

### v1.x — Quality of Life

- **v1.1** — toggle between sort modes at runtime
- **v1.2** — config file for default cities, sort preference, display format
- **v1.3** — 12-hour / 24-hour time format toggle
- **v1.4** — date display alongside time

### v2.0 — Weather Integration

Live weather data per region via API. Temperature, conditions, and feels-like surfaced alongside each timezone.

### v3.0 — Regional News Feed

Headlines per timezone pulled from a news API. TPOCH becomes a full environmental dashboard — time, weather, and news at a glance.

### GUI Transition

A GUI version is planned alongside the TUI. The terminal interface stays — it will live on as a standalone mode or separate project.

---

## Running Locally

```bash
git clone https://github.com/JalilB-Dev/TPOCH.git
cd TPOCH
python3 worldclock.py
```

No dependencies beyond the Python standard library.

---

Built by [JalilB-Dev](https://github.com/JalilB-Dev)
