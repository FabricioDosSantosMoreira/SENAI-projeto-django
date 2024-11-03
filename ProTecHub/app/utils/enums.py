from django.db import models


class TipoUsuario(models.TextChoices):

    ADMINISTRADOR  = 'ADMINISTRADOR', 'Administrador'
    SUPERVISOR     = 'SUPERVISOR',    'Supervisor'
    COLABORADOR    = 'COLABORADOR',   'Colaborador'


class Cargos(models.TextChoices):

    CONSTRUTOR = 'CONSTRUTOR', 'Construtor'
    MARKETING  = 'MARKETING',  'Marketing'
    LOGISTICA  = 'LOGISTICA',  'Logística'
    GERENTE    = 'GERENTE',    'Gerente'
    TI         = 'TI',         'Técnico de TI'


class CategoriaEPI(models.TextChoices):

    PROTECAO_OCULAR_E_FACIAL = 'PROTECAO_OCULAR_E_FACIAL', 'Proteção Ocular e Facial'
    PROTECAO_MAOS_E_BRACOS   = 'PROTECAO_MAOS_E_BRACOS',   'Proteção das Mãos e Braços'
    PROTECAO_CONTRA_QUEDA    = 'PROTECAO_CONTRA_QUEDA',    'Proteção Contra Queda'
    PROTECAO_RESPIRATORIA    = 'PROTECAO_RESPIRATORIA',    'Proteção Respiratória'
    PROTECAO_PES_E_PERNAS    = 'PROTECAO_PES_E_PERNAS',    'Proteção dos Pés e Pernas'
    PROTECAO_AUDITIVA        = 'PROTECAO_AUDITIVA',        'Proteção Auditiva'
    

class StatusEmprestimo(models.TextChoices):

    EMPRESTADO = "EMPRESTADO", "Emprestado"
    EM_USO     = "EM_USO",     "Em Uso"
    FORNECIDO  = "FORNECIDO",  "Fornecido"
    DEVOLVIDO  = "DEVOLVIDO",  "Devolvido"
    DANIFICADO = "DANIFICADO", "Danificado"
    PERDIDO    = "PERDIDO",    "Perdido"

    
    @classmethod
    def obter_status_para_cadastro(cls):
        return [
            (cls.EMPRESTADO, cls.EMPRESTADO.label),
            (cls.EM_USO, cls.EM_USO.label),
            (cls.FORNECIDO, cls.FORNECIDO.label),
        ]
    
    @classmethod
    def obter_status_para_arquivar(cls):
        return [
            (cls.DEVOLVIDO, cls.DEVOLVIDO.label),
            (cls.DANIFICADO, cls.DANIFICADO.label),
            (cls.PERDIDO, cls.PERDIDO.label),
        ]

