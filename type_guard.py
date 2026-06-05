def ensure_type(
    instance: object,
    expected_type: type,
    variable_name: str,
) -> None:
    if not isinstance(instance, expected_type):
        raise TypeError(
            f"'{variable_name}' must be of type {expected_type.__name__}, ",
            f"got {type(instance).__name__}",
        )
