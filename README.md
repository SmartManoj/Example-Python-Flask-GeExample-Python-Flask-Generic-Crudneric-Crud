

# Example Python Flask Generic Crud

 Simple example python flask generic crud app for sqlite.

Forked from : https://github.com/gurkanakdeniz/example-flask-crud.git

Need little cleaning ; Feel free to PR 

## Screenshots


![image](screenshots.png)  
 
 
### Installing (for linux)

open the terminal and follow the white rabbit.


```
git clone https://github.com/gurkanakdeniz/example-flask-crud.git
```
```
cd example-flask-crud/
```
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
export FLASK_APP=crudapp.py
```
```
flask db init
```
```
flask db migrate -m "entries table"
```
```
flask db upgrade
```
```
flask run
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
