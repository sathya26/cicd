from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator


def create_app() -> FastAPI:
    app = FastAPI(title="CI/CD FastAPI App")

    Instrumentator().instrument(app).expose(app)

    @app.get("/", tags=["Root"])
    def read_root():
        return {"message": "CI/CD Working!"}

    @app.get("/health", tags=["Health"])
    def health():
        return {"status": "ok"}

    return app


app = create_app()
