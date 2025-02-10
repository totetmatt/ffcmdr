import pytest

from ffcmdr.filter_complex import Filter
from ffcmdr.filter_complex import FilterChain
from ffcmdr.filter_complex import FilterGraph


filter_a = Filter("filter_a")
filter_b = Filter("filter_b")
filter_c = Filter("filter_c")
filter_d = Filter("filter_d")


@pytest.mark.parametrize(
    "test_input,expected_render,expected_class",
    [
        pytest.param(
            FilterChain() >> filter_a,
            "filter_a",
            FilterChain,
            id="FilterChain() >> filter_a",
        ),
        pytest.param(
            filter_a >> FilterChain(),
            "filter_a",
            FilterChain,
            id="filter_a >> FilterChain()",
        ),
        pytest.param(
            filter_a >> filter_b,
            "filter_a,filter_b",
            FilterChain,
            id="filter_a >> filter_b",
        ),
        pytest.param(
            filter_a >> (FilterChain() >> filter_b),
            "filter_a,filter_b",
            FilterChain,
            id="filter_a >> (FilterChain() >> filter_b)",
        ),
        pytest.param(
            filter_a >> filter_b >> filter_c,
            "filter_a,filter_b,filter_c",
            FilterChain,
            id="filter_a >> filter_b >> filter_c",
        ),
        pytest.param(
            (filter_a >> filter_b) >> filter_c,
            "filter_a,filter_b,filter_c",
            FilterChain,
            id="(filter_a >> filter_b) >> filter_c",
        ),
        pytest.param(
            filter_a >> (filter_b >> filter_c),
            "filter_a,filter_b,filter_c",
            FilterChain,
            id="filter_a >>(filter_b >> filter_c)",
        ),
        pytest.param(
            (filter_a >> filter_b) >> (filter_c >> filter_d),
            "filter_a,filter_b,filter_c,filter_d",
            FilterChain,
            id="(filter_a >>filter_b) >> (filter_c>>filter_d)",
        ),
        pytest.param(
            FilterGraph() >> filter_a,
            "filter_a",
            FilterGraph,
            id="FilterGraph() >> filter_a",
        ),
        pytest.param(
            filter_a >> FilterGraph(),
            "filter_a",
            FilterGraph,
            id="filter_a >> FilterGraph()",
        ),
        pytest.param(
            filter_a >> filter_b >> FilterGraph(),
            "filter_a,filter_b",
            FilterGraph,
            id="filter_a  >> filter_b >> FilterGraph()",
        ),
        pytest.param(
            FilterGraph() >> filter_a >> filter_b,
            "filter_a,filter_b",
            FilterGraph,
            id="FilterGraph() >> filter_a  >> filter_b",
        ),
        pytest.param(
            FilterGraph() >> (filter_a >> filter_b),
            "filter_a,filter_b",
            FilterGraph,
            id="FilterGraph() >> (filter_a  >> filter_b)",
        ),
        pytest.param(
            filter_a + FilterChain(),
            "filter_a",
            FilterGraph,
            id="filter_a +  FilterChain()",
        ),
        pytest.param(
            FilterChain() + filter_a,
            "filter_a",
            FilterGraph,
            id="FilterChain()+ filter_a",
        ),
        pytest.param(
            FilterChain() + filter_a >> filter_b,
            "filter_a,filter_b",
            FilterGraph,
            id="FilterChain()+ filter_a >> filter_b",
        ),
        pytest.param(
            FilterChain() + (filter_a >> filter_b),
            "filter_a,filter_b",
            FilterGraph,
            id="FilterChain()+ (filter_a >> filter_b)",
        ),
        pytest.param(
            filter_a >> filter_b + FilterChain(),
            "filter_a,filter_b",
            FilterGraph,
            id="filter_a >> filter_b + FilterChain()",
        ),
        pytest.param(
            (filter_a >> filter_b) + FilterChain(),
            "filter_a,filter_b",
            FilterGraph,
            id="(filter_a >> filter_b) + FilterChain()",
        ),
        pytest.param(
            filter_a + filter_b,
            "filter_a;filter_b",
            FilterGraph,
            id="filter_a + filter_b",
        ),
        pytest.param(
            filter_a + filter_b + filter_c,
            "filter_a;filter_b;filter_c",
            FilterGraph,
            id="filter_a + filter_b + filter_c",
        ),
        pytest.param(
            filter_a >> filter_b + filter_c,
            "filter_a,filter_b;filter_c",
            FilterGraph,
            id="filter_a >> filter_b + filter_c",
        ),
        pytest.param(
            (filter_a >> filter_b) + filter_c,
            "filter_a,filter_b;filter_c",
            FilterGraph,
            id="(filter_a >> filter_b) + filter_c",
        ),
        # pytest.param( (FilterChain() >> filter_a) + filter_b, "filter_a;filter_b",FilterGraph,id="(FilterChain() >> filter_a) + filter_b"),
        pytest.param(
            filter_a + FilterGraph(),
            "filter_a",
            FilterGraph,
            id="filter_a + FilterGraph()",
        ),
        pytest.param(
            filter_a + (FilterGraph() >> filter_b),
            "filter_a;filter_b",
            FilterGraph,
            id="filter_a + (FilterGraph() >> filter_b)",
        ),
        pytest.param(
            (FilterChain() >> filter_a) + (FilterGraph()),
            "filter_a",
            FilterGraph,
            id="(FilterChain()>>filter_a) + (FilterGraph())",
        ),
        pytest.param(
            (FilterChain() >> filter_a) + (FilterGraph() >> filter_b),
            "filter_a;filter_b",
            FilterGraph,
            id="(FilterChain()>>filter_a) + (FilterGraph())",
        ),
        pytest.param(
            (FilterGraph() >> filter_a) + (FilterChain() >> filter_b),
            "filter_a;filter_b",
            FilterGraph,
            id="(FilterGraph()>>filter_a) + (FilterChain()>>filter_b)",
        ),
    ],
)
def test_filter_composition(test_input, expected_render, expected_class):
    print(test_input)
    assert test_input.render() == expected_render
    assert type(test_input) == expected_class


@pytest.mark.parametrize(
    "test_input,expected_render",
    [
        pytest.param(filter_a, "filter_a", id="Default"),
        pytest.param(filter_a[["a"]:], "[a]filter_a", id="input"),
        pytest.param(filter_a[:["a"]], "filter_a[a]", id="output"),
        pytest.param(filter_a[["a"]:["b"]], "[a]filter_a[b]", id="input and output"),
        pytest.param(
            filter_a[["a", "c"]:["b", "d"]],
            "[a][c]filter_a[b][d]",
            id="input and output",
        ),
        pytest.param(Filter("filter_a", 1, 2), "filter_a=1:2", id="unnamed params"),
        pytest.param(
            Filter("filter_a", a=1, b=2), "filter_a=a=1:b=2", id="named params"
        ),
        pytest.param(
            Filter("filter_a", 1, b=2), "filter_a=1:b=2", id="unnamed and named params"
        ),
        pytest.param(filter_a(1, b=2), "filter_a=1:b=2", id="unnamed and named params"),
    ],
)
def test_filter_selector(test_input, expected_render):
    assert test_input.render() == expected_render


def test_immutable_operation():
    tmp_filter_a = filter_a[["a"]:["b"]]
    assert tmp_filter_a.render() == "[a]filter_a[b]"
    assert filter_a.render() == "filter_a"
