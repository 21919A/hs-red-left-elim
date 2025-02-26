#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from high_stakes.events import *

# Open log based on config
config_open_log()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    # Reset robot position and inertial heading to the starting autonomous position and heading
    robot_position.reset(Position(-1500, 600))
    inertial.set_heading(-90)

    # Then try resetting to GPS if GPS sensor is installed and reports high quality
    reset_robot_position_and_heading_to_gps()

    trigger_mover.move(Position(-500, 600), REVERSE)

    clamp.set(True)
    trigger_turner.turn(350, FRAME_ABSOLUTE)

    intake.spin_forward()

    reset_robot_position_and_heading_to_gps()

    trigger_mover.move(Position(-596, 1142))
    trigger_turner.turn(50, FRAME_ABSOLUTE)
    trigger_mover.move(Position(-389, 1315))

    reset_robot_position_and_heading_to_gps()

    trigger_turner.turn(330, FRAME_ABSOLUTE)
    trigger_mover.move(Position(-89, 796), REVERSE)

    wait(1000, MSEC)
    reset_robot_position_and_heading_to_gps()

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
