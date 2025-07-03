from requests import Request, Session
from requests.exceptions import HTTPError
import Clases.Utils as utils
from Clases.ApiResponse import ApiResponse
from enum import Enum

class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

def send_request(method = HttpMethod.GET, url = None, payload = None) -> ApiResponse:
    
    try:
        session = Session()
        req = Request(method.value, utils.URL_SERVER + url, json = payload)
        prepped = session.prepare_request(req)
        res = session.send(prepped, timeout=5)
        res.raise_for_status()
        return ApiResponse(data=res.json())
    except HTTPError as err:
        print(f"error: {err}")
        error = err.response.json()
        return ApiResponse(error=error.get("detail", "Error con el servidor"))
    except Exception as err:
        print(f"error: {err}")
        return ApiResponse(error="Error conectando al servidor")

        
    