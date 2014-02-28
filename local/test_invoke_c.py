from ctypes import *
import os

isRotate = cdll.LoadLibrary(os.getcwd() + "/socket_test_local.so")
print isRotate.unix_socket_send("121dsdsdsdssdsds");
