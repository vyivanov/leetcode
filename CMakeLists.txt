project(leetcode)
cmake_minimum_required(VERSION 3.15)

add_subdirectory(easy)
add_subdirectory(medium)
add_subdirectory(hard)

set(problem_SRCS ${easy_SRCS} ${medium_SRCS} ${hard_SRCS})
add_executable(${CMAKE_PROJECT_NAME}
  ${problem_SRCS}
  main.cpp)

target_compile_definitions(${CMAKE_PROJECT_NAME} PRIVATE _GLIBCXX_DEBUG)
target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE
  -Wall
  -Wextra
  -Wpedantic
  -std=c++20)
