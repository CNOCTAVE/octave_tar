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

## -*- texinfo -*-
## @deftypefn {} {} tar_unpack (@var{tar_filename}, @var{destination_dir})
## 将tar文件解包到指定文件夹
## @example
## param: tar_filename, destination_dir
##
## return: status
## @end example
##
## @end deftypefn

function status = tar_unpack(tar_filename, destination_dir)
    if nargin < 2
        print_usage();
    endif
    [ret, status] = python("tar_unpack.py", tar_filename, destination_dir)
end