from flask import Flask
from flask import request, jsonify
from models.tasks import Tasks 

#Instanciando a class do flask
app = Flask(__name__)


#Discos em memória
tasks = []
id_control = 1

#Criar tarefa
@app.route('/tasks',methods=['POST'])
def create_task():
    global id_control
    data = request.get_json()
    new_task = Tasks(id=id_control,title=data["title"],description=data["description"])
    id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"mensagem":"Nova tarefa criada com sucesso!","id": new_task.id})

#Ler todas as tarefas
@app.route("/tasks",methods=['GET'])
def get_tasks():
    #Conversão de valores para dict usando o list comprehesion
    task_list = [task.to_dict() for task in tasks]

    #Conversão de valores para dict usando metodo verboso
    #for task in tasks:
    #    task_list.append(task.to_dict())

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

#Ler uma tarefa especifica
#Rota com paramentos onde fazemos uma converção para inteiros
@app.route('/tasks/<int:id>',methods=['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"mensagem": "tarefa não encontrada"}), 404




#Rota de atualização de registros
@app.route("/tasks/<int:id>",methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t #Seta como a tarefa que foi localizada que estava como None
            break
    if task == None:
        return jsonify({"mensagem":"Não foi possivel encontar a tarefa"}),404
    
    data = request.get_json()
    print(data)
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]
    return jsonify({"mensagem":"Tarefa atualizado com sucesso!"}),200
    
#Rota para deleção de tarefas    
@app.route("/tasks/<int:id>",methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
        print(task)
    if task == None:
        return jsonify({"mensagem":"Não foi possivel encontar a tarefa"}),404
    
    tasks.remove(task)
    return jsonify({"mensagem":"Tarefa removida com sucesso!"}),200





#Rota para aprendizado de uso de rotas com paramentos
# @app.route("/users/<string:username>",methods=['GET'])
# def get_user(username):
#     return jsonify(username)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=False)

