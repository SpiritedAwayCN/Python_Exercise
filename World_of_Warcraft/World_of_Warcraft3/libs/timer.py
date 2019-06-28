#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: timer.py
# modified: 2019-06-28

__all__ = ["timer"]

class _Timer(object):

    def __init__(self):
        self._hour = 0
        self._minute = 0

    def __str__(self):
        return "%03d:%02d" % (self._hour, self._minute)

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        self._minute = minute

    @property
    def total(self):
        return self._hour * 60 + self._minute

    def next_hour(self):
        self._hour += 1
        self._minute = 0

    def reset(self):
        self.__init__()


timer = _Timer()