cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)

rosbuild_init()

#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#uncomment if you have defined messages
#rosbuild_genmsg()
#uncomment if you have defined services
rosbuild_gensrv()

#common commands for building c++ executables and libraries
#rosbuild_add_library(${PROJECT_NAME} src/example.cpp)
#target_link_libraries(${PROJECT_NAME} another_library)
#rosbuild_add_boost_directories()
#rosbuild_link_boost(${PROJECT_NAME} thread)
#rosbuild_add_executable(example examples/example.cpp)
#target_link_libraries(example ${PROJECT_NAME})

#rosbuild_add_executable(hsv_camshift src/hsv_camshift.cpp)
#rosbuild_add_executable(rgb_camshift src/rgb_camshift.cpp)
#rosbuild_add_executable(ian_demo src/ian_method_demo.cpp)
#rosbuild_add_executable(ian_method src/ian_method.cpp)
#rosbuild_add_executable(ian_method3 src/ian_method3.cpp)
rosbuild_add_executable(find_by_color src/find_by_color.cpp)
rosbuild_add_executable(color_specific_tracker src/color_specific_tracker.cpp)
rosbuild_add_executable(wubble_world src/wubble_world.cpp)
rosbuild_add_executable(histogram_tool src/histogram_tool.cpp)
