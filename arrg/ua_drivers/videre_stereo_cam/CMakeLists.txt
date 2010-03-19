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
#rosbuild_gensrv()

#common commands for building c++ executables and libraries
#rosbuild_add_library(${PROJECT_NAME} src/example.cpp)
#target_link_libraries(${PROJECT_NAME} another_library)
#rosbuild_add_boost_directories()
#rosbuild_link_boost(${PROJECT_NAME} thread)
#rosbuild_add_executable(example examples/example.cpp)
#target_link_libraries(example ${PROJECT_NAME})

rosbuild_add_library(videre_stereo_cam src/videre_stereo_cam/stereolib.c src/videre_stereo_cam/stereolib2.cpp src/videre_stereo_cam/stereodcam.cpp src/videre_stereo_cam/stereoimage.cpp)
rosbuild_add_compile_flags(videre_stereo_cam "-msse2 -mpreferred-stack-boundary=4")
target_link_libraries(videre_stereo_cam dcam1394 videre_stereo_cam)

rosbuild_add_executable(videre_stereo_node src/videre_stereo_node.cpp)
rosbuild_add_compile_flags(videre_stereo_node -msse3)
target_link_libraries(videre_stereo_node videre_stereo_cam)
