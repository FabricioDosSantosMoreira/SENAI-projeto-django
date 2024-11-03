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

    PROTECAO_OCULAR_E_FACIAL = 'Proteção Ocular e Facial',   'Proteção Ocular e Facial'
    PROTECAO_MAOS_E_BRACOS   = 'Proteção das Mãos e Braços', 'Proteção das Mãos e Braços'
    PROTECAO_CONTRA_QUEDA    = 'Proteção Contra Queda',      'Proteção Contra Queda'
    PROTECAO_RESPIRATORIA    = 'Proteção Respiratória',      'Proteção Respiratória'
    PROTECAO_PES_E_PERNAS    = 'Proteção dos Pés e Pernas',  'Proteção dos Pés e Pernas'
    PROTECAO_AUDITIVA        = 'Proteção Auditiva',          'Proteção Auditiva'
    

class StatusEmprestimo(models.TextChoices):

    EMPRESTADO = "Emprestado", "Emprestado"
    EM_USO     = "Em Uso",     "Em Uso"
    FORNECIDO  = "Fornecido",  "Fornecido"
    DEVOLVIDO  = "Devolvido",  "Devolvido"
    DANIFICADO = "Danificado", "Danificado"
    PERDIDO    = "Perdido",    "Perdido"

    
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

