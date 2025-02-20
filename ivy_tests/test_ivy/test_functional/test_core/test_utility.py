"""Collection of tests for utility functions."""

# global
from hypothesis import strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_test


# all
@handle_test(
    fn_tree="functional.ivy.all",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("valid"),
        valid_axis=True,
        max_axes_size=1,
    ),
    keepdims=st.booleans(),
)
def test_all(
    dtype_x_axis,
    keepdims,
    as_variable,
    num_positional_args,
    native_array,
    container_flags,
    with_out,
    instance_method,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtype, x, axis = dtype_x_axis
    axis = axis if axis is None or isinstance(axis, int) else axis[0]
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        num_positional_args=num_positional_args,
        native_array_flags=native_array,
        container_flags=container_flags,
        instance_method=instance_method,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        x=x[0],
        axis=axis,
        keepdims=keepdims,
    )


# any
@handle_test(
    fn_tree="functional.ivy.any",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("valid", full=True),
        valid_axis=True,
        max_axes_size=1,
    ),
    keepdims=st.booleans(),
)
def test_any(
    dtype_x_axis,
    keepdims,
    as_variable,
    num_positional_args,
    native_array,
    container_flags,
    with_out,
    instance_method,
    backend_fw,
    fn_name,
    on_device,
    ground_truth_backend,
):
    input_dtype, x, axis = dtype_x_axis
    axis = axis if axis is None or isinstance(axis, int) else axis[0]
    helpers.test_function(
        ground_truth_backend=ground_truth_backend,
        input_dtypes=input_dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        num_positional_args=num_positional_args,
        native_array_flags=native_array,
        container_flags=container_flags,
        instance_method=instance_method,
        fw=backend_fw,
        fn_name=fn_name,
        on_device=on_device,
        x=x[0],
        axis=axis,
        keepdims=keepdims,
    )
