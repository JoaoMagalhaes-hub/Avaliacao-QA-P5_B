import pytest
from password_validator import validar_senha

def test_tamanho_invalido():
    assert not validar_senha("Ab1!")  # Muito curta
    assert not validar_senha("A" * 21 + "b1!")  # Muito longa

def test_falta_maiuscula():
    assert not validar_senha("senha@123")

def test_falta_minuscula():
    assert not validar_senha("SENHA@123")

def test_falta_numero():
    assert not validar_senha("Senha@")

def test_falta_caractere_especial():
    assert not validar_senha("Senha123")

def test_contem_espaco():
    assert not validar_senha("Senha 123!")

def test_senha_valida():
    assert validar_senha("Senha@123")
    assert validar_senha("Abcdef1!")
