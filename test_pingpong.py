# _*_ encoding: utf-8 _*_

import pingpong
import unittest
import re
from collections import Counter


class TestPing(unittest.TestCase):
    # ping function unit tests
    def test_is_ping(self):
        ans = pingpong.ping(3)

        assert ans == "ping"

    def test_is_not_ping(self):
        ans = pingpong.ping(2)

        assert ans == ""


class TestPong(unittest.TestCase):
    # pong function unit tests
    def test_is_pong(self):
        ans = pingpong.pong(5)

        assert ans == "pong"

    def test_is_not_pong(self):
        ans = pingpong.pong(2)

        assert ans == ""


class TestPingPong(unittest.TestCase):
    # pingpong function unit tests
    def test_pingpong_empty(self):
        ans = pingpong.pingpong(0)

        assert ans == ""

    def test_pinpong_one_ping(self):
        ans = pingpong.pingpong(4)
        length = len(re.findall(r"ping", ans))

        self.assertEqual(length, 1)

    def test_pingpong_two_pings_one_pong(self):
        ans  = pingpong.pingpong(7)
        ping_length = len(re.findall(r"ping", ans))
        pong_length = len(re.findall(r"pong", ans))

        self.assertEqual(ping_length, 2)
        self.assertEqual(pong_length, 1)

    def test_ping_and_pong(self):
        ans = pingpong.pingpong(16)

        ping_length = len(re.findall(r"ping", ans))
        pong_length = len(re.findall(r"pong", ans))
        ping_and_pong_length = len(re.findall(r"ping pong", ans))

        self.assertEqual(ping_and_pong_length, 1)
        self.assertEqual(ping_length, 5)
        self.assertEqual(pong_length, 3)

    if __name__ == "__main__":
        unittest.main()