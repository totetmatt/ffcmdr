from ffcmdr.cmd import FFmpegArg
from ffcmdr.cmd import FFmpegInput
from ffcmdr.cmd import FFmpegOutput
from ffcmdr.cmd import FFprobe
from ffcmdr.cmd import FFmpegInputOutput
from ffcmdr.cmd import FFmpegGlobal
from ffcmdr.cmd import ArgFlag
from ffcmdr.cmd import FFmpegCmd
from ffcmdr.filter_complex import FilterGraph
from ffcmdr.filter_complex import FilterChain
from ffcmdr.filter_complex import Filter

import unittest
import pytest


global_arg_1 = FFmpegArg("global_arg_1", ArgFlag.GLOBAL)
global_arg_2 = FFmpegArg("global_arg_2", ArgFlag.GLOBAL)
global_arg_3 = FFmpegArg("global_arg_3", ArgFlag.GLOBAL)

input_arg_1 = FFmpegArg("input_arg_1", ArgFlag.IN)
input_arg_2 = FFmpegArg("input_arg_2", ArgFlag.IN)
input_arg_3 = FFmpegArg("input_arg_3", ArgFlag.IN)

input_arg_name = FFmpegArg("i", ArgFlag.IN)

output_arg_1 = FFmpegArg("output_arg_1", ArgFlag.OUT)
output_arg_2 = FFmpegArg("output_arg_2", ArgFlag.OUT)
output_arg_3 = FFmpegArg("output_arg_3", ArgFlag.OUT)

io_arg_1 = FFmpegArg("io_arg_1", ArgFlag.IN | ArgFlag.OUT)
io_arg_2 = FFmpegArg("io_arg_2", ArgFlag.IN | ArgFlag.OUT)
io_arg_3 = FFmpegArg("io_arg_3", ArgFlag.IN | ArgFlag.OUT)


class GlobalArgsTest(unittest.TestCase):
    def test_global_args(self):
        global_chunk = global_arg_1 + global_arg_2
        with self.subTest("Adding 2 arg create a FFmpegGlobal"):
            assert type(global_chunk) == FFmpegGlobal
            assert (
                global_chunk.render() == global_arg_1.render() + global_arg_2.render()
            )

        global_chunk_2 = global_chunk + global_arg_3
        with self.subTest("Adding FFmpegGlobal + arg to create a new FFmpegGlobal"):

            assert type(global_chunk_2) == FFmpegGlobal
            assert global_chunk.group_option != global_chunk_2.group_option

        global_chunk_3 = global_arg_3 + global_chunk
        with self.subTest("Adding arg + FFmpegGlobal to create a new FFmpegGlobal"):
            assert type(global_chunk_3) == FFmpegGlobal
            assert global_chunk.group_option != global_chunk_3.group_option

        with self.subTest(
            "arg + FFmpegGlobal and FFmpegGlobal + arg should be rendering different"
        ):
            assert global_chunk_2.render() != global_chunk_3.render()

        with self.subTest("Exception when type doesn't match"):
            with pytest.raises(Exception) as _:
                global_arg_1 + input_arg_1
            with pytest.raises(Exception) as _:
                global_arg_1 + output_arg_1
            with pytest.raises(Exception) as _:
                global_chunk + input_arg_1
            with pytest.raises(Exception) as _:
                global_chunk + output_arg_1
            with pytest.raises(Exception) as _:
                global_chunk + io_arg_1

            with pytest.raises(Exception) as _:
                input_arg_1 + global_chunk
            with pytest.raises(Exception) as _:
                output_arg_1 + global_chunk
            with pytest.raises(Exception) as _:
                io_arg_1 + global_chunk


class InputArgsTest(unittest.TestCase):
    def test_input_args(self):
        input_chunk = input_arg_1 + input_arg_2
        with self.subTest("Adding 2 arg create a FFmpegInput"):
            assert type(input_chunk) == FFmpegInput

        with (
            self.subTest("Render should raise error as no url or -i is given so far"),
            pytest.raises(Exception) as _,
        ):
            input_chunk.render()

        input_chunk_2 = input_chunk + input_arg_3
        with self.subTest("Adding FFmpegInput + arg to create a new FFmpegInput"):
            assert type(input_chunk_2) == FFmpegInput
            assert input_chunk.group_option != input_chunk_2.group_option

        input_chunk_3 = input_arg_3 + input_chunk
        with self.subTest("Adding arg + FFmpegInput to create a new FFmpegInput"):
            assert type(input_chunk_3) == FFmpegInput
            assert input_chunk.group_option != input_chunk_3.group_option

        with self.subTest(
            "arg + FFmpegGlobal and FFmpegGlobal + arg should be rendering different"
        ):
            assert input_chunk_2.group_option != input_chunk_3.group_option

        with self.subTest("Exception when type doesn't match"):
            with pytest.raises(Exception) as _:
                input_arg_1 + output_arg_1
            with pytest.raises(Exception) as _:
                input_arg_1 + global_arg_1
            with pytest.raises(Exception) as _:
                input_chunk + global_arg_1
            with pytest.raises(Exception) as _:
                input_chunk + output_arg_1

            with pytest.raises(Exception) as _:
                global_arg_1 + input_chunk
            with pytest.raises(Exception) as _:
                output_arg_1 + input_chunk

        with self.subTest("Can handle InOut args"):
            input_chunk_from_io_1 = input_arg_1 + io_arg_1
            assert type(input_chunk_from_io_1) == FFmpegInput

            input_chunk_from_io_2 = io_arg_1 + input_arg_1
            assert type(input_chunk_from_io_2) == FFmpegInput

            assert (
                input_chunk_from_io_1.group_option != input_chunk_from_io_2.group_option
            )


class OutputArgsTest(unittest.TestCase):
    def test_output_args(self):
        output_chunk = output_arg_1 + output_arg_2
        with self.subTest("Adding 2 arg create a FFmpegOutput"):
            assert type(output_chunk) == FFmpegOutput

        with (
            self.subTest("Render should raise error as no url is given so far"),
            pytest.raises(Exception) as _,
        ):
            output_chunk.render()

        output_chunk_2 = output_chunk + output_arg_3
        with self.subTest("Adding FFmpegOutput + arg to create a new FFmpegOutput"):
            assert type(output_chunk_2) == FFmpegOutput
            assert output_chunk.group_option != output_chunk_2.group_option

        output_chunk_3 = output_arg_3 + output_chunk
        with self.subTest("Adding arg + FFmpegOutput to create a new FFmpegOutput"):
            assert type(output_chunk_3) == FFmpegOutput
            assert output_chunk.group_option != output_chunk_3.group_option

        with self.subTest(
            "arg + FFmpegOutput and FFmpegOutput + arg should be rendering different"
        ):
            assert output_chunk_2.group_option != output_chunk_3.group_option

        with self.subTest("Exception when type doesn't match"):
            with pytest.raises(Exception) as _:
                output_arg_1 + input_arg_1
            with pytest.raises(Exception) as _:
                output_arg_1 + global_arg_1
            with pytest.raises(Exception) as _:
                output_chunk + global_arg_1
            with pytest.raises(Exception) as _:
                output_chunk + input_arg_1

            with pytest.raises(Exception) as _:
                global_arg_1 + output_chunk
            with pytest.raises(Exception) as _:
                input_arg_1 + output_chunk

        with self.subTest("Can handle InOut args"):
            output_chunk_from_io_1 = output_arg_1 + io_arg_1
            assert type(output_chunk_from_io_1) == FFmpegOutput

            output_chunk_from_io_2 = io_arg_1 + output_arg_1
            assert type(output_chunk_from_io_2) == FFmpegOutput

            assert (
                output_chunk_from_io_1.group_option
                != output_chunk_from_io_2.group_option
            )


class InputOutputArgsTest(unittest.TestCase):
    def test_input_output_args(self):
        io_chunk = io_arg_1 + io_arg_2
        with self.subTest("Adding 2 arg create a FFmpegInputOutput"):
            assert type(io_chunk) == FFmpegInputOutput

        """with self.subTest("Render should raise error as no url is given so far"),\
         pytest.raises(Exception) as _:
            io_chunk.render()"""

        io_chunk_2 = io_chunk + io_arg_3
        with self.subTest(
            "Adding FFmpegInputOutput + arg to create a new FFmpegInputOutput"
        ):
            assert type(io_chunk_2) == FFmpegInputOutput
            assert io_chunk.group_option != io_chunk_2.group_option

        io_chunk_3 = io_arg_3 + io_chunk_2
        with self.subTest(
            "Adding arg + FFmpegInputOutput to create a new FFmpegInputOutput"
        ):
            assert type(io_chunk_3) == FFmpegInputOutput
            assert io_chunk.group_option != io_chunk_3.group_option

        with self.subTest(
            "arg + FFmpegInputOutput and FFmpegInputOutput + arg should be rendering different"
        ):
            assert io_chunk_2.group_option != io_chunk_3.group_option

        with self.subTest("Exception when type doesn't match"):
            with pytest.raises(Exception) as _:
                io_arg_1 + global_arg_1
            with pytest.raises(Exception) as _:
                io_chunk + global_arg_1

            with pytest.raises(Exception) as _:
                global_arg_1 + io_chunk

        with self.subTest("InOut Chunk + Input arg = InputChunk"):
            in_from_io = io_chunk + input_arg_1
            assert type(in_from_io) == FFmpegInput
        with self.subTest("InOut Chunk + Output arg = OutputChunk"):
            out_from_io = io_chunk + output_arg_1
            assert type(out_from_io) == FFmpegOutput


class FFmpegCmdTest(unittest.TestCase):
    def test_ffmpeg_cmd_args(self):
        cmd = FFmpegCmd()
        with self.subTest("Test Input args "):
            cmd_in = cmd + input_arg_1
            assert len(cmd_in.input_chunks) == 1
            assert len(cmd_in.output_chunks) == 0
            assert len(cmd_in.global_chunk.group_option) == 0
            assert cmd_in.input_chunks[0].group_option[0] == input_arg_1
            assert type(cmd_in.input_chunks[0]) == FFmpegInput

        with self.subTest("Test Output args"):
            cmd_out = cmd + output_arg_1
            assert len(cmd_out.input_chunks) == 0
            assert len(cmd_out.output_chunks) == 1
            assert len(cmd_out.global_chunk.group_option) == 0
            assert cmd_out.output_chunks[0].group_option[0] == output_arg_1
            assert type(cmd_out.output_chunks[0]) == FFmpegOutput

        with self.subTest("Test InOut args"), pytest.raises(Exception) as _:
            cmd + io_arg_1

        with self.subTest("Test Global args"):
            cmd_global = cmd + global_arg_1
            assert len(cmd_global.input_chunks) == 0
            assert len(cmd_global.output_chunks) == 0
            assert len(cmd_global.global_chunk.group_option) == 1
            assert cmd_global.global_chunk.group_option[0] == global_arg_1

        with self.subTest("Test Global Chunk"):
            cmd_global = cmd + (FFmpegGlobal() + global_arg_1)
            assert cmd_global.global_chunk.group_option == [global_arg_1]

        with (
            self.subTest("Can't add FFmpegInputOutput chunk"),
            pytest.raises(Exception) as _,
        ):
            cmd + FFmpegInputOutput()

    def test_complex_case(self):
        cmd = FFmpegCmd()
        cmd = (
            cmd
            + global_arg_1
            + (input_arg_1 + input_arg_2)("in.mp4")
            + input_arg_3("in2.mp4")
            + global_arg_2
            + (output_arg_1 + output_arg_2)("out.mp4")
        )
        assert cmd.render() == [
            "ffmpeg",
            "-global_arg_1",
            "-global_arg_2",
            "-input_arg_1",
            "-input_arg_2",
            "-input_arg_3",
            "in2.mp4",
            "-i",
            "in.mp4",
            "-output_arg_1",
            "-output_arg_2",
            "out.mp4",
        ]


class FFprobeCmdTest(unittest.TestCase):
    def test_ffprobe_cmd_args(self):
        cmd = FFprobe()
        cmd = (
            cmd + FFmpegArg("test", ArgFlag.GLOBAL) + FFmpegArg("test2", ArgFlag.GLOBAL)
        )
        cmd = cmd + FFmpegOutput("test.mp4")
        assert cmd.render() == ["ffprobe", "-test", "-test2", "test.mp4"]


@pytest.mark.parametrize(
    "test_input",
    [
        pytest.param(input_arg_1, id="Valid render expect input to have url"),
        pytest.param(
            input_arg_1 + input_arg_2, id="Valid render expect input to have url"
        ),
        pytest.param(output_arg_1, id="Valid render expect output to have url"),
        pytest.param(
            output_arg_1 + output_arg_2, id="Valid render expect output to have url"
        ),
    ],
)
def test_failure_rendering(test_input):
    with pytest.raises(Exception) as _:
        (FFmpegCmd() + test_input).render()


def test_stream_selector():
    tmp = input_arg_1["v"]
    assert tmp.render()[0] == f"-{input_arg_1.key}:v"


@pytest.mark.parametrize(
    "left,right,result",
    [
        pytest.param(FFmpegInput(), FFmpegInput(), FFmpegInput()),
        pytest.param(FFmpegInput(), FFmpegInputOutput(), FFmpegInput()),
        pytest.param(FFmpegOutput(), FFmpegOutput(), FFmpegOutput()),
        pytest.param(FFmpegOutput(), FFmpegInputOutput(), FFmpegOutput()),
        pytest.param(FFmpegInputOutput(), FFmpegInput(), FFmpegInput()),
        pytest.param(FFmpegInputOutput(), FFmpegOutput(), FFmpegOutput()),
        pytest.param(FFmpegInputOutput(), FFmpegInputOutput(), FFmpegInputOutput()),
        pytest.param(FFmpegGlobal(), FFmpegGlobal(), FFmpegGlobal()),
    ],
)
def test_chunk_resolution(left, right, result):
    assert type(result) == type(left + right)


@pytest.mark.parametrize(
    "left,right",
    [
        pytest.param(FFmpegInput(), FFmpegOutput()),
        pytest.param(FFmpegInput(), FFmpegGlobal()),
        pytest.param(FFmpegOutput(), FFmpegInput()),
        pytest.param(FFmpegOutput(), FFmpegGlobal()),
        pytest.param(FFmpegGlobal(), FFmpegInput()),
        pytest.param(FFmpegGlobal(), FFmpegOutput()),
        pytest.param(FFmpegGlobal(), FFmpegInputOutput()),
        pytest.param(FFmpegInputOutput(), FFmpegGlobal()),
    ],
)
def test_chunk_resolution_incorrect(left, right):
    with pytest.raises(Exception) as _:
        left + right


@pytest.mark.parametrize(
    "test",
    [
        pytest.param(
            FilterGraph() >> Filter("dummy", a="a", b=1)[["a"]:["b"]],
            id="FilterGraph object should be rendered",
        ),
        pytest.param(
            FilterChain() >> Filter("dummy", a="a", b=1)[["a"]:["b"]],
            id="FilterChain object should be rendered",
        ),
        pytest.param(
            Filter("dummy", a="a", b=1)[["a"]:["b"]],
            id="Filter object should be rendered",
        ),
    ],
)
def test_cmd_filter_graph(test):

    cmd = FFmpegCmd() + global_arg_2(test)
    assert cmd.render() == ["ffmpeg", "-global_arg_2", "[a]dummy=a=a:b=1[b]"]
