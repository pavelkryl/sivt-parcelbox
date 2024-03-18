from parcelbox import Person, AbstractParcelBox
from unittest.mock import Mock


def test_hand_in_success() -> None:
    "test ze pri hand_in probehla notifikace odesilatele i prijemce"
    ...


def test_hand_out_success() -> None:
    "test ze pri hand_out probehla notifikace odesilatele o vyzvednute zasilce"
    ...


def test_fail_handout_bad_id() -> None:
    "test ze pri hand_out a nespravnem id nevratil parcelbox nic/vratil None"
    ...

def test_fail_handout_bad_pin() -> None:
    "test ze pri hand_out a spravnem id a nespravnem pinu nevratil parcelbox nic/vratil None"
    ...