# Backend and IoT service

- Make sure to install all dependencies in `requirements.txt`
```c
$ pip install -r requirements.txt
```

## Steps to start the Backend

- Start server with any port (in this case, port 3000)
```c
$ uvicorn app:be_app --port 3000 --reload
```
- If any error occurs, check if another port is open (in this case, port 8080)
```c
$ lsof -i :8080
```

## Steps to start IoT app for face recognition