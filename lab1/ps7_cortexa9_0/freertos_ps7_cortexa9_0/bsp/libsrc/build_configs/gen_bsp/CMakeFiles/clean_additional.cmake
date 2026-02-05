# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "")
  file(REMOVE_RECURSE
  "C:\\Users\\wewanchu\\School\\ECE315\\lab1\\ECE315lab1\\lab1\\ps7_cortexa9_0\\freertos_ps7_cortexa9_0\\bsp\\include\\sleep.h"
  "C:\\Users\\wewanchu\\School\\ECE315\\lab1\\ECE315lab1\\lab1\\ps7_cortexa9_0\\freertos_ps7_cortexa9_0\\bsp\\include\\xiltimer.h"
  "C:\\Users\\wewanchu\\School\\ECE315\\lab1\\ECE315lab1\\lab1\\ps7_cortexa9_0\\freertos_ps7_cortexa9_0\\bsp\\include\\xtimer_config.h"
  "C:\\Users\\wewanchu\\School\\ECE315\\lab1\\ECE315lab1\\lab1\\ps7_cortexa9_0\\freertos_ps7_cortexa9_0\\bsp\\lib\\libxiltimer.a"
  )
endif()
