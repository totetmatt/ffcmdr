import pytest
from ffcmdr.run import run
from ffcmdr.cmd import FFmpegCmd
from ffcmdr.cmd import FFmpegInput
from ffcmdr.cmd import FFmpegOutput
from subprocess import PIPE
from unittest import mock


@pytest.fixture(autouse=True)
def mock_popen():
    with mock.patch(
        "ffcmdr.run.Popen",
        autospec=True,
    ) as _mock:
        _mock.return_value.communicate.return_value = (b"", b"")
        _mock.return_value.poll.return_value = 0
        yield _mock


@pytest.mark.parametrize(
    "test_cmd,expected_popen_call",
    [
        pytest.param(
            FFmpegCmd(),
            {"stdin": None, "stdout": None, "stderr": None},
            id="No pipe input",
        ),
        pytest.param(
            FFmpegCmd() + FFmpegInput("pipe:0"),
            {"stdin": PIPE, "stdout": None, "stderr": None},
            id="Pipe stdin",
        ),
        pytest.param(
            FFmpegCmd() + FFmpegOutput("pipe:1"),
            {"stdin": None, "stdout": PIPE, "stderr": None},
            id="Pipe stdout",
        ),
        pytest.param(
            FFmpegCmd() + FFmpegInput("pipe:0") + FFmpegOutput("pipe:1"),
            {"stdin": PIPE, "stdout": PIPE, "stderr": None},
            id="Pipe stdout",
        ),
    ],
)
def test_run(mock_popen, test_cmd, expected_popen_call):
    run(test_cmd)
    mock_popen.assert_called_with(test_cmd.render(), **expected_popen_call)
    pass


def test_run_exception_when_poll_return_not_0(mock_popen):
    mock_popen.return_value.poll.return_value = 1
    with pytest.raises(Exception) as _:
        run(FFmpegCmd())
