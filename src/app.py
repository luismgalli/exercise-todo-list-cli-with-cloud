import json, requests


apiURL = "http://ljavierrodriguez.pythonanywhere.com"
urlLogin = apiURL + "/api/login/"
urlPosts = apiURL + "/api/posts/"
urlRegister=apiURL+"/api/register/"

current_user = {}
todos = []

def getLogin(url,username,password):
    global current_user
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "username": user,
        "password": clave
    }
    req = requests.post(url=url, headers=headers, data=json.dumps(data))    
    print(req)
    current_user = req.json()
    print(current_user)
    

def getPosts(url):
    global current_user, todos
    header = {
        "Content-Type": "application/json",
        "Authorization": "Token " + current_user["token"]
    }
    req = requests.get(url=url, headers=header)
    print(req)
    todos = req.json()
    print(todos)
    
def savePost(url,title,content):
    global current_user, todos
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Token " + current_user["token"]
    }
    data = {
        "title": title,
        "content": content,
        "user_id": current_user["id"]
    }
    req = requests.post(url=url, headers=headers, data=json.dumps(data))

    if req.status_code == 201:
        todos.append(req.json())
    else:
        print("Error manao")


if __name__ == '__main__':
    stop = False
    print("Initializing todos with previous data or creating a new todo's list...")
    
    while stop == False:
        print("""
    Choose an option: 
        1. Logearse
        2. Ver tus post
        3. Crear un post
        4. Exit
    """)
        response = input()
        if response == "4":
            stop = True
        elif response == "3":
            print("crea tus post")
            print("Pon tu titulo: ")
            title = input()
            print("Pon tu contenido: ")
            content = input()
            savePost(urlPosts,title,content)
            pass
        elif response == "2":
            print("vacila tus posts")
            getPosts(urlPosts)
        elif response == "1":
            print("usuario: ")
            user = input()
            print("constraseña: ")
            clave = input()
            getLogin(urlLogin,user,clave)
        else:
            print("Invalid response, asking again...")