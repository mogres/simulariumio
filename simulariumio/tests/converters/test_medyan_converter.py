#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pytest

from simulariumio.medyan import MedyanConverter, MedyanData
from simulariumio import MetaData, DisplayData, InputFileData, JsonWriter
from simulariumio.constants import DEFAULT_CAMERA_SETTINGS, CURRENT_VERSION


@pytest.mark.parametrize(
    "trajectory, expected_data",
    [
        # truncated data from 50filaments_motor_linker example
        (
            MedyanData(
                meta_data=MetaData(
                    box_size=np.array([1000.0, 1000.0, 500.0]),
                ),
                snapshot_file=InputFileData(
                    file_path="simulariumio/tests/data/medyan/snapshot.traj"
                ),
                filament_display_data={
                    0: DisplayData(
                        name="Actin",
                        radius=2,
                        color="#d71f5f",
                    ),
                },
                linker_display_data={
                    1: DisplayData(
                        name="Xlink",
                        radius=0.5,
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
                    "timeStepSize": 1.0,
                    "totalSteps": 3,
                    "spatialUnits": {
                        "magnitude": 1.0,
                        "name": "nm",
                    },
                    "size": {"x": 1000.0, "y": 1000.0, "z": 500.0},
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
                            "name": "Actin",
                            "geometry": {
                                "displayType": "FIBER",
                                "color": "#d71f5f",
                            },
                        },
                        "1": {
                            "name": "linker0",
                            "geometry": {
                                "displayType": "FIBER",
                            },
                        },
                        "2": {
                            "name": "Xlink",
                            "geometry": {
                                "displayType": "FIBER",
                                "color": "#0080ff",
                            },
                        },
                        "3": {
                            "name": "linker2",
                            "geometry": {
                                "displayType": "FIBER",
                            },
                        },
                        "4": {
                            "name": "motor1",
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
                    "bundleSize": 3,
                    "bundleData": [
                        {
                            "frameNumber": 0,
                            "time": 0.0,
                            "data": [
                                1001.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                6.0,
                                454.3434234,
                                363.439226,
                                265.4405349,
                                519.7377041,
                                351.5737487,
                                180.312405,
                                1001.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                6.0,
                                547.5943503,
                                280.3075619,
                                307.4127023,
                                535.194707,
                                173.0325428,
                                308.9355694,
                            ],
                        },
                        {
                            "frameNumber": 1,
                            "time": 1.000038293,
                            "data": [
                                1001.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                18.0,
                                443.3162276,
                                369.8644852,
                                293.1521372,
                                458.4600122,
                                366.5425284,
                                274.4414626,
                                525.5102849,
                                351.3129172,
                                191.1648549,
                                595.4174881,
                                336.6403217,
                                110.1741389,
                                672.5234407,
                                322.3132598,
                                35.94250437,
                                678.3129825,
                                321.2378855,
                                30.3779709,
                                1001.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                15.0,
                                549.7619454,
                                310.7627687,
                                302.0296124,
                                547.773019,
                                286.5808386,
                                303.3456815,
                                537.9496947,
                                179.2424416,
                                309.5407552,
                                518.8214547,
                                73.12680239,
                                314.8723733,
                                509.9893907,
                                28.15495189,
                                317.0372613,
                                1001.0,
                                2.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                216.8006048,
                                854.8097767,
                                302.9108981,
                                191.2656514,
                                867.5975965,
                                281.4725825,
                                1001.0,
                                3.0,
                                2.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.5,
                                6.0,
                                657.3317212,
                                421.4935263,
                                212.7250047,
                                662.1669685,
                                436.2944039,
                                182.6128889,
                                1001.0,
                                4.0,
                                3.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                639.8034428,
                                430.9883592,
                                162.5605615,
                                670.9326577,
                                411.1640706,
                                178.0690934,
                                1001.0,
                                5.0,
                                4.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                541.3878582,
                                216.8108805,
                                307.3724794,
                                584.5992533,
                                412.7637236,
                                381.2579975,
                            ],
                        },
                        {
                            "frameNumber": 2,
                            "time": 2.000139228,
                            "data": [
                                1001.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                18.0,
                                419.3626297,
                                381.10638,
                                315.8483744,
                                446.7371319,
                                375.818468,
                                282.8508029,
                                516.3105843,
                                361.2676189,
                                201.5443633,
                                592.9597694,
                                344.2612152,
                                127.3963243,
                                679.1547838,
                                328.7033152,
                                64.22840104,
                                728.0327863,
                                320.5202629,
                                31.49161861,
                                1001.0,
                                2.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                219.5947346,
                                861.7155242,
                                300.8401219,
                                190.1993603,
                                868.6151397,
                                282.8074954,
                                1001.0,
                                3.0,
                                2.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.5,
                                6.0,
                                655.5447164,
                                417.8251525,
                                217.1708231,
                                669.7077335,
                                432.941762,
                                190.7921575,
                                1001.0,
                                6.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                748.6131058,
                                312.0532071,
                                295.8168199,
                                713.2424309,
                                307.8785764,
                                295.6282915,
                                1001.0,
                                7.0,
                                3.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                543.4687581,
                                148.8799083,
                                277.8911145,
                                529.893394,
                                146.6094325,
                                312.4195341,
                                1001.0,
                                5.0,
                                4.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                610.406461,
                                152.6068272,
                                304.3073239,
                                432.9961836,
                                229.7552013,
                                191.6383788,
                                1001.0,
                                8.0,
                                4.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                668.8368056,
                                523.9037131,
                                357.0977571,
                                721.9538022,
                                345.9688898,
                                427.5226707,
                            ],
                        },
                    ],
                },
                "plotData": {"version": CURRENT_VERSION.PLOT_DATA, "data": []},
            },
        ),
        # same data but add drawing endpoints
        (
            MedyanData(
                meta_data=MetaData(
                    box_size=np.array([1000.0, 1000.0, 500.0]),
                ),
                snapshot_file=InputFileData(
                    file_path="simulariumio/tests/data/medyan/snapshot.traj"
                ),
                filament_display_data={
                    0: DisplayData(
                        name="Actin",
                        radius=2,
                        color="#ff1493",
                    ),
                },
                linker_display_data={
                    0: DisplayData(
                        name="Xlink0",
                        radius=1.0,
                        color="#0080ff",
                    ),
                    1: DisplayData(
                        name="Xlink1",
                        radius=0.5,
                    ),
                },
                agents_with_endpoints=["Xlink0", "Xlink1"],
            ),
            {
                "trajectoryInfo": {
                    "version": CURRENT_VERSION.TRAJECTORY_INFO,
                    "timeUnits": {
                        "magnitude": 1.0,
                        "name": "s",
                    },
                    "timeStepSize": 1.0,
                    "totalSteps": 3,
                    "spatialUnits": {
                        "magnitude": 1.0,
                        "name": "nm",
                    },
                    "size": {"x": 1000.0, "y": 1000.0, "z": 500.0},
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
                            "name": "Actin",
                            "geometry": {
                                "displayType": "FIBER",
                                "color": "#ff1493",
                            },
                        },
                        "1": {
                            "name": "Xlink0",
                            "geometry": {
                                "displayType": "FIBER",
                                "color": "#0080ff",
                            },
                        },
                        "2": {
                            "name": "Xlink0 End",
                            "geometry": {
                                "displayType": "SPHERE",
                            },
                        },
                        "3": {
                            "name": "Xlink1",
                            "geometry": {
                                "displayType": "FIBER",
                            },
                        },
                        "4": {
                            "name": "Xlink1 End",
                            "geometry": {
                                "displayType": "SPHERE",
                            },
                        },
                        "5": {
                            "name": "linker2",
                            "geometry": {
                                "displayType": "FIBER",
                            },
                        },
                        "6": {
                            "name": "motor1",
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
                    "bundleSize": 3,
                    "bundleData": [
                        {
                            "frameNumber": 0,
                            "time": 0.0,
                            "data": [
                                1001.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                6.0,
                                454.3434234,
                                363.439226,
                                265.4405349,
                                519.7377041,
                                351.5737487,
                                180.312405,
                                1001.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                6.0,
                                547.5943503,
                                280.3075619,
                                307.4127023,
                                535.194707,
                                173.0325428,
                                308.9355694,
                            ],
                        },
                        {
                            "frameNumber": 1,
                            "time": 1.000038293,
                            "data": [
                                1001.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                18.0,
                                443.3162276,
                                369.8644852,
                                293.1521372,
                                458.4600122,
                                366.5425284,
                                274.4414626,
                                525.5102849,
                                351.3129172,
                                191.1648549,
                                595.4174881,
                                336.6403217,
                                110.1741389,
                                672.5234407,
                                322.3132598,
                                35.94250437,
                                678.3129825,
                                321.2378855,
                                30.3779709,
                                1001.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                15.0,
                                549.7619454,
                                310.7627687,
                                302.0296124,
                                547.773019,
                                286.5808386,
                                303.3456815,
                                537.9496947,
                                179.2424416,
                                309.5407552,
                                518.8214547,
                                73.12680239,
                                314.8723733,
                                509.9893907,
                                28.15495189,
                                317.0372613,
                                1001.0,
                                2.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                216.8006048,
                                854.8097767,
                                302.9108981,
                                191.2656514,
                                867.5975965,
                                281.4725825,
                                1000.0,
                                3.0,
                                2.0,
                                216.8006048,
                                854.8097767,
                                302.9108981,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                4.0,
                                2.0,
                                191.2656514,
                                867.5975965,
                                281.4725825,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1001.0,
                                5.0,
                                3.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.5,
                                6.0,
                                657.3317212,
                                421.4935263,
                                212.7250047,
                                662.1669685,
                                436.2944039,
                                182.6128889,
                                1000.0,
                                6.0,
                                4.0,
                                657.3317212,
                                421.4935263,
                                212.7250047,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                7.0,
                                4.0,
                                662.1669685,
                                436.2944039,
                                182.6128889,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1001.0,
                                8.0,
                                5.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                639.8034428,
                                430.9883592,
                                162.5605615,
                                670.9326577,
                                411.1640706,
                                178.0690934,
                                1001.0,
                                9.0,
                                6.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                541.3878582,
                                216.8108805,
                                307.3724794,
                                584.5992533,
                                412.7637236,
                                381.2579975,
                            ],
                        },
                        {
                            "frameNumber": 2,
                            "time": 2.000139228,
                            "data": [
                                1001.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                18.0,
                                419.3626297,
                                381.10638,
                                315.8483744,
                                446.7371319,
                                375.818468,
                                282.8508029,
                                516.3105843,
                                361.2676189,
                                201.5443633,
                                592.9597694,
                                344.2612152,
                                127.3963243,
                                679.1547838,
                                328.7033152,
                                64.22840104,
                                728.0327863,
                                320.5202629,
                                31.49161861,
                                1001.0,
                                2.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                219.5947346,
                                861.7155242,
                                300.8401219,
                                190.1993603,
                                868.6151397,
                                282.8074954,
                                1000.0,
                                3.0,
                                2.0,
                                219.5947346,
                                861.7155242,
                                300.8401219,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                4.0,
                                2.0,
                                190.1993603,
                                868.6151397,
                                282.8074954,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1001.0,
                                5.0,
                                3.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.5,
                                6.0,
                                655.5447164,
                                417.8251525,
                                217.1708231,
                                669.7077335,
                                432.941762,
                                190.7921575,
                                1000.0,
                                6.0,
                                4.0,
                                655.5447164,
                                417.8251525,
                                217.1708231,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1000.0,
                                7.0,
                                4.0,
                                669.7077335,
                                432.941762,
                                190.7921575,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                0.0,
                                1001.0,
                                10.0,
                                1.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                748.6131058,
                                312.0532071,
                                295.8168199,
                                713.2424309,
                                307.8785764,
                                295.6282915,
                                1000.0,
                                11.0,
                                2.0,
                                748.6131058,
                                312.0532071,
                                295.8168199,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1000.0,
                                12.0,
                                2.0,
                                713.2424309,
                                307.8785764,
                                295.6282915,
                                0.0,
                                0.0,
                                0.0,
                                2.0,
                                0.0,
                                1001.0,
                                13.0,
                                5.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                543.4687581,
                                148.8799083,
                                277.8911145,
                                529.893394,
                                146.6094325,
                                312.4195341,
                                1001.0,
                                9.0,
                                6.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                610.406461,
                                152.6068272,
                                304.3073239,
                                432.9961836,
                                229.7552013,
                                191.6383788,
                                1001.0,
                                14.0,
                                6.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                0.0,
                                1.0,
                                6.0,
                                668.8368056,
                                523.9037131,
                                357.0977571,
                                721.9538022,
                                345.9688898,
                                427.5226707,
                            ],
                        },
                    ],
                },
                "plotData": {"version": CURRENT_VERSION.PLOT_DATA, "data": []},
            },
        ),
    ],
)
def test_medyan_converter(trajectory, expected_data):
    converter = MedyanConverter(trajectory)
    buffer_data = JsonWriter.format_trajectory_data(converter._data)
    assert expected_data == buffer_data
    assert JsonWriter._check_agent_ids_are_unique_per_frame(buffer_data)
