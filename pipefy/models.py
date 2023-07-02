from django.db import models


class PipesConfig(models.Model):
    empresa = models.CharField(max_length=20, null=False, blank=False)
    pipe_name = models.CharField(max_length=30, null=False, blank=False)
    pipe_id = models.IntegerField(null=False, blank=False)
    phase_motor = models.CharField(max_length=20,null=False, blank=False)
    url_webhook = models.CharField(max_length=200,null=False, blank=False)
    def __str__(self):
        return f"{self.empresa} - {self.pipe_name}"


class PipesManutencao(models.Model):
    pipes_opcoes = [(pipe.id, pipe.__str__()) for pipe in PipesConfig.objects.all()]
    pipe = models.CharField(max_length=30, null=False, blank=False, choices=pipes_opcoes)
    processar_atrazados=models.BooleanField(default=False)

