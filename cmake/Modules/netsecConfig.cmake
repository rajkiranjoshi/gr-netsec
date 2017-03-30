INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_NETSEC netsec)

FIND_PATH(
    NETSEC_INCLUDE_DIRS
    NAMES netsec/api.h
    HINTS $ENV{NETSEC_DIR}/include
        ${PC_NETSEC_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    NETSEC_LIBRARIES
    NAMES gnuradio-netsec
    HINTS $ENV{NETSEC_DIR}/lib
        ${PC_NETSEC_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(NETSEC DEFAULT_MSG NETSEC_LIBRARIES NETSEC_INCLUDE_DIRS)
MARK_AS_ADVANCED(NETSEC_LIBRARIES NETSEC_INCLUDE_DIRS)

