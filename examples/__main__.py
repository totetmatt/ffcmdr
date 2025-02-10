import argparse

class Examples:
    def simple():
        from ffcmdr.cmd import FFmpegCmd
        from ffcmdr.cmd import FFmpegInput
        from ffcmdr.cmd import FFmpegOutput

        from ffcmdr.run import run

        from ffcmdr.arg import yes
        """
        Simple in to out
        """
        cmd = FFmpegCmd() + yes + FFmpegInput("in.mp4") + FFmpegOutput("out.mp4")
        run(cmd)

    def filter_simple():
        from ffcmdr.cmd import FFmpegCmd
        from ffcmdr.cmd import FFmpegInput
        from ffcmdr.cmd import FFmpegOutput
        from ffcmdr.cmd import FFmpegArg
        from ffcmdr.cmd import ArgFlag
        from ffcmdr.filter_complex import Filter

        from ffcmdr.run import run

        from ffcmdr.arg import yes
        """
        Simple filter
        """
        graph = Filter("scale", "320",-2)

        cmd = (
            FFmpegCmd()
            + yes
            + FFmpegInput("in.mp4")
            + (FFmpegOutput("out.mp4") + FFmpegArg("vf", flag=ArgFlag.OUT)(graph))
        )

        run(cmd)

    def double_output():
        from ffcmdr.cmd import FFmpegCmd
        from ffcmdr.cmd import FFmpegInput
        from ffcmdr.cmd import FFmpegOutput
        from ffcmdr.cmd import FFmpegArg
        from ffcmdr.cmd import ArgFlag
        from ffcmdr.filter_complex import Filter

        from ffcmdr.run import run

        from ffcmdr.arg import yes
        """
        Shows how to compose the ffmpeg command via loop
        """
        # If the Args don't exists, can create itlike this
        vf = FFmpegArg("vf", flag=ArgFlag.OUT)

        finput = FFmpegInput("in.mp4")
        cmd = FFmpegCmd() + yes + finput
        for size in [320, 480]:
            out = FFmpegOutput(f"out_{size}.mp4") + vf(Filter("scale", f"{size}:-2"))
            cmd = cmd + out
        run(cmd)

        """ Could also be expressed like this in a more oneliner way
        graph_1 = Filter("scale","320:-2")
        graph_2 = Filter("scale","480:-2")
        cmd = FFmpegCmd() + yes \
            + FFmpegInput("in.mp4")\
            + (FFmpegOutput("out_320.mp4") + vf(graph_1)) \
            + (FFmpegOutput("out_480.mp4") + vf(graph_2))
        """

    def blur_background():
        from ffcmdr.cmd import FFmpegCmd
        from ffcmdr.cmd import FFmpegInput
        from ffcmdr.cmd import FFmpegOutput
        from ffcmdr.cmd import FFmpegArg
        from ffcmdr.cmd import ArgFlag
        from ffcmdr.filter_complex import Filter

        from ffcmdr.run import run

        from ffcmdr.arg import yes
        """

        """

        target_width = 720
        target_height = 1080
        split = Filter("split")[["0:v"]:["bg", "fg"]]
        scale = Filter("scale", target_width, target_height, flags="neighbor")[["bg"]:]
        avgblur = Filter("avgblur", sizeX=200)[:["bg_out"]]
        overlay = Filter("overlay", x=f"(main_w-overlay_w)/2",y="(main_h-overlay_h)/2")[["bg_out", "fg"]:["vout"]]
        graph = (split >> scale >> avgblur ) >> overlay

        map = FFmpegArg("map", ArgFlag.OUT)

        cmd = (
            FFmpegCmd()
            + FFmpegInput("in.mp4")
            + yes
            + FFmpegArg("filter_complex", ArgFlag.GLOBAL, graph)
            + (FFmpegOutput("out.mp4") + map("[vout]") + map("0:a"))
        )
        run(cmd)
        pass

    def ffprobe_as_json():
        import subprocess
        from pprint import pprint
        import json
        from ffcmdr import FFprobe
        from ffcmdr.arg import yes, hide_banner, loglevel, show_error, show_format,show_streams, print_format
        from ffcmdr.run import run
        from ffcmdr import FFmpegOutput
        probe = FFprobe() + yes\
        + hide_banner + loglevel("fatal") + show_error + show_format + show_streams\
        + print_format("json") + FFmpegOutput("in.mp4")

        out, _ = run(probe, stdout=subprocess.PIPE)
        data = json.loads(out)
        pprint(data)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="FFcmdr Examples")
    parser.add_argument("example_name")
    args = parser.parse_args()
    examples = {k: v for k, v in Examples.__dict__.items() if callable(v)}

    example_func = examples.get(args.example_name)
    if not example_func:
        raise Exception(f"No example named '{args.example_name}'")
    example_func()
