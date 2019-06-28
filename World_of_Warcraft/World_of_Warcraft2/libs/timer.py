#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: timer.py
# modified: 2019-06-28

__all__ = ["Timer"]

class Timer(object):

    def __init__(self):
        self._hour = 0
        self._minute = 0

    def __str__(self):
        return "%03d" % self._hour

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    def next_hour(self):
        self._hour += 1
        self._minute = 0