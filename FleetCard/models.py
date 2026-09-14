from django.db import models


class Veiculo(models.Model):

    TIPOS_VEICULO = [
        ('carro', 'Carro'),
        ('moto', 'Motocicleta'),
        ('caminhao', 'Caminhão'),
    ]

    COMBUSTIVEIS = [
        ('gasolina', 'Gasolina'),
        ('etanol', 'Etanol'),
        ('diesel', 'Diesel'),
        ('flex', 'Flex'),
        ('eletrico', 'Elétrico'),
        ('hibrido', 'Híbrido'),
    ]

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS_VEICULO,
        verbose_name='Tipo'
    )

    marca = models.CharField(
        max_length=100,
        verbose_name='Marca'
    )

    modelo = models.CharField(
        max_length=100,
        verbose_name='Modelo'
    )

    placa = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Placa'
    )

    ano = models.IntegerField(
        verbose_name='Ano'
    )

    cor = models.CharField(
        max_length=50,
        verbose_name='Cor'
    )

    combustivel = models.CharField(
        max_length=20,
        choices=COMBUSTIVEIS,
        verbose_name='Combustível'
    )

    quilometragem = models.IntegerField(
        default=0,
        verbose_name='Quilometragem'
    )

    observacoes = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observações'
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de cadastro'
    )

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'