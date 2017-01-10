#!/usr/bin/env python
# encoding: utf-8
import os
import sys


reload(sys)
sys.setdefaultencoding("utf8")
# 不知道上面是什么神奇代码总之管用了

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yangyao.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
