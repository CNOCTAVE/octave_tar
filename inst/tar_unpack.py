## Copyright (C) 2024 Yu Hongbo <yuhongbo@member.fsf.org>, 
##                    CNOCTAVE <cnoctave@qq.com>
##
## This program is free software; you can redistribute it and/or modify it under
## the terms of the GNU General Public License as published by the Free Software
## Foundation; either version 3 of the License, or (at your option) any later
## version.
##
## This program is distributed in the hope that it will be useful, but WITHOUT
## ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
## details.
##
## You should have received a copy of the GNU General Public License along with
## this program; if not, see <http://www.gnu.org/licenses/>.

import sys
import tarfile
import os

if len(sys.argv) < 3:
    print("Usage: tar_unpack(tar_filename, destination_dir)")
    sys.exit(1)

def untar_file(tar_filename, destination_dir):
    if not os.path.exists(tar_filename):
        print(f"File {tar_filename} does not exist.")
        return

    if not os.path.isfile(tar_filename):
        print(f"{tar_filename} is not a file.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    with tarfile.open(tar_filename, "r:") as tar:
        tar.extractall(path=destination_dir)

    print(f"File {tar_filename} has been untarred to {destination_dir}.")

if __name__ == "__main__":
    untar_file(sys.argv[1], sys.argv[2])