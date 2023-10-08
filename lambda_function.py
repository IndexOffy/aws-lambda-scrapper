from driver import chrome_browser


def handler(event, context) -> dict:
    driver = chrome_browser()
    driver.get("http://www.python.org")
    return {
        "statusCode": 200,
        "body": driver.title
    }
