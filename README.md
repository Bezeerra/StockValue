first steep:
    uvicorn main:app --reload

route:
    @app.route("directory")
    def index():
        return "hey"

monitoring:
    localhost:8000/docs
