kill -9 $(lsof -t -i:5x000)
nohup python3 -m flask run --host=0.0.0.0 &


echo ws started
kill -9 $(lsof -t -i:8000)
nohup python3 -m http.server &


echo ui started