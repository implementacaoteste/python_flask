from modules.gestao_de_tarefa.models.tarefa import Tarefa
from modules.gestao_de_tarefa.dal.tarefa_dal import salvar_tarefa_no_bd

def salvar_tarefa(tarefa):
    # Aqui você pode adicionar qualquer lógica de validação antes de salvar a tarefa
    salvar_tarefa_no_bd(tarefa)
