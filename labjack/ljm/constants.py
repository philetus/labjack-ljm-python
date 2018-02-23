"""
LJM library constants.

"""

# Read/Write direction constants:
READ = 0
WRITE = 1

# Data types:
# Automatic endian conversion, if needed by the processor
UINT16 = 0
UINT32 = 1
INT32 = 2
FLOAT32 = 3

# Advanced users data types:
# Does not do any endianness conversion
BYTE = 99
STRING = 98
STRING_MAX_SIZE = 49
STRING_ALLOCATION_SIZE = 50

# namesToAddresses sets this when a register name is not found
INVALID_NAME_ADDRESS = -1
MAX_NAME_SIZE = 256

MAC_STRING_SIZE = 18
IPv4_STRING_SIZE = 16

BYTES_PER_REGISTER = 2

# Device types:
dtANY = 0
dtT4 = 4
dtT7 = 7
dtDIGIT = 200
dtTSERIES = 84

# Connection types:
ctANY = 0
ctANY_TCP = ctANY

ctUSB = 1

ctTCP = 2
ctNETWORK_TCP = ctTCP
ctETHERNET = 3
ctETHERNET_TCP = ctETHERNET
ctWIFI = 4
ctWIFI_TCP = ctWIFI

# UDP
ctNETWORK_UDP = 5
ctETHERNET_UDP = 6
ctWIFI_UDP = 7

# TCP or UDP
ctNETWORK_ANY = 8
ctETHERNET_ANY = 9
ctWIFI_ANY = 10

# Network constants:
TCP_PORT = 502
ETHERNET_UDP_PORT = 52362
WIFI_UDP_PORT = 502
NO_IP_ADDRESS = 0
NO_PORT = 0

# Identifier types:
DEMO_MODE = "-1"
idANY = 0

# addressesToMBFB Constants
DEFAULT_FEEDBACK_ALLOCATION_SIZE = 62
USE_DEFAULT_MAXBYTESPERMBFB = 0

# mbfbComm Constants
DEFAULT_UNIT_ID = 1

# listAll Constants
LIST_ALL_SIZE = 128

# Timeout Constants
NO_TIMEOUT = 0
DEFAULT_USB_SEND_RECEIVE_TIMEOUT_MS = 2600
DEFAULT_ETHERNET_OPEN_TIMEOUT_MS = 1000
DEFAULT_ETHERNET_SEND_RECEIVE_TIMEOUT_MS = 2600
DEFAULT_WIFI_OPEN_TIMEOUT_MS = 1000
DEFAULT_WIFI_SEND_RECEIVE_TIMEOUT_MS = 4000

# Stream Constants
DUMMY_VALUE = -9999
SCAN_NOT_READ = -8888
GND = 199

# Thermocouple Type Constants
ttB = 6001
ttE = 6002
ttJ = 6003
ttK = 6004
ttN = 6005
ttR = 6006
ttS = 6007
ttT = 6008
ttC = 6009

# Config Parameters
USB_SEND_RECEIVE_TIMEOUT_MS = "LJM_USB_SEND_RECEIVE_TIMEOUT_MS"
ETHERNET_SEND_RECEIVE_TIMEOUT_MS = "LJM_ETHERNET_SEND_RECEIVE_TIMEOUT_MS"
WIFI_SEND_RECEIVE_TIMEOUT_MS = "LJM_WIFI_SEND_RECEIVE_TIMEOUT_MS"
SEND_RECEIVE_TIMEOUT_MS = "LJM_SEND_RECEIVE_TIMEOUT_MS"
ETHERNET_OPEN_TIMEOUT_MS = "LJM_ETHERNET_OPEN_TIMEOUT_MS"
WIFI_OPEN_TIMEOUT_MS = "LJM_WIFI_OPEN_TIMEOUT_MS"
OPEN_TCP_DEVICE_TIMEOUT_MS = "LJM_OPEN_TCP_DEVICE_TIMEOUT_MS"

DEBUG_LOG_MODE = "LJM_DEBUG_LOG_MODE"
DEBUG_LOG_MODE_NEVER = 1
DEBUG_LOG_MODE_CONTINUOUS = 2
DEBUG_LOG_MODE_ON_ERROR = 3

DEBUG_LOG_LEVEL = "LJM_DEBUG_LOG_LEVEL"
STREAM_PACKET = 1
TRACE = 2
DEBUG = 4
INFO = 6
PACKET = 7
WARNING = 8
ERROR = 10
FATAL = 12

DEBUG_LOG_BUFFER_MAX_SIZE = "LJM_DEBUG_LOG_BUFFER_MAX_SIZE"
DEBUG_LOG_SLEEP_TIME_MS = "LJM_DEBUG_LOG_SLEEP_TIME_MS"

LIBRARY_VERSION = "LJM_LIBRARY_VERSION"

ALLOWS_AUTO_MULTIPLE_FEEDBACKS = "LJM_ALLOWS_AUTO_MULTIPLE_FEEDBACKS"
ALLOWS_AUTO_CONDENSE_ADDRESSES = "LJM_ALLOWS_AUTO_CONDENSE_ADDRESSES"

AUTO_IPS_FILE = "LJM_AUTO_IPS_FILE"
AUTO_IPS = "LJM_AUTO_IPS"

AUTO_RECONNECT_STICKY_CONNECTION = "LJM_AUTO_RECONNECT_STICKY_CONNECTION"
AUTO_RECONNECT_STICKY_SERIAL = "LJM_AUTO_RECONNECT_STICKY_SERIAL"
AUTO_RECONNECT_WAIT_MS = "LJM_AUTO_RECONNECT_WAIT_MS"

MODBUS_MAP_CONSTANTS_FILE = "LJM_MODBUS_MAP_CONSTANTS_FILE"
ERROR_CONSTANTS_FILE = "LJM_ERROR_CONSTANTS_FILE"
DEBUG_LOG_FILE = "LJM_DEBUG_LOG_FILE"
DEEP_SEARCH_FILE = "LJM_DEEP_SEARCH_FILE"
CONSTANTS_FILE = "LJM_CONSTANTS_FILE"
DEBUG_LOG_FILE_MAX_SIZE = "LJM_DEBUG_LOG_FILE_MAX_SIZE"
SPECIFIC_IPS_FILE = "LJM_SPECIFIC_IPS_FILE"

STREAM_AIN_BINARY = "LJM_STREAM_AIN_BINARY"
STREAM_SCANS_RETURN = "LJM_STREAM_SCANS_RETURN"
STREAM_SCANS_RETURN_ALL = 1
STREAM_SCANS_RETURN_ALL_OR_NONE = 2
STREAM_SCANS_RETURN_AVAILABLE = 3

STREAM_RECEIVE_TIMEOUT_MODE = "LJM_STREAM_RECEIVE_TIMEOUT_MODE"
STREAM_RECEIVE_TIMEOUT_MODE_CALCULATED = 1
STREAM_RECEIVE_TIMEOUT_MODE_MANUAL = 2

STREAM_RECEIVE_TIMEOUT_MS = "LJM_STREAM_RECEIVE_TIMEOUT_MS"
STREAM_TRANSFERS_PER_SECOND = "LJM_STREAM_TRANSFERS_PER_SECOND"

RETRY_ON_TRANSACTION_ID_MISMATCH = "LJM_RETRY_ON_TRANSACTION_ID_MISMATCH"

OLD_FIRMWARE_CHECK = "LJM_OLD_FIRMWARE_CHECK"

USE_TCP_INIT_FOR_T7_WIFI_TCP = "LJM_USE_TCP_INIT_FOR_T7_WIFI_TCP"

ZERO_LENGTH_ARRAY_MODE = "LJM_ZERO_LENGTH_ARRAY_MODE"
ZERO_LENGTH_ARRAY_ERROR = 1
ZERO_LENGTH_ARRAY_IGNORE_OPERATION = 2

DEFAULT_PORT = 502  # Deprecated - use TCP_PORT
UDP_PORT = 52362  # Deprecated - ETHERNET_UDP_PORT or WIFI_UDP_PORT

MAX_TCP_PACKET_NUM_BYTES_T7 = 1040  # Deprecated - Maximum packet size should be read from the getHandleInfo function
MAX_USB_PACKET_NUM_BYTES = 64  # Deprecated - Maximum packet size should be read from the getHandleInfo function
MAX_ETHERNET_PACKET_NUM_BYTES_T7 = 1040  # Deprecated - Maximum packet size should be read from the getHandleInfo function
MAX_WIFI_PACKET_NUM_BYTES_T7 = 500  # Deprecated - Maximum packet size should be read from the getHandleInfo function

SPECIAL_ADDRESSES_FILE = "LJM_SPECIAL_ADDRESSES_FILE"  # Deprecated - use SPECIFIC_IPS_FILE instead
SPECIAL_ADDRESSES_STATUS = "LJM_SPECIAL_ADDRESSES_STATUS"  # Deprecated - use getSpecificIPsInfo function instead

OPEN_MODE = "LJM_OPEN_MODE"  # Deprecated
KEEP_OPEN = 1  # Deprecated
OPEN_CLOSE = 2  # Deprecated
