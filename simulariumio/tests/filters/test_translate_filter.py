#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy as np

from simulariumio import FileConverter
from simulariumio.filters import TranslateFilter


@pytest.mark.parametrize(
    "input_path, _filter, expected_data",
    [
        (
            # translate agents
            "simulariumio/tests/data/cytosim/aster_pull3D_couples_actin_solid_3_frames"
            "/aster_pull3D_couples_actin_solid_3_frames_small.json",
            TranslateFilter(translation_per_type_id={1: np.array([10, 0, 50])}),
            {
                "trajectoryInfo": {
                    "version": 2,
                    "timeUnits": {
                        "magnitude": 1.0,
                        "name": "s",
                    },
                    "timeStepSize": 0.05,
                    "totalSteps": 3,
                    "spatialUnits": {
                        "magnitude": 1.0,
                        "name": "µm",
                    },
                    "size": {"x": 200.0, "y": 200.0, "z": 200.0},
                    "typeMapping": {
                        "1": {"name": "microtubule"},
                        "7": {"name": "motor complex"},
                    },
                },
                "spatialData": {
                    "version": 1,
                    "msgType": 1,
                    "bundleStart": 0,
                    "bundleSize": 3,
                    "bundleData": [
                        {
                            "frameNumber": 0,
                            "time": 0.0,
                            "data": [
                                1001.0,
                                1.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                15.0,
                                46.93,
                                36.8,
                                66.78,
                                40.55,
                                43.87,
                                69.84,
                                34.17,
                                50.93,
                                72.900000000000002,
                                27.78,
                                57.99999999999999,
                                75.95,
                                21.4,
                                65.07,
                                79.01,
                                1000.0,
                                12.0,
                                7.0,
                                -73.8,
                                -25.2,
                                -43.89,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 1,
                            "time": 0.05,
                            "data": [
                                1001.0,
                                1.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                18.0,
                                54.55,
                                33.97,
                                58.86,
                                46.63,
                                38.269999999999996,
                                54.51,
                                38.96,
                                43.28,
                                50.5,
                                31.83,
                                49.61,
                                47.48,
                                26.0,
                                57.66,
                                46.42,
                                22.85,
                                66.92,
                                48.53,
                                1000.0,
                                12.0,
                                7.0,
                                -72.519999999999996,
                                -21.9,
                                -43.59,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 2,
                            "time": 0.1,
                            "data": [
                                1001.0,
                                1.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                15.0,
                                54.55,
                                33.97,
                                58.86,
                                46.63,
                                38.269999999999996,
                                54.51,
                                38.96,
                                43.28,
                                50.5,
                                31.83,
                                49.61,
                                47.48,
                                26.0,
                                57.66,
                                46.42,
                                1000.0,
                                12.0,
                                7.0,
                                -72.519999999999996,
                                -21.9,
                                -43.59,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                    ],
                },
                "plotData": {"version": 1, "data": []},
            },
        ),
    ],
)
def test_translate_filter(input_path, _filter, expected_data):
    converter = FileConverter(input_path)
    filtered_data = converter.filter_data([_filter])
    buffer_data = converter._read_trajectory_data(filtered_data)
    assert expected_data == buffer_data
