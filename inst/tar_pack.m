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
## @deftypefn {} {} tar_pack (@var{source1}, @var{source2}, @var{...} , @var{output_filename})
## 将一个或多个文件或文件夹打包为tar文件
## @example
## param: source1, source2, ... , output_filename
##
## return: status
## @end example
##
## @end deftypefn

function status = tar_pack(varargin)
    if nargin < 2
        print_usage();
    endif
    [ret, status] = python("tar_pack.py", varargin{:});
end