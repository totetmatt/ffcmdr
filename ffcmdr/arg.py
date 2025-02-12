from .cmd import FFmpegArg
from .cmd import ArgFlag

from .cmd import IArg
from .cmd import OArg
from .cmd import IOArg
from .cmd import GArg
"""
    TODO: Add from time to time cmd argument, maybe try to improve organisation
"""
license = GArg("license")
h = GArg("h")
version = GArg("version")
muxers = GArg("muxers")
demuxers = GArg("demuxers")
devices = GArg("devices")
decoders = GArg("decoders")
encoders = GArg("encoders")
filters = GArg("filters")
pix_fmts = GArg("pix_fmts")
layouts = GArg("layouts")
sample_fmts = GArg("sample_fmts")
help = GArg("help")
buildconf = GArg("buildconf")
formats = GArg("formats")
codecs = GArg("codecs")
bsfs = GArg("bsfs")
protocols = GArg("protocols")
dispositions = GArg("dispositions")
colors = GArg("colors")
sources = GArg("sources")
sinks = GArg("sinks")
hwaccels = GArg("hwaccels")

hide_banner = GArg("hide_banner")
filter_complex = GArg("filter_complex")

format = IOArg("f")

yes = GArg("y")
no = GArg("n")

stream_loop = IArg("stream_loop")
recast_media = GArg("recast_media")

codec = IOArg("c")
duration = IOArg("t")

file_size = OArg("fs")
sseof = IArg("sseof")

map = OArg("map")
ar = IOArg("ar")
map_metadata = OArg("map_metadata")

movflags = OArg("movflags")
crf = OArg("crf")
fflags = OArg("fflags")

frames = OArg("frames")
update = OArg("update")

loglevel = GArg("v")

## FFProbe
show_error = GArg("show_error")
show_format = GArg("show_format")
show_streams = GArg("show_streams")
print_format = GArg("print_format")
