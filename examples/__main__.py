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

    def simple_pipe():
        from ffcmdr.cmd import FFmpegCmd
        from ffcmdr.cmd import FFmpegInput
        from ffcmdr.cmd import FFmpegOutput

        from ffcmdr.run import run

        from ffcmdr.arg import f, movflags

        """
        Simple in to out pipe
        """
        data = b""
        with open("in.mp4", "rb") as file:
            data = file.read()
        cmd = (
            FFmpegCmd()
            + FFmpegInput("pipe:0")
            + (FFmpegOutput("pipe:1") + f("mp4") + movflags("frag_keyframe+empty_moov"))
        )
        out, _ = run(cmd, input_stream=data)
        with open("out.mp4", "wb") as file:
            file.write(out)

    def filter_simple():
        from ffcmdr.cmd import FFmpegCmd
        from ffcmdr.cmd import FFmpegInput
        from ffcmdr.cmd import FFmpegOutput
        from ffcmdr.cmd import FFmpegArg
        from ffcmdr.cmd import ArgFlag
        from ffcmdr.filter_complex import Filter

        from ffcmdr.run import run

        from ffcmdr.arg import y

        """
        Simple filter
        """
        graph = Filter("scale", "320", -2)

        cmd = (
            FFmpegCmd()
            + y
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

        from ffcmdr.arg import y

        """
        Shows how to compose the ffmpeg command via loop
        """
        # If the Args don't exists, can create it like this
        vf = FFmpegArg("vf", flag=ArgFlag.OUT)

        finput = FFmpegInput("in.mp4")
        cmd = FFmpegCmd() + y + finput
        for size in [320, 480]:
            out = FFmpegOutput(f"out_{size}.mp4") + vf(Filter("scale", f"{size}:-2"))
            cmd = cmd + out
        run(cmd)

        """ Could also be expressed like this in a more oneliner way
        graph_1 = Filter("scale","320:-2")
        graph_2 = Filter("scale","480:-2")
        cmd = FFmpegCmd() + y \
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

        from ffcmdr.arg import y

        """

        """

        target_width = 720
        target_height = 1080
        split = Filter("split")[["0:v"]:["bg", "fg"]]
        scale = Filter("scale", target_width, target_height, flags="neighbor")[["bg"]:]
        avgblur = Filter("avgblur", sizeX=200)[:["bg_out"]]
        overlay = Filter(
            "overlay", x=f"(main_w-overlay_w)/2", y="(main_h-overlay_h)/2"
        )[["bg_out", "fg"]:["vout"]]
        graph = (split >> scale >> avgblur) >> overlay

        map = FFmpegArg("map", ArgFlag.OUT)

        cmd = (
            FFmpegCmd()
            + FFmpegInput("in.mp4")
            + y
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
        from ffcmdr.arg import (
            y,
            hide_banner,
            loglevel,
            show_error,
            show_format,
            show_streams,
            print_format,
        )
        from ffcmdr.run import run
        from ffcmdr import FFmpegInput

        probe = (
            FFprobe()
            + y
            + hide_banner
            + loglevel("fatal")
            + show_error
            + show_format
            + show_streams
            + print_format("json")
            + FFmpegInput("in.mp4")
        )

        out, _ = run(probe, stdout=subprocess.PIPE)
        data = json.loads(out)
        pprint(data)

    def inputs_named_pipe():
        """
            Using 2 input stream with named pipe.
            Not best way, might worth looking integrating this into lib
        """
        import subprocess
        from ffcmdr.arg import y,  b, filter_complex, loop, pix_fmt, c, shortest,  movflags, f , map
        from ffcmdr.cmd import FFmpegCmd
        from ffcmdr.run import run_async
        from ffcmdr import FFmpegOutput, FFmpegInput
        from ffcmdr.filter_complex import Filter
        import os
        from threading import Thread
        with open("image.png",'rb') as file:
            binary_image = file.read()

        with open("audio.mp3",'rb') as file:
            binary_audio = file.read()

        path_image = "input_pipe_image"
        os.mkfifo(path_image) if not os.path.exists(path_image) else None

        path_audio = "input_pipe_audio"
        os.mkfifo(path_audio) if not os.path.exists(path_audio) else None

        graph = (
            Filter("showspectrum",s="720x320",fscale="log",slide="rscroll",color="intensity")[["0:a"]:["wf"]]
            >> Filter("scale","-2:rh")[["wf","1:v"]:["2nd"]] 
            >> Filter("hstack")[["1:v","2nd"]:["out"]]
            )

        cmd = (
            FFmpegCmd()  +y + filter_complex(graph)
            + (FFmpegInput(path_audio))
            + (FFmpegInput(path_image)+ loop("1"))

            + (
                    FFmpegOutput("pipe:1") 
                    + shortest 
                    + f("mp4") 
                    + map('[out]')
                    + map("0:a")
                    + c['v']("libx264")
                    + c['a']("aac")
                    + b['a']("192k")
                    + pix_fmt("yuv420p")
                    + movflags("frag_keyframe+empty_moov")
                )
                )
        process=  run_async(cmd,stdout=subprocess.PIPE)

        def write_to_pipe(pipe_name, binary):
            fd_pipe = os.open(pipe_name,os.O_WRONLY )
            os.write(fd_pipe,binary)
            os.close(fd_pipe)

        thread = Thread(target = write_to_pipe, args=(path_image,binary_image))
        thread2 = Thread(target = write_to_pipe, args=(path_audio,binary_audio))
        thread.start()
        thread2.start()

        out , _ = process.communicate()

        with open("out_pipe.mp4",'wb') as file:
            file.write(out)
        for t in [thread2,thread]:
            t.join()
        os.unlink(path_image)
        os.unlink(path_audio)
if __name__ == "__main__":
    examples = {k: v for k, v in Examples.__dict__.items() if callable(v)}
    parser = argparse.ArgumentParser()
    parser.add_argument("example_name",choices=examples.keys())
    args = parser.parse_args()


    example_func = examples.get(args.example_name)
    if not example_func:
        raise Exception(f"No example named '{args.example_name}'")
    example_func()
