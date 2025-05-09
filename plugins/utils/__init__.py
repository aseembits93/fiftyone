"""
FiftyOne builtin plugins.

| Copyright 2017-2025, Voxel51, Inc.
| `voxel51.com <https://voxel51.com/>`_
|
"""
from functools import lru_cache


def get_subsets_from_custom_code(ctx, custom_code):
    try:
        local_vars = {}
        _EXEC_GLOBALS['ctx'] = ctx
        code_obj = _compile_custom_code(custom_code)
        exec(code_obj, _EXEC_GLOBALS, local_vars)
        data = local_vars.pop("subsets", {})
        return data, None
    except Exception as e:
        return None, str(e)

@lru_cache(maxsize=128)
def _compile_custom_code(custom_code):
    return compile(custom_code, "<string>", "exec")

_EXEC_GLOBALS = {"__builtins__": __builtins__}
