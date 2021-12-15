import constant
from path import Path

# Math done on https://www.desmos.com/calculator/36hsvhf6gq

GRAVITY = 100
THROW_VX = 200
THROW_VY = 300
CATCH_TIME = 0.75
CATCH_ACCEL = 400

flight_time = 2 * THROW_VY / GRAVITY


def cascade_xt(t):
    if t <= flight_time:
        return THROW_VX * t
    elif flight_time < t and t <= CATCH_TIME + flight_time:
        return THROW_VX * flight_time
    elif flight_time + CATCH_TIME < t and t <= 2 * flight_time + CATCH_TIME:
        return THROW_VX * flight_time - THROW_VX * (t - flight_time - CATCH_TIME)
    else:
        return 0


def cascade_yt(t):
    if t <= flight_time:
        return GRAVITY * t ** 2 / 2 - THROW_VY * t
    elif flight_time < t and t <= CATCH_TIME + flight_time:
        return -CATCH_ACCEL*(t - flight_time) ** 2 + (CATCH_TIME * CATCH_ACCEL)*(t - flight_time)
    elif flight_time + CATCH_TIME < t and t <= 2 * flight_time + CATCH_TIME:
        return GRAVITY * (t - flight_time - CATCH_TIME) ** 2 / 2 - THROW_VY * (t - flight_time - CATCH_TIME)
    else:
        return -CATCH_ACCEL*(t - 2 * flight_time - CATCH_TIME) ** 2 + (CATCH_TIME * CATCH_ACCEL)*(t - 2 * flight_time - CATCH_TIME)


period = 2 * (flight_time + CATCH_TIME)

cascade_path = Path(cascade_xt, cascade_yt, period)

print(f"6.75: {cascade_yt(6.75)}, 6.76: {cascade_yt(6.76)}")
