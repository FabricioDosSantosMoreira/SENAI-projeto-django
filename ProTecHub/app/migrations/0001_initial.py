import app.utils.enums
import app.utils.utils

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    # Insere dados de exemplo
    def inserir_dados(apps, schema_editor):
        from app.utils import (
            obter_data_atual, 
            obter_data_do_proximo_mes,
            obter_data_do_proximo_ano,            
        )

        Usuario = apps.get_model('app', 'Usuario')
        Equipamento = apps.get_model('app', 'Equipamento')
        Emprestimo = apps.get_model('app', 'Emprestimo')
        Historico = apps.get_model('app', 'Historico')
        
        # Inserir usuários
        if not Usuario.objects.filter(email="administrador@example.com").exists():
            Usuario.objects.create(
                nome="Administrador",
                email="administrador@example.com",
                cargo="TI",
                tipo="ADMINISTRADOR",
                foto="usuarios/exemplos/exemplo-1.jpg",
                data_admissao=obter_data_atual(),
                password="pbkdf2_sha256$870000$msPKoTTGCXKpkI8n62hPL1$WHF8h4UtRTg5hJ9xakoNcU5n7lnOIxcnTQqcK6kflIE=",
                is_superuser=False,
                username="administrador@example.com",
                first_name="..",
                last_name="..",
                is_staff=False,
                is_active=True,
                date_joined=obter_data_atual(),
            )
                
        if not Usuario.objects.filter(email="supervisor@example.com").exists():
            Usuario.objects.create(
                nome="Supervisor",
                email="supervisor@example.com",
                cargo="GERENTE",
                tipo="SUPERVISOR",
                foto="usuarios/exemplos/exemplo-2.jpg",
                data_admissao=obter_data_atual(),
                password="pbkdf2_sha256$870000$msPKoTTGCXKpkI8n62hPL1$WHF8h4UtRTg5hJ9xakoNcU5n7lnOIxcnTQqcK6kflIE=",
                is_superuser=False,
                username="supervisor@example.com",
                first_name="..",
                last_name="..",
                is_staff=False,
                is_active=True,
                date_joined=obter_data_atual(),
            )
            
        if not Usuario.objects.filter(email="colaborador@example.com").exists():
            Usuario.objects.create(
                nome="Colaborador",
                email="colaborador@example.com",
                cargo="CONSTRUTOR",
                tipo="COLABORADOR",
                foto="usuarios/exemplos/exemplo-1.jpg",
                data_admissao=obter_data_atual(),
                password="pbkdf2_sha256$870000$msPKoTTGCXKpkI8n62hPL1$WHF8h4UtRTg5hJ9xakoNcU5n7lnOIxcnTQqcK6kflIE=",
                is_superuser=False,
                username="colaborador@example.com",
                first_name="..",
                last_name="..",
                is_staff=False,
                is_active=True,
                date_joined=obter_data_atual(),
            )

        # Inserir equipamentos
        if not Equipamento.objects.filter(nome="Óculos de Proteção").exists():
            Equipamento.objects.create(
                nome="Óculos de Proteção",
                categoria="PROTECAO_OCULAR_E_FACIAL",
                quantidade_total=50,
                validade=obter_data_do_proximo_ano()
            )

        if not Equipamento.objects.filter(nome="Luvas de Segurança").exists():
            Equipamento.objects.create(
                nome="Luvas de Segurança",
                categoria="PROTECAO_MAOS_E_BRACOS",
                quantidade_total=100,
                validade=obter_data_do_proximo_ano()
            )

        if not Equipamento.objects.filter(nome="Capacete de Segurança").exists():
            Equipamento.objects.create(
                nome="Capacete de Segurança",
                categoria="PROTECAO_CONTRA_QUEDA",
                quantidade_total=75,
                validade=obter_data_do_proximo_ano()
            )

        # Inserir empréstimos
        if not Emprestimo.objects.filter(usuario_id=2, equipamento_id=1).exists():
            Emprestimo.objects.create(
                quantidade=25,
                status="EMPRESTADO",
                data_emprestimo=obter_data_atual(),
                data_devolucao_prevista=obter_data_do_proximo_mes(),
                usuario_id=2,
                equipamento_id=1
            )

        if not Emprestimo.objects.filter(usuario_id=3, equipamento_id=2).exists():
            Emprestimo.objects.create(
                quantidade=2,
                status="EM_USO",
                data_emprestimo=obter_data_atual(),
                data_devolucao_prevista=obter_data_do_proximo_mes(),
                usuario_id=3,
                equipamento_id=2
            )

        if not Emprestimo.objects.filter(usuario_id=3, equipamento_id=3).exists():
            Emprestimo.objects.create(
                quantidade=1,
                status="FORNECIDO",
                data_emprestimo=obter_data_atual(),
                data_devolucao_prevista=obter_data_do_proximo_mes(),
                usuario_id=3,
                equipamento_id=3
            )

        # Inserir histórico
        if not Historico.objects.filter(nome_equipamento="Óculos de Proteção", nome_usuario="Supervisor").exists():
            Historico.objects.create(
                quantidade=50,
                status="DEVOLVIDO",
                observacao="Equipamento devolvido em boas condições.",
                data_emprestimo=obter_data_atual(),
                data_devolucao_efetiva=obter_data_atual(),
                nome_equipamento="Óculos de Proteção",
                nome_usuario="Supervisor"
            )

        if not Historico.objects.filter(nome_equipamento="Luvas de Segurança", nome_usuario="Colaborador").exists():
            Historico.objects.create(
                quantidade=2,
                status="DANIFICADO",
                observacao="Equipamento apresentou desgaste durante o uso.",
                data_emprestimo=obter_data_atual(),
                data_devolucao_efetiva=obter_data_atual(),
                nome_equipamento="Luvas de Segurança",
                nome_usuario="Colaborador"
            )

        if not Historico.objects.filter(nome_equipamento="Capacete de Segurança", nome_usuario="Colaborador").exists():
            Historico.objects.create(
                quantidade=1,
                status="PERDIDO",
                observacao="Equipamento não foi devolvido no prazo.",
                data_emprestimo=obter_data_atual(),
                data_devolucao_efetiva=None,
                nome_equipamento="Capacete de Segurança",
                nome_usuario="Colaborador"
            )
               
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('categoria', models.CharField(choices=[('PROTECAO_OCULAR_E_FACIAL', 'Proteção Ocular e Facial'), ('PROTECAO_MAOS_E_BRACOS', 'Proteção das Mãos e Braços'), ('PROTECAO_CONTRA_QUEDA', 'Proteção Contra Queda'), ('PROTECAO_RESPIRATORIA', 'Proteção Respiratória'), ('PROTECAO_PES_E_PERNAS', 'Proteção dos Pés e Pernas'), ('PROTECAO_AUDITIVA', 'Proteção Auditiva')], max_length=100)),
                ('quantidade_total', models.PositiveIntegerField(default=1)),
                ('validade', models.DateField(default=app.utils.utils.obter_data_do_proximo_ano)),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('status', models.CharField(choices=app.utils.enums.StatusEmprestimo.obter_status_para_arquivar, default='DEVOLVIDO', max_length=20)),
                ('observacao', models.TextField()),
                ('data_emprestimo', models.DateTimeField()),
                ('data_devolucao_efetiva', models.DateTimeField(default=app.utils.utils.obter_data_atual, null=True)),
                ('nome_equipamento', models.CharField(max_length=255)),
                ('nome_usuario', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cargo', models.CharField(choices=[('CONSTRUTOR', 'Construtor'), ('MARKETING', 'Marketing'), ('LOGISTICA', 'Logística'), ('GERENTE', 'Gerente'), ('TI', 'Técnico de TI')], max_length=24)),
                ('tipo', models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('SUPERVISOR', 'Supervisor'), ('COLABORADOR', 'Colaborador')], max_length=24)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='usuarios/')),
                ('data_admissao', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(choices=app.utils.enums.StatusEmprestimo.obter_status_para_cadastro, default='EMPRESTADO', max_length=20)),
                ('data_emprestimo', models.DateTimeField(default=app.utils.utils.obter_data_atual)),
                ('data_devolucao_prevista', models.DateTimeField(default=app.utils.utils.obter_data_do_proximo_mes)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos', to='app.equipamento')),
            ],
        ),

        migrations.RunPython(inserir_dados),
    ]
