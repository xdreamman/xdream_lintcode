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
        temp = n % 5
        if temp == 0:
            result = n / 5
        else:
            result = 0
        return result


if __name__ == '__main__':
    aaa = Solution()
    print(aaa.trailingZeros(10))
