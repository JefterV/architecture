from starlette.responses import JSONResponse


def generate_error_message(message: str, title: str = None, **kwargs) -> dict:
    return {"title": title, "message": message, **kwargs}


def generate_error_response(*, status: int, message: str, title: str = "Erro", **kwargs) -> JSONResponse:
    return JSONResponse(status_code=status, content=generate_error_message(message, title=title, **kwargs))
