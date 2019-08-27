cmake_minimum_required(VERSION 2.8.3)

project(turtlebot_lidar_tasks)

find_package(catkin REQUIRED COMPONENTS	message_generation)

add_service_files(DIRECTORY srv
                  FILES
                  SetBatteryLevel.srv)

generate_messages()

catkin_package(DEPENDS CATKIN DEPENDS message_runtime)

#catkin_python_setup()

#catkin_install_python(PROGRAMS examples/parallel_example.py
#                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
