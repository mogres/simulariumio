#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from simulariumio.springsalad import SpringsaladConverter, SpringsaladData
from simulariumio import DisplayData, MetaData, InputFileData, JsonWriter
from simulariumio.constants import (
    DEFAULT_CAMERA_SETTINGS,
    CURRENT_VERSION,
    DISPLAY_TYPE,
)


@pytest.mark.parametrize(
    "trajectory, expected_data",
    [
        # truncated data from tutorial example
        (
            SpringsaladData(
                sim_view_txt_file=InputFileData(
                    file_path=(
                        "simulariumio/tests/data/springsalad/"
                        "Simulation0_SIM_VIEW_Run0.txt"
                    ),
                ),
                meta_data=MetaData(
                    scale_factor=0.1,
                ),
                display_data={
                    "GREEN": DisplayData(
                        name="A",
                        radius=10.0,
                        display_type=DISPLAY_TYPE.OBJ,
                        url="a.obj",
                        color="#dfdacd",
                    ),
                    "RED": DisplayData(
                        name="B",
                        display_type=DISPLAY_TYPE.SPHERE,
                        color="#0080ff",
                    ),
                },
                draw_bonds=False,
            ),
            {
                "trajectoryInfo": {
                    "version": CURRENT_VERSION.TRAJECTORY_INFO,
                    "timeUnits": {
                        "magnitude": 1.0,
                        "name": "s",
                    },
                    "timeStepSize": 0.1,
                    "totalSteps": 2,
                    "spatialUnits": {
                        "magnitude": 10.0,
                        "name": "nm",
                    },
                    "size": {"x": 10.0, "y": 10.0, "z": 20.0},
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
                    "typeMapping": {
                        "0": {
                            "name": "A",
                            "geometry": {
                                "displayType": "OBJ",
                                "url": "a.obj",
                                "color": "#dfdacd",
                            },
                        },
                        "1": {
                            "name": "B",
                            "geometry": {
                                "displayType": "SPHERE",
                                "color": "#0080ff",
                            },
                        },
                        "2": {
                            "name": "GRAY",
                            "geometry": {
                                "displayType": "SPHERE",
                            },
                        },
                        "3": {
                            "name": "CYAN",
                            "geometry": {
                                "displayType": "SPHERE",
                            },
                        },
                        "4": {
                            "name": "BLUE",
                            "geometry": {
                                "displayType": "SPHERE",
                            },
                        },
                    },
                },
                "spatialData": {
                    "version": CURRENT_VERSION.SPATIAL_DATA,
                    "msgType": 1,
                    "bundleStart": 0,
                    "bundleSize": 2,
                    "bundleData": [
                        {
                            "frameNumber": 0,
                            "time": 0.0,
                            "data": [
                                1000.0,
                                100000000.0,
                                0.0,
                                -2.3515194000000004,
                                4.1677663,
                                -0.2872943,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                100010000.0,
                                0.0,
                                -1.1726563,
                                3.7363461000000004,
                                -0.47181300000000004,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                100200001.0,
                                1.0,
                                -0.3749313,
                                0.6674895000000001,
                                -0.5000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100200000.0,
                                2.0,
                                -0.3749313,
                                0.6674895000000001,
                                0.000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100200002.0,
                                3.0,
                                -0.3749313,
                                0.6674895000000001,
                                0.5000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100300000.0,
                                4.0,
                                -2.9673074,
                                0.5123882000000001,
                                5.0633669,
                                0.0,
                                0.0,
                                0.0,
                                0.1,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 1,
                            "time": 0.10000000998802996,
                            "data": [
                                1000.0,
                                100200001.0,
                                1.0,
                                3.8385084999999997,
                                -2.5307899000000003,
                                -0.5000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100200000.0,
                                2.0,
                                3.7610036000000004,
                                -2.4899603,
                                0.000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100200002.0,
                                3.0,
                                3.6784268,
                                -2.5100304,
                                0.5000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100210001.0,
                                1.0,
                                0.9422604,
                                1.1849763,
                                -0.5000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100300000.0,
                                4.0,
                                1.7784686,
                                0.8480382000000001,
                                1.8389947,
                                0.0,
                                0.0,
                                0.0,
                                0.1,
                                0.0,
                            ],
                        },
                    ],
                },
                "plotData": {"version": CURRENT_VERSION.PLOT_DATA, "data": []},
            },
        ),
        # truncated data from tutorial example (and draw bonds)
        (
            SpringsaladData(
                sim_view_txt_file=InputFileData(
                    file_path=(
                        "simulariumio/tests/data/springsalad/"
                        "Simulation0_SIM_VIEW_Run0.txt"
                    ),
                ),
                meta_data=MetaData(
                    scale_factor=0.1,
                ),
                display_data={
                    "GREEN": DisplayData(
                        name="A",
                        radius=10.0,
                        display_type=DISPLAY_TYPE.OBJ,
                        url="a.obj",
                        color="#dfdacd",
                    ),
                    "RED": DisplayData(
                        name="B",
                        display_type=DISPLAY_TYPE.SPHERE,
                        color="#0080ff",
                    ),
                },
            ),
            {
                "trajectoryInfo": {
                    "version": CURRENT_VERSION.TRAJECTORY_INFO,
                    "timeUnits": {
                        "magnitude": 1.0,
                        "name": "s",
                    },
                    "timeStepSize": 0.1,
                    "totalSteps": 2,
                    "spatialUnits": {
                        "magnitude": 10.0,
                        "name": "nm",
                    },
                    "size": {"x": 10.0, "y": 10.0, "z": 20.0},
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
                    "typeMapping": {
                        "0": {
                            "name": "A",
                            "geometry": {
                                "displayType": "OBJ",
                                "url": "a.obj",
                                "color": "#dfdacd",
                            },
                        },
                        "1": {
                            "name": "B",
                            "geometry": {
                                "displayType": "SPHERE",
                                "color": "#0080ff",
                            },
                        },
                        "2": {
                            "name": "GRAY",
                            "geometry": {
                                "displayType": "SPHERE",
                            },
                        },
                        "3": {
                            "name": "CYAN",
                            "geometry": {
                                "displayType": "SPHERE",
                            },
                        },
                        "4": {
                            "name": "BLUE",
                            "geometry": {
                                "displayType": "SPHERE",
                            },
                        },
                        "5": {
                            "name": "Link",
                            "geometry": {
                                "displayType": "FIBER",
                            },
                        },
                    },
                },
                "spatialData": {
                    "version": CURRENT_VERSION.SPATIAL_DATA,
                    "msgType": 1,
                    "bundleStart": 0,
                    "bundleSize": 2,
                    "bundleData": [
                        {
                            "frameNumber": 0,
                            "time": 0.0,
                            "data": [
                                1000.0,
                                100000000.0,
                                0.0,
                                -2.3515194000000004,
                                4.1677663,
                                -0.2872943,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                100010000.0,
                                0.0,
                                -1.1726563,
                                3.7363461000000004,
                                -0.47181300000000004,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                100200001.0,
                                1.0,
                                -0.3749313,
                                0.6674895000000001,
                                -0.5000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100200000.0,
                                2.0,
                                -0.3749313,
                                0.6674895000000001,
                                0.000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100200002.0,
                                3.0,
                                -0.3749313,
                                0.6674895000000001,
                                0.5000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100300000.0,
                                4.0,
                                -2.9673074,
                                0.5123882000000001,
                                5.0633669,
                                0.0,
                                0.0,
                                0.0,
                                0.1,
                                0.0,
                                1001.0,
                                0.0,
                                5.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                -0.3749313,
                                0.6674895000000001,
                                0.000000,
                                -0.3749313,
                                0.6674895000000001,
                                -0.5000000,
                                1001.0,
                                1.0,
                                5.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                -0.3749313,
                                0.6674895000000001,
                                0.000000,
                                -0.3749313,
                                0.6674895000000001,
                                0.5000000,
                            ],
                        },
                        {
                            "frameNumber": 1,
                            "time": 0.10000000998802996,
                            "data": [
                                1000.0,
                                100200001.0,
                                1.0,
                                3.8385084999999997,
                                -2.5307899000000003,
                                -0.5000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100200000.0,
                                2.0,
                                3.7610036000000004,
                                -2.4899603,
                                0.000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100200002.0,
                                3.0,
                                3.6784268,
                                -2.5100304,
                                0.5000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100210001.0,
                                1.0,
                                0.9422604,
                                1.1849763,
                                -0.5000000,
                                0.0,
                                0.0,
                                0.0,
                                0.2,
                                0.0,
                                1000.0,
                                100300000.0,
                                4.0,
                                1.7784686,
                                0.8480382000000001,
                                1.8389947,
                                0.0,
                                0.0,
                                0.0,
                                0.1,
                                0.0,
                                1001.0,
                                0.0,
                                5.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                3.7610036000000004,
                                -2.4899603,
                                0.000000,
                                3.8385084999999997,
                                -2.5307899000000003,
                                -0.5000000,
                                1001.0,
                                1.0,
                                5.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                3.7610036000000004,
                                -2.4899603,
                                0.000000,
                                3.6784268,
                                -2.5100304,
                                0.5000000,
                            ],
                        },
                    ],
                },
                "plotData": {"version": CURRENT_VERSION.PLOT_DATA, "data": []},
            },
        ),
    ],
)
def test_springsalad_converter(trajectory, expected_data):
    converter = SpringsaladConverter(trajectory)
    buffer_data = JsonWriter.format_trajectory_data(converter._data)
    assert expected_data == buffer_data
    assert JsonWriter._check_agent_ids_are_unique_per_frame(buffer_data)
