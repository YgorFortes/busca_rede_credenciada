from enum import Enum


class Cargo(Enum):
    ADMIN = 1
    GERENTE = 2
    USUARIO = 3
    OBSERVADOR = 4


CARGOS_ESPERADOS = {Cargo.ADMIN, Cargo.GERENTE, Cargo.OBSERVADOR, Cargo.USUARIO}
