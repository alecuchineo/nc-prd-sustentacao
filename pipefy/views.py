import requests
import json
import time

from django.shortcuts import render, redirect
from pipefy.forms import ReprocessamentoPipefy,PipesManutencao
from pipefy.models import PipesManutencao, PipesConfig
from django.contrib import messages


token = "Bearer "

PARAR_PROCESSO = False

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = ReprocessamentoPipefy()
    
    return render(request, "pipefy/index.html", {"form": form})

def submit(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = ReprocessamentoPipefy()
    if request.method == "POST":
        
        form = ReprocessamentoPipefy(request.POST)
        
        if form.is_valid():
            PARAR_PROCESSO = False
            phase_id = form["phase"].value()
            url_webhook = form["url"].value()
            tempo = form["tempo_pausa"].value() * 60 if form["tempo_pausa"].value() else 300
            pipe_req = busca_pipe_id(phase_id)
            pipe_id = pipe_req["data"]["phase"]["repo_id"]
            
            cards = get_cards_phase(phase_id)

            counter = 0
            for card in cards["data"]["phase"]["cards"]["edges"]:
                if counter > 10:
                    counter = 0
                    time.sleep(tempo)
                
                counter +=1
                
                if PARAR_PROCESSO:
                    break
                
                request_reprocessa(card["node"]["id"], phase_id, pipe_id, url_webhook)
                print( card["node"]["id"])
                
                time.sleep(2)
    return render(request, "pipefy/index.html", {"form": form})


def parar_processo(request):
    PARAR_PROCESSO = True

def request_pipefy(query: str) -> requests.Response:
    try:
        resp = requests.post(
            url="https://api.pipefy.com/graphql",
            json={"query": query},
            headers={'Content-Type': 'application/json',
                     'Authorization': token}
        )
        return resp.json()
    except ValueError:
        print(ValueError)

def request_reprocessa(id_card, pipe_id, phase, url):
    body = {
      "data": {
          "action": "card.create",
          "card": {
              "id": id_card,
              "pipe_id": pipe_id
          },
          "to":{
              "id": phase
          }
      }
    }

    headers = {"Authorization": ""}

    ret = requests.post(url, data=json.dumps(body), headers=headers)
    return ret.text


def get_cards_phase(phase_id):
    query =f"{{phase(id:{phase_id}){{cards{{edges{{node{{id}}}}}}}}}}"
    return request_pipefy(query)

def busca_pipe_id(phase_id):
    query =f"{{phase(id:{phase_id}){{repo_id}}}}"
    return request_pipefy(query)