import pytest

from src.worker_sdk.function_registry import FunctionRegistry


class TestFunctionRegistry:
    def test_registering_without_namespace(self) -> None:
        function_registry = FunctionRegistry()
        name = "inner"

        def inner_func() -> None:
            pass

        with pytest.raises(
            Exception, match="cannot find registered function with name"
        ):
            function_registry.get_function(name=name)

        function_registry.register_function(inner_func, name=name)
        func = function_registry.get_function(name=name)

        assert func == inner_func

        with pytest.raises(
            Exception, match="must not register multiple functions with the same name"
        ):
            function_registry.register_function(inner_func, name=name)

    def test_registering_with_namespace(self) -> None:
        function_registry = FunctionRegistry()
        name = "inner"
        namespace = "some_namespace"

        def inner_func() -> None:
            pass

        with pytest.raises(
            Exception, match="cannot find registered function with namespace"
        ):
            function_registry.get_function(name=name, namespace=namespace)

        function_registry.register_function(inner_func, name=name, namespace=namespace)
        func = function_registry.get_function(name=name, namespace=namespace)

        assert func == inner_func

        with pytest.raises(
            Exception,
            match="must not register multiple functions with the same namespace",
        ):
            function_registry.register_function(
                inner_func, name=name, namespace=namespace
            )

    def test_registering_multiple_functions(self) -> None:
        function_registry = FunctionRegistry()

        def inner_func() -> None:
            pass

        def inner_func2() -> None:
            pass

        def inner_func3() -> None:
            pass

        function_registry.register_function(inner_func, name="inner")
        function_registry.register_function(inner_func2, name="inner2")

        function_registry.register_function(
            inner_func, name="inner", namespace="some_namespace"
        )
        function_registry.register_function(
            inner_func3, name="inner3", namespace="some_namespace"
        )

        function_registry.register_function(
            inner_func, name="inner", namespace="another_namespace"
        )

        assert inner_func == function_registry.get_function(name="inner")
        assert inner_func2 == function_registry.get_function(name="inner2")

        assert inner_func == function_registry.get_function(
            name="inner", namespace="some_namespace"
        )
        assert inner_func3 == function_registry.get_function(
            name="inner3", namespace="some_namespace"
        )

        assert inner_func == function_registry.get_function(
            name="inner", namespace="another_namespace"
        )
