"""
AX-12+ Constants
"""
# Control Table Constants
AX_MODEL_NUMBER_L = 0
AX_MODOEL_NUMBER_H = 1
AX_VERSION = 2
AX_ID = 3
AX_BAUD_RATE = 4
AX_RETURN_DELAY_TIME = 5
AX_CW_ANGLE_LIMIT_L = 6
AX_CW_ANGLE_LIMIT_H = 7
AX_CCW_ANGLE_LIMIT_L = 8
AX_CCW_ANGLE_LIMIT_H = 9
AX_SYSTEM_DATA2 = 10
AX_LIMIT_TEMPERATURE = 11
AX_DOWN_LIMIT_VOLTAGE = 12
AX_UP_LIMIT_VOLTAGE = 13
AX_MAX_TORQUE_L = 14
AX_MAX_TORQUE_H = 15
AX_RETURN_LEVEL = 16
AX_ALARM_LED = 17
AX_ALARM_SHUTDOWN = 18
AX_OPERATING_MODE = 19
AX_DOWN_CALIBRATION_L = 20
AX_DOWN_CALIBRATION_H = 21
AX_UP_CALIBRATION_L = 22
AX_UP_CALIBRATION_H = 23
AX_TORQUE_ENABLE = 24
AX_LED = 25
AX_CW_COMPLIANCE_MARGIN = 26
AX_CCW_COMPLIANCE_MARGIN = 27
AX_CW_COMPLIANCE_SLOPE = 28
AX_CCW_COMPLIANCE_SLOPE = 29
AX_GOAL_POSITION_L = 30
AX_GOAL_POSITION_H = 31
AX_GOAL_SPEED_L = 32
AX_GOAL_SPEED_H = 33
AX_TORQUE_LIMIT_L = 34
AX_TORQUE_LIMIT_H = 35
AX_PRESENT_POSITION_L = 36
AX_PRESENT_POSITION_H = 37
AX_PRESENT_SPEED_L = 38
AX_PRESENT_SPEED_H = 39
AX_PRESENT_LOAD_L = 40
AX_PRESENT_LOAD_H = 41
AX_PRESENT_VOLTAGE = 42
AX_PRESENT_TEMPERATURE = 43
AX_REGISTERED_INSTRUCTION = 44
AX_PAUSE_TIME = 45
AX_MOVING = 46
AX_LOCK = 47
AX_PUNCH_L = 48
AX_PUNCH_H = 49

# Status Return Levels
AX_RETURN_NONE = 0
AX_RETURN_READ = 1
AX_RETURN_ALL = 2

# Instruction Set
AX_PING = 1
AX_READ_DATA = 2
AX_WRITE_DATA = 3
AX_REG_WRITE = 4
AX_ACTION = 5
AX_RESET = 6
AX_SYNC_WRITE = 131

# Broadcast Constant
AX_BROADCAST = 254

# Error Codes
AX_INSTRUCTION_ERROR = 64
AX_OVERLOAD_ERROR = 32
AX_CHECKSUM_ERROR = 16
AX_RANGE_ERROR = 8
AX_OVERHEATING_ERROR = 4
AX_ANGLE_LIMIT_ERROR = 2
AX_INPUT_VOLTAGE_ERROR = 1
AX_NO_ERROR = 0

# Static parameters
AX_TICKS = 1024
AX_MAX_POSITION = 1023

AX_RANGE_DEG = 300
AX_RAW_DEG_RATIO = 3.41333333333333333333     # how many ticks in degree
AX_DEG_RAW_RATIO = 0.29296875                 # how many degrees in a tick
AX_MAX_SPEED_DEG = 684.0                      # degrees per second

AX_RANGE_RAD = 5.235987756
AX_RAW_RAD_RATIO = 195.569594071              # how many ticks in radian
AX_RAD_RAW_RATIO = 0.005113269                # how many radians in a tick
AX_MAX_SPEED_RAD = 11.938052084               # radians per second

