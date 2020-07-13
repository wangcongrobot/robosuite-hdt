"""
Tests two finger gripper and left two finger gripper on grabbing task
"""
from robosuite.models.grippers import (
    TwoFingerGripper,
    GripperTester,
    LeftTwoFingerGripper,
    HDTGripper
)


def test_hdt_gripper():
    hdt_gripper_tester(False)


def hdt_gripper_tester(render,
                      total_iters=1,
                      test_y=True):
    gripper = HDTGripper()
    tester = GripperTester(
        gripper=gripper,
        pos="0 0 0.25",
        quat="0 0 1 0",
        gripper_low_pos=0,
        gripper_high_pos=0.1,
        render=render,
    )
    tester.start_simulation()
    tester.loop(total_iters=total_iters,
                test_y=test_y)


if __name__ == "__main__":
    hdt_gripper_tester(True, 20, True)
