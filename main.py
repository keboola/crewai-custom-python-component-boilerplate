import logging

import httpx
from keboola.component import CommonInterface, UserException

from src import shapes


def get_request(url) -> httpx.Response:
    try:
        response = httpx.get(url)
        response.raise_for_status()
        return response
    except httpx.HTTPError as e:
        raise Exception(f"Error fetching data from {url}: {e}")


def main():

    # accessing Keboola Common Interface
    ci = CommonInterface()
    params = ci.configuration.parameters
    print("User parameters:", params)
    print("Data folder path:", ci.data_folder_path)

    # running code from an imported module
    a = params.get("rectangle_a")
    b = params.get("rectangle_b")
    if a is None or b is None:
        raise UserException("Parameters 'rectangle_a' and 'rectangle_b' must be provided.")

    r = shapes.Rectangle(a=a, b=b)
    logging.info("Rectangle area: %s", r.area())
    logging.info("Rectangle perimeter: %s", r.perimeter())

    # making an HTTP request
    endpoint = params.get("endpoint")
    if not endpoint:
        raise UserException("Parameter 'endpoint' must be provided.")

    if resp := get_request(endpoint):
        print(resp.request.url, resp.status_code)

main()
