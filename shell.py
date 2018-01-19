#!/usr/bin/env python3
import sys
SHELL_STATUS_RUN = 1
SHELL_STATUS_STOP = 0

def shell_loop():
    status = SHELL_STATUS_RUN
    while status == SHELL_STATUS_RUN:
        ### 显示命令提示符
        sys.stdout.write('> ')
        sys.stdout.flush()
        ### 读取命令输入
        cmd = sys.stdin.readline()
        ### 切分命令输入
        cmd_tokens = tokenize(cmd)
        ### 执行该命令并获取新的状态
        status = execute(cmd_tokens)

shell_loop()
