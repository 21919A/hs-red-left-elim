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

    # Reset odometry to the starting autonomous position
    odometry.reset(PositionWithHeading(-1500, 600, -90))

    # Then try resetting it to GPS if GPS sensor is installed and reports high quality
    reset_odometry_to_gps()

    intake_1st_stage.set_velocity(470, RPM)
    intake_2nd_stage.set_velocity(470, RPM)
    pid_driver.drive(-1000, True)
    clamp.set(True)
    pid_turner.turn(80, FRAME_HEADING_RELATIVE)

    intake_1st_stage.spin(REVERSE)
    intake_2nd_stage.spin(FORWARD)

    wait(1000, MSEC)
    reset_odometry_to_gps()

    pid_driver.drive(550)
    pid_turner.turn(60, FRAME_HEADING_RELATIVE)
    pid_driver.drive(270)

    wait(1000, MSEC)
    reset_odometry_to_gps()

    pid_turner.turn(-80, FRAME_HEADING_RELATIVE)
    pid_driver.drive(-600, False)

    wait(1000, MSEC)
    reset_odometry_to_gps()

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
