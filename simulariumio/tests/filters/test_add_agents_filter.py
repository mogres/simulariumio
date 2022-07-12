#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from simulariumio import TrajectoryConverter, JsonWriter
from simulariumio.filters import AddAgentsFilter
from simulariumio.tests.conftest import (
    three_default_agents,
    default_agents_type_mapping,
)
from simulariumio.constants import DEFAULT_CAMERA_SETTINGS, CURRENT_VERSION


@pytest.mark.parametrize(
    "trajectory, _filter, expected_data",
    [
        (
            three_default_agents(),
            AddAgentsFilter(new_agent_data=three_default_agents().agent_data),
            {
                "trajectoryInfo": {
                    "version": CURRENT_VERSION.TRAJECTORY_INFO,
                    "timeUnits": {
                        "magnitude": 1.0,
                        "name": "ns",
                    },
                    "timeStepSize": 0.5,
                    "totalSteps": 3,
                    "spatialUnits": {
                        "magnitude": 1.0,
                        "name": "nm",
                    },
                    "size": {"x": 100.0, "y": 100.0, "z": 100.0},
                    "cameraDefault": {
                        "position": {
                            "x": DEFAULT_CAMERA_SETTINGS.CAMERA_POSITION[0],
                            "y": DEFAULT_CAMERA_SETTINGS.CAMERA_POSITION[1],
                            "z": DEFAULT_CAMERA_SETTINGS.CAMERA_POSITION[2],
                        },
                        "lookAtPosition": {
                            "x": DEFAULT_CAMERA_SETTINGS.LOOK_AT_POSITION[0],
                            "y": DEFAULT_CAMERA_SETTINGS.LOOK_AT_POSITION[1],
                            "z": DEFAULT_CAMERA_SETTINGS.LOOK_AT_POSITION[2],
                        },
                        "upVector": {
                            "x": DEFAULT_CAMERA_SETTINGS.UP_VECTOR[0],
                            "y": DEFAULT_CAMERA_SETTINGS.UP_VECTOR[1],
                            "z": DEFAULT_CAMERA_SETTINGS.UP_VECTOR[2],
                        },
                        "fovDegrees": DEFAULT_CAMERA_SETTINGS.FOV_DEGREES,
                    },
                    "typeMapping": default_agents_type_mapping(),
                },
                "spatialData": {
                    "version": CURRENT_VERSION.SPATIAL_DATA,
                    "msgType": 1,
                    "bundleStart": 0,
                    "bundleSize": 3,
                    "bundleData": [
                        {
                            "frameNumber": 0,
                            "time": 0.0,
                            "data": [
                                1000.0,
                                0.0,
                                0.0,
                                4.89610492,
                                -29.81564851,
                                40.77254057,
                                40.77254057,
                                -29.81564851,
                                4.89610492,
                                8.38656327,
                                0.0,
                                1000.0,
                                1.0,
                                1.0,
                                43.43048197,
                                48.00424379,
                                -36.02881338,
                                -36.02881338,
                                48.00424379,
                                43.43048197,
                                6.18568039,
                                0.0,
                                1000.0,
                                2.0,
                                0.0,
                                29.84924588,
                                -38.02769707,
                                2.46644825,
                                2.46644825,
                                -38.02769707,
                                29.84924588,
                                6.61459206,
                                0.0,
                                1000.0,
                                3.0,
                                0.0,
                                4.89610492,
                                -29.81564851,
                                40.77254057,
                                40.77254057,
                                -29.81564851,
                                4.89610492,
                                8.38656327,
                                0.0,
                                1000.0,
                                4.0,
                                1.0,
                                43.43048197,
                                48.00424379,
                                -36.02881338,
                                -36.02881338,
                                48.00424379,
                                43.43048197,
                                6.18568039,
                                0.0,
                                1000.0,
                                5.0,
                                0.0,
                                29.84924588,
                                -38.02769707,
                                2.46644825,
                                2.46644825,
                                -38.02769707,
                                29.84924588,
                                6.61459206,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 1,
                            "time": 0.5,
                            "data": [
                                1000.0,
                                0.0,
                                1.0,
                                -43.37181102,
                                -13.41127423,
                                -17.31316927,
                                -17.31316927,
                                -13.41127423,
                                -43.37181102,
                                5.26366739,
                                0.0,
                                1000.0,
                                1.0,
                                2.0,
                                9.62132397,
                                13.4774314,
                                -20.30846039,
                                -20.30846039,
                                13.4774314,
                                9.62132397,
                                6.69209780,
                                0.0,
                                1000.0,
                                2.0,
                                3.0,
                                41.41039848,
                                -45.85543786,
                                49.06208485,
                                49.06208485,
                                -45.85543786,
                                41.41039848,
                                9.88033853,
                                0.0,
                                1000.0,
                                3.0,
                                1.0,
                                -43.37181102,
                                -13.41127423,
                                -17.31316927,
                                -17.31316927,
                                -13.41127423,
                                -43.37181102,
                                5.26366739,
                                0.0,
                                1000.0,
                                4.0,
                                2.0,
                                9.62132397,
                                13.4774314,
                                -20.30846039,
                                -20.30846039,
                                13.4774314,
                                9.62132397,
                                6.69209780,
                                0.0,
                                1000.0,
                                5.0,
                                3.0,
                                41.41039848,
                                -45.85543786,
                                49.06208485,
                                49.06208485,
                                -45.85543786,
                                41.41039848,
                                9.88033853,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 2,
                            "time": 1.0,
                            "data": [
                                1000.0,
                                0.0,
                                4.0,
                                -24.91450698,
                                -44.79360525,
                                13.32273796,
                                13.32273796,
                                -44.79360525,
                                -24.91450698,
                                8.91022619,
                                0.0,
                                1000.0,
                                1.0,
                                5.0,
                                4.10861266,
                                43.86451151,
                                21.93697483,
                                21.93697483,
                                43.86451151,
                                4.10861266,
                                9.01379396,
                                0.0,
                                1000.0,
                                2.0,
                                6.0,
                                -7.16740679,
                                -13.06491594,
                                44.97026158,
                                44.97026158,
                                -13.06491594,
                                -7.16740679,
                                8.39880154,
                                0.0,
                                1000.0,
                                3.0,
                                4.0,
                                -24.91450698,
                                -44.79360525,
                                13.32273796,
                                13.32273796,
                                -44.79360525,
                                -24.91450698,
                                8.91022619,
                                0.0,
                                1000.0,
                                4.0,
                                5.0,
                                4.10861266,
                                43.86451151,
                                21.93697483,
                                21.93697483,
                                43.86451151,
                                4.10861266,
                                9.01379396,
                                0.0,
                                1000.0,
                                5.0,
                                6.0,
                                -7.16740679,
                                -13.06491594,
                                44.97026158,
                                44.97026158,
                                -13.06491594,
                                -7.16740679,
                                8.39880154,
                                0.0,
                            ],
                        },
                    ],
                },
                "plotData": {"version": CURRENT_VERSION.PLOT_DATA, "data": []},
            },
        ),
    ],
)
def test_add_agents_filter(trajectory, _filter, expected_data):
    converter = TrajectoryConverter(trajectory)
    filtered_data = converter.filter_data([_filter])
    buffer_data = JsonWriter.format_trajectory_data(filtered_data)
    assert expected_data == buffer_data
    assert JsonWriter._check_agent_ids_are_unique_per_frame(buffer_data)
