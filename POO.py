from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict
import yaml

@dataclass
class Question:
    title: str
    prompt: str
    hints: List[str]
    tags: List[str]

def _nuevas_poo() -> List[Question]:
    return [
        Question(
            title="Sumar 2 números",
            prompt="Definí una clase Calculadora con un método sumar(a, b) que devuelva la suma de dos enteros.",
            hints=["Definí un método dentro de la clase", "Retorná a + b"],
            tags=["basico", "clases", "metodos"]
        ),
        Question(
            title="Clase Persona",
            prompt="Creá una clase Persona con atributos nombre y edad. Implementá un método que imprima un saludo.",
            hints=["Usá __init__ para inicializar", "self.nombre y self.edad"],
            tags=["POO", "clases", "basico"]
        ),
        Question(
            title="Cuenta bancaria",
            prompt="Definí una clase CuentaBancaria con métodos depositar() y extraer(). Evitá que el saldo quede negativo.",
            hints=["Usá un atributo saldo", "Validá antes de restar"],
            tags=["POO", "encapsulamiento", "intermedio"]
        ),
        Question(
            title="Rectángulo",
            prompt="Creá una clase Rectangulo con base y altura. Agregá métodos area() y perimetro().",
            hints=["Métodos que devuelven base*altura", "Suma de lados para perímetro"],
            tags=["POO", "clases", "geometria"]
        ),
        Question(
            title="Empleado y Gerente",
            prompt="Implementá una clase Empleado y una subclase Gerente que agregue el atributo departamento.",
            hints=["Usá super() en el constructor", "Sobrescribí __str__"],
            tags=["POO", "herencia", "intermedio"]
        ),
        Question(
            title="Agenda de contactos",
            prompt="Definí una clase Agenda que guarde objetos Contacto (nombre, teléfono) y permita buscarlos por nombre.",
            hints=["Usá una lista interna", "Recorré los contactos"],
            tags=["POO", "composicion", "listas"]
        ),
        Question(
            title="Vehículos",
            prompt="Creá una clase Vehiculo y subclases Auto y Moto que sobrescriban un método descripcion().",
            hints=["Definí una clase base", "Sobrescribí métodos en subclases"],
            tags=["POO", "herencia", "polimorfismo"]
        ),
        Question(
            title="Animales que hablan",
            prompt="Definí una clase Animal con método hablar(). Subclases Perro y Gato deben devolver 'Guau' y 'Miau'.",
            hints=["Sobrescribí hablar() en cada clase", "Instanciá y probá"],
            tags=["POO", "herencia", "polimorfismo"]
        ),
        Question(
            title="Producto con precio",
            prompt="Creá una clase Producto con atributo privado _precio y validación para que no sea negativo.",
            hints=["Usá property para getters/setters", "Validá en el setter"],
            tags=["POO", "encapsulamiento", "validacion"]
        ),
        Question(
            title="Biblioteca y Libros",
            prompt="Definí clases Libro y Biblioteca. La biblioteca debe almacenar libros y listar sus títulos.",
            hints=["Composición: lista de objetos", "Agregá método listar()"],
            tags=["POO", "composicion", "intermedio"]
        ),
    ]


def cargar_preguntas(problems_path: Path) -> None:
    nuevas = _nuevas_poo()

    existentes: List[Dict] = []
    if problems_path.exists():
        with problems_path.open("r", encoding="utf-8") as f:
            existentes = yaml.safe_load(f) or []
        if not isinstance(existentes, list):
            existentes = []

    existentes.extend(asdict(q) for q in nuevas)

    with problems_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(existentes, f, allow_unicode=True, sort_keys=False)
