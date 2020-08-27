def aumentar(preco = 0, taxa = 0, formato=False):
    """
    :param preco: É o valor digitado pelo cliente
    :param taxa: Corresponde a porcentagem
    :param formato: Formatação de moeda.
    :return: Valor com aumento em porcentagem.
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco = 0, taxa = 0, formato=False):
    """
    :param preco: Valor digitado pelo cliente.
    :param taxa: Valor que será descontado.
    :param formato: Formatação em moeda.
    :return: Valor com desconto em porcentagem.
    """
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco = 0, formato=False):
    """
    :param preco: Valor informado pelo cliente.
    :param formato: Formatação em moeda.
    :return: Valor em dobro.
    """
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco = 0, formato=False):
    """
    :param preco: Valor informado pelo cliente.
    :param formato: Formatação em moeda.
    :return: Valor pela metade.
    """
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco = 0, moeda ='R$'):
    """
    :param preco: Valor informado pelo cliente.
    :param moeda: Se não informada, será em R$.
    :return: Moeda formatada em R$ e com virgula no lugar de ponto.
    """
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
