from .cmd import FFmpegArg
from .cmd import FFmpegInput
from .cmd import ArgFlag

from .cmd import IArg
from .cmd import OArg
from .cmd import IOArg
from .cmd import GArg

"""
    TODO: Add from time to time cmd argument, maybe try to improve organisation
"""
# https://ffmpeg.org/ffmpeg.html#Generic-options
L, license = GArg("L"), GArg("license")
h, help = GArg("h"), GArg("help")

version = GArg("version")
buildconf = GArg("buildconf")
formats = GArg("formats")
demuxers = GArg("demuxers")
muxers = GArg("muxers")
devices = GArg("devices")
codecs = GArg("codecs")
decoders = GArg("decoders")
encoders = GArg("encoders")
bsfs = GArg("bsfs")
protocols = GArg("protocols")
filters = GArg("filters")
pix_fmts = GArg("pix_fmts")
sample_fmts = GArg("sample_fmts")
layouts = GArg("layouts")
dispositions = GArg("dispositions")
colors = GArg("colors")
sources = GArg("sources")
sinks = GArg("sinks")
v, loglevel = GArg("v"), GArg("loglevel")
hide_banner = GArg("hide_banner")
cpuflags = GArg("cpuflag")
cpucount = GArg("cpucount")
max_alloc = GArg("max_alloc")

# AVOptions https://ffmpeg.org/ffmpeg.html#AVOptions
f = IOArg("f")
i = FFmpegInput()
y = GArg("y")
n = GArg("n")
stream_loop = IArg("stream_loop")
recast_media = GArg("recast_media")
c, codec = IOArg("c"), IOArg("codec")
t = IOArg("t")
to = IOArg("to")
fs = OArg("fs")
ss = IOArg("ss")
sseof = IArg("sseof")
isync = IArg("isync")
itsoffset = IArg("itsoffset")
itsscale = IArg("itsscale")
timestamp = OArg("timestamp")
metadata = OArg("metadata")
disposition = OArg("disposition")
program = OArg("program")
stream_group = OArg("stream_group")
target = OArg("target")
dn = IOArg("dn")
frames = OArg("frames")
q = OArg("q")
qscale = OArg("qscale")
filter = OArg("filter")
reinit_filter = IArg("reinit_filter")
filter_threads = GArg("filter_threads")
pre = OArg("pre")
stats = GArg("stats")
stats_period = GArg("stats_period")
progress = GArg("progress")
stdin = GArg("stdin")
debug_ts = GArg("debug_ts")
attach = OArg("attach")
dump_attachment = IArg("dump_attachment")

# Video Options https://ffmpeg.org/ffmpeg.html#Video-Options

r = IOArg("r")
fpsmax = OArg("fpsmax")
s = IOArg("s")
aspect = OArg("aspect")
display_rotation = IArg("display_rotation")
display_hflip = IArg("display_hflip")
display_vflip = IArg("display_vflip")
vn = IOArg("vn")
vcodec = OArg("vcodec")
pass_ = OArg("pass")
passlogfile = OArg("passlogfile")
vf = OArg("vf")
autorotate = IOArg("autorotate")
autoscale = IOArg("autoscale")


# Advanced Video options https://ffmpeg.org/ffmpeg.html#Advanced-Video-options
pix_fmt = IOArg("pix_fmt")
sws_flags = IOArg("sws_flags")
rc_override = OArg("rc_override")
vstats = GArg("vstats")
vstats_file = GArg("vstats_file")
vstats_version = GArg("vstats_version")
vtag = OArg("vtag")

force_key_frames = OArg("force_key_frames")
apply_cropping = IArg("apply_cropping")
copyinkf = OArg("copyinkf")
init_hw_device = GArg("init_hw_device")
filter_hw_device = GArg("filter_hw_device")
hwaccel = IArg("hwaccel")
hwaccel_device = IArg("hwaccel_device")
hwaccels = GArg("hwaccels")
fix_sub_duration_heartbeat = IO("fix_sub_duration_heartbeat")

# Audio Options https://ffmpeg.org/ffmpeg.html#Audio-Options
aframes = OArg("aframes")
ar = IOArg("ar")
aq = OArg("aq")
ac = IOArg("ac")
an = IOArg("an")
acodec = IOArg("acodec")
sample_fmt = OArg("sample_fmt")
af = OArg("af")

# Advanced Audio options https://ffmpeg.org/ffmpeg.html#Advanced-Audio-options
atag = OArg("atag")
ch_layout = IOArg("ch_layout")
channel_layout = IOArg("channel_layout")
guess_layout_max = IArg("guess_layout_max")

# Subtitle options https://ffmpeg.org/ffmpeg.html#Subtitle-options
scodec = IOArg("scodec")
sn = IOArg("sn")

# Advanced Subtitle options https://ffmpeg.org/ffmpeg.html#Advanced-Subtitle-options
fix_sub_duration = IOArg("fix_sub_duration")
canvas_size = IOArg("canvas_size")

# Advanced options https://ffmpeg.org/ffmpeg.html#Advanced-options


map = OArg("map")
ignore_unknown = GArg("ignore_unknown")
copy_unknown = GArg("copy_unknown")
map_metadata = OArg("map_metadata")
map_chapters = OArg("map_chapters")
benchmark = GArg("benchmark")
benchmark_all = GArg("benchmark_all")
timelimit = GArg("timelimit")
dump = GArg("dump")
hex = GArg("hex")
readrate = IArg("readrate")
re = IArg("re")
readrate_initial_burst = IOArg("readrate_initial_burst")
vsync = GArg("vsync")
fps_mode = OArg("fps_mode")
frame_drop_threshold = GArg("frame_drop_threshold")
apad = OArg("apad")
copyts = IOArg("copyts")
start_at_zero = IOArg("start_at_zero")
copytb = IOArg("copytb")
enc_time_base = OArg("enc_time_base")
bitexact = IOArg("bitexact")
shortest = OArg("shortest")
shortest_buf_duration = OArg("shortest_buf_duration")
dts_delta_threshold = GArg("dts_delta_threshold")
dts_error_threshold = GArg("dts_error_threshold")
muxdelay = OArg("muxdelay")
muxpreload = OArg("muxpreload")
streamid = OArg("streamid")
bsf = IOArg("bsf")
tag = IOArg("tag")
timecode = GArg("timecode")
filter_complex, lavfi = GArg("filter_complex"), GArg("lavfi")
filter_complex_threads = GArg("filter_complex_threads")
accurate_seek = IArg("accurate_seek")
seek_timestamp = IArg("seek_timestamp")
thread_queue_size = IOArg("thread_queue_size")
sdp_file = GArg("sdp_file")
discard = IArg("discard")
abort_on = GArg("abort_on")
max_error_rate = GArg("max_error_rate")
xerror = GArg("xerror")
max_muxing_queue_size = OArg("max_muxing_queue_size")
muxing_queue_data_threshold = OArg("muxing_queue_data_threshold")
auto_conversion_filters = GArg("auto_conversion_filters")
bits_per_raw_sample = OArg("bits_per_raw_sample")
stats_enc_pre = OArg("stats_enc_pre")
stats_enc_post = OArg("stats_enc_post")
stats_mux_pre = OArg("stats_mux_pre")
stats_enc_pre_fmt = OArg("stats_enc_pre_fmt")
stats_enc_post_fmt = OArg("stats_enc_post_fmt")
stats_mux_pre_fmt = OArg("stats_mux_pre_fmt")
update = OArg("update")


## FFProbe
show_error = GArg("show_error")
show_format = GArg("show_format")
show_streams = GArg("show_streams")
print_format = GArg("print_format")
