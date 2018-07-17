#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide configure file management service in i18n environment.

Authors: wangweihong(xdream888@163.com)
Date:    2018/7/5 17:51
"""


class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        count = 0
        while n > 0:
            count += n / 5
            n = n / 5
        return count


if __name__ == '__main__':
    aaa = Solution()
    print(aaa.trailingZeros(10))
