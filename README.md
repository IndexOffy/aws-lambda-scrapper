# aws-lambda-scrapper

![GitHub Org's stars](https://img.shields.io/github/stars/IndexOffy?label=IndexOffy&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/IndexOffy/aws-lambda-scrapper?style=flat-square)

## Test the image locally

1 - Build the Docker image with the docker build command. The following example names the image `aws-lambda-scrapper` and gives it the `test` tag.

```bash
docker build --platform linux/amd64 -t aws-lambda-scrapper:test .
```

2 - Start the Docker image with the docker run command. In this example, `aws-lambda-scrapper` is the image name and `test` is the tag.

```bash
docker run -p 9000:8080 aws-lambda-scrapper:test
```

3 - This command invokes the function with an empty event and returns a response.

```bash
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"aws-lambda-scrapper"}'
```

### Commit Style

- ⚙️ FEATURE
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 BUILD
- ❤️️ TEST
- ⬆️ CI/CD
- ⚠️ SECURITY

### License

![GitHub](https://img.shields.io/github/license/IndexOffy/aws-lambda-scrapper?style=flat-square)

This project is licensed under the terms of the MIT license.

### Links

- [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads/version-selection)
- [Chrome for Testing availability](https://googlechromelabs.github.io/chrome-for-testing/#stable)
- [Seleniumhq.github.io - Service](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/drivers/test_service.py)
- [Deploy Python Lambda functions with container images](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions)
