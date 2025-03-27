#!python

from typing import Callable
import re

verifications: list[tuple[Callable[[str], bool], str]] = [
    (lambda x: len(x) > 8, "Senha deve ser maior do que 8 caracteres"),
    (lambda x: len(x) < 16, "Senha deve ser menor do que 8 caracteres"),
    (lambda x: re.search("[A-Z]", x) is not None, "Senha deve conter ao menos uma letra maiuscula"),
    (lambda x: re.search("[0-9]", x) is not None, "Senha deve conter ao menos um digito"),
    (
        lambda x: re.search(
            "\\!|\"|\\#|\\$|\\%|\\&|'|\\(|\\)|\\*|\\+|\\,|\\-|\\.|\\/|\\:|\\;|\\<|\\=|\\>|\\?|\\@|\\[|\\\\|\\]\\^|\\_|\\{\\||\\}",
            x,
        )
        is not None,
        "Senha deve conter pelo menos um carater especial",
    ),
    (lambda x: " " not in x, "Senha não deve conter espaços"),
]

password = input("Digite sua senha: ").strip()
errors = filter(
    None, map(lambda validator: None if validator[0](password) else validator[1], verifications)
)

for error in errors:
    print(error)
else:
    print("Sucesso")
