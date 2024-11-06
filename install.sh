#!/bin/bash

task_management_folder="/usr/local/share/task-management"
username=$SUDO_USER
desktop_file_icon="/home/$username/.local/share/applications"
echo "$desktop_file_icon"

# Check for sudo privileges
if [ "$EUID" -ne 0 ]; then
  echo "please run as sudo or use root"
  exit 1
fi

# install dependencies
# apt update
if ! command -v python3 &>/dev/null; then
  echo "python is not installed"
  apt install -y python3 python3-pip
fi

echo "Installing application"
chmod +x dist

echo "Verify if task management folder exists"
if ! [ -d "$task_management_folder" ]; then
  mkdir -p "$task_management_folder"
  chown -R "$username":"$username" "$task_management_folder"
fi


chmod +x /usr/local/share/task-management

echo "Verify if icon folder exists"
if ! [ -d "$task_management_folder/icon/" ]; then
  mkdir "$task_management_folder/icon/"
fi

echo "Verify if data folder exists"
if ! [ -d "$task_management_folder/data/" ]; then
  mkdir -p "$task_management_folder/data/"
fi

echo "Verify if data in progress files exists"
if ! [ -d "$task_management_folder/data/tasks.json" ]; then
  touch "$task_management_folder/data/tasks.json"
  echo "[]" >  "$task_management_folder/data/tasks.json"
fi

echo "Verify if data finished files exists"
if ! [ -d "$task_management_folder/data/finished.json" ]; then
  touch "$task_management_folder/data/finished.json"
  echo "[]" >  "$task_management_folder/data/finished.json"
fi

chown -R "$username":"$username" "$task_management_folder/data/"
chmod -R 700 "$task_management_folder/data/"


cp dist/task-management /usr/local/bin/task-management
cp dist/task.png /usr/local/share/task-management/icon/icon.png

chmod +x /usr/local/bin/task-management

echo "Creating a desktop icon"

if [ -e "$desktop_file_icon/task-management.desktop" ]; then
  rm "$desktop_file_icon/task-management.desktop"
fi

touch "$desktop_file_icon/task-management.desktop"
echo "[Desktop Entry]" >> "$desktop_file_icon/task-management.desktop"
echo "Version=1.0" >> "$desktop_file_icon/task-management.desktop"
echo "Name=Task Management" >> "$desktop_file_icon/task-management.desktop"
echo "Exec=/usr/local/bin/task-management" >> "$desktop_file_icon/task-management.desktop"
echo "Icon=/usr/local/share/task-management/icon/icon.png" >> "$desktop_file_icon/task-management.desktop"
echo "Type=Application" >> "$desktop_file_icon/task-management.desktop"
echo "Terminal=false" >> "$desktop_file_icon/task-management.desktop"

echo "Updating icons database"
update-desktop-database "$desktop_file_icon"
 
echo "Installed with success"
