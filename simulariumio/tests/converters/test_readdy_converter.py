#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pytest

from simulariumio.readdy import ReaddyConverter, ReaddyData
from simulariumio import UnitData, MetaData, DisplayData, JsonWriter
from simulariumio.constants import (
    DEFAULT_CAMERA_SETTINGS,
    CURRENT_VERSION,
    DISPLAY_TYPE,
)


@pytest.mark.parametrize(
    "trajectory, expected_data",
    [
        # 4 particles 3 frames
        (
            ReaddyData(
                meta_data=MetaData(
                    box_size=np.array([20.0, 20.0, 20.0]),
                ),
                timestep=0.1,
                path_to_readdy_h5="simulariumio/tests/data/readdy/test.h5",
                display_data={
                    "A": DisplayData(
                        name="C",
                        display_type=DISPLAY_TYPE.SPHERE,
                        radius=3.0,
                        color="#0080ff",
                    ),
                    "B": DisplayData(
                        name="B",
                        radius=2.0,
                        display_type=DISPLAY_TYPE.OBJ,
                        url="c.obj",
                        color="#dfdacd",
                    ),
                    "D": DisplayData(
                        name="C",
                        display_type=DISPLAY_TYPE.SPHERE,
                        radius=3.0,
                        color="#0080ff",
                    ),
                },
                ignore_types=["E"],
                time_units=UnitData("ms", 1e-6),
                spatial_units=UnitData("nm"),
            ),
            {
                "trajectoryInfo": {
                    "version": CURRENT_VERSION.TRAJECTORY_INFO,
                    "timeUnits": {
                        "magnitude": 1.0,
                        "name": "ns",
                    },
                    "timeStepSize": 0.1,
                    "totalSteps": 3,
                    "spatialUnits": {
                        "magnitude": 1.0,
                        "name": "nm",
                    },
                    "size": {"x": 20.0, "y": 20.0, "z": 20.0},
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
                            "name": "C",
                            "geometry": {
                                "displayType": "SPHERE",
                                "color": "#0080ff",
                            },
                        },
                        "1": {
                            "name": "B",
                            "geometry": {
                                "displayType": "OBJ",
                                "url": "c.obj",
                                "color": "#dfdacd",
                            },
                        },
                    },
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
                                -4.076107488021348,
                                3.9849372168961708,
                                7.892235671222785,
                                0.0,
                                0.0,
                                0.0,
                                3.0,
                                0.0,
                                1000.0,
                                1.0,
                                1.0,
                                -2.780407911074236,
                                4.762366216929244,
                                9.202490133610398,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                2.0,
                                0.0,
                                8.19869797660185,
                                1.4425866729829266,
                                6.215047907498356,
                                0.0,
                                0.0,
                                0.0,
                                3.0,
                                0.0,
                                1000.0,
                                3.0,
                                1.0,
                                8.66544980756901,
                                1.97558947182814,
                                8.08535556794141,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 1,
                            "time": 0.1,
                            "data": [
                                1000.0,
                                0.0,
                                0.0,
                                -3.600301271046627,
                                4.360124409946104,
                                6.956371030429721,
                                0.0,
                                0.0,
                                0.0,
                                3.0,
                                0.0,
                                1000.0,
                                1.0,
                                1.0,
                                -2.761977374836856,
                                4.835017769931593,
                                9.136878226258032,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                2.0,
                                0.0,
                                7.755862317430045,
                                1.3102736549734222,
                                6.862906605118455,
                                0.0,
                                0.0,
                                0.0,
                                3.0,
                                0.0,
                                1000.0,
                                3.0,
                                1.0,
                                8.704102749692902,
                                1.8166930930965905,
                                7.8727242890809475,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                        {
                            "frameNumber": 2,
                            "time": 0.2,
                            "data": [
                                1000.0,
                                0.0,
                                0.0,
                                -2.5613935239104135,
                                5.2768511678362575,
                                -9.666619435197141,
                                0.0,
                                0.0,
                                0.0,
                                3.0,
                                0.0,
                                1000.0,
                                1.0,
                                1.0,
                                -4.252869632733068,
                                4.420710058343225,
                                6.427577234992345,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                2.0,
                                0.0,
                                4.230292288749659,
                                0.2170518151763472,
                                3.88903614029613,
                                0.0,
                                0.0,
                                0.0,
                                3.0,
                                0.0,
                                1000.0,
                                3.0,
                                1.0,
                                -8.417490965010238,
                                4.002378907710486,
                                -9.198614964227042,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                            ],
                        },
                    ],
                },
                "plotData": {"version": CURRENT_VERSION.PLOT_DATA, "data": []},
            },
        )
    ],
)
def test_readdy_converter(trajectory, expected_data):
    converter = ReaddyConverter(trajectory)
    buffer_data = JsonWriter.format_trajectory_data(converter._data)
    assert expected_data == buffer_data
    assert JsonWriter._check_agent_ids_are_unique_per_frame(buffer_data)
