from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK


async def excecute(function: callable, *args, **kwargs) -> JSONResponse:
    """
    Ejecuta una funcion del servicio y devuelve una respuesta.
    :param function: Funcion del servicio.
    :param args: Argumentos de la funcion del servicio.
    :param kwargs: Argumentos de la funcion ejecutora.
    :return: Respuesta del servicio.
    """
    try:
        response = await function(*args)
        is_created = kwargs.get("created", False)
        return JSONResponse(content=jsonable_encoder(response),
                            status_code=HTTP_201_CREATED if is_created else HTTP_200_OK)
    except Exception as exception:
        return JSONResponse(content={"error": str(exception)}, status_code=HTTP_400_BAD_REQUEST)
