#!/bin/bash

# 获取脚本文件名
script_name=$(basename "$0")

# 目标目录
target_dir="./"
# 新文件夹
new_folder="./renamed_files"

# 首项
start=21

# 公差
difference=1

# 当前编号
current_number=$start

# 创建新的文件夹
mkdir -p "$new_folder"

# 切换到目标目录
cd "$target_dir" || exit

# 遍历所有文件,ls的默认顺序，$(ls | sort)
for file in *; do
# 遍历所有文件，按自然顺序排序文件名
#for file in $(ls -v); do
# 遍历所有文件，按创建时间排序
#for file in $(ls -1 | xargs -I{} stat --format '%W %n' {} | sort -n | awk '{print $2}'); do
  if [ -f "$file" ]; then
    # 检查是否为脚本自身
    if [ "$file" != "$script_name" ]; then
      # 提取文件扩展名
      extension="${file##*.}"
      # 新文件名
      new_name="${current_number}.${extension}"
      # 复制文件到新的文件夹
      cp "$file" "$new_folder/$new_name"
      # 更新当前编号
      current_number=$((current_number + difference))
    fi
  fi
done
