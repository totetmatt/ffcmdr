from .cmd import FFmpegArg
from .cmd import ArgFlag
"""
    TODO: Add from time to time cmd argument, maybe try to improve organisation
"""
license = FFmpegArg("license", ArgFlag.GLOBAL)
h = FFmpegArg("h", ArgFlag.GLOBAL)
version = FFmpegArg("version", ArgFlag.GLOBAL)
muxers = FFmpegArg("muxers", ArgFlag.GLOBAL)
demuxers = FFmpegArg("demuxers", ArgFlag.GLOBAL)
devices = FFmpegArg("devices", ArgFlag.GLOBAL)
decoders = FFmpegArg("decoders", ArgFlag.GLOBAL)
encoders = FFmpegArg("encoders", ArgFlag.GLOBAL)
filters = FFmpegArg("filters", ArgFlag.GLOBAL)
pix_fmts = FFmpegArg("pix_fmts", ArgFlag.GLOBAL)
layouts = FFmpegArg("layouts", ArgFlag.GLOBAL)
sample_fmts = FFmpegArg("sample_fmts", ArgFlag.GLOBAL)
help = FFmpegArg("help", ArgFlag.GLOBAL)
buildconf = FFmpegArg("buildconf", ArgFlag.GLOBAL)
formats = FFmpegArg("formats", ArgFlag.GLOBAL)
codecs = FFmpegArg("codecs", ArgFlag.GLOBAL)
bsfs = FFmpegArg("bsfs", ArgFlag.GLOBAL)
protocols = FFmpegArg("protocols", ArgFlag.GLOBAL)
dispositions = FFmpegArg("dispositions", ArgFlag.GLOBAL)
colors = FFmpegArg("colors", ArgFlag.GLOBAL)
sources = FFmpegArg("sources", ArgFlag.GLOBAL)
sinks = FFmpegArg("sinks", ArgFlag.GLOBAL)
hwaccels = FFmpegArg("hwaccels", ArgFlag.GLOBAL)

hide_banner = FFmpegArg("hide_banner", ArgFlag.GLOBAL)
filter_complex = FFmpegArg("filter_complex", ArgFlag.GLOBAL)

format = FFmpegArg("f", ArgFlag.IN | ArgFlag.OUT)

yes = FFmpegArg("y", ArgFlag.GLOBAL)
no = FFmpegArg("n", ArgFlag.GLOBAL)

stream_loop = FFmpegArg("stream_loop", ArgFlag.IN)
recast_media = FFmpegArg("recast_media", ArgFlag.GLOBAL)

codec = FFmpegArg("c", ArgFlag.IN | ArgFlag.OUT)
duration = FFmpegArg("t", ArgFlag.IN | ArgFlag.OUT)

file_size = FFmpegArg("fs", ArgFlag.OUT)
sseof = FFmpegArg("sseof", ArgFlag.IN)

map = FFmpegArg("map", ArgFlag.OUT)
ar = FFmpegArg("ar", ArgFlag.IN | ArgFlag.OUT)
map_metadata = FFmpegArg("map_metadata", ArgFlag.OUT)

movflags = FFmpegArg("movflags", ArgFlag.OUT)
crf = FFmpegArg("crf", ArgFlag.OUT)
fflags = FFmpegArg("fflags", ArgFlag.OUT)

frames = FFmpegArg("frames", ArgFlag.OUT)
update = FFmpegArg("update", ArgFlag.OUT)

loglevel = FFmpegArg("v", ArgFlag.GLOBAL)

## FFProbe
show_error = FFmpegArg("show_error", ArgFlag.GLOBAL)
show_format = FFmpegArg("show_format", ArgFlag.GLOBAL)
show_streams = FFmpegArg("show_streams", ArgFlag.GLOBAL)
print_format = FFmpegArg("print_format", ArgFlag.GLOBAL)
