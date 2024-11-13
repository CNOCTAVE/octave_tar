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
import warnings
from builtins import UserWarning

class output(UserWarning):
    pass

def custom_warning_format(message, category, filename, lineno, file=None, line=None):
    formatted_message = f"{category.__name__}: {message}"
    print(formatted_message, end='\n')
 
# 设置自定义的警告显示处理函数
warnings.showwarning = custom_warning_format

def print_log(message, category=output, stacklevel=1, source=None):
    """Logger function. 
    1. You cannot call print() to directly print to Octave terminal.
    2. Octave package doesn't allow to make deeper Python package dir.
    So use this instead."""
    warnings.warn(message, category, stacklevel, source)

if len(sys.argv) < 3:
    print("Usage: tar_pack(source1, source2, ... , output_filename)")
    sys.exit(1)

def tar_directory(source_list_output_filename):
    source_list = source_list_output_filename[:-1]
    output_filename = source_list_output_filename[-1]
    try:
        with tarfile.open(output_filename, "w:") as tar:
            for path in source_list:
                tar.add(path, arcname=os.path.basename(path))
                print_log(f"Source {path} has been tarred to {output_filename}.")
        return 0
    except BaseException as e:
        print_log(e)
        return 1

if __name__ == "__main__":
    tar_directory(sys.argv[1:])