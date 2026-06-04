# firstF1

A small Fast F1 telemetry helper that uses `fastf1` to download race session data, cache it locally, and print driver telemetry for the fastest lap.

## Overview

- Uses `fastf1` to load the 2026 Montreal sprint session (`2026`, `Montreal`, `R`).
- Enables local caching in `./f1-cache` to avoid repeated downloads.
- Prints the fastest lap telemetry for a selected driver, including speed, throttle, brake, and track coordinates.

## Requirements

- Python 3.13+
- `fastf1` >= 3.8.3
- `matplotlib` >= 3.10.9

## Installation

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

> If `requirements.txt` does not exist, install directly from `pyproject.toml` dependencies.

## Usage

Run the main script:

```powershell
python main.py
```

The default driver code is `VER` (Max Verstappen). Modify `get_driver_tele('VER')` in `main.py` to query another driver.

## Cache

The project stores downloaded Fast F1 session data in `./f1-cache`.
This makes subsequent runs faster by reusing previously downloaded telemetry data.

## Notes

- `main.py` currently queries the fastest lap for the given driver and prints a subset of telemetry data.
- The project can be extended with plotting or additional session analysis.
