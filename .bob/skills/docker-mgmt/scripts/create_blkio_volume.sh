#!/bin/bash
#
# Usage: create_blkio_volume.sh <volume_name> <volume_size> 
#
# Example: create_blkio_volume.sh my_container_vol 1GiB
#
# Description: Create a new blkio disk image with filesystem for Docker volumes
#
# High Level workflow
# Create blank disk image
# Configure desired filesystem
# Mount and confirm readiness for container volume


mount_disk_img(){
  if [ -e "$mntpt" ]; then
    echo "mounting VM disk..."
    mount "$mntpt" "$target"
    echo "successfully mounted $mntpt to $target"
  else
    echo "Not a valid mount point"
  fi
}

setup_volfs() {
  mntpt=$loopdv
  target=/mnt/${$1}_vol
  mkdir -p "$target"
  mount_disk_img
}

# Create and format blkio disk image
voldsk=/tmp/${$1}.raw
disksz=$2
fallocate -l ${$2} $voldsk
echo "Created $voldsk"

loopdv=$(losetup -f --show "$voldsk")
mkfs.ext4 "$loopdv"
setup_volfs
echo "Container volume at $target"
echo "Unmount with 'umount $target', then 'losetup -v -d "$loopdv"'"