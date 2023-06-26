
import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'app.main:app',
        port=8099,
        host="0.0.0.0",
        reload=True, reload_dirs=['app'],
        log_level="warning",
    )

    