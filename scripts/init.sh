#!/bin/bash

# 创建目录结构
mkdir -pv src/example_pkg/   \
          test/example_pkg/  \
          .github/workflows/

touch setup.py Dockerfile readme.md \
      src/example_pkg/__init__.py   \
      src/example_pkg/core.py       \
      test/example_pkg/core.py      \

# 提示初始化完成
echo "项目初始化完成"
