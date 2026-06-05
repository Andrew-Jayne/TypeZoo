def load_var[ReturnType](
    var_name: str,
    *,
    default_value: ReturnType = None,
    return_type: type[ReturnType] = str,
    mandatory: bool = False,
) -> ReturnType:
    from json import JSONDecodeError, loads
    from os import environ

    value = environ.get(var_name)
    if value is None:
        if mandatory is True:
            raise OSError(f"Environment variable '{var_name}' is required but not set.")
        return default_value

    try:
        match return_type():
            case bool():  # MUST come before int(): bool is a subclass of int
                match value:
                    case "True":
                        return True  # pyright: ignore[reportReturnType]
                    case "False":
                        return False  # pyright: ignore[reportReturnType]
                    case _:
                        raise ValueError(
                            f"value {value!r} cannot be converted to bool.",
                            "Only 'True' and 'False' are accepted.",
                        )
            case int():
                return int(value)  # pyright: ignore[reportReturnType]
            case float():
                return float(value)  # pyright: ignore[reportReturnType]
            case str():
                return value  # pyright: ignore[reportReturnType]
            case list():
                return loads(value)  # pyright: ignore[reportAny]
            case dict():
                return loads(value)  # pyright: ignore[reportAny]
            case _:
                raise TypeError(f"Unsupported return_type: {return_type}")
    except (ValueError, TypeError, JSONDecodeError) as conversion_error:
        raise ValueError(
            f"Failed to convert environment variable '{var_name}': {conversion_error}"
        ) from conversion_error
