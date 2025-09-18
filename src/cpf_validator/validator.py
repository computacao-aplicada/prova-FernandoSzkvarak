# src/cpf_validator/validator.py
import re

class Validador:
    @staticmethod
    def _sanitizar(cpf: str) -> str | None:
        if not isinstance(cpf, str) or not cpf.strip():
            return None
        return re.sub(r'[.\-\s]', '', cpf)

    @staticmethod
    def _calcular_dv(digitos: list[int]) -> int:
        pesos = range(len(digitos) + 1, 1, -1)
        soma_ponderada = sum(d * p for d, p in zip(digitos, pesos))
        resto = soma_ponderada % 11
        
        return 0 if resto < 2 else 11 - resto

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        cpf_limpo = Validador._sanitizar(cpf)

        if not cpf_limpo or not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
            return False

        if len(set(cpf_limpo)) == 1:
            return False

        digitos = [int(d) for d in cpf_limpo]

        dv1_calculado = Validador._calcular_dv(digitos[:9])
        if dv1_calculado != digitos[9]:
            return False

        dv2_calculado = Validador._calcular_dv(digitos[:10])
        if dv2_calculado != digitos[10]:
            return False

        return True