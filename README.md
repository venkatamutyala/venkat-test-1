# QR-code-generator

A FastAPI endpoint that creates QR codes based off given URLs

## Running the QR code generator

- Development environment

```python
uvicorn qr-generator:app --reload
```

- Ensure [public](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/restricting-the-visibility-of-forwarded-ports#overview) port forwarding in codespace.

## Running the Dockerfile

```bash
$ docker build -t my-fastapi-app .
$ docker run -p 80:80 my-fastapi-app
```

## Access the website

- In your browser, navigate to ```https://mbaoma-ominous-yodel-7pj9wxg69jx2w6j5-8000.preview.app.github.dev/v1/qr?url=<your-url>```

A QR code will be generated
<img width="931" alt="image" src="https://github.com/GlueOps/github-actions-build-push-containers/assets/49791498/d66f773c-e05c-43db-b978-0bebbb303bb2">
