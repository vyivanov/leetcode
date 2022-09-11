#!/usr/bin/env bash

function run_analysis() {
    echo '------ [MYPY] ------'
    if ! mypy --pretty ./; then
        return 100
    fi
}

function run_tests() {
    local tests
    local counter
    tests=$(find . -type f -name '*.py')
    counter=1
    echo '------ [TEST] ------'
    for file in ${tests}; do
        if ! python3 "${file}"; then
            return 150
        fi
        printf '%02d) %s [OK]\n' "${counter}" "${file}"
        ((counter++))
    done
}

function show_dirt() {
    local script
    script=$(basename "${0}")
    dirt=$(grep --recursive           \
                --line-number         \
                --exclude "${script}" \
                --extended-regexp '(TODO|FIXME|XXX)')
    if [ -n "${dirt}" ]; then
        echo '------ [DIRT] ------'
        echo "${dirt}"
    fi
}

time (run_analysis && run_tests && show_dirt)
