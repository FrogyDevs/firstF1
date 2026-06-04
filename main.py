import fastf1 as ff
from fastf1 import plotting
from matplotlib import pyplot as plt



def get_driver_tele(driver: str):
    session = ff.get_session(2026, 'Montreal', 'R')
    session.load()

    laps = session.laps
    print(f'Total laps: {len(laps)}')

    verstappen_laps = laps.pick_driver(driver)
    fastest_lap = verstappen_laps.pick_fastest()

    telemetry = fastest_lap.get_telemetry()

    print(telemetry[['Speed', 'Throttle', 'Brake', 'X', 'Y']])


def main():
    ff.Cache.enable_cache('./f1-cache')
    get_driver_tele('VER')
    

if __name__ == "__main__":
    main()
