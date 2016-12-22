##
# pytibrv use Python standard library : ctypes as the wrapper to TIBRV C API
# It is not a Python Extension, not required to re-compile C Source(Python Extension) 
# for deployment. 
# 
# In practice,
# TIBRV would be installed at /opt/tibco/tibrv for multiple version
# 
# /opt/tibco/tibrv/
#                  8.4.1/
#                  8.4.2/
#                  8.4.5/
# 
# The environment variable LD_LIBRARY_PATH, wuld be set to indicate specific TIBRV version.
# ex:
#   TIBRV_HOME=/opt/tibco/tibrv/8.4.5
#   LD_LIBRARY_PATH=${TIBRV_HOME}/lib:$LD_LIBRARY_PATH
# 
# For Windows, it would like as 
# 
# d:\tibco\tibrv\
#                8.4.1\
#                8.4.2\
#                8.4.5\
# 
# The environment variable Path, wuld be set to indicate specific TIBRV version.
# ex:
#   TIBRV_HOME=d:\tibco\tibrv\8.4.5
#   Path=%TIBRV_HOME%\bin;%Path%
# 
# ctypes LoadLibrary behave different for OS
#
# In Darwin(OSX)
#   find_library() would search in LD_LIBRARY_PATH and return the full path
#   ex: 
#   lib = find_library('C') -> '/opt/tibco/tibrv/8.4.5/lib/libtibrv64.dylib'
#   _rv = ctypes.cdll.LoadLibrary(lib) 
# 
# In Linux
#   find_library() use 'ldconfig -p' to find the lib name
#   just call LoadLibrary() 
#   ex: 
#   find_library('tibrv64')       -> None 
#   find_library('libtibrv64.so') -> None 
#   _rv = ctypes.cdll.LoadLibrary('libtibrv64.so') 
# 
# In Windows
#   find_library() would searcho DLL in Path and return full path
#   lib = dind_library('tibrv')   -> 'd:\\tibco\\tibrv\\8.4.5\\bin\\tibrv.dll' 
#   _rv = _ctypes.windll.LoadLibrary(lib)
# 
# 
__version__ = '1.0.0'
__all__ = ['api', 'status', 'tport', 'queue', 'events', 'disp', 'msg']