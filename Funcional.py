{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/camila-funes/Laboratorio1_PA/blob/Funcional/Funcional.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/camila-funes/Laboratorio1_PA.git\n",
        "%cd Laboratorio1_PA"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LlsqCrWuFxFt",
        "outputId": "17608933-bd92-4b8b-c605-ea89a04926a7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'Laboratorio1_PA'...\n",
            "remote: Enumerating objects: 28, done.\u001b[K\n",
            "remote: Counting objects: 100% (28/28), done.\u001b[K\n",
            "remote: Compressing objects: 100% (25/25), done.\u001b[K\n",
            "remote: Total 28 (delta 6), reused 0 (delta 0), pack-reused 0 (from 0)\u001b[K\n",
            "Receiving objects: 100% (28/28), 13.98 KiB | 13.98 MiB/s, done.\n",
            "Resolving deltas: 100% (6/6), done.\n",
            "/content/Laboratorio1_PA\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "x2lkbSrsF59C"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "03UsztDQ1Bx6",
        "outputId": "a9aebcf3-1d59-43e6-ef9a-ba2719cfd733"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting Funcional.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile Funcional.py\n",
        "import yaml\n",
        "\n",
        "def crear_pregunta(title, prompt, hints, tags):\n",
        "    return {\n",
        "        \"title\": title,\n",
        "        \"prompt\": prompt,\n",
        "        \"hints\": hints,\n",
        "        \"tags\": tags\n",
        "    }\n",
        "\n",
        "def cargar_preguntas():\n",
        "    preguntas = [\n",
        "        crear_pregunta(\"Invertir cadena\", \"Escribe una función que invierta una cadena dada.\",\n",
        "                       [\"Podés usar slicing con [::-1]\", \"Pensá en un bucle for\"], [\"strings\", \"principiante\"]),\n",
        "        crear_pregunta(\"Números pares\", \"Genera una lista con todos los números pares del 1 al 100.\",\n",
        "                       [\"Usá range() con pasos\"], [\"loops\", \"listas\"]),\n",
        "        crear_pregunta(\"Factorial\", \"Implementa una función que calcule el factorial de un número.\",\n",
        "                       [\"Recursión es una opción\", \"Un bucle también funciona\"], [\"math\", \"recursión\"]),\n",
        "        crear_pregunta(\"Contar vocales\", \"Escribe una función que cuente cuántas vocales hay en una cadena.\",\n",
        "                       [\"Pensá en lower()\"], [\"strings\", \"funciones\"]),\n",
        "        crear_pregunta(\"Palíndromo\", \"Verifica si una palabra es un palíndromo.\",\n",
        "                       [\"Compara cadena con su inverso\"], [\"strings\", \"principiante\"]),\n",
        "        crear_pregunta(\"Máximo en lista\", \"Encuentra el número mayor en una lista sin usar max().\",\n",
        "                       [\"Iterá con un bucle\"], [\"listas\", \"principiante\"]),\n",
        "        crear_pregunta(\"Números primos\", \"Crea una función que determine si un número es primo.\",\n",
        "                       [\"Dividí por todos los menores a él\", \"Optimización: hasta la raíz cuadrada\"], [\"math\", \"funciones\"]),\n",
        "        crear_pregunta(\"Frecuencia de palabras\", \"Cuenta cuántas veces aparece cada palabra en un texto.\",\n",
        "                       [\"Usá un diccionario\", \"Pensá en split()\"], [\"diccionarios\", \"strings\"]),\n",
        "        crear_pregunta(\"Ordenar lista\", \"Ordena una lista de números sin usar sorted().\",\n",
        "                       [\"Probá con burbuja (bubble sort)\"], [\"algoritmos\", \"listas\"]),\n",
        "        crear_pregunta(\"Serie Fibonacci\", \"Genera los primeros N números de la serie de Fibonacci.\",\n",
        "                       [\"Usá un bucle y guardá los anteriores\"], [\"math\", \"principiante\"]),\n",
        "    ]\n",
        "\n",
        "    def cargar_preguntas_funcional(problems_path: Path) -> None:\n",
        "    \"\"\"Lee el YAML si existe, agrega las preguntas funcionales y reescribe el archivo.\"\"\"\n",
        "    existentes: List[Dict] = []\n",
        "    if problems_path.exists():\n",
        "        with problems_path.open(\"r\", encoding=\"utf-8\") as f:\n",
        "            existentes = yaml.safe_load(f) or []\n",
        "        if not isinstance(existentes, list):\n",
        "            existentes = []\n",
        "\n",
        "    nuevas = _nuevas_funcionales()\n",
        "    with problems_path.open(\"w\", encoding=\"utf-8\") as f:\n",
        "        yaml.safe_dump(existentes + nuevas, f, allow_unicode=True, sort_keys=False)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "CFj9_5L1FVtQ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}