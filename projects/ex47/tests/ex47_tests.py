﻿from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom", "이 방에는 주워 담을 수 있는 금이 있습니다. 북쪽에는 문이 있습니다.")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "가운데의 테스트 방.")
    north = Room("North", "북쪽의 테스트 방.")
    south = Room("South", "남쪽의 테스트 방.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "")
    west = Room("Trees", "")
    down = Room("Dungeon", "")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)