import subprocess
from typing import Optional
from ffcmdr.cmd import FFmpegCmd

# From https://github.com/kkroening/ffmpeg-python/blob/master/ffmpeg/_run.py


# cwd
# shell
def run_async(
    cmd: FFmpegCmd,
    *,
    stdin: Optional[int] = None,
    stdout: Optional[int] = None,
    stderr: Optional[int] = None,
    **kwargs,
) -> subprocess.Popen:
    return subprocess.Popen(
        cmd.render(), stdin=stdin, stdout=stdout, stderr=stderr, **kwargs
    )


def run(
    cmd: FFmpegCmd,
    *,
    stdin: Optional[int] = None,
    stdout: Optional[int] = None,
    stderr: Optional[int] = None,
    input_stream=None,
    **kwargs,
) -> tuple:
    process = run_async(cmd, stdin=stdin, stdout=stdout, stderr=stderr, **kwargs)
    out, err = process.communicate(input_stream)
    retcode = process.poll()
    if retcode:
        raise Exception("ffmpeg", out, err)
    return out, err
