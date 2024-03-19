#!/usr/bin/env bash

readonly BUILD_DIR=build-auto

function run_analysis() {
  echo '------ [ANALYSIS] ------'
  if ! mypy --pretty ./; then
    return 100
  fi
}

function build_solutions() {
  echo '------ [BUILD] ------'
  rm -rf ${BUILD_DIR:?}/ && \
  cmake -B${BUILD_DIR} -S./ -G'Unix Makefiles' -DCMAKE_BUILD_TYPE=Debug && \
  cmake --build ${BUILD_DIR} --config Debug --target leetcode -- -j "$(nproc --all)"
}

function run_tests() {
  echo '------ [TESTS] ------'
  echo '... C++ ...'
  ${BUILD_DIR}/leetcode
  echo '... Python ...'
  local TESTS
  TESTS=$(find . -type f -name '*.py')
  readonly TESTS
  local counter
  counter=1
  for file in ${TESTS}; do
    if ! python3 "${file}"; then
      return 150
    fi
    printf '%03d) %s [OK]\n' "${counter}" "${file}"
    ((counter++))
  done
}

function show_dirties() {
  local DIRTIES
  DIRTIES=$(grep      \
    --recursive       \
    --line-number     \
    --include '*.cpp' \
    --include '*.py'  \
    --extended-regexp '(TODO|FIXME|XXX)')
  readonly DIRTIES
  if [ -n "${DIRTIES}" ]; then
    echo '------ [DIRTIES] ------'
    echo "${DIRTIES}"
  fi
}

time (                \
  run_analysis;       \
  build_solutions &&  \
  run_tests &&        \
  show_dirties        \
)
