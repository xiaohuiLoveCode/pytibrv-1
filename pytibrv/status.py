##
# tibrv/status.py
#   TIBRV Library for PYTHON
#
# LAST MODIFIED : V1.0 20161211 ARIEN
#
# DESCRIPTIONS
# ---------------------------------------------------
#
#
# FEATURES: * = un-implement
# ------------------------------------------------------
#   tibrvStatus_GetText
#
# CHANGED LOGS
# ---------------------------------------------------
# 20161211 ARIEN V1.0
#   CREATED
#
##

import ctypes as _ctypes
from .api import _rv
from .api import *

##-----------------------------------------------------------------------------
## CONSTANTS
# tibrv/status.h

TIBRV_OK                        = 0
TIBRV_INIT_FAILURE              = 1
TIBRV_INVALID_TRANSPORT         = 2
TIBRV_INVALID_ARG               = 3
TIBRV_NOT_INITIALIZED           = 4
TIBRV_ARG_CONFLICT              = 5

TIBRV_SERVICE_NOT_FOUND         = 16
TIBRV_NETWORK_NOT_FOUND         = 17
TIBRV_DAEMON_NOT_FOUND          = 18
TIBRV_NO_MEMORY                 = 19
TIBRV_INVALID_SUBJECT           = 20
TIBRV_DAEMON_NOT_CONNECTED      = 21
TIBRV_VERSION_MISMATCH          = 22
TIBRV_SUBJECT_COLLISION         = 23
TIBRV_VC_NOT_CONNECTED          = 24

TIBRV_NOT_PERMITTED             = 27

TIBRV_INVALID_NAME              = 30
TIBRV_INVALID_TYPE              = 31
TIBRV_INVALID_SIZE              = 32
TIBRV_INVALID_COUNT             = 33

TIBRV_NOT_FOUND                 = 35
TIBRV_ID_IN_USE                 = 36
TIBRV_ID_CONFLICT               = 37
TIBRV_CONVERSION_FAILED         = 38
TIBRV_RESERVED_HANDLER          = 39
TIBRV_ENCODER_FAILED            = 40
TIBRV_DECODER_FAILED            = 41
TIBRV_INVALID_MSG               = 42
TIBRV_INVALID_FIELD             = 43
TIBRV_INVALID_INSTANCE          = 44
TIBRV_CORRUPT_MSG               = 45
TIBRV_ENCODING_MISMATCH         = 46

TIBRV_TIMEOUT                   = 50
TIBRV_INTR                      = 51

TIBRV_INVALID_DISPATCHABLE      = 52
TIBRV_INVALID_DISPATCHER        = 53

TIBRV_INVALID_EVENT             = 60
TIBRV_INVALID_CALLBACK          = 61
TIBRV_INVALID_QUEUE             = 62
TIBRV_INVALID_QUEUE_GROUP       = 63

TIBRV_INVALID_TIME_INTERVAL     = 64

TIBRV_INVALID_IO_SOURCE         = 65
TIBRV_INVALID_IO_CONDITION      = 66
TIBRV_SOCKET_LIMIT              = 67

TIBRV_OS_ERROR                  = 68

TIBRV_INSUFFICIENT_BUFFER       = 70
TIBRV_EOF                       = 71
TIBRV_INVALID_FILE              = 72
TIBRV_FILE_NOT_FOUND            = 73
TIBRV_IO_FAILED                 = 74

TIBRV_NOT_FILE_OWNER            = 80
TIBRV_USERPASS_MISMATCH         = 81

TIBRV_TOO_MANY_NEIGHBORS        = 90
TIBRV_ALREADY_EXISTS            = 91

TIBRV_PORT_BUSY                 = 100
TIBRV_DELIVERY_FAILED           = 101
TIBRV_QUEUE_LIMIT               = 102

TIBRV_INVALID_CONTENT_DESC      = 110
TIBRV_INVALID_SERIALIZED_BUFFER = 111
TIBRV_DESCRIPTOR_NOT_FOUND      = 115
TIBRV_CORRUPT_SERIALIZED_BUFFER = 116

TIBRV_IPM_ONLY                  = 117

##-----------------------------------------------------------------------------
##
# tibrv/status.h
# const char * tibrv_GetText(tibrv_status)
#
_rv.tibrvStatus_GetText.argtypes = [c_tibrv_status]
_rv.tibrvStatus_GetText.restype = _ctypes.c_char_p


def tibrvStatus_GetText(code: tibrv_status) -> str:
    c = c_tibrv_status(code)
    sz = _rv.tibrvStatus_GetText(c)
    return sz.decode()

class TibrvError(Exception):
    def __init__(self, code: tibrv_status, text = None):
        self._err = code
        self._text = text

    def __str__(self):
        return self.text()

    def code(self) -> tibrv_status:
        return self._err

    def text(self) -> str:
        if self._text is None:
            return tibrvStatus_GetText(self._err)
        else:
            return self._text

    def isOK(self) -> bool:
        if self._err == TIBRV_OK:
            return True
        else:
            return False

class TibrvStatus:

    _exception = False

    @staticmethod
    def exception(*args):
        if len(args) == 0:
            return TibrvStatus._exception
        if args[0]:
            TibrvStatus._exception = True
        else:
            TibrvStatus._exception = False

    @staticmethod
    def text(code: tibrv_status) -> str:
        return tibrvStatus_GetText(code)

    @staticmethod
    def error(code: tibrv_status, text = None) -> TibrvError:
        if code == TIBRV_OK:
            return None

        ex = TibrvError(code, text)

        if TibrvStatus._exception:
            raise ex

        return ex

