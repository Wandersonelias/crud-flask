import pytest
import requests

#Criano o teste de CRUD
BASE_URL = "http://127.0.0.1:5000"
task =[]


#Testando o create task
def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f'{BASE_URL}/tasks',json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "mensagem" in response_json # Verifica se mensagem retornou
    assert "id" in response_json #Verifica se o id está vindo na menagem
    task.append(response_json['id']) # Testando se ele está adicionando as tasks

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if task:
        task_id = task[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]

def test_update_task():
    if task:
        task_id = task[0]
        payload = {
	                    "title":"configurar servidor",
	                    "description": "Nova descrição usando os testes",
                        "completed": True
                    }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}",json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "mensagem" in response_json

        #Verifica se relamente ocorreu a atulização da tarefa

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]




def test_delete_task():
    if task:
        task_id = task[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert "mensagem" in response_json
