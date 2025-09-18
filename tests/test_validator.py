# tests/test_validator.py
from src.cpf_validator.validator import Validador

def test_deve_validar_cpf_valido():
    assert Validador.validar_cpf("529.982.247-25") is True
    assert Validador.validar_cpf("52998224725") is True

def test_deve_rejeitar_entradas_invalidas():
    assert Validador.validar_cpf(None) is False
    assert Validador.validar_cpf("") is False
    assert Validador.validar_cpf("   ") is False
    assert Validador.validar_cpf("529.982.247-2X") is False
    assert Validador.validar_cpf("00000000000") is False
    assert Validador.validar_cpf("111.111.111-11") is False

def test_deve_rejeitar_tamanhos_incorretos():
    assert Validador.validar_cpf("1234567890") is False
    assert Validador.validar_cpf("123456789012") is False

def test_deve_rejeitar_cpf_com_dv_incorreto():
    assert Validador.validar_cpf("529.982.247-24") is False
    assert Validador.validar_cpf("123.456.789-00") is False